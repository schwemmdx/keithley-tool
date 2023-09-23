from typing import Optional

from pyforms.ui_settings_dialog import *
from PySide6.QtWidgets import QDialog

class SettingsDialog(QDialog):
    def __init__(self, parent=None,**kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.hide()


        ##later use settings-file for loading previous data
        self.data = {
            'tcp':{
                'ip': "192.168.0.57",
                'port': 5025,
                'timeout': 1000
            },
            'misc': {},
            'graph':{}
        }

        self.__setData()

        self.ui.buttonBox.accepted.connect(self.on_ok_clicked)
        self.ui.buttonBox.rejected.connect(self.on_reject_cklicked)


    def __setData(self):
        self.ui.timeoutVal.setValue(self.data['tcp']['timeout'])
        self.ui.ipAddr.setText(self.data['tcp']['ip'])
        self.ui.portVal.setValue(self.data['tcp']['port'])
        
    def __getData(self):
         
        self.data['tcp'] = {
            'ip': self.ui.ipAddr.text(),
            'port' : self.ui.portVal.value(),
            'timeout': self.ui.timeoutVal.value()
        }

        self.data['misc'] = {}
        self.data['graph'] = {}
        

    def getTCPSettings(self):
        return self.data['tcp']   

    def on_reject_cklicked(self):
        self.__setData()
        self.hide()     
    
    def on_ok_clicked(self):
        self.__getData()
        self.hide()