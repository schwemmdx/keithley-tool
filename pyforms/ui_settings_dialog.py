# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(640, 480)
        self.gridLayout = QGridLayout(SettingsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabSettings = QTabWidget(SettingsDialog)
        self.tabSettings.setObjectName(u"tabSettings")
        self.tabSettings.setTabPosition(QTabWidget.North)
        self.tcpSettings = QWidget()
        self.tcpSettings.setObjectName(u"tcpSettings")
        self.gridLayout_2 = QGridLayout(self.tcpSettings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.tcpSettings)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.tcpSettings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.portAddr = QLineEdit(self.tcpSettings)
        self.portAddr.setObjectName(u"portAddr")

        self.gridLayout_2.addWidget(self.portAddr, 1, 3, 1, 1)

        self.timeoutVal = QDoubleSpinBox(self.tcpSettings)
        self.timeoutVal.setObjectName(u"timeoutVal")

        self.gridLayout_2.addWidget(self.timeoutVal, 2, 3, 1, 1)

        self.ipAddr = QLineEdit(self.tcpSettings)
        self.ipAddr.setObjectName(u"ipAddr")
        self.ipAddr.setMaxLength(40)
        self.ipAddr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ipAddr.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.ipAddr, 0, 2, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.label_2 = QLabel(self.tcpSettings)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 2, 1, 1)

        icon = QIcon(QIcon.fromTheme(u"network-transmit-receive"))
        self.tabSettings.addTab(self.tcpSettings, icon, "")
        self.miscSettings = QWidget()
        self.miscSettings.setObjectName(u"miscSettings")
        icon1 = QIcon(QIcon.fromTheme(u"system-run"))
        self.tabSettings.addTab(self.miscSettings, icon1, "")
        self.graphSettings = QWidget()
        self.graphSettings.setObjectName(u"graphSettings")
        icon2 = QIcon(QIcon.fromTheme(u"image-loading"))
        self.tabSettings.addTab(self.graphSettings, icon2, "")

        self.gridLayout.addWidget(self.tabSettings, 0, 0, 1, 3)

        self.pushButton_2 = QPushButton(SettingsDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton = QPushButton(SettingsDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(447, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.retranslateUi(SettingsDialog)

        self.tabSettings.setCurrentIndex(0)
        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"IP Adress", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"RX Timeout", None))
        self.portAddr.setText(QCoreApplication.translate("SettingsDialog", u"5025", None))
        self.ipAddr.setText(QCoreApplication.translate("SettingsDialog", u"192.168.0.56", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Port", None))
        self.tabSettings.setTabText(self.tabSettings.indexOf(self.tcpSettings), QCoreApplication.translate("SettingsDialog", u"Connection", None))
        self.tabSettings.setTabText(self.tabSettings.indexOf(self.miscSettings), QCoreApplication.translate("SettingsDialog", u"Misc.", None))
        self.tabSettings.setTabText(self.tabSettings.indexOf(self.graphSettings), QCoreApplication.translate("SettingsDialog", u"Graph", None))
        self.pushButton_2.setText(QCoreApplication.translate("SettingsDialog", u"Abort", None))
        self.pushButton.setText(QCoreApplication.translate("SettingsDialog", u"OK", None))
    # retranslateUi

