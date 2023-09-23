from typing import Optional

from pyforms.ui_settings_dialog import *
from PySide6.QtWidgets import QDialog

class SettingsDialog(QDialog):
    def __init__(self, parent=None,**kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.hide()
        