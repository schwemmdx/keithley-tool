# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smu_control_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QWidget)

class Ui_SMUControlWidget(object):
    def setupUi(self, SMUControlWidget):
        if not SMUControlWidget.objectName():
            SMUControlWidget.setObjectName(u"SMUControlWidget")
        SMUControlWidget.resize(1488, 683)
        self.gridLayout_10 = QGridLayout(SMUControlWidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabWidget = QTabWidget(SMUControlWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.smua = QWidget()
        self.smua.setObjectName(u"smua")
        self.gridLayout = QGridLayout(self.smua)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget.addTab(self.smua, "")
        self.smub = QWidget()
        self.smub.setObjectName(u"smub")
        self.gridLayout_2 = QGridLayout(self.smub)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget.addTab(self.smub, "")

        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 2)

        self.pushButton = QPushButton(SMUControlWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_8.addWidget(self.pushButton, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(528, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.groupBox = QGroupBox(SMUControlWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 3, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 0, 3, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 1, 5, 1, 1)

        self.smua_c_2 = QLabel(self.groupBox_2)
        self.smua_c_2.setObjectName(u"smua_c_2")
        self.smua_c_2.setMaximumSize(QSize(200, 50))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(16)
        font.setBold(True)
        self.smua_c_2.setFont(font)
        self.smua_c_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.smua_c_2, 1, 4, 1, 1)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_5.addWidget(self.label_21, 3, 5, 1, 1)

        self.smua_r_2 = QLabel(self.groupBox_2)
        self.smua_r_2.setObjectName(u"smua_r_2")
        self.smua_r_2.setMaximumSize(QSize(200, 50))
        self.smua_r_2.setFont(font)
        self.smua_r_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.smua_r_2, 3, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 2, 3, 1, 1)

        self.smua_v_2 = QLabel(self.groupBox_2)
        self.smua_v_2.setObjectName(u"smua_v_2")
        self.smua_v_2.setMaximumSize(QSize(200, 50))
        self.smua_v_2.setFont(font)
        self.smua_v_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.smua_v_2, 1, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_5.addWidget(self.label_23, 1, 2, 1, 1)

        self.smua_p_2 = QLabel(self.groupBox_2)
        self.smua_p_2.setObjectName(u"smua_p_2")
        self.smua_p_2.setMaximumSize(QSize(200, 50))
        self.smua_p_2.setFont(font)
        self.smua_p_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.smua_p_2, 3, 4, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 268, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.smub_p_2 = QLabel(self.groupBox_3)
        self.smub_p_2.setObjectName(u"smub_p_2")
        self.smub_p_2.setMaximumSize(QSize(200, 50))
        self.smub_p_2.setFont(font)
        self.smub_p_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.smub_p_2, 3, 4, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_6.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_6.addWidget(self.label_26, 1, 2, 1, 1)

        self.smub_v_2 = QLabel(self.groupBox_3)
        self.smub_v_2.setObjectName(u"smub_v_2")
        self.smub_v_2.setMaximumSize(QSize(200, 50))
        self.smub_v_2.setFont(font)
        self.smub_v_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.smub_v_2, 1, 1, 1, 1)

        self.smub_r_2 = QLabel(self.groupBox_3)
        self.smub_r_2.setObjectName(u"smub_r_2")
        self.smub_r_2.setMaximumSize(QSize(200, 50))
        self.smub_r_2.setFont(font)
        self.smub_r_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.smub_r_2, 3, 0, 1, 2)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_6.addWidget(self.label_27, 2, 3, 1, 1)

        self.label_28 = QLabel(self.groupBox_3)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_6.addWidget(self.label_28, 0, 3, 1, 1)

        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_6.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_30 = QLabel(self.groupBox_3)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_6.addWidget(self.label_30, 3, 5, 1, 1)

        self.label_31 = QLabel(self.groupBox_3)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_6.addWidget(self.label_31, 3, 2, 1, 1)

        self.smub_c_2 = QLabel(self.groupBox_3)
        self.smub_c_2.setObjectName(u"smub_c_2")
        self.smub_c_2.setMaximumSize(QSize(200, 50))
        self.smub_c_2.setFont(font)
        self.smub_c_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.smub_c_2, 1, 4, 1, 1)

        self.label_32 = QLabel(self.groupBox_3)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_6.addWidget(self.label_32, 1, 5, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 0, 2, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox, 2, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.plotPlane = QWidget(SMUControlWidget)
        self.plotPlane.setObjectName(u"plotPlane")
        self.gridLayout_9 = QGridLayout(self.plotPlane)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_2 = QSpacerItem(768, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.plotPlane, 0, 1, 1, 1)


        self.retranslateUi(SMUControlWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SMUControlWidget)
    # setupUi

    def retranslateUi(self, SMUControlWidget):
        SMUControlWidget.setWindowTitle(QCoreApplication.translate("SMUControlWidget", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.smua), QCoreApplication.translate("SMUControlWidget", u"SMU A", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.smub), QCoreApplication.translate("SMUControlWidget", u"SMU B", None))
        self.pushButton.setText(QCoreApplication.translate("SMUControlWidget", u"Reset", None))
        self.groupBox.setTitle(QCoreApplication.translate("SMUControlWidget", u"Measurements", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SMUControlWidget", u"SMU A", None))
        self.label_15.setText(QCoreApplication.translate("SMUControlWidget", u"Ohm", None))
        self.label_5.setText(QCoreApplication.translate("SMUControlWidget", u"Current", None))
        self.label_17.setText(QCoreApplication.translate("SMUControlWidget", u"A", None))
        self.smua_c_2.setText(QCoreApplication.translate("SMUControlWidget", u"0.0", None))
        self.label_21.setText(QCoreApplication.translate("SMUControlWidget", u"W", None))
        self.smua_r_2.setText(QCoreApplication.translate("SMUControlWidget", u"0.0", None))
        self.label_6.setText(QCoreApplication.translate("SMUControlWidget", u"Voltage", None))
        self.label_7.setText(QCoreApplication.translate("SMUControlWidget", u"Power", None))
        self.smua_v_2.setText(QCoreApplication.translate("SMUControlWidget", u"0.0", None))
        self.label_23.setText(QCoreApplication.translate("SMUControlWidget", u"V", None))
        self.smua_p_2.setText(QCoreApplication.translate("SMUControlWidget", u"0.0", None))
        self.label_8.setText(QCoreApplication.translate("SMUControlWidget", u"Resistance", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SMUControlWidget", u"SMU B", None))
        self.smub_p_2.setText(QCoreApplication.translate("SMUControlWidget", u"0.0", None))
        self.label_25.setText(QCoreApplication.translate("SMUControlWidget", u"Voltage", None))
        self.label_26.setText(QCoreApplication.translate("SMUControlWidget", u"V", None))
        self.smub_v_2.setText(QCoreApplication.translate("SMUControlWidget", u"0.0", None))
        self.smub_r_2.setText(QCoreApplication.translate("SMUControlWidget", u"0.0", None))
        self.label_27.setText(QCoreApplication.translate("SMUControlWidget", u"Power", None))
        self.label_28.setText(QCoreApplication.translate("SMUControlWidget", u"Current", None))
        self.label_29.setText(QCoreApplication.translate("SMUControlWidget", u"Resistance", None))
        self.label_30.setText(QCoreApplication.translate("SMUControlWidget", u"W", None))
        self.label_31.setText(QCoreApplication.translate("SMUControlWidget", u"Ohm", None))
        self.smub_c_2.setText(QCoreApplication.translate("SMUControlWidget", u"0.0", None))
        self.label_32.setText(QCoreApplication.translate("SMUControlWidget", u"A", None))
    # retranslateUi

