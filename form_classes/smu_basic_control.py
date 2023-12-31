from pyforms.ui_smu_control_widget import *
from pyforms.ui_smu_basic_control import *
from PySide6.QtWidgets import QWidget

from modules import K2636
from threading import Thread
from time import sleep

import numpy as np

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

        self.secMeasInterval = 1.0

        self.measureData = {
            'smua':
            {
                'vItem' : pg.PlotItem(),
                'iItem' : pg.PlotItem(),
                'v' :np.array([]),
                'i' :np.array([]),
            },
            'smub':
            {
                'vItem' : pg.PlotItem(),
                'iItem' : pg.PlotItem(),
                'v' :np.array([]),
                'i' :np.array([]),
            },
            'comul_time':np.array([])
        }
        

        self.measureThread =Thread(target=self.measureTask)
        

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


        
        self.view = pg.GraphicsLayoutWidget(size=(100,100))
        self.ui.graphLayout.addWidget(self.view)


        # self.ui.graphLayout.addWidget(self.lowerCanvas)
        

        self.smuaPen = pg.mkPen({'width': 2,'color': "#4E79A7",'cosmetic':True})
        self.smubPen = pg.mkPen({'width': 2,'color': "#F28E2B",'cosmetic':True})
       
       
        self.measureData['smua']['vItem']= pg.PlotDataItem(x= self.measureData['comul_time'],
                                                        y = self.measureData['smua']['v'],
                                                        pen=self.smuaPen,
                                                        symbol ='o', 
                                                        symbolBrush =("#4E79A7"),
                                                        antialias=True
                                                        )
       
        self.measureData['smua']['iItem']= pg.PlotDataItem(x= self.measureData['comul_time'],y = self.measureData['smua']['i'],
             pen=self.smuaPen,symbol ='o', symbolBrush =("#4E79A7"),antialias=True)
        
        self.measureData['smub']['vItem']= pg.PlotDataItem(x= self.measureData['comul_time'],y = self.measureData['smub']['v'],
             pen=self.smubPen,symbol ='s', symbolBrush =("#F28E2B"),antialias=True)
        self.measureData['smub']['iItem']= pg.PlotDataItem(x= self.measureData['comul_time'],y = self.measureData['smub']['i'],
             pen=self.smubPen,symbol ='s', symbolBrush =("#F28E2B"),antialias=True)
        
        
        
        self.upperCanvas = self.view.addPlot(row=0,col=0)
        self.lowerCanvas = self.view.addPlot(row=1,col=0)
        self.upperCanvas.setLabel('left', "Voltage [V]")
        self.lowerCanvas.setLabel('left', "Current [A]")
        self.lowerCanvas.setLabel('bottom', "Time  [n*s]")


        self.upperCanvas.setXLink(self.lowerCanvas)
        self.upperCanvas.getAxis('bottom').setStyle(showValues=False)

        self.upperCanvas.addItem(self.measureData['smua']['vItem'])
        self.lowerCanvas.addItem(self.measureData['smua']['iItem'])
        
        self.measureData['smua']['vItem']


        self.lowerCanvas.addItem(self.measureData['smub']['iItem'])
        self.upperCanvas.addItem(self.measureData['smub']['vItem'])

        self.ui.resetInstrBtn.clicked.connect(self.instr.reset)
        self.ui.clearGraphBtn.clicked.connect(self.clearGraphData)
        self.ui.measInterval.currentIndexChanged.connect(self.measIntervalChanged)
        

        self.measureThreadShouldRun = True
        self.measureThread.start()
    
    def measIntervalChanged(self):
        text = self.ui.measInterval.currentText()
        val,suffix = text.split(' ')
        if suffix == 'ms':
            self.secMeasInterval = float(val)/1e3
        if suffix == 's':
            self.secMeasInterval = float(val)
        

    def measureTask(self):

        while self.measureThreadShouldRun:
            self.measureData['comul_time'] = np.concatenate([self.measureData['comul_time'],[len(self.measureData['comul_time'])]],0)
            for name,box,uiFields in zip(['smua','smub'],[self.ui.smua_grpBox,self.ui.smub_grpBox],
                                     [(self.ui.smua_v,self.ui.smua_i,self.ui.smua_r,self.ui.smua_p),
                                      (self.ui.smub_v,self.ui.smub_i,self.ui.smub_r,self.ui.smub_p)]):
                
                if box.isChecked():
                    params = self.instr.measure(name,['v','i'])
                    try:
                        v = float(params['v'])  
                    except:
                        v = np.nan

                    try:
                        i = float(params['i'])
                    except:
                        i = np.nan
                 
                    self.measureData[name]['v'] = np.concatenate([self.measureData[name]['v'],[v]],0)
                    self.measureData[name]['i'] = np.concatenate([self.measureData[name]['i'],[i]],0)

                    uiFields[0].setText(f"{v:2.3e}")
                    uiFields[1].setText(f"{i:2.3e}")
                    uiFields[2].setText(f"{v/i:2.3e}")
                    uiFields[3].setText(f"{v*i:2.3e}")  

                    self.measureData[name]['vItem'].setData(self.measureData['comul_time'],y= self.measureData[name]['v'])
                    self.measureData[name]['iItem'].setData(self.measureData['comul_time'],y = self.measureData[name]['i'])

                    
                else:
                    for val in uiFields:
                        val.setText('0.0')

            self.measureData['comul_time'] = np.concatenate([self.measureData['comul_time'],[len(self.measureData['comul_time'])]],0)
            
            sleep(self.secMeasInterval)
            


    def killMeasureThread(self):
        self.measureThreadShouldRun = False

    def clearGraphData(self):
        for smu in ['smua','smub']:
            for data,item in zip(['i','v'],['vItem','iItem']):
                self.measureData[smu][data] = np.array([])
                self.measureData[smu][item].setData(self.measureData['comul_time'],self.measureData[smu][data])

