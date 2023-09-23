# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tcp_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_tcpSettings(object):
    def setupUi(self, tcpSettings):
        if not tcpSettings.objectName():
            tcpSettings.setObjectName(u"tcpSettings")
        tcpSettings.setWindowModality(Qt.ApplicationModal)
        tcpSettings.resize(472, 177)
        self.gridLayout = QGridLayout(tcpSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(142, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.label_2 = QLabel(tcpSettings)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.portAddr = QLineEdit(tcpSettings)
        self.portAddr.setObjectName(u"portAddr")

        self.gridLayout.addWidget(self.portAddr, 1, 2, 1, 3)

        self.timeoutVal = QDoubleSpinBox(tcpSettings)
        self.timeoutVal.setObjectName(u"timeoutVal")

        self.gridLayout.addWidget(self.timeoutVal, 2, 2, 1, 1)

        self.applyBtn = QPushButton(tcpSettings)
        self.applyBtn.setObjectName(u"applyBtn")

        self.gridLayout.addWidget(self.applyBtn, 4, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(359, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 3)

        self.label = QLabel(tcpSettings)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(tcpSettings)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)

        self.label_3 = QLabel(tcpSettings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.ipAddr = QLineEdit(tcpSettings)
        self.ipAddr.setObjectName(u"ipAddr")
        self.ipAddr.setMaxLength(40)
        self.ipAddr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ipAddr.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.ipAddr, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)


        self.retranslateUi(tcpSettings)

        QMetaObject.connectSlotsByName(tcpSettings)
    # setupUi

    def retranslateUi(self, tcpSettings):
        tcpSettings.setWindowTitle(QCoreApplication.translate("tcpSettings", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("tcpSettings", u"Port", None))
        self.portAddr.setText(QCoreApplication.translate("tcpSettings", u"5025", None))
        self.applyBtn.setText(QCoreApplication.translate("tcpSettings", u"OK", None))
        self.label.setText(QCoreApplication.translate("tcpSettings", u"IP Adress", None))
        self.label_4.setText(QCoreApplication.translate("tcpSettings", u"s", None))
        self.label_3.setText(QCoreApplication.translate("tcpSettings", u"Timeout", None))
        self.ipAddr.setText(QCoreApplication.translate("tcpSettings", u"192.168.0.56", None))
    # retranslateUi

