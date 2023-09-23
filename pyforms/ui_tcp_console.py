# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tcp_console.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_tcpConsole(object):
    def setupUi(self, tcpConsole):
        if not tcpConsole.objectName():
            tcpConsole.setObjectName(u"tcpConsole")
        tcpConsole.resize(684, 446)
        font = QFont()
        font.setKerning(False)
        tcpConsole.setFont(font)
        self.gridLayout = QGridLayout(tcpConsole)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sendBtn = QPushButton(tcpConsole)
        self.sendBtn.setObjectName(u"sendBtn")

        self.gridLayout.addWidget(self.sendBtn, 1, 1, 1, 1)

        self.consoleHistory = QTextEdit(tcpConsole)
        self.consoleHistory.setObjectName(u"consoleHistory")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(11)
        font1.setKerning(False)
        self.consoleHistory.setFont(font1)
        self.consoleHistory.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.consoleHistory.setLineWrapColumnOrWidth(80)
        self.consoleHistory.setReadOnly(True)

        self.gridLayout.addWidget(self.consoleHistory, 0, 0, 1, 2)

        self.inputLine = QLineEdit(tcpConsole)
        self.inputLine.setObjectName(u"inputLine")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(11)
        font2.setKerning(True)
        self.inputLine.setFont(font2)
        self.inputLine.setFrame(False)
        self.inputLine.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.inputLine, 1, 0, 1, 1)


        self.retranslateUi(tcpConsole)

        QMetaObject.connectSlotsByName(tcpConsole)
    # setupUi

    def retranslateUi(self, tcpConsole):
        tcpConsole.setWindowTitle(QCoreApplication.translate("tcpConsole", u"Raw Console", None))
        self.sendBtn.setText(QCoreApplication.translate("tcpConsole", u"Send", None))
    # retranslateUi

