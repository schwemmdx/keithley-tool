from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget,QPlainTextEdit

from pyforms.ui_tcp_console import Ui_tcpConsole
from modules.keithley_lib import K2636

class TCPConsole(QPlainTextEdit):

    def __init__(self, parent: QWidget | None ,instr: K2636) -> None:
        super().__init__(parent)
        self.instr = instr
        self.ui = Ui_tcpConsole()
        self.ui.setupUi(self)
        
    def initConsole(self):
        self.ui.consoleHistory.setText(f"Connected to {self.instr.tcpSock.ipUsed}::{self.instr.tcpSock.portUsed}\n")

    def newInputLine(self):
        self.ui.consoleHistory.append("\ntcp$> ")
    

    