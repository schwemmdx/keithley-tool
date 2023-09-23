# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'script_dlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QListWidget, QListWidgetItem, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)

class Ui_ScriptDialog(object):
    def setupUi(self, ScriptDialog):
        if not ScriptDialog.objectName():
            ScriptDialog.setObjectName(u"ScriptDialog")
        ScriptDialog.resize(879, 526)
        self.gridLayout = QGridLayout(ScriptDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scriptList = QListWidget(ScriptDialog)
        self.scriptList.setObjectName(u"scriptList")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scriptList.sizePolicy().hasHeightForWidth())
        self.scriptList.setSizePolicy(sizePolicy)
        self.scriptList.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.scriptList.setFont(font)

        self.gridLayout.addWidget(self.scriptList, 0, 0, 1, 4)

        self.scriptEdit = QPlainTextEdit(ScriptDialog)
        self.scriptEdit.setObjectName(u"scriptEdit")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(12)
        self.scriptEdit.setFont(font1)
        self.scriptEdit.setFrameShape(QFrame.StyledPanel)
        self.scriptEdit.setReadOnly(True)
        self.scriptEdit.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.scriptEdit, 0, 4, 1, 3)

        self.toolButton = QToolButton(ScriptDialog)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.toolButton, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(391, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.uploadBtn = QPushButton(ScriptDialog)
        self.uploadBtn.setObjectName(u"uploadBtn")

        self.gridLayout.addWidget(self.uploadBtn, 1, 5, 1, 1)

        self.runBtn = QPushButton(ScriptDialog)
        self.runBtn.setObjectName(u"runBtn")

        self.gridLayout.addWidget(self.runBtn, 1, 6, 1, 1)

        self.pushButton = QPushButton(ScriptDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)

        self.pushButton_2 = QPushButton(ScriptDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)


        self.retranslateUi(ScriptDialog)

        QMetaObject.connectSlotsByName(ScriptDialog)
    # setupUi

    def retranslateUi(self, ScriptDialog):
        ScriptDialog.setWindowTitle(QCoreApplication.translate("ScriptDialog", u"TSP Scripts", None))
        self.scriptEdit.setDocumentTitle(QCoreApplication.translate("ScriptDialog", u"TSP Preview ", None))
        self.toolButton.setText(QCoreApplication.translate("ScriptDialog", u"...", None))
        self.uploadBtn.setText(QCoreApplication.translate("ScriptDialog", u"Upload", None))
        self.runBtn.setText(QCoreApplication.translate("ScriptDialog", u"Run", None))
        self.pushButton.setText(QCoreApplication.translate("ScriptDialog", u"New", None))
        self.pushButton_2.setText(QCoreApplication.translate("ScriptDialog", u"Reload", None))
    # retranslateUi

