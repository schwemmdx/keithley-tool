
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget

from pyforms.ui_sweep_widget import Ui_SweepWidget

import pyqtgraph as pg

import numpy as np

import json

class SweepWidget(QWidget):
    def __init__(self, parent: QWidget | None ,instr=None) -> None:
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