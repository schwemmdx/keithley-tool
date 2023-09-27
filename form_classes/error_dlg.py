
from typing import Optional
import PySide6.QtCore
from pyforms.ui_error_dlg import Ui_ErrorDlg
from PySide6.QtWidgets import QDialog,QWidget,QTableWidgetItem,QFileDialog,QMessageBox

from modules.keithley_lib import K2636,KeithleyError
from datetime import datetime

class ErrorDialog(QDialog):
    def __init__(self, parent: QWidget,instr: K2636,save_location='logs/error_dump.log',**kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.instr = instr
        self.save_location=save_location
        self.ui = Ui_ErrorDlg()
        self.ui.setupUi(self)
        self.hide()
        self.ui.refreshBtn.clicked.connect(self.read)
        self.ui.saveBtn.clicked.connect(self.save_errors)
        self.ui.clearBtn.clicked.connect(self.clearTable)

    def read(self,save_location = None):
        if save_location:
            sl = save_location
        else:
            sl =self.save_location
        
        errs = self.instr.readErrors(autosave=False,save_location=sl)
        #for err in errs:
        errCount = 0
        if len(errs)>0:
            for err in errs:
                for col,content in zip([0,1,2,3],[err.error_code,err.severity,err.node,err.message]):
                    self.ui.errorTable.setItem(errCount,col,QTableWidgetItem(str(content)))
                errCount+=1

            #self.ui.errorTable.setRowCount(errCount)
        else:
            for col,content in zip([0,1,2,3],['0','-','-','No Errors']):
                self.ui.errorTable.setItem(errCount,col,QTableWidgetItem(str(content)))
            #self.ui.errorTable.setRowCount(20)
        
    def save_errors(self):
        location,_ = QFileDialog.getSaveFileName(self,
                                                 "Save Error List",
                                                 f"{self.save_location}/error_log_{datetime.now().strftime('%Y-%m-%d__%H_%M_%S')}.log",
                                                 )
        if location:
            with open(location,'w') as pSaveFile:
                pSaveFile.write(f"{'Code':<10}\t{'Severity':<10}\t{'Node':<10}\t{'Msg'}\n")
                err = {}
                for row in range(self.ui.errorTable.rowCount()):
                    if self.ui.errorTable.item(row,0):
                        for col,key in zip(range(4),['error_code','severity','node','msg']):
                            err[key] =  self.ui.errorTable.item(row,col).text()
                
                        pSaveFile.write(f"{err['error_code']:<10}\t{err['severity']:<10}\t{err['node']:<10}\t{err['msg']}\n")

    def clearTable(self):
        ans = QMessageBox.question(self,"Delete All Entries..","All Entries will be deleted and are no longer available for later use\nAre You sure?")
        print(ans)
        if ans == QMessageBox.StandardButton.Yes:
            self.ui.errorTable.clearContents()
        