# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'measure_dock.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QGridLayout, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)

class Ui_measureDock(object):
    def setupUi(self, measureDock):
        if not measureDock.objectName():
            measureDock.setObjectName(u"measureDock")
        measureDock.resize(1287, 190)
        measureDock.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        measureDock.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.TopDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_4 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 5, 1, 1)

        self.smua_c = QLabel(self.groupBox)
        self.smua_c.setObjectName(u"smua_c")
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(16)
        font.setBold(True)
        self.smua_c.setFont(font)
        self.smua_c.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.smua_c, 1, 4, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 5, 1, 1)

        self.smua_r = QLabel(self.groupBox)
        self.smua_r.setObjectName(u"smua_r")
        self.smua_r.setFont(font)
        self.smua_r.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.smua_r, 3, 0, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)

        self.smua_v = QLabel(self.groupBox)
        self.smua_v.setObjectName(u"smua_v")
        self.smua_v.setFont(font)
        self.smua_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.smua_v, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)

        self.smua_p = QLabel(self.groupBox)
        self.smua_p.setObjectName(u"smua_p")
        self.smua_p.setFont(font)
        self.smua_p.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.smua_p, 3, 4, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 4, 1)

        self.statusField = QLabel(self.dockWidgetContents)
        self.statusField.setObjectName(u"statusField")
        self.statusField.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.statusField, 0, 4, 1, 1)

        self.groupBox_3 = QGroupBox(self.dockWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.smub_p = QLabel(self.groupBox_3)
        self.smub_p.setObjectName(u"smub_p")
        self.smub_p.setFont(font)
        self.smub_p.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.smub_p, 3, 4, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)

        self.smub_v = QLabel(self.groupBox_3)
        self.smub_v.setObjectName(u"smub_v")
        self.smub_v.setFont(font)
        self.smub_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.smub_v, 1, 1, 1, 1)

        self.smub_r = QLabel(self.groupBox_3)
        self.smub_r.setObjectName(u"smub_r")
        self.smub_r.setFont(font)
        self.smub_r.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.smub_r, 3, 0, 1, 2)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 2, 3, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 0, 3, 1, 1)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 3, 5, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 3, 2, 1, 1)

        self.smub_c = QLabel(self.groupBox_3)
        self.smub_c.setObjectName(u"smub_c")
        self.smub_c.setFont(font)
        self.smub_c.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.smub_c, 1, 4, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 1, 5, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 8, 4, 1)

        self.label_5 = QLabel(self.dockWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 1, 1, 1)

        self.intervalBox = QComboBox(self.dockWidgetContents)
        self.intervalBox.addItem("")
        self.intervalBox.addItem("")
        self.intervalBox.addItem("")
        self.intervalBox.addItem("")
        self.intervalBox.addItem("")
        self.intervalBox.addItem("")
        self.intervalBox.addItem("")
        self.intervalBox.setObjectName(u"intervalBox")

        self.gridLayout_4.addWidget(self.intervalBox, 1, 2, 1, 1)

        self.label_6 = QLabel(self.dockWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(298, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.measureOptionsBtn = QToolButton(self.dockWidgetContents)
        self.measureOptionsBtn.setObjectName(u"measureOptionsBtn")

        self.gridLayout_4.addWidget(self.measureOptionsBtn, 1, 5, 1, 1)

        self.holdPeak = QPushButton(self.dockWidgetContents)
        self.holdPeak.setObjectName(u"holdPeak")

        self.gridLayout_4.addWidget(self.holdPeak, 1, 6, 1, 1)

        self.recordBtn = QPushButton(self.dockWidgetContents)
        self.recordBtn.setObjectName(u"recordBtn")

        self.gridLayout_4.addWidget(self.recordBtn, 1, 7, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 29, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 2, 6, 1, 1)

        self.groupBox_4 = QGroupBox(self.dockWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.smua_complience = QCheckBox(self.groupBox_4)
        self.smua_complience.setObjectName(u"smua_complience")
        self.smua_complience.setCheckable(False)

        self.gridLayout_3.addWidget(self.smua_complience, 0, 0, 1, 1)

        self.smub_complience = QCheckBox(self.groupBox_4)
        self.smub_complience.setObjectName(u"smub_complience")
        self.smub_complience.setCheckable(False)

        self.gridLayout_3.addWidget(self.smub_complience, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 3, 1, 1, 7)

        measureDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(measureDock)

        QMetaObject.connectSlotsByName(measureDock)
    # setupUi

    def retranslateUi(self, measureDock):
        measureDock.setWindowTitle(QCoreApplication.translate("measureDock", u"Measurements", None))
        self.groupBox.setTitle(QCoreApplication.translate("measureDock", u"SMU A", None))
        self.label_10.setText(QCoreApplication.translate("measureDock", u"Ohm", None))
        self.label_2.setText(QCoreApplication.translate("measureDock", u"Current", None))
        self.label_11.setText(QCoreApplication.translate("measureDock", u"A", None))
        self.smua_c.setText(QCoreApplication.translate("measureDock", u"0.0", None))
        self.label_12.setText(QCoreApplication.translate("measureDock", u"W", None))
        self.smua_r.setText(QCoreApplication.translate("measureDock", u"0.0", None))
        self.label.setText(QCoreApplication.translate("measureDock", u"Voltage", None))
        self.label_4.setText(QCoreApplication.translate("measureDock", u"Power", None))
        self.smua_v.setText(QCoreApplication.translate("measureDock", u"0.0", None))
        self.label_9.setText(QCoreApplication.translate("measureDock", u"V", None))
        self.smua_p.setText(QCoreApplication.translate("measureDock", u"0.0", None))
        self.label_3.setText(QCoreApplication.translate("measureDock", u"Resistance", None))
        self.statusField.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("measureDock", u"SMU B", None))
        self.smub_p.setText(QCoreApplication.translate("measureDock", u"0.0", None))
        self.label_13.setText(QCoreApplication.translate("measureDock", u"Voltage", None))
        self.label_16.setText(QCoreApplication.translate("measureDock", u"V", None))
        self.smub_v.setText(QCoreApplication.translate("measureDock", u"0.0", None))
        self.smub_r.setText(QCoreApplication.translate("measureDock", u"0.0", None))
        self.label_20.setText(QCoreApplication.translate("measureDock", u"Power", None))
        self.label_14.setText(QCoreApplication.translate("measureDock", u"Current", None))
        self.label_19.setText(QCoreApplication.translate("measureDock", u"Resistance", None))
        self.label_24.setText(QCoreApplication.translate("measureDock", u"W", None))
        self.label_22.setText(QCoreApplication.translate("measureDock", u"Ohm", None))
        self.smub_c.setText(QCoreApplication.translate("measureDock", u"0.0", None))
        self.label_18.setText(QCoreApplication.translate("measureDock", u"A", None))
        self.label_5.setText(QCoreApplication.translate("measureDock", u"Interval", None))
        self.intervalBox.setItemText(0, QCoreApplication.translate("measureDock", u"1", None))
        self.intervalBox.setItemText(1, QCoreApplication.translate("measureDock", u"0.1", None))
        self.intervalBox.setItemText(2, QCoreApplication.translate("measureDock", u"2", None))
        self.intervalBox.setItemText(3, QCoreApplication.translate("measureDock", u"5", None))
        self.intervalBox.setItemText(4, QCoreApplication.translate("measureDock", u"30", None))
        self.intervalBox.setItemText(5, QCoreApplication.translate("measureDock", u"60", None))
        self.intervalBox.setItemText(6, QCoreApplication.translate("measureDock", u"ASAP", None))

        self.label_6.setText(QCoreApplication.translate("measureDock", u"s", None))
        self.measureOptionsBtn.setText(QCoreApplication.translate("measureDock", u"...", None))
        self.holdPeak.setText(QCoreApplication.translate("measureDock", u"Hold Peak", None))
        self.recordBtn.setText(QCoreApplication.translate("measureDock", u"Record", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("measureDock", u"Complience", None))
        self.smua_complience.setText(QCoreApplication.translate("measureDock", u"SMUA", None))
        self.smub_complience.setText(QCoreApplication.translate("measureDock", u"SMUB", None))
    # retranslateUi

