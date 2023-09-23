# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QSizePolicy,
    QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1418, 771)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionConnect.setCheckable(True)
        icon = QIcon(QIcon.fromTheme(u"network-wired"))
        self.actionConnect.setIcon(icon)
        self.actionRaw_Console = QAction(MainWindow)
        self.actionRaw_Console.setObjectName(u"actionRaw_Console")
        self.actionRaw_Console.setEnabled(True)
        icon1 = QIcon(QIcon.fromTheme(u"utilities-terminal"))
        self.actionRaw_Console.setIcon(icon1)
        self.actionScripts = QAction(MainWindow)
        self.actionScripts.setObjectName(u"actionScripts")
        icon2 = QIcon(QIcon.fromTheme(u"application-x-executable"))
        self.actionScripts.setIcon(icon2)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        icon3 = QIcon(QIcon.fromTheme(u"package-x-generic"))
        self.actionSettings.setIcon(icon3)
        self.actionBasic_SMU_Control = QAction(MainWindow)
        self.actionBasic_SMU_Control.setObjectName(u"actionBasic_SMU_Control")
        icon4 = QIcon(QIcon.fromTheme(u"utilities-system-monitor"))
        self.actionBasic_SMU_Control.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QSize(36, 0))
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.LeftToolBarArea)
        self.toolBar.setOrientation(Qt.Vertical)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addAction(self.actionBasic_SMU_Control)
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionRaw_Console)
        self.toolBar.addAction(self.actionScripts)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.actionConnect.setToolTip(QCoreApplication.translate("MainWindow", u"Connect", None))
#endif // QT_CONFIG(tooltip)
        self.actionRaw_Console.setText(QCoreApplication.translate("MainWindow", u"Raw Console", None))
        self.actionScripts.setText(QCoreApplication.translate("MainWindow", u"Scripts", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionBasic_SMU_Control.setText(QCoreApplication.translate("MainWindow", u"Basic SMU Control", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

