# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smu_basic_control.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_SMUBasicControl(object):
    def setupUi(self, SMUBasicControl):
        if not SMUBasicControl.objectName():
            SMUBasicControl.setObjectName(u"SMUBasicControl")
        SMUBasicControl.resize(434, 471)
        self.gridLayout = QGridLayout(SMUBasicControl)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_5 = QGroupBox(SMUBasicControl)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_11 = QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.voltForceCheck = QCheckBox(self.groupBox_5)
        self.voltForceCheck.setObjectName(u"voltForceCheck")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voltForceCheck.sizePolicy().hasHeightForWidth())
        self.voltForceCheck.setSizePolicy(sizePolicy)
        self.voltForceCheck.setChecked(True)
        self.voltForceCheck.setAutoExclusive(True)

        self.gridLayout_11.addWidget(self.voltForceCheck, 0, 4, 1, 1)

        self.sourceCurrVal = QDoubleSpinBox(self.groupBox_5)
        self.sourceCurrVal.setObjectName(u"sourceCurrVal")
        self.sourceCurrVal.setDecimals(3)
        self.sourceCurrVal.setMinimum(-999.000000000000000)
        self.sourceCurrVal.setMaximum(999.000000000000000)
        self.sourceCurrVal.setValue(10.000000000000000)

        self.gridLayout_11.addWidget(self.sourceCurrVal, 1, 2, 1, 1)

        self.currForceCheck = QCheckBox(self.groupBox_5)
        self.currForceCheck.setObjectName(u"currForceCheck")
        sizePolicy.setHeightForWidth(self.currForceCheck.sizePolicy().hasHeightForWidth())
        self.currForceCheck.setSizePolicy(sizePolicy)
        self.currForceCheck.setAutoExclusive(True)
        self.currForceCheck.setTristate(False)

        self.gridLayout_11.addWidget(self.currForceCheck, 1, 4, 1, 1)

        self.sourceVoltPrefix = QComboBox(self.groupBox_5)
        self.sourceVoltPrefix.addItem("")
        self.sourceVoltPrefix.addItem("")
        self.sourceVoltPrefix.addItem("")
        self.sourceVoltPrefix.addItem("")
        self.sourceVoltPrefix.setObjectName(u"sourceVoltPrefix")

        self.gridLayout_11.addWidget(self.sourceVoltPrefix, 0, 3, 1, 1)

        self.label_25 = QLabel(self.groupBox_5)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_11.addWidget(self.label_25, 0, 0, 1, 1)

        self.sourceVoltVal = QDoubleSpinBox(self.groupBox_5)
        self.sourceVoltVal.setObjectName(u"sourceVoltVal")
        self.sourceVoltVal.setDecimals(3)
        self.sourceVoltVal.setMinimum(-999.000000000000000)
        self.sourceVoltVal.setMaximum(999.000000000000000)
        self.sourceVoltVal.setValue(1.000000000000000)

        self.gridLayout_11.addWidget(self.sourceVoltVal, 0, 2, 1, 1)

        self.label_26 = QLabel(self.groupBox_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_11.addWidget(self.label_26, 1, 0, 1, 1)

        self.sourceCurrPrefix = QComboBox(self.groupBox_5)
        self.sourceCurrPrefix.addItem("")
        self.sourceCurrPrefix.addItem("")
        self.sourceCurrPrefix.addItem("")
        self.sourceCurrPrefix.addItem("")
        self.sourceCurrPrefix.addItem("")
        self.sourceCurrPrefix.setObjectName(u"sourceCurrPrefix")
        sizePolicy.setHeightForWidth(self.sourceCurrPrefix.sizePolicy().hasHeightForWidth())
        self.sourceCurrPrefix.setSizePolicy(sizePolicy)

        self.gridLayout_11.addWidget(self.sourceCurrPrefix, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_5, 0, 0, 1, 5)

        self.groupBox_9 = QGroupBox(SMUBasicControl)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_10 = QGridLayout(self.groupBox_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.measCurrRange = QComboBox(self.groupBox_9)
        self.measCurrRange.addItem("")
        self.measCurrRange.addItem("")
        self.measCurrRange.addItem("")
        self.measCurrRange.addItem("")
        self.measCurrRange.setObjectName(u"measCurrRange")

        self.gridLayout_10.addWidget(self.measCurrRange, 1, 2, 1, 1)

        self.label_27 = QLabel(self.groupBox_9)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_10.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_28 = QLabel(self.groupBox_9)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_10.addWidget(self.label_28, 0, 0, 1, 1)

        self.measVoltRange = QComboBox(self.groupBox_9)
        self.measVoltRange.addItem("")
        self.measVoltRange.addItem("")
        self.measVoltRange.addItem("")
        self.measVoltRange.addItem("")
        self.measVoltRange.addItem("")
        self.measVoltRange.setObjectName(u"measVoltRange")
        self.measVoltRange.setAutoFillBackground(True)

        self.gridLayout_10.addWidget(self.measVoltRange, 0, 2, 1, 1)

        self.label_37 = QLabel(self.groupBox_9)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_10.addWidget(self.label_37, 2, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_11, 0, 1, 1, 1)

        self.measInterval = QComboBox(self.groupBox_9)
        self.measInterval.addItem("")
        self.measInterval.addItem("")
        self.measInterval.addItem("")
        self.measInterval.addItem("")
        self.measInterval.setObjectName(u"measInterval")

        self.gridLayout_10.addWidget(self.measInterval, 2, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_9)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.checkBox = QCheckBox(self.groupBox_9)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox_9)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_9)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.groupBox_9)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout.addWidget(self.checkBox_4)


        self.gridLayout_10.addLayout(self.horizontalLayout, 3, 0, 1, 3)


        self.gridLayout.addWidget(self.groupBox_9, 1, 0, 1, 5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(129, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(SMUBasicControl)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton = QPushButton(SMUBasicControl)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 3, 1, 1)

        self.pushButton_2 = QPushButton(SMUBasicControl)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 4, 1, 1)


        self.retranslateUi(SMUBasicControl)

        QMetaObject.connectSlotsByName(SMUBasicControl)
    # setupUi

    def retranslateUi(self, SMUBasicControl):
        SMUBasicControl.setWindowTitle(QCoreApplication.translate("SMUBasicControl", u"Form", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SMUBasicControl", u"Source Configuration", None))
        self.voltForceCheck.setText(QCoreApplication.translate("SMUBasicControl", u"Force", None))
        self.currForceCheck.setText(QCoreApplication.translate("SMUBasicControl", u"Force", None))
        self.sourceVoltPrefix.setItemText(0, QCoreApplication.translate("SMUBasicControl", u"V", None))
        self.sourceVoltPrefix.setItemText(1, QCoreApplication.translate("SMUBasicControl", u"mV", None))
        self.sourceVoltPrefix.setItemText(2, QCoreApplication.translate("SMUBasicControl", u"\u00b5V", None))
        self.sourceVoltPrefix.setItemText(3, QCoreApplication.translate("SMUBasicControl", u"nV", None))

        self.label_25.setText(QCoreApplication.translate("SMUBasicControl", u"Voltage", None))
        self.sourceVoltVal.setPrefix("")
        self.sourceVoltVal.setSuffix("")
        self.label_26.setText(QCoreApplication.translate("SMUBasicControl", u"Current", None))
        self.sourceCurrPrefix.setItemText(0, QCoreApplication.translate("SMUBasicControl", u"mA", None))
        self.sourceCurrPrefix.setItemText(1, QCoreApplication.translate("SMUBasicControl", u"\u00b5A", None))
        self.sourceCurrPrefix.setItemText(2, QCoreApplication.translate("SMUBasicControl", u"nA", None))
        self.sourceCurrPrefix.setItemText(3, QCoreApplication.translate("SMUBasicControl", u"pA", None))
        self.sourceCurrPrefix.setItemText(4, QCoreApplication.translate("SMUBasicControl", u"A", None))

        self.groupBox_9.setTitle(QCoreApplication.translate("SMUBasicControl", u"Measure Configuration", None))
        self.measCurrRange.setItemText(0, QCoreApplication.translate("SMUBasicControl", u"Auto", None))
        self.measCurrRange.setItemText(1, QCoreApplication.translate("SMUBasicControl", u"1e-3", None))
        self.measCurrRange.setItemText(2, QCoreApplication.translate("SMUBasicControl", u"1e-6", None))
        self.measCurrRange.setItemText(3, QCoreApplication.translate("SMUBasicControl", u"1e-9", None))

        self.label_27.setText(QCoreApplication.translate("SMUBasicControl", u"Current Range", None))
        self.label_28.setText(QCoreApplication.translate("SMUBasicControl", u"Voltage Range", None))
        self.measVoltRange.setItemText(0, QCoreApplication.translate("SMUBasicControl", u"Auto", None))
        self.measVoltRange.setItemText(1, QCoreApplication.translate("SMUBasicControl", u"1e-3", None))
        self.measVoltRange.setItemText(2, QCoreApplication.translate("SMUBasicControl", u"1e-6", None))
        self.measVoltRange.setItemText(3, QCoreApplication.translate("SMUBasicControl", u"1e-9", None))
        self.measVoltRange.setItemText(4, "")

        self.label_37.setText(QCoreApplication.translate("SMUBasicControl", u"Measure Interval", None))
        self.measInterval.setItemText(0, QCoreApplication.translate("SMUBasicControl", u"1 s", None))
        self.measInterval.setItemText(1, QCoreApplication.translate("SMUBasicControl", u"0,1 s", None))
        self.measInterval.setItemText(2, QCoreApplication.translate("SMUBasicControl", u"0,5 s", None))
        self.measInterval.setItemText(3, QCoreApplication.translate("SMUBasicControl", u"10 s", None))

        self.label.setText(QCoreApplication.translate("SMUBasicControl", u"Selection", None))
        self.checkBox.setText(QCoreApplication.translate("SMUBasicControl", u"V", None))
        self.checkBox_2.setText(QCoreApplication.translate("SMUBasicControl", u"I", None))
        self.checkBox_3.setText(QCoreApplication.translate("SMUBasicControl", u"R", None))
        self.checkBox_4.setText(QCoreApplication.translate("SMUBasicControl", u"P", None))
        self.pushButton_3.setText(QCoreApplication.translate("SMUBasicControl", u"Reset", None))
        self.pushButton.setText(QCoreApplication.translate("SMUBasicControl", u"Apply", None))
        self.pushButton_2.setText(QCoreApplication.translate("SMUBasicControl", u"Enable", None))
    # retranslateUi

