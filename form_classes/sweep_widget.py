
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from modules.keithley_lib import K2636

from pyforms.ui_sweep_widget import Ui_SweepWidget

import pyqtgraph as pg

import numpy as np

import json

class SweepWidget(QWidget):
    def __init__(self, parent: QWidget | None ,instr: K2636) -> None:
        super().__init__(parent)#
        self.instr = instr

        self.ui = Ui_SweepWidget()
        self.ui.setupUi(self)

        self.canvas = pg.PlotWidget()
        self.ui.canvasLayout.addWidget(self.canvas)


        self.sweepOngoing = False

        self.sweepData ={
            'smua': {
                'v': np.array([]),
                'i': np.array([]),
                'r': np.array([]),
                'p': np.array([])
            },
            'smub': {
                'v': np.array([]),
                'i': np.array([]),
                'r': np.array([]),
                'p': np.array([])
            }
        }

        self.ui.runBtn.clicked.connect(self.runSweep)
        self.ui.StopBtn.clicked.connect(self.stopSweep)

    def runSweep(self):
        sweepCfg = self.getSweepValues()
        with open("./settings/sweep_settings.json",'w') as pOut:
            json.dump(sweepCfg,pOut,indent=4)

            #check if we only perform a sweep on one smu 
            if self.ui.smuA_grp.isEnabled() and self.ui.smub_grp.isEnabled():
                #perform dual smu sweep
                self.sweepDualSMU(self.getSweepValues())
            elif self.ui.smuA_grp.isEnabled():
                #perfom sweep on smua
                self.sweepSMU('smua',self.getSweepValues()['smua'])
            else:
                self.sweepSMU('smub',self.getSweepValues()['smub'])

        
    def sweepSMU(self,smuName,sweepCfg):
        sweepVals = np.arange(sweepCfg['start'],sweepCfg['stop'],sweepCfg['step'])
        self.instr
        

    def sweepDualSMU(self,sweepCfg):
        pass





    def stopSweep(self):
        pass

    def sweepStateChanged(self,state):
        pass

    def getSweepValues(self):
        aVals = {
            'enabled': self.ui.smuA_grp.isEnabled(),
            'type': self.ui.aTypeBox.currentText(),
            'limit': self.ui.aLimitVal.value(),
            'start': self.ui.aStartVal.value(),
            'stop': self.ui.aEndVal.value(),
            'step':self.ui.aStepVal.value(),
            'int_time': self.ui.aIntTimeBox.currentText()
        }
        bVals = {
            'enabled': self.ui.smuB_grp.isEnabled(),
            'type': self.ui.bTypeBox.currentText(),
            'limit': self.ui.bLimitVal.value(),
            'start': self.ui.bStartVal.value(),
            'stop': self.ui.bEndVal.value(),
            'step':self.ui.bStepVal.value(),
            'int_time': self.ui.bIntTimeBox.currentText()
        }
        return {'smua': aVals,'smub':bVals}