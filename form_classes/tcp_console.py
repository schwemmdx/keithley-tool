from typing import Optional
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget,QPlainTextEdit,QGridLayout
from PySide6.QtGui import QFont

from modules.keithley_lib import K2636
import form_classes
import modules

class TCPConsole(QPlainTextEdit):

    def __init__(self, parent: QWidget | None ,instr: K2636) -> None:
        super().__init__(parent)
        
        self.instr = instr
        self.ui = QPlainTextEdit()
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(12)
        font1.setKerning(True)
        self.ui.setFont(font1)


        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.ui)
        self.ui.installEventFilter(self)
        self.prompt = r"tcp$>"
        self.localToken = "#local "

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                inp = self.getInput()
                ret = self.processInput(inp)
                
                if ret:
                    self.ui.appendPlainText(ret)
                self.ui.appendPlainText(self.prompt)
                return True
        return super().eventFilter(obj, event)

    def processInput(self,cmd:str):
        if cmd.startswith(self.localToken): 
            cleanCmd = cmd.replace(self.localToken,'')
            return self.handleLocalCmd(cleanCmd)
        else:
            return self.instr.tcpSock.query(cmd)


        
        
    def initConsole(self):
        self.ui.setPlainText(f"Connected to {self.instr.tcpSock.ipUsed}::{self.instr.tcpSock.portUsed} as <tcp>\n"+'-'*10+'\n'+self.prompt)

    def getInput(self):
        buf = self.ui.toPlainText().split('\n')[-1].replace(self.prompt,'')
        return buf

    def handleLocalCmd(self,cmd: str):
        if cmd == '-version':
            return f"UI Version: {form_classes.__version__}\nModules Version: {modules.__version__}"
        
        else:
            return None
        
    def setInteractionState(self,state):
        if state:
            self.initConsole()
            self.ui.setReadOnly(False)
        else:
            self.ui.setPlainText('No TCP Connection Established!')
            self.ui.setReadOnly(True)
