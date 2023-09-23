from typing import Optional
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget

from pyforms.ui_smu_basic_control import Ui_SMUBasicControl

from modules.keithley_lib import K2636,get_default_channel_config

from PySide6.QtGui import QIcon

class SMUChannelControl(QWidget):
    def __init__(self, parent: QWidget | None,instr: K2636,name) -> None:
        super().__init__(parent)
        self.instr = instr
        self.smuName = name
        self.outputState = False
        self.ui = Ui_SMUBasicControl()
        self.ui.setupUi(self)
        self.enableIcon = QIcon()
        self.enableIcon.addFile(u":/materials/materials/netz_ein.png", QSize(), QIcon.Normal, QIcon.Off)
        self.disbleIcon = QIcon()
        self.disbleIcon.addFile(u":/materials/materials/netz_aus.png", QSize(), QIcon.Normal, QIcon.Off)


        self.ui.enableBtn.setIcon(self.enableIcon)

        self.ui.applyBtn.clicked.connect(self.applySettings)
        self.ui.enableBtn.clicked.connect(self.switchOutput)


    def switchOutput(self):
        self.outputState = self.ui.enableBtn.isChecked()
        self.instr.setOutput(self.smuName,int(self.outputState))

        if self.outputState:
            self.ui.enableBtn.setText("Disable")
            self.ui.enableBtn.setIcon(self.disbleIcon)
            self.instr.beep(0.1,2000)
            self.instr.beep(0.1,2400)
        else:
            self.ui.enableBtn.setText("Enable")
            self.ui.enableBtn.setIcon(self.enableIcon)
            self.instr.beep(0.1,2400)
            self.instr.beep(0.1,2000)

        
    def getConfigFromUi(self):
        config = get_default_channel_config()
        #Checks in order to figure out if Volts or CUrrents needed to be forced 
        if self.ui.voltForceCheck:
            config['source']['forcev'] = True
            config['source']['forcei'] = False
            config['source']['levelv'] = self.getFloatFromPrefix(self.ui.sourceVoltVal.value(),
                                             self.ui.sourceVoltPrefix.currentText())
            config['source']['limiti'] = self.getFloatFromPrefix(self.ui.sourceCurrVal.value(),
                                             self.ui.sourceCurrPrefix.currentText())
        else:
            config['source']['forcev'] = False
            config['source']['forcei'] = True
            config['source']['limitv'] = self.getFloatFromPrefix(self.ui.sourceVoltVal.value(),
                                             self.ui.sourceVoltPrefix.currentText())
            config['source']['leveli'] = self.getFloatFromPrefix(self.ui.sourceCurrVal.value(),
                                             self.ui.sourceCurrPrefix.currentText())
        
        config['measure']['rangev'] = self.ui.measVoltRange.currentText()
        config['measure']['rangei'] = self.ui.measCurrRange.currentText()
        config['measure']['interval'] = self.ui.measInterval.currentText()
        return config

    def applySettings(self):
        cfg = self.getConfigFromUi()
        self.instr.applyConfig(self.smuName,cfg)

        
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

    def resetChannel(self):
        if self.smuName == 'smua':
            ptr = self.instr.smua
        elif self.smuName == 'smub':
            ptr = self.instr.smub
        ptr.reset()



    
    
    
    
        