# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smu_control_dock.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QToolBox, QToolButton,
    QWidget)

class Ui_SMUControlDock(object):
    def setupUi(self, SMUControlDock):
        if not SMUControlDock.objectName():
            SMUControlDock.setObjectName(u"SMUControlDock")
        SMUControlDock.resize(420, 675)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SMUControlDock.sizePolicy().hasHeightForWidth())
        SMUControlDock.setSizePolicy(sizePolicy)
        SMUControlDock.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        SMUControlDock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolBox = QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        self.smu1 = QWidget()
        self.smu1.setObjectName(u"smu1")
        self.smu1.setGeometry(QRect(0, 0, 402, 552))
        self.gridLayout_2 = QGridLayout(self.smu1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.toolBox.addItem(self.smu1, u"SMU A")
        self.smu2 = QWidget()
        self.smu2.setObjectName(u"smu2")
        self.smu2.setGeometry(QRect(0, 0, 402, 552))
        self.gridLayout_3 = QGridLayout(self.smu2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.toolBox.addItem(self.smu2, u"SMU B")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.detailConfigBtn = QToolButton(self.dockWidgetContents)
        self.detailConfigBtn.setObjectName(u"detailConfigBtn")

        self.gridLayout.addWidget(self.detailConfigBtn, 1, 1, 1, 1)

        self.enableSMUA = QPushButton(self.dockWidgetContents)
        self.enableSMUA.setObjectName(u"enableSMUA")

        self.gridLayout.addWidget(self.enableSMUA, 1, 2, 1, 1)

        self.enableSMUB = QPushButton(self.dockWidgetContents)
        self.enableSMUB.setObjectName(u"enableSMUB")

        self.gridLayout.addWidget(self.enableSMUB, 1, 3, 1, 1)

        SMUControlDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(SMUControlDock)

        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(4)


        QMetaObject.connectSlotsByName(SMUControlDock)
    # setupUi

    def retranslateUi(self, SMUControlDock):
        SMUControlDock.setWindowTitle("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.smu1), QCoreApplication.translate("SMUControlDock", u"SMU A", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.smu2), QCoreApplication.translate("SMUControlDock", u"SMU B", None))
        self.detailConfigBtn.setText(QCoreApplication.translate("SMUControlDock", u"...", None))
        self.enableSMUA.setText(QCoreApplication.translate("SMUControlDock", u"Enable A", None))
        self.enableSMUB.setText(QCoreApplication.translate("SMUControlDock", u"Enable B", None))
    # retranslateUi

