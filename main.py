#!/bin/python

import sys
from PySide6.QtWidgets import QApplication
from form_classes.main_win import MainGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    mainApp  = MainGUI(None)
    mainApp.show()
    ret = app.exec()
    sys.exit(ret)
