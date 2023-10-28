
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget,QGraphicsView,QApplication,QMessageBox

from modules.keithley_lib import K2636

from pyforms.ui_sweep_widget import Ui_SweepWidget
from form_classes.sweep_channel_control import SweepConfigWidget

import pyqtgraph as pg

import numpy as np

import json
from threading import Thread

from modules.keithley_lib import get_default_channel_config

from time import sleep

class SweepWidget(QWidget):
    def __init__(self, parent: QWidget | None ,instr: K2636) -> None:
        super().__init__(parent)#
        self.instr = instr

        self.ui = Ui_SweepWidget()
        self.ui.setupUi(self)

        self.smuaWidget = SweepConfigWidget(self)
        self.bmuaWidget = SweepConfigWidget(self)

        self.ui.aLayout.addWidget(self.smuaWidget)
        self.ui.bLayout.addWidget(self.bmuaWidget)

        self.canvas = pg.PlotWidget()
        #self.canvas.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.ui.canvasLayout.addWidget(self.canvas)

        #self.updatePlotThread =Thread(target=self.updatePlot)

        self.sweepAborted = False
        self.updatePlotRunning = False

        self.smuaCfg = get_default_channel_config()
        self.smubCfg = get_default_channel_config()

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
        self.ui.clearPlotBtn.clicked.connect(self.clearPlot)

        self.smuaPen = pg.mkPen({'width': 2,'color': "#4E79A7",'cosmetic':True})
        
        self.trace= pg.PlotDataItem(x= self.sweepData['smua']['v'],y = self.sweepData['smua']['i'],
             pen=self.smuaPen,symbol ='o', symbolBrush =("#4E79A7"),antialias=True)

        self.canvas.addItem(self.trace)
        



    def runSweep(self):


            #check if we only perform a sweep on one smu 
            if self.ui.smuA_grp.isChecked() and self.ui.smuB_grp.isChecked():
                #perform dual smu sweep
                self.sweepDualSMU(self.getSweepValues())
            elif self.ui.smuA_grp.isChecked():
                #perfom sweep on smua
                self.sweepSMU('smua')

            elif self.ui.smuB_grp.isChecked():
                self.sweepSMU('smub')

        
    def sweepSMU(self,smuName):
        self.ui.statusLabel.setText(f"Single Sweep on {smuName} started!")
        
        if smuName == 'smua':
            smuWidget = self.smuaWidget
            smuHandle = self.instr.smua
        else: 
            smuWidget = self.smubWidget
            smuHandle = self.instr.smub

        cfg = smuWidget.getConfig()

        self.canvas.setXRange(min(cfg['vals']),max(cfg['vals']))

        ch_cfg = get_default_channel_config()
        self.instr.applyConfig(smuName,ch_cfg)



        if cfg['force'] == "v":
            force_fun = self.instr.applyVoltage
        else:
            force_fun = self.instr.applyCurrent
        smuHandle.source.output(1)
        for i,val in enumerate(cfg['vals']):
            
            self.ui.statusLabel.setText(f"Seeping {smuName}: {int(i/len(cfg['vals'])*100)} %")
            if self.sweepAborted:    
                break
            force_fun(smuName,val,cfg['limit'])

            results = self.instr.measure(smuName,['i','v'])
            print(f"{val}: {results['v']},{results['i']}")
            self.sweepData[smuName]['i'] = np.append(self.sweepData[smuName]['i'],results['i'])
            self.sweepData[smuName]['v'] = np.append(self.sweepData[smuName]['v'],val)

            self.trace.setData(self.sweepData[smuName]['v'],self.sweepData[smuName]['i'],clear=True)
            QApplication.processEvents()

        if self.sweepAborted:
            self.ui.statusLabel.setText("Sweep Aborted!")
        else:
            self.ui.statusLabel.setText("Sweep Done!")
        smuHandle.source.output(0)
        smuHandle.reset()
        self.sweepAborted = False


    def sweepDualSMU(self,sweepCfg):
        pass

    def stopSweep(self):
        self.sweepAborted = True
    

    def sweepStateChanged(self,state):
        pass

    def getSweepValues(self):
        aVals = {
            'enabled': self.ui.smuA_grp.isChecked(),
            'type': self.ui.aTypeBox.currentText(),
            'limit': self.ui.aLimitVal.value(),
            'start': self.ui.aStartVal.value(),
            'stop': self.ui.aEndVal.value(),
            'npts':self.ui.aNpts.value(),
            'int_time': self.ui.aIntTimeBox.currentText()
        }
        bVals = {
            'enabled': self.ui.smuB_grp.isChecked(),
            'type': self.ui.bTypeBox.currentText(),
            'limit': self.ui.bLimitVal.value(),
            'start': self.ui.bStartVal.value(),
            'stop': self.ui.bEndVal.value(),
            'npts':self.ui.bNpts.value(),
            'int_time': self.ui.bIntTimeBox.currentText()
        }
        return {'smua': aVals,'smub':bVals}

    def renameLimit(self,cfg,limitBox,arg):
        if arg == 0:
            limitBox.setSuffix(" A")
            cfg['source']['forcev'] = True
            cfg['source']['forcei'] = False
        elif arg == 1:
            limitBox.setSuffix(" V")
            cfg['source']['forcev'] = False
            cfg['source']['forcei'] = True

    def clearPlot(self):
        ans = QMessageBox.question(self,"Clear Plot","Are you sure to clean all tracies?")
        if ans == QMessageBox.StandardButton.Yes:
            self.trace.clear()
            self.sweepData['smua']['i'] = []
            self.sweepData['smua']['v'] = []
          
        