
from typing import Optional
import PySide6.QtCore
from pyforms.ui_smu_sweep_config_widget import Ui_SweepConfigWidget

from modules.keithley_lib import get_vRange,get_iRange

from PySide6.QtWidgets import QWidget,QMessageBox,QAbstractItemView

import numpy as np

DEBUG_FLAG = True

class SweepConfigWidget(QWidget):

    def __init__(self, parent: QWidget,smuName) -> None:
        super().__init__(parent)
        self.smuName = smuName
        self.cfg = {
            'smu':self.smuName,
            'type':'lin',
            'force':'v',
            'start':0,
            'stop':1,
            'npts':10,
            'vals':np.array([])

        }
        self.ui = Ui_SweepConfigWidget()
        self.ui.setupUi(self)
        self.sweepTypeChanged(0)
        self.forceTypeChanged(0)
        self.measRangeTypeChanged()
        self.ui.forceType.currentIndexChanged.connect(lambda arg: self.forceTypeChanged(arg))
        self.ui.sweepTypeBox.currentIndexChanged.connect(lambda arg: self.sweepTypeChanged(arg))

        self.ui.endVal.valueChanged.connect(self.valueInputChanged)
        self.ui.startVal.valueChanged.connect(self.valueInputChanged)
        self.ui.limitVal.valueChanged.connect(self.valueInputChanged)
        self.ui.nPts.valueChanged.connect(self.valueInputChanged)
        self.ui.currentRange.valueChanged.connect(self.valueInputChanged)
        self.ui.voltageRange.valueChanged.connect(self.valueInputChanged)
        self.ui.measureCurrent.clicked.connect(self.valueInputChanged)
        self.ui.measureVoltage.clicked.connect(self.valueInputChanged)

        self.ui.rangeTypeVolt.currentIndexChanged.connect(self.measRangeTypeChanged)
        self.ui.rangeTypeCurrent.currentIndexChanged.connect(self.measRangeTypeChanged)


    def valueInputChanged(self):
        self.cfg['start'] = self.ui.startVal.value()
        self.cfg['stop'] = self.ui.endVal.value()
        self.cfg['npts'] = self.ui.nPts.value()
        self.cfg['limit'] = self.ui.limitVal.value()

        self.cfg['measurei'] = self.ui.measureCurrent.isChecked()
        self.cfg['measurev'] = self.ui.measureVoltage.isChecked()
        
        self.cfg['rangei'] = self.getCurrentRange()
        self.cfg['rangev'] = self.getVoltageRange()

        if self.cfg['type'] == 'lin':
            self.cfg['vals'] = np.linspace(self.cfg['start'],self.cfg['stop'],num = self.cfg['npts'])
        elif self.cfg['type'] == 'log':
            try:
                self.cfg['vals'] = np.geomspace(self.cfg['start'],self.cfg['stop'],num = self.cfg['npts'])
            except ValueError as ex:
                QMessageBox.warning(self,"Error Occured!",f"Log series encounterd an error:\n{ex}\n\nPlease check your start/stop/npts input!")
        elif self.cfg['type'] == 'list':
            self.__getValsFromSweepList()
            
            
        elif self.cfg['type'] == 'const':
            self.cfg['vals'] = [self.cfg['start']]

        self.__updateSweepList()
        if DEBUG_FLAG:
            print('-'*20)
            print(self.cfg)
            print('-'*20)

    def measRangeTypeChanged(self):
        
        for rTypeObj,rangeObj,cfgKey in zip([self.ui.rangeTypeVolt,self.ui.rangeTypeCurrent],
                                     [self.ui.voltageRange,self.ui.currentRange],['rangev','rangei']):
            if rTypeObj.currentText() == 'fixed':
                rangeObj.setEnabled(True)
            else:
                rangeObj.setEnabled(False)
                self.cfg[cfgKey]= 'auto'
        self.valueInputChanged()
    
    def getVoltageRange(self):
        if self.ui.rangeTypeVolt.currentText() == 'auto':
            self.ui.voltageRange.setEnabled(False)
            return 'auto'
        else:
            self.ui.voltageRange.setEnabled(True)
            return 2*10**self.ui.voltageRange.value()
        
    def getCurrentRange(self):
        if self.ui.rangeTypeCurrent.currentText() == 'auto':
            self.ui.currentRange.setEnabled(False)
            return 'auto'
        else:
            self.ui.currentRange.setEnabled(True)
            return 10**self.ui.currentRange.value()


    def forceTypeChanged(self,arg):
        if arg==0:
            #force type is voltage
            self.ui.endVal.setSuffix(' V')
            self.ui.startVal.setSuffix(' V')
            self.ui.limitVal.setSuffix(' A')
            self.ui.SweepListLabel.setText("Sweep List [V]")
            self.cfg['force'] = 'v'
        if arg == 1:
            self.ui.endVal.setSuffix(' A')
            self.ui.startVal.setSuffix(' A')
            self.ui.limitVal.setSuffix(' V')
            self.ui.SweepListLabel.setText("Sweep List [A]")
            self.cfg['force'] = 'i'
        self.__updateSweepList()
        self.__updateMeasureSelection()
        
    def sweepTypeChanged(self,arg):
        
        self.__setEnableState(True)
        self.ui.sweepList.setReadOnly(True)
        self.ui.sweepList.setEnabled(True)
        self.ui.StartLabel.setText("Start")
        
        sweepType = self.ui.sweepTypeBox.currentText()
        if sweepType=='Linear':
            #type linear
            self.cfg['type'] = 'lin'
            
        elif sweepType=='Log':
            self.cfg['type'] = 'log'
            
          
            #type log
        elif sweepType == 'Constant':
            # type const:
            
            self.ui.endVal.setEnabled(False)
            self.ui.StartLabel.setText("Const. Value")
            self.ui.startVal.setEnabled(True)
            self.ui.nPts.setEnabled(False)
            self.cfg['type'] = 'const'

        elif sweepType=='List':
            self.cfg['type'] = 'list'
            self.ui.endVal.setEnabled(False)
            self.ui.startVal.setEnabled(False)
            self.ui.nPts.setEnabled(False)
            self.ui.sweepList.setReadOnly(False)
            self.ui.sweepList.clear()
            # type list
        elif sweepType == 'Unused':
            self.cfg['type'] = 'unused'
            self.__setEnableState(False)
            self.ui.sweepList.setEnabled(False)
            
        self.valueInputChanged()


    def getConfig(self):
        self.valueInputChanged()
        return self.cfg
    
    def __updateSweepList(self):
       
        self.ui.sweepList.clear()
        buf = ""
        for val in self.cfg['vals']:
            buf+=f"{val:.3f}\n"
        self.ui.sweepList.setPlainText(buf)
    
    def __getValsFromSweepList(self):
        vals = self.ui.sweepList.toPlainText().split()
        buf = []
        for val in vals:
            buf.append(float(val))
        self.cfg['vals'] = buf

    def __setEnableState(self,state):
        p = self.ui
        for elem in [p.forceType,
                        p.limitVal,
                        p.startVal,
                        p.endVal,
                        p.nPts,
                        p.measureCurrent,
                        p.measureVoltage,
                        p.currentRange,
                        p.voltageRange,
                        p.rangeTypeCurrent,
                        p.rangeTypeVolt]:
            elem.setEnabled(state)

    def __updateMeasureSelection(self):
        if self.cfg['force'] == 'v':
            self.ui.measureCurrent.setChecked(True)
            self.ui.measureVoltage.setChecked(False)
        else:
            self.ui.measureCurrent.setChecked(False)
            self.ui.measureVoltage.setChecked(True)
