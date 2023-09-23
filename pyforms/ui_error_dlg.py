# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_dlg.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_ErrorDlg(object):
    def setupUi(self, ErrorDlg):
        if not ErrorDlg.objectName():
            ErrorDlg.setObjectName(u"ErrorDlg")
        ErrorDlg.setWindowModality(Qt.ApplicationModal)
        ErrorDlg.resize(853, 512)
        self.gridLayout = QGridLayout(ErrorDlg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.clearBtn = QPushButton(ErrorDlg)
        self.clearBtn.setObjectName(u"clearBtn")

        self.gridLayout.addWidget(self.clearBtn, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(ErrorDlg)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 5)

        self.okBtn = QPushButton(ErrorDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.gridLayout.addWidget(self.okBtn, 1, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(428, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.refreshBtn = QPushButton(ErrorDlg)
        self.refreshBtn.setObjectName(u"refreshBtn")

        self.gridLayout.addWidget(self.refreshBtn, 1, 3, 1, 1)

        self.saveBtn = QPushButton(ErrorDlg)
        self.saveBtn.setObjectName(u"saveBtn")

        self.gridLayout.addWidget(self.saveBtn, 1, 2, 1, 1)


        self.retranslateUi(ErrorDlg)

        QMetaObject.connectSlotsByName(ErrorDlg)
    # setupUi

    def retranslateUi(self, ErrorDlg):
        ErrorDlg.setWindowTitle(QCoreApplication.translate("ErrorDlg", u"Form", None))
        self.clearBtn.setText(QCoreApplication.translate("ErrorDlg", u"Clear", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ErrorDlg", u"Error Code", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ErrorDlg", u"Severity", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ErrorDlg", u"Node", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ErrorDlg", u"Message", None));
        self.okBtn.setText(QCoreApplication.translate("ErrorDlg", u"Ok", None))
        self.refreshBtn.setText(QCoreApplication.translate("ErrorDlg", u"Refresh", None))
        self.saveBtn.setText(QCoreApplication.translate("ErrorDlg", u"Save", None))
    # retranslateUi

