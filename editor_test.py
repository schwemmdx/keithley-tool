# editor.py


import sys
from PySide6 import QtGui

from PySide6.QtWidgets import QApplication,QPlainTextEdit
import syntax

app = QApplication(sys.argv)

editor = QPlainTextEdit()
highlight = syntax.PythonHighlighter(editor.document())
editor.show()

# Load syntax.py into the editor for demo purposes
infile = open('syntax.py', 'r')
editor.setPlainText(infile.read())

app.exec_()