from pyforms.ui_smu_control_widget import *
from pyforms.ui_smu_basic_control import *
from PySide6.QtWidgets import QWidget
from modules import K2636

from PySide6.QtGui import QIcon

import pyqtgraph as pg
from form_classes.smu_channel_control import SMUChannelControl

class SMUControlWidget(QWidget):
    def __init__(self, parent: QWidget | None, instr : K2636) -> None:
        super().__init__(parent)

        self.instr = instr
        self.measureThreadShouldRun = False
        self.ui = Ui_SMUControlWidget()
        self.ui.setupUi(self)

        self.smuaControl = SMUChannelControl(self,instr,'smua')
        self.smubControl = SMUChannelControl(self,instr,'smub')


        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.addTab(self.smuaControl,'SMU A')
        self.smuaIcon = QIcon()
        self.smubIcon = QIcon()
        

        self.smuaIcon.addFile(u":/materials/materials/letter-a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.tabWidget.setTabIcon(0,self.smuaIcon)

        self.ui.tabWidget.addTab(self.smubControl,'SMU B')
        
        self.smubIcon.addFile(u":/materials/materials/letter-b.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.tabWidget.setTabIcon(1,self.smubIcon)


        self.upperCanvas = pg.PlotWidget(self)
        self.lowerCanvas = pg.PlotWidget(self)
        self.ui.graphLayout.addWidget(self.upperCanvas)
        self.ui.graphLayout.addWidget(self.lowerCanvas)

        self.ui.resetInstrBtn.clicked.connect(self.instr.reset)



    def measureThread(self):
        pass
        

