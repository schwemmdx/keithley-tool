
from typing import Optional
import traceback
import PySide6.QtCore
from pyforms.ui_maingui import *
from PySide6.QtWidgets import QMainWindow, QStackedWidget,QMessageBox


from form_classes.settings_dlg import SettingsDialog
from form_classes.error_dlg import ErrorDialog
from form_classes.smu_basic_control import SMUControlWidget
from form_classes.tcp_console import TCPConsole
from form_classes.sweep_widget import SweepWidget

from pyforms.ui_maingui import Ui_KeithleyTool
from modules import K2636

from modules.keithley_dipshit import theme

class MainGUI(QMainWindow):
    def __init__(self, parent: QWidget | None ,**kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.ui = Ui_KeithleyTool()
        self.ui.setupUi(self)

        #Setup Hardware Devie 
        self.instr = K2636()
        
        self.iconNotConnected = QIcon()
        self.iconConnected = QIcon()
        self.iconConnected.addFile(u":/materials/materials/lan_connected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconNotConnected.addFile(u":/materials/materials/lan.png", QSize(), QIcon.Normal, QIcon.Off)
        
        #seperatee Dialogs and Widgets shown inside the stackwidget
        self.settingsDlg = SettingsDialog(self)
        self.errorDlg = ErrorDialog(self,instr=self.instr)
        self.smuBasicControl = SMUControlWidget(self,instr=self.instr)
        self.tcpConsole = TCPConsole(self,self.instr)
        self.sweepWidget = SweepWidget(self)

        self.stack = QStackedWidget(self)

        self.stack.addWidget(QWidget())
        self.stack.addWidget(self.smuBasicControl)
        self.stack.addWidget(self.errorDlg)
        self.stack.addWidget(self.tcpConsole)
        self.stack.addWidget(self.sweepWidget)


        self.setCentralWidget(self.stack)
        self.stack.setCurrentIndex(0)
        

        self.configure_actions()
        self.connectionStateChanged()

    def configure_actions(self):

        self.ui.actionConnect.triggered.connect(self.connect_to_endpoint)
        self.ui.actionSettings.triggered.connect(self.settingsDlg.show)
        self.ui.actionBasic_SMU_Control.triggered.connect(lambda : self.stack.setCurrentWidget(self.smuBasicControl))
        self.ui.actionRaw_Console.triggered.connect(lambda: self.stack.setCurrentWidget(self.tcpConsole))
        self.ui.actionSweep_Tool.triggered.connect(lambda: self.stack.setCurrentWidget(self.sweepWidget))
        self.ui.actionErrors.triggered.connect(self.onActionErrorDlg)
        


    def connect_to_endpoint(self):
        settings = self.settingsDlg.getTCPSettings()
        if not self.instr.isConnected():
            try:
                self.instr.tcpConnect(settings['ip'],settings['port'],settings['timeout'])

                self.instr.fanfareConnect()

            except Exception as ex :
                self.ui.actionConnect.setChecked(False)
                tb = traceback.format_exc()
                msgBox = QMessageBox(self)
                msgBox.setText(f"Error occured during connection attempt to:\n{settings['ip']}::{settings['port']}")
                msgBox.setWindowTitle("Conncetion Error")
                msgBox.setDetailedText(str(ex)+":\n\n"+str(tb))
                msgBox.show()
                return
        else:
            self.instr.fanfareDisonnect()
            self.instr.tcpSock.close()
            self.ui.actionConnect.setChecked(False)
        
        self.connectionStateChanged()
            

    def connectionStateChanged(self):

        if self.instr.isConnected():

            self.ui.actionConnect.setIcon(self.iconConnected)
        else:
            self.ui.actionConnect.setIcon(self.iconNotConnected)
            self.stack.setCurrentIndex(0)

        for act in [
            self.smuBasicControl.ui.resetInstrBtn,
            self.ui.actionBasic_SMU_Control,
            self.ui.actionRaw_Console,
            self.ui.actionSweep_Tool,
            self.ui.actionErrors
        ]:
            act.setEnabled(self.instr.isConnected())
        

        for channel in [self.smuBasicControl.smuaControl,self.smuBasicControl.smubControl]:
            channel.ui.applyBtn.setEnabled(self.instr.isConnected())
            channel.ui.enableBtn.setEnabled(self.instr.isConnected())
            channel.ui.resetSMUBtn.setEnabled(self.instr.isConnected())

        self.tcpConsole.setInteractionState(self.instr.isConnected())
            
    def onActionErrorDlg(self):
         self.errorDlg.read()
         self.stack.setCurrentWidget(self.errorDlg)
