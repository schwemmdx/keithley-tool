
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget,QGraphicsView,QApplication,QMessageBox

from modules.keithley_lib import K2636

from pyforms.ui_sweep_widget import Ui_SweepWidget
from form_classes.sweep_channel_control import SweepConfigWidget

import pyqtgraph as pg

import numpy as np

import json
from threading import Thread

from modules.keithley_lib import get_default_channel_config

from time import sleep

class SweepWidget(QWidget):
    def __init__(self, parent: QWidget | None ,instr: K2636) -> None:
        super().__init__(parent)#
        self.instr = instr

        self.ui = Ui_SweepWidget()
        self.ui.setupUi(self)

        self.smuaWidget = SweepConfigWidget(self)
        self.smubWidget = SweepConfigWidget(self)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.addTab(self.smuaWidget,"SMU A")
        self.ui.tabWidget.addTab(self.smubWidget,"SMU B")


        self.canvas = pg.PlotWidget()

        self.ui.canvasLayout.addWidget(self.canvas)

        self.sweepAborted = False

        self.smuaCfg = get_default_channel_config()
        self.smubCfg = get_default_channel_config()

        self.sweepData ={
            'smua': {
                'v': np.array([]),
                'i': np.array([]),
                'r': np.array([]),
                'p': np.array([])
            },
            'smub': {
                'v': np.array([]),
                'i': np.array([]),
                'r': np.array([]),
                'p': np.array([])
            }
        }

        self.ui.runBtn.clicked.connect(self.runSweep)
        self.ui.StopBtn.clicked.connect(self.stopSweep)
        self.ui.clearPlotBtn.clicked.connect(self.clearPlot)


        for target in [
            self.ui.axisXSMU,
            self.ui.axisYSMU,
            self.ui.axisXType,
            self.ui.axisYType
        ]:
            target.currentIndexChanged.connect(self.changeDisplayedData)
        
        
        self.smuaPen = pg.mkPen({'width': 2,'color': "#4E79A7",'cosmetic':True})
        
        self.trace= pg.PlotDataItem(x= [],y = [],
             pen=self.smuaPen,symbol ='o', symbolBrush =("#4E79A7"),antialias=True)
        self.changeDisplayedData()
        self.canvas.addItem(self.trace)
        
    
    def changeDisplayedData(self):
        xsmu = self.ui.axisXSMU.currentText().replace(' ','').lower()
        ysmu = self.ui.axisYSMU.currentText().replace(' ','').lower()

        if self.ui.axisXType.currentText() == 'Voltage':
            xVal = 'v'
        else: 
            xVal = 'i'

        if self.ui.axisYType.currentText() == 'Voltage':
            yVal = 'v'
        else: 
            yVal = 'i'
        self.trace.setData(x=self.sweepData[xsmu][xVal],y=self.sweepData[ysmu][yVal])

    def runSweep(self):

            #check if we only perform a sweep on one smu 
            if self.ui.smuA_grp.isChecked() and self.ui.smuB_grp.isChecked():
                #perform dual smu sweep
                self.sweepDualSMU()
            
            elif self.ui.smuA_grp.isChecked():
                #perfom sweep on smua
                self.sweepSMU('smua')

            elif self.ui.smuB_grp.isChecked():
                self.sweepSMU('smub')

        
    def sweepSMU(self,smuName):
        self.ui.statusLabel.setText(f"Single Sweep on {smuName} started!")
        
        if smuName == 'smua':
            smuWidget = self.smuaWidget
            smuHandle = self.instr.smua

        else: 
            smuWidget = self.smubWidget
            smuHandle = self.instr.smub

        cfg = smuWidget.getConfig()

        self.canvas.setXRange(min(cfg['vals']),max(cfg['vals']))

        ch_cfg = get_default_channel_config()
        self.instr.applyConfig(smuName,ch_cfg)



        if cfg['force'] == "v":
            force_fun = self.instr.applyVoltage
        else:
            force_fun = self.instr.applyCurrent
        smuHandle.source.output(1)
        for i,val in enumerate(cfg['vals']):
            
            self.ui.statusLabel.setText(f"Seeping {smuName}: {int(i/len(cfg['vals'])*100)} %")
            if self.sweepAborted:    
                break
            force_fun(smuName,val,cfg['limit'])
            for smu in ['smua','smub']:
                results = self.instr.measure(smu,['i','v'],)
                print(f"{smu}: {val} -  {results['v']},{results['i']}")
                
                self.sweepData[smu]['i'] = np.append(self.sweepData[smu]['i'],results['i'])
                self.sweepData[smu]['v'] = np.append(self.sweepData[smu]['v'],val)

            self.changeDisplayedData()
            QApplication.processEvents()

        if self.sweepAborted:
            self.ui.statusLabel.setText("Sweep Aborted!")
        else:
            self.ui.statusLabel.setText("Sweep Done!")
        smuHandle.source.output(0)
        smuHandle.reset()
        self.sweepAborted = False


    def sweepDualSMU(self):
        
        aCfg = self.smuaWidget.getConfig()
        bCfg = self.smubWidget.getConfig()

        #check if one of the smu's is in constant mode 
        if aCfg['type'] == 'const':
            constCfg = aCfg
            constSMU = 'smua'
            sweepSMU = 'smub'
            constHandle = self.instr.smua
        elif bCfg['type'] == 'const':
            constCfg = bCfg
            constSMU = 'smub'
            sweepSMU = 'smua'
            constHandle = self.instr.smub
    
        if constCfg['force'] == 'v':
            self.instr.applyVoltage(constSMU,constCfg['vals'][0],constCfg['limit'])
        elif bCfg['force'] == 'i':
            self.instr.applyCurrent(constSMU,constCfg['vals'][0],constCfg['limit'])
        constHandle.source.output(1)
        self.sweepSMU(sweepSMU)
        constHandle.source.output(0)
        constHandle.reset()


    def stopSweep(self):
        self.sweepAborted = True
    



    def clearPlot(self):
        ans = QMessageBox.question(self,"Clear Plot","Are you sure to clean all tracies?")
        if ans == QMessageBox.StandardButton.Yes:
            self.trace.clear()
            self.sweepData['smua']['i'] = []
            self.sweepData['smua']['v'] = []
            self.sweepData['smub']['i'] = []
            self.sweepData['smub']['v'] = []
          
    

