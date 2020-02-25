# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_LogIn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_LogIn(object):
    def setupUi(self, LogIn):
        if LogIn.objectName():
            LogIn.setObjectName(u"LogIn")
        LogIn.resize(800, 480)
        self.roundDisplay_5 = QPushButton(LogIn)
        self.roundDisplay_5.setObjectName(u"roundDisplay_5")
        self.roundDisplay_5.setGeometry(QRect(245, 240, 50, 50))
        font = QFont()
        font.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font.setPointSize(15)
        self.roundDisplay_5.setFont(font)
        self.roundDisplay_5.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"color: rgb(255, 253, 233);")
        self.roundDisplay_4 = QPushButton(LogIn)
        self.roundDisplay_4.setObjectName(u"roundDisplay_4")
        self.roundDisplay_4.setGeometry(QRect(185, 240, 50, 50))
        self.roundDisplay_4.setFont(font)
        self.roundDisplay_4.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"color: rgb(255, 253, 233);")
        self.roundDisplay_8 = QPushButton(LogIn)
        self.roundDisplay_8.setObjectName(u"roundDisplay_8")
        self.roundDisplay_8.setGeometry(QRect(425, 240, 50, 50))
        self.roundDisplay_8.setFont(font)
        self.roundDisplay_8.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"color: rgb(255, 253, 233);")
        self.DialogueShadow = QFrame(LogIn)
        self.DialogueShadow.setObjectName(u"DialogueShadow")
        self.DialogueShadow.setEnabled(True)
        self.DialogueShadow.setGeometry(QRect(0, 0, 800, 480))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DialogueShadow.sizePolicy().hasHeightForWidth())
        self.DialogueShadow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 0, 0, 100))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.DialogueShadow.setPalette(palette)
        self.DialogueShadow.setAutoFillBackground(True)
        self.DialogueShadow.setStyleSheet(u"")
        self.DialogueCheck = QFrame(self.DialogueShadow)
        self.DialogueCheck.setObjectName(u"DialogueCheck")
        self.DialogueCheck.setGeometry(QRect(200, 140, 400, 200))
        self.DialogueCheck.setContextMenuPolicy(Qt.NoContextMenu)
        self.DialogueCheck.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px\n"
"")
        self.DLabelName = QLabel(self.DialogueCheck)
        self.DLabelName.setObjectName(u"DLabelName")
        self.DLabelName.setGeometry(QRect(0, 50, 400, 41))
        self.DLabelName.setStyleSheet(u"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(71, 71, 71);")
        self.DLabelName.setAlignment(Qt.AlignCenter)
        self.DLabelQ = QLabel(self.DialogueCheck)
        self.DLabelQ.setObjectName(u"DLabelQ")
        self.DLabelQ.setGeometry(QRect(0, 90, 400, 41))
        self.DLabelQ.setStyleSheet(u"font: 18pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(71, 71, 71);")
        self.DLabelQ.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.DialogueCheck)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 139, 401, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.DButtonYes = QPushButton(self.horizontalLayoutWidget)
        self.DButtonYes.setObjectName(u"DButtonYes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DButtonYes.sizePolicy().hasHeightForWidth())
        self.DButtonYes.setSizePolicy(sizePolicy1)
        self.DButtonYes.setStyleSheet(u"font: 18pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(72, 112, 242);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.DButtonYes)

        self.DButtonNo = QPushButton(self.horizontalLayoutWidget)
        self.DButtonNo.setObjectName(u"DButtonNo")
        sizePolicy1.setHeightForWidth(self.DButtonNo.sizePolicy().hasHeightForWidth())
        self.DButtonNo.setSizePolicy(sizePolicy1)
        self.DButtonNo.setStyleSheet(u"font: 18pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(232, 77, 33);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.DButtonNo)

        self.roundDisplay_6 = QPushButton(LogIn)
        self.roundDisplay_6.setObjectName(u"roundDisplay_6")
        self.roundDisplay_6.setGeometry(QRect(305, 240, 50, 50))
        self.roundDisplay_6.setFont(font)
        self.roundDisplay_6.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"color: rgb(255, 253, 233);")
        self.roundDisplay_1 = QPushButton(LogIn)
        self.roundDisplay_1.setObjectName(u"roundDisplay_1")
        self.roundDisplay_1.setGeometry(QRect(5, 240, 50, 50))
        self.roundDisplay_1.setFont(font)
        self.roundDisplay_1.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"color: rgb(255, 253, 233);")
        self.roundDisplay_7 = QPushButton(LogIn)
        self.roundDisplay_7.setObjectName(u"roundDisplay_7")
        self.roundDisplay_7.setGeometry(QRect(365, 240, 50, 50))
        self.roundDisplay_7.setFont(font)
        self.roundDisplay_7.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"color: rgb(255, 253, 233);")
        self.KeypadWidget = QWidget(LogIn)
        self.KeypadWidget.setObjectName(u"KeypadWidget")
        self.KeypadWidget.setGeometry(QRect(479, 60, 321, 421))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        brush2 = QBrush(QColor(251, 233, 197, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.KeypadWidget.setPalette(palette1)
        self.KeypadWidget.setAutoFillBackground(True)
        self.KeypadWidget.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(self.KeypadWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 301, 401))
        self.Keypad = QGridLayout(self.gridLayoutWidget)
        self.Keypad.setObjectName(u"Keypad")
        self.Keypad.setContentsMargins(0, 0, 0, 0)
        self.KeypadButton_7 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_7.setObjectName(u"KeypadButton_7")
        self.KeypadButton_7.setMaximumSize(QSize(80, 80))
        self.KeypadButton_7.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_7, 2, 0, 1, 1)

        self.KeypadButton_8 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_8.setObjectName(u"KeypadButton_8")
        self.KeypadButton_8.setMaximumSize(QSize(80, 80))
        self.KeypadButton_8.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_8, 2, 1, 1, 1)

        self.KeypadButton_6 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_6.setObjectName(u"KeypadButton_6")
        self.KeypadButton_6.setMaximumSize(QSize(80, 80))
        self.KeypadButton_6.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_6, 1, 2, 1, 1)

        self.KeypadButton_4 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_4.setObjectName(u"KeypadButton_4")
        self.KeypadButton_4.setMaximumSize(QSize(80, 80))
        self.KeypadButton_4.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_4, 1, 0, 1, 1)

        self.KeypadButton_9 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_9.setObjectName(u"KeypadButton_9")
        self.KeypadButton_9.setMaximumSize(QSize(80, 80))
        self.KeypadButton_9.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_9, 2, 2, 1, 1)

        self.KeypadButton_1 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_1.setObjectName(u"KeypadButton_1")
        self.KeypadButton_1.setMaximumSize(QSize(80, 80))
        self.KeypadButton_1.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_1, 0, 0, 1, 1)

        self.KeypadButton_3 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_3.setObjectName(u"KeypadButton_3")
        self.KeypadButton_3.setMaximumSize(QSize(80, 80))
        self.KeypadButton_3.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_3, 0, 2, 1, 1)

        self.KeypadButton_5 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_5.setObjectName(u"KeypadButton_5")
        self.KeypadButton_5.setMaximumSize(QSize(80, 80))
        self.KeypadButton_5.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_5, 1, 1, 1, 1)

        self.KeypadButton_2 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_2.setObjectName(u"KeypadButton_2")
        self.KeypadButton_2.setMaximumSize(QSize(80, 80))
        self.KeypadButton_2.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_2, 0, 1, 1, 1)

        self.KeypadButton_0 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_0.setObjectName(u"KeypadButton_0")
        self.KeypadButton_0.setMaximumSize(QSize(80, 80))
        self.KeypadButton_0.setStyleSheet(u"border-radius: 40px;\n"
"font: 48pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_0, 3, 1, 1, 1)

        self.roundDisplay_3 = QPushButton(LogIn)
        self.roundDisplay_3.setObjectName(u"roundDisplay_3")
        self.roundDisplay_3.setGeometry(QRect(125, 240, 50, 50))
        self.roundDisplay_3.setFont(font)
        self.roundDisplay_3.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"color: rgb(255, 253, 233);")
        self.roundDisplay_2 = QPushButton(LogIn)
        self.roundDisplay_2.setObjectName(u"roundDisplay_2")
        self.roundDisplay_2.setGeometry(QRect(65, 240, 50, 50))
        self.roundDisplay_2.setFont(font)
        self.roundDisplay_2.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"color: rgb(255, 253, 233);")
        self.MenuBar = QFrame(LogIn)
        self.MenuBar.setObjectName(u"MenuBar")
        self.MenuBar.setGeometry(QRect(0, 0, 800, 60))
        self.MenuBar.setStyleSheet(u"background-color: rgb(241, 145, 039);")
        self.MenuBar.setFrameShape(QFrame.StyledPanel)
        self.MenuBar.setFrameShadow(QFrame.Raised)
        self.ButtonNFC = QPushButton(self.MenuBar)
        self.ButtonNFC.setObjectName(u"ButtonNFC")
        self.ButtonNFC.setGeometry(QRect(700, 5, 80, 51))
        self.ButtonNFC.setLayoutDirection(Qt.RightToLeft)
        self.ButtonNFC.setStyleSheet(u"border-radius: 1px;\n"
"background-color: rgba(241, 145, 039, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ud55c\ub098\uccb4 Air\";")
        icon = QIcon()
        icon.addFile(u"Images/Phone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonNFC.setIcon(icon)
        self.ButtonNFC.setIconSize(QSize(32, 32))
        self.ButtonRegister = QPushButton(self.MenuBar)
        self.ButtonRegister.setObjectName(u"ButtonRegister")
        self.ButtonRegister.setGeometry(QRect(10, 5, 91, 51))
        self.ButtonRegister.setStyleSheet(u"border-radius: 1px;\n"
"background-color: rgba(241, 145, 039, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ud55c\ub098\uccb4 Air\";")
        icon1 = QIcon()
        icon1.addFile(u"Images/Document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonRegister.setIcon(icon1)
        self.ButtonRegister.setIconSize(QSize(32, 32))
        self.ButtonRegister.setAutoRepeat(False)
        self.MenuPageLabel = QLabel(self.MenuBar)
        self.MenuPageLabel.setObjectName(u"MenuPageLabel")
        self.MenuPageLabel.setGeometry(QRect(310, 0, 200, 60))
        font1 = QFont()
        font1.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \ud55c\ub098\uccb4 Air")
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setWeight(75)
        self.MenuPageLabel.setFont(font1)
        self.MenuPageLabel.setAlignment(Qt.AlignCenter)
        self.roundDisplay_5.raise_()
        self.roundDisplay_4.raise_()
        self.roundDisplay_8.raise_()
        self.roundDisplay_6.raise_()
        self.roundDisplay_1.raise_()
        self.roundDisplay_7.raise_()
        self.KeypadWidget.raise_()
        self.roundDisplay_3.raise_()
        self.roundDisplay_2.raise_()
        self.MenuBar.raise_()
        self.DialogueShadow.raise_()

        self.retranslateUi(LogIn)

        QMetaObject.connectSlotsByName(LogIn)
    # setupUi

    def retranslateUi(self, LogIn):
        LogIn.setWindowTitle(QCoreApplication.translate("LogIn", u"Form", None))
#if QT_CONFIG(accessibility)
        self.DialogueShadow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.DLabelName.setText(QCoreApplication.translate("LogIn", u"\uc774\uc9c4\uc601 \ub2d8", None))
        self.DLabelQ.setText(QCoreApplication.translate("LogIn", u"\uc0ac\uc6a9\ud558\uc2dc\uaca0\uc2b5\ub2c8\uae4c?", None))
        self.DButtonYes.setText(QCoreApplication.translate("LogIn", u"\ud655\uc778", None))
        self.DButtonNo.setText(QCoreApplication.translate("LogIn", u"\ucde8\uc18c", None))
#if QT_CONFIG(accessibility)
        self.KeypadWidget.setAccessibleName(QCoreApplication.translate("LogIn", u"KeyboardWidget", None))
#endif // QT_CONFIG(accessibility)
        self.KeypadButton_7.setText(QCoreApplication.translate("LogIn", u"7", None))
        self.KeypadButton_8.setText(QCoreApplication.translate("LogIn", u"8", None))
        self.KeypadButton_6.setText(QCoreApplication.translate("LogIn", u"6", None))
        self.KeypadButton_4.setText(QCoreApplication.translate("LogIn", u"4", None))
        self.KeypadButton_9.setText(QCoreApplication.translate("LogIn", u"9", None))
        self.KeypadButton_1.setText(QCoreApplication.translate("LogIn", u"1", None))
        self.KeypadButton_3.setText(QCoreApplication.translate("LogIn", u"3", None))
        self.KeypadButton_5.setText(QCoreApplication.translate("LogIn", u"5", None))
        self.KeypadButton_2.setText(QCoreApplication.translate("LogIn", u"2", None))
        self.KeypadButton_0.setText(QCoreApplication.translate("LogIn", u"0", None))
        self.ButtonNFC.setText(QCoreApplication.translate("LogIn", u"NFC", None))
        self.ButtonRegister.setText(QCoreApplication.translate("LogIn", u"\ub4f1\ub85d", None))
        self.MenuPageLabel.setText(QCoreApplication.translate("LogIn", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">\ubc88\ud638 \uc785\ub825</span></p></body></html>", None))
    # retranslateUi

