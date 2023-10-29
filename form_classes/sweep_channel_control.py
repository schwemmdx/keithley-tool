
from typing import Optional
import PySide6.QtCore
from pyforms.ui_smu_sweep_config_widget import Ui_SweepConfigWidget

from modules.keithley_lib import get_vRange,get_iRange

from PySide6.QtWidgets import QWidget,QMessageBox

import numpy as np

class SweepConfigWidget(QWidget):

    def __init__(self, parent: QWidget ) -> None:
        super().__init__(parent)
        self.cfg = {
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
        self.ui.forceType.currentIndexChanged.connect(lambda arg: self.forceTypeChanged(arg))
        self.ui.sweepTypeBox.currentIndexChanged.connect(lambda arg: self.sweepTypeChanged(arg))

        self.ui.endVal.valueChanged.connect(self.valueInputChanged)
        self.ui.startVal.valueChanged.connect(self.valueInputChanged)
        self.ui.limitVal.valueChanged.connect(self.valueInputChanged)
        self.ui.nPts.valueChanged.connect(self.valueInputChanged)

    def valueInputChanged(self):
        self.cfg['start'] = self.ui.startVal.value()
        self.cfg['stop'] = self.ui.endVal.value()
        self.cfg['npts'] = self.ui.nPts.value()
        self.cfg['limit'] = self.ui.limitVal.value()


        if self.cfg['force'] == 'v':
            self.cfg['limitv'] = get_vRange(self.cfg['stop'])

        elif self.cfg['force'] == 'i':
            self.cfg['limiti'] = get_vRange(self.cfg['stop'])
            

        if self.cfg['type'] == 'lin':
            self.cfg['vals'] = np.linspace(self.cfg['start'],self.cfg['stop'],num = self.cfg['npts'])
        elif self.cfg['type'] == 'log':
            try:
                self.cfg['vals'] = np.geomspace(self.cfg['start'],self.cfg['stop'],num = self.cfg['npts'])
            except ValueError as ex:
                QMessageBox.warning(self,"Error Occured!",f"Log series encounterd an error:\n{ex}\n\nPlease check your start/stop/npts input!")
        elif self.cfg['type'] == 'list':
            paramStr = self.ui.sweepList.text()
            paramStr = paramStr.split(',')
            params = []
            for param in paramStr:
                if not param == '':
                    params.append(float(param))
            self.cfg['vals'] = np.array(params)

        elif self.cfg['type'] == 'const':
            self.cfg['vals'] = [self.cfg['start']]

        print(self.cfg['vals'])
    def forceTypeChanged(self,arg):
        if arg==0:
            #force type is voltage
            self.ui.endVal.setSuffix(' V')
            self.ui.startVal.setSuffix(' V')
            self.ui.limitVal.setSuffix(' A')
            self.cfg['force'] = 'v'
        if arg == 1:
            self.ui.endVal.setSuffix(' A')
            self.ui.startVal.setSuffix(' A')
            self.ui.limitVal.setSuffix(' V')
            self.cfg['force'] = 'i'
        
    def sweepTypeChanged(self,arg):
        self.ui.endVal.setEnabled(True)
        self.ui.startVal.setEnabled(True)
        self.ui.nPts.setEnabled(True)
        if arg==0:
            #type linear
            self.cfg['type'] = 'lin'
            self.ui.sweepList.setEnabled(False)
        elif arg==1:
            self.cfg['type'] = 'log'
            
            self.ui.sweepList.setEnabled(False)
            #type log
        elif arg == 2:
            # type const:
            self.ui.sweepList.setEnabled(False)
            self.ui.endVal.setEnabled(False)
            self.ui.startVal.setEnabled(True)
            self.ui.nPts.setEnabled(False)
            self.cfg['type'] = 'const'

        elif arg==3:
            self.cfg['type'] = 'list'
            self.ui.endVal.setEnabled(False)
            self.ui.startVal.setEnabled(False)
            self.ui.nPts.setEnabled(False)
            self.ui.sweepList.setEnabled(True)
            # type list
        self.valueInputChanged()


    def getConfig(self):
        self.valueInputChanged()
        return self.cfg
    

