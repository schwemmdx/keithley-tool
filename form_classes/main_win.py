
from typing import Optional
import PySide6.QtCore
from pyforms.ui_maingui import *
from PySide6.QtWidgets import QMainWindow


from form_classes.settings_dlg import SettingsDialog
from form_classes.error_dlg import ErrorDialog
from form_classes.smu_basic_control import SMUControlWidget

class MainGUI(QMainWindow):
    def __init__(self, parent: QWidget | None ,**kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settingsDlg = SettingsDialog(self)
        self.errorDlg = ErrorDialog(self)
        self.smuBasicControl = SMUControlWidget(self)
        self.setCentralWidget(self.smuBasicControl)

        self.configure_actions()

    def configure_actions(self):

        self.ui.actionSettings.triggered.connect(self.settingsDlg.show)
        self.ui.actionBasic_SMU_Control.triggered.connect(lambda: self.setCentralWidget(self.smuBasicControl) )
        #self.ui.actionRaw_Console.triggered.connect(lambda: self.setCentralWidget(self.errorDlg) )
        


    