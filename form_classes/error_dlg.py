
from typing import Optional
import PySide6.QtCore
from pyforms.ui_error_dlg import Ui_ErrorDlg
from PySide6.QtWidgets import QDialog,QWidget



class ErrorDialog(QDialog):
    def __init__(self, parent: QWidget | None = ..., **kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.ui = Ui_ErrorDlg()
        self.ui.setupUi(self)
        self.hide()