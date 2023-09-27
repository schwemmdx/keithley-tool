# This Python file uses the following encoding: utf-8
REBUILD_UI_FILES = True

import os
from pathlib import Path
from time import sleep

import path
import sys
import traceback

from PySide6.QtWidgets import QApplication, QWidget,QMainWindow,QDockWidget, QStatusBar, QDialog, QMessageBox, QPlainTextEdit
from PySide6.QtCore import QFile
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette
 
from modules.keithley_lib import K2636,get_default_channel_config

import pyqtgraph as pg
from threading import Thread
import modules.syntax as syntax
import numpy as np

from build_tasks import force_rebuild

import subprocess, os

force_rebuild()

try:

    from pyforms.maingui import Ui_MainWindow
    from pyforms.smu_control_dock import Ui_SMUControlDock
    from pyforms.smu_basic_control import Ui_SMUBasicControl
    from pyforms.tcp_settings import Ui_tcpSettings
    from pyforms.measure_dock import Ui_measureDock
    from pyforms.error_dlg import Ui_ErrorDlg
    from pyforms.tcp_console import Ui_tcpConsole
    from pyforms.script_dlg import Ui_ScriptDialog
except:
    print("No pre-generated ui.py files found!")


from modules.keithley_dipshit import theme


class main_gui(QMainWindow):
    def __init__(self, parent=None):

        super().__init__(parent)

        self.kDevice = K2636()
        self.subThreadShouldRun = True
        self.measureThread = Thread(target=self.threadMeasure)
        self.errorChecker = Thread(target=self.threadErrorChecker)
        
        #setting up all gui elements        

        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.smuControlDock = QDockWidget(self)
        

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.smuControlDock_ui = Ui_SMUControlDock()
        self.smuControlDock_ui.setupUi(self.smuControlDock)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea,self.smuControlDock)

        self.measureDock = QDockWidget(self)
        self.measureDock_ui = Ui_measureDock()
        self.measureDock_ui.setupUi(self.measureDock)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea,self.measureDock)

        #Error Dialog
        self.errorDlg = QDialog(self)
        self.errorDlg_ui = Ui_ErrorDlg()
        self.errorDlg_ui.setupUi(self.errorDlg)
        self.errorDlg.hide()
        

 
        
        self.tcpConsole = QDialog(self)
        self.tcpConsole_ui = Ui_tcpConsole()
        self.tcpConsole_ui.setupUi(self.tcpConsole)
        self.tcpConsole.hide()

        self.scriptDlg = QDialog(self)
        self.scriptDlg_ui = Ui_ScriptDialog()
        self.scriptDlg_ui.setupUi(self.scriptDlg)
        self.scriptFolder = "./tsp_scripts"
        self.scriptDlg.hide()
        self.scriptDlg_ui.scriptList.itemClicked.connect(self.loadClickedItemIntoEdit)
        self.scriptDlg_ui.scriptList.itemDoubleClicked.connect(
            lambda :self.openWithDefaultApp(self.scriptDlg_ui.scriptList.selectedItems()[0].text()))
        self.scriptDlg.setWindowModality(Qt.WindowModality.NonModal)
        p = self.scriptDlg_ui.scriptEdit.palette()
        p.setColor(QPalette.ColorGroup.Active,QPalette.ColorRole.Base,'#464646')
        p.setColor(QPalette.ColorGroup.Active,QPalette.ColorRole.BrightText,'#d6d6d6')
        p.setColor(QPalette.ColorGroup.Active,QPalette.ColorRole.Text,'#d6d6d6')

        self.scriptDlg_ui.scriptEdit.setPalette(p)
        
        #self.tcpConsole_ui.inputLine.returnPressed



        self.smuaBasic = QWidget()
        self.smubBasic = QWidget()

        self.tcpSettings = QDialog()
        self.tcpSettings_ui = Ui_tcpSettings()
        self.tcpSettings_ui.setupUi(self.tcpSettings)

        self.smuaBasic_ui = Ui_SMUBasicControl()
        self.smubBasic_ui = Ui_SMUBasicControl()

        self.smuaBasic_ui.setupUi(self.smuaBasic)
        self.smubBasic_ui.setupUi(self.smubBasic)

        self.smuControlDock_ui.toolBox.removeItem(0)
        self.smuControlDock_ui.toolBox.removeItem(0)
        self.smuControlDock_ui.toolBox.addItem(self.smuaBasic,'SMU A')
        self.smuControlDock_ui.toolBox.addItem(self.smubBasic,'SMU B')


        
        self.canvas = pg.PlotWidget() 

        self.canvas.showGrid(True,True)
        self.canvas.setLabel('left', "Voltage [V]")
        self.canvas.setLabel('bottom', "Time  [n*s]")
        self.linePen = pg.mkPen({'width': 2,'color': "#41FF00",'cosmetic':True})
        self.setCentralWidget(self.canvas)
        #self.canvas.setBackground((120,120,120))
        

        # connect the singals to do shit 
        self.smuControlDock_ui.enableSMUA.clicked.connect(self.enableSMUA)
        self.statusBar.showMessage("No K26XX Connected, establish a connection!")


       
        self.smuMeasureDataVec = {
            'smua':{
                't':np.array([]),
                'i': np.array([]),
                'v': np.array([]),
                'r': np.array([]),
                'p': np.array([]),
            },
            'smub':
            {
                't':np.array([]),
                'i': np.array([]),
                'v': np.array([]),
                'r': np.array([]),
                'p': np.array([]),
            }
        }

    
        self.loadDefaultConfig()

        self.main_ui.actionConnection_Settings.triggered.connect(self.tcpSettings.show)
        self.main_ui.actionRaw_Console.triggered.connect(self.tcpConsole.show)
        #self.main_ui.actionScripts.triggered.connect(self.scriptWidgetTriggered)
        self.main_ui.actiionError.triggered.connect(self.errorDlg.show)

        self.main_ui.actionConnect.triggered.connect(self.connect_to_instrument)
        self.tcpSettings_ui.applyBtn.clicked.connect(self.apply_tcp_settings)

        #SMU Config Data:
        self.smuaConfig  = get_default_channel_config()
        self.smubConfig  = get_default_channel_config()

       #disable SMUA&B Buttons of not connected
        self.tcpConnectionStateChanged()

        self.graphItemSMUA_v = pg.PlotDataItem(x=self.smuMeasureDataVec['smua']['t'],y=self.smuMeasureDataVec['smua']['v'],
                                               pen=self.linePen,symbol ='o', symbolBrush =("#41FF00"),antialias=True)
        self.graphItemSMUA_i = pg.PlotDataItem(x=self.smuMeasureDataVec['smua']['t'],y=self.smuMeasureDataVec['smua']['i'],
                                               pen=self.linePen,symbol ='o', symbolBrush =("#41FF00"),antialias=True)

        self.canvas.addItem(self.graphItemSMUA_v)

        #self.graphItemSMUA_i = pg.PlotDataItem(self.xData,self.smuaData_i,symbol ='o',antialias=True)
        
        #python poor threading lib is a mess and cannot pause a thread, 
        # #therefore inside the thread the pause is handled
        self.measureThread.start()

    def loadClickedItemIntoEdit(self):
        selection = self.scriptDlg_ui.scriptList.selectedItems()[0]
        selText = selection.text()
        with open(self.scriptFolder+'/'+selText,'r') as pFile:
            data = pFile.read()
        highlight = syntax.PythonHighlighter(self.scriptDlg_ui.scriptEdit.document())
        self.scriptDlg_ui.scriptEdit.setPlainText(data)

    def refresh_script_dlg(self):
        try:
            availableScripts = os.listdir(self.scriptFolder)
            self.scriptDlg_ui.scriptList.clear()
            self.scriptDlg_ui.scriptList.addItems(availableScripts)
        except Exception as ex:
            print(ex)
        self.scriptDlg.show()     


    def threadMeasure(self):
        """Subthread for getting Measurements"""
        
        while(self.subThreadShouldRun):
            if self.tcpConnectionEstablished:
                if self.smuaState:
                    self.getMeasurements('smua')

                    self.graphItemSMUA_v.setData(list(range(len(self.smuaData_v))),self.smuaData_v)
                    

                if self.smubState:
                    self.getMeasurements('smub')
                
                sleep(float(self.measureDock_ui.intervalBox.currentText()))

            else:
                sleep(1)
    
    def threadErrorChecker(self):
        """Subthread for checking if during operation errors occured, if so, the user is notified by an messagebox.
        By Default the errors are saved into an error logfile."""

        while(self.subThreadShouldRun):
            if self.tcpConnectionEstablished:
                if self.kDevice.check_errors():
                    msg = QMessageBox(self)
                    msg.setWindowTitle("Keithley Error Occured!")
                    msg.setText("Error(s) occured during instrument operation, see errors for further details")
                    self.occuredErrors = self.kDevice.error_queue.read_all(autosave=True)
            sleep(60)


                    

        

    def getMeasurements(self,smuName,which=['v','i','r','p']):
        
        r = self.kDevice.measure(smuName,which)

        if smuName == 'smua':
            self.measureDock_ui.smua_v.setText(r['v'])
            self.measureDock_ui.smua_c.setText(r['i'])
            self.measureDock_ui.smua_r.setText(r['r'])
            self.measureDock_ui.smua_p.setText(r['p'])
           
        else:
            self.measureDock_ui.smub_v.setText(r['v'])
            self.measureDock_ui.smub_c.setText(r['i'])
            self.measureDock_ui.smub_r.setText(r['r'])
            self.measureDock_ui.smub_p.setText(r['p'])
        
        for key in r:
            np.append(self.smuMeasureDataVec[smuName][key],r[key],axis=0)
        np.append(self.smuMeasureDataVec[smuName]['t'],len(self.smuMeasureDataVec[smuName]['t'])+1,axis=0)
            #self.smuaData_v.append(float(r['v']))
            
 

    def loadDefaultConfig(self):
        
        self.sessionIp = "192.168.0.56"
        self.sessionPort = 5025
        self.smuaState = False
        self.smubState = False
        self.tcpConnectionEstablished = False


        
    
    def apply_tcp_settings(self):
        
        self.sessionIp = self.tcpSettings_ui.ipAddr.text()
        self.sessionPort = int(self.tcpSettings_ui.portAddr.text())
        self.tcpSettings.hide()
        
    def connect_to_instrument(self):

        if not self.tcpConnectionEstablished:
            
            try:
                self.statusBar.showMessage(f"Connecting to {self.sessionIp}:{self.sessionPort}")
                self.kDevice.tcpConnect(self.sessionIp,self.sessionPort)
                
            except Exception as ex :
                tb = traceback.format_exc()
                msgBox = QMessageBox(self)
                msgBox.setText(f"Error occured during connection attempt to:\n{self.sessionIp}::{self.sessionPort}")
                msgBox.setWindowTitle("Conncetion Error")
                msgBox.setDetailedText(str(ex)+":\n\n"+str(tb))
                msgBox.show()
                return
           
            self.statusBar.showMessage(f"Connected to {self.sessionIp}::{self.sessionPort}")
            self.main_ui.actionConnect.setChecked(True)
            self.tcpConnectionEstablished = True
            self.main_ui.actionConnect.setText("Disconnect")
            self.kDevice.fanfareConnect()
            

            
            
        else:
            
            self.kDevice.fanfareDisonnect()
            self.kDevice.tcpSock.close()
            self.main_ui.actionConnect.setText("Connect")
            self.tcpConnectionEstablished = False
            self.main_ui.actionConnect.setChecked(False)

        self.tcpConnectionStateChanged()
        

    def enableSMUA(self):
        
        if not self.smuaState:
            config = self.getSMUConfigfromUi(self.smuaBasic_ui)


            self.kDevice.applyConfig('smua',config)
            self.kDevice.setOutput('smua',1)
            self.smuControlDock_ui.enableSMUA.setText('Disable A')
            self.statusBar.showMessage(r"SMU A: ARMED")
            self.smuaState = True
            self.kDevice.beep(0.1,2000)
            self.kDevice.beep(0.1,2400)
            
        else:
            self.smuControlDock_ui.enableSMUA.setText('Enable A')
            self.kDevice.setOutput('smua',0)
            self.statusBar.showMessage(r"SMU A: DISARMED")
            self.smuaState = False
            self.kDevice.beep(0.1,2400)
            self.kDevice.beep(0.1,2000)
       
            
        

        
    def smub_enable(self):
        print("B Clicked")
        
    def getSMUConfigfromUi(self,ui:Ui_SMUBasicControl):
        config = get_default_channel_config()
        #Checks in order to figure out if Volts or CUrrents needed to be forced 
        if ui.voltForceCheck:
            config['source']['forcev'] = True
            config['source']['forcei'] = False
            config['source']['levelv'] = self.getFloatFromPrefix(ui.sourceVoltVal.value(),
                                             ui.sourceVoltPrefix.currentText())
            config['source']['limiti'] = self.getFloatFromPrefix(ui.sourceCurrVal.value(),
                                             ui.sourceCurrPrefix.currentText())
        else:
            config['source']['forcev'] = False
            config['source']['forcei'] = True
            config['source']['limitv'] = self.getFloatFromPrefix(ui.sourceVoltVal.value(),
                                             ui.sourceVoltPrefix.currentText())
            config['source']['leveli'] = self.getFloatFromPrefix(ui.sourceCurrVal.value(),
                                             ui.sourceCurrPrefix.currentText())
        
        config['measure']['rangev'] = ui.measVoltRange.currentText()
        config['measure']['rangei'] = ui.measCurrRange.currentText()
        config['measure']['interval'] = ui.measInterval.currentText()
        return config
        


        
    def getFloatFromPrefix(self,num,prefix):
        
        if prefix in ['mV','mA']:
            flt= 1e-3
        elif prefix in ['µV','µA']:
            flt = 1e-6
        elif prefix in ['nV','nA']:
            flt = 1e-9
        elif prefix in ['pA']:
            flt = 1e-12
        else:
            flt=1
        return flt*float(num)
    
    #@QtCore.pyqtSlot()
    def tcpConnectionStateChanged(self):

        self.smuControlDock_ui.enableSMUA.setEnabled(self.tcpConnectionEstablished)
        self.smuControlDock_ui.enableSMUB.setEnabled(self.tcpConnectionEstablished)
        #self.main_ui.actionRaw_Console.setEnabled(self.tcpConnectionEstablished)
        self.tcpConsole_ui.sendBtn.setEnabled(self.tcpConnectionEstablished)

    def onAppExit(self):
        self.subThreadShouldRun = False
        
    def openWithDefaultApp(self,filepath):
        filepath= self.scriptFolder+'\\'+filepath

        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(filepath)
        else:                                   # linux variants
            subprocess.call(('xdg-open', filepath))


    def scriptWidgetTriggered(self):
        theme(self.kDevice)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    widget = main_gui()
    widget.showMaximized()
    ret = app.exec()
    widget.onAppExit()
    sys.exit()
