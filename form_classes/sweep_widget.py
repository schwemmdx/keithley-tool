
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

        self.smuaWidget = SweepConfigWidget(self,'smua')
        self.smubWidget = SweepConfigWidget(self,'smub')
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.addTab(self.smuaWidget,"SMU A")
        self.ui.tabWidget.addTab(self.smubWidget,"SMU B")


        self.canvas = pg.PlotWidget()

        self.ui.canvasLayout.addWidget(self.canvas)

        self.sweepAborted = False

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


        for target in [
            self.ui.axisXSMU,
            self.ui.axisYSMU,
            self.ui.axisXType,
            self.ui.axisYType
        ]:
            target.currentIndexChanged.connect(self.changeDisplayedData)
        
        
        self.smuaPen = pg.mkPen({'width': 2,'color': "#00aa00",'cosmetic':True})
        
        self.trace= pg.PlotDataItem(x= [],y = [],
             pen=self.smuaPen,symbol='o',antialias=True,symbolPen=pg.mkPen({'width': 1,'color': "#008800",'cosmetic':True}),symbolBrush =pg.mkBrush(wize=0.01,color="#00bb00",cosmetic=True))
        self.changeDisplayedData()
        self.canvas.addItem(self.trace)
        
    
    def changeDisplayedData(self):
        xsmu = self.ui.axisXSMU.currentText().replace(' ','').lower()
        ysmu = self.ui.axisYSMU.currentText().replace(' ','').lower()

        if self.ui.axisXType.currentText() == 'Voltage':
            xVal = 'v'
        else: 
            xVal = 'i'

        if self.ui.axisYType.currentText() == 'Voltage':
            yVal = 'v'
        else: 
            yVal = 'i'
        self.trace.setData(x=self.sweepData[xsmu][xVal],y=self.sweepData[ysmu][yVal])

    def runSweep(self):

            #check if we only perform a sweep on one smu 
            aCfg = self.smuaWidget.getConfig()
            bCfg = self.smubWidget.getConfig()

            if aCfg['type'] == 'unused':
                self.sweepSMU('smub')
            elif bCfg['type'] == 'unused':
                self.sweepSMU('smua')
            else:
                #perform dual smu sweep
                self.sweepDualSMU()
                    

        
    def sweepSMU(self,smuName):
        self.ui.statusLabel.setText(f"Single Sweep on {smuName} started!")

        aCfg = self.smuaWidget.getConfig()
        bCfg = self.smubWidget.getConfig()

        if smuName == 'smua':
            smuWidget = self.smuaWidget
            smuHandle = self.instr.smua

        else: 
            smuWidget = self.smubWidget
            smuHandle = self.instr.smub
        
        cfg = smuWidget.getConfig()

        self.canvas.setXRange(min(cfg['vals']),max(cfg['vals']))

        ch_cfg = get_default_channel_config()
        
        if cfg['force']=='v':
            ch_cfg['source']['limiti'] = cfg['limit']
            ch_cfg['source']['limitv'] = max(cfg['vals'])
        else:
            ch_cfg['source']['limitv'] = cfg['limit']
            ch_cfg['source']['limiti'] = max(cfg['vals'])
        
        self.instr.applyConfig(smuName,ch_cfg)

        smuHandle.measure.delay(0)
       
            
        smuHandle.source.output(1)
        for i,val in enumerate(cfg['vals']):
            
            self.ui.statusLabel.setText(f"Seeping {smuName}: {int(i/len(cfg['vals'])*100)} %")
            if self.sweepAborted:    
                break
            
            if cfg['force'] == "v":
                self.instr.applyVoltage(smuName,val,ilim=cfg['limit'],iRange=cfg['rangei'],vRange=cfg['rangev'])
            else:
                self.instr.applyCurrent(smuName,val,vlim=cfg['limit'],iRange=cfg['rangei'],vRange=cfg['rangev'])
            
            for config,smu_name,handle in zip([aCfg,bCfg],['smua','smub'],[self.instr.smua,self.instr.smub]):
                if not config['type'] == 'unused':
                    if config['measurei']:
                        i = handle.measure.i()
                        self.sweepData[smu_name]['i'] = np.append(self.sweepData[smu_name]['i'],i)
                    if config['measurev']:
                        v = handle.measure.v()
                        self.sweepData[smu_name]['v'] = np.append(self.sweepData[smu_name]['v'],v)

            self.changeDisplayedData()
            QApplication.processEvents()

        if self.sweepAborted:
            self.ui.statusLabel.setText("Sweep Aborted!")
        else:
            self.ui.statusLabel.setText("Sweep Done!")
        smuHandle.source.output(0)
        smuHandle.reset()
        self.sweepAborted = False


    def sweepDualSMU(self):
        
        aCfg = self.smuaWidget.getConfig()
        bCfg = self.smubWidget.getConfig()


        #check if one of the smu's is in constant mode 
        if aCfg['type'] == 'const' or bCfg['type'] == 'const':
            if aCfg['type'] == 'const':
                constCfg = aCfg
                sweepCfg = bCfg
                if bCfg['type'] == 'const':
                    QMessageBox.warning(self,"SMU Sweep Type Clash", "Only one of the SMU's can be configured to output a constant value, not both!\nIf you want to measure an operation point, consider\n\t'basic smu mode'")
                    return
            elif bCfg['type'] == 'const':
                constCfg = bCfg
                sweepCfg = aCfg
            
            self.performConstSweep(constCfg,sweepCfg)
            return
        
        else:
            #both smus really need to be swept:
            for val1 in aCfg['vals']:
                #check force type
                if aCfg['force']=='v':
                    forceFun = self.instr.applyVoltage
                else: 
                    forceFun = self.instr.applyCurrent
                forceFun(aCfg['smu'],val1,aCfg['limit'],aCfg['rangev'],aCfg['rangei'])
                self.instr.smua.source.output(1)
                self.sweepSMU(bCfg['smu'])
        
    
    

        

    def performConstSweep(self,constSMUCfg,SweepSMUCfg):
        if constSMUCfg['smu'] == 'smua':
            constHandle = self.instr.smua
            sweepHandle = self.instr.smub

        if constSMUCfg['force'] == 'v':
            fun = self.instr.applyVoltage
            
        elif constSMUCfg['force'] == 'i':
            fun = self.instr.applyCurrent
        fun(constSMUCfg['smu'],constSMUCfg['vals'][0],constSMUCfg['limit'])
        
        constHandle.source.output(1)
        self.sweepSMU(SweepSMUCfg['smu'])
        constHandle.source.output(0)
        constHandle.reset()

    def stopSweep(self):
        self.sweepAborted = True
    



    def clearPlot(self):
        ans = QMessageBox.question(self,"Clear Plot","Are you sure to clean all tracies?")
        if ans == QMessageBox.StandardButton.Yes:
            self.trace.clear()
            self.sweepData['smua']['i'] = []
            self.sweepData['smua']['v'] = []
            self.sweepData['smub']['i'] = []
            self.sweepData['smub']['v'] = []
          
    

