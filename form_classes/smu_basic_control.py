from pyforms.ui_smu_control_widget import *
from pyforms.ui_smu_basic_control import *
from PySide6.QtWidgets import QWidget

class SMUControlWidget(QWidget):
    def __init__(self, parent: QWidget | None ) -> None:
        super().__init__(parent)
        self.ui = Ui_SMUControlWidget()
        self.ui.setupUi(self)
        self.smuaControl = QWidget()
        self.smubControl = QWidget()
        self.smuaControl_ui = Ui_SMUBasicControl()
        self.smuaControl_ui.setupUi(self.smuaControl)
        self.smubControl_ui = Ui_SMUBasicControl()
        self.smubControl_ui.setupUi(self.smubControl)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.addTab(self.smuaControl,'SMU A')
        self.ui.tabWidget.addTab(self.smubControl,'SMU B')


        

