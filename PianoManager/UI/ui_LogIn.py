# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_LogIn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        if LogIn.objectName():
            LogIn.setObjectName(u"LogIn")
        LogIn.resize(800, 480)
        self.KeypadFrame = QFrame(LogIn)
        self.KeypadFrame.setObjectName(u"KeypadFrame")
        self.KeypadFrame.setGeometry(QRect(0, 250, 800, 230))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.KeypadFrame.setPalette(palette)
        self.KeypadFrame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.Keypad = QFrame(self.KeypadFrame)
        self.Keypad.setObjectName(u"Keypad")
        self.Keypad.setGeometry(QRect(116, 25, 568, 180))
        self.KeypadButton_9 = QPushButton(self.Keypad)
        self.KeypadButton_9.setObjectName(u"KeypadButton_9")
        self.KeypadButton_9.setGeometry(QRect(352, 93, 80, 80))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KeypadButton_9.sizePolicy().hasHeightForWidth())
        self.KeypadButton_9.setSizePolicy(sizePolicy)
        self.KeypadButton_9.setMaximumSize(QSize(80, 80))
        font = QFont()
        font.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50);
        self.KeypadButton_9.setFont(font)
        self.KeypadButton_9.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.KeypadButton_1 = QPushButton(self.Keypad)
        self.KeypadButton_1.setObjectName(u"KeypadButton_1")
        self.KeypadButton_1.setGeometry(QRect(28, 8, 80, 80))
        sizePolicy.setHeightForWidth(self.KeypadButton_1.sizePolicy().hasHeightForWidth())
        self.KeypadButton_1.setSizePolicy(sizePolicy)
        self.KeypadButton_1.setMaximumSize(QSize(80, 80))
        self.KeypadButton_1.setFont(font)
        self.KeypadButton_1.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.KeypadButton_4 = QPushButton(self.Keypad)
        self.KeypadButton_4.setObjectName(u"KeypadButton_4")
        self.KeypadButton_4.setGeometry(QRect(352, 8, 80, 80))
        sizePolicy.setHeightForWidth(self.KeypadButton_4.sizePolicy().hasHeightForWidth())
        self.KeypadButton_4.setSizePolicy(sizePolicy)
        self.KeypadButton_4.setMaximumSize(QSize(80, 80))
        self.KeypadButton_4.setFont(font)
        self.KeypadButton_4.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.KeypadButton_0 = QPushButton(self.Keypad)
        self.KeypadButton_0.setObjectName(u"KeypadButton_0")
        self.KeypadButton_0.setGeometry(QRect(460, 93, 80, 80))
        sizePolicy.setHeightForWidth(self.KeypadButton_0.sizePolicy().hasHeightForWidth())
        self.KeypadButton_0.setSizePolicy(sizePolicy)
        self.KeypadButton_0.setMaximumSize(QSize(80, 80))
        self.KeypadButton_0.setFont(font)
        self.KeypadButton_0.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.KeypadButton_5 = QPushButton(self.Keypad)
        self.KeypadButton_5.setObjectName(u"KeypadButton_5")
        self.KeypadButton_5.setGeometry(QRect(460, 8, 80, 80))
        sizePolicy.setHeightForWidth(self.KeypadButton_5.sizePolicy().hasHeightForWidth())
        self.KeypadButton_5.setSizePolicy(sizePolicy)
        self.KeypadButton_5.setMaximumSize(QSize(80, 80))
        self.KeypadButton_5.setFont(font)
        self.KeypadButton_2 = QPushButton(self.Keypad)
        self.KeypadButton_2.setObjectName(u"KeypadButton_2")
        self.KeypadButton_2.setGeometry(QRect(136, 8, 80, 80))
        sizePolicy.setHeightForWidth(self.KeypadButton_2.sizePolicy().hasHeightForWidth())
        self.KeypadButton_2.setSizePolicy(sizePolicy)
        self.KeypadButton_2.setMaximumSize(QSize(80, 80))
        self.KeypadButton_2.setFont(font)
        self.KeypadButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.KeypadButton_7 = QPushButton(self.Keypad)
        self.KeypadButton_7.setObjectName(u"KeypadButton_7")
        self.KeypadButton_7.setGeometry(QRect(136, 93, 80, 80))
        sizePolicy.setHeightForWidth(self.KeypadButton_7.sizePolicy().hasHeightForWidth())
        self.KeypadButton_7.setSizePolicy(sizePolicy)
        self.KeypadButton_7.setMaximumSize(QSize(80, 80))
        self.KeypadButton_7.setFont(font)
        self.KeypadButton_7.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.KeypadButton_3 = QPushButton(self.Keypad)
        self.KeypadButton_3.setObjectName(u"KeypadButton_3")
        self.KeypadButton_3.setGeometry(QRect(244, 8, 80, 80))
        sizePolicy.setHeightForWidth(self.KeypadButton_3.sizePolicy().hasHeightForWidth())
        self.KeypadButton_3.setSizePolicy(sizePolicy)
        self.KeypadButton_3.setMaximumSize(QSize(80, 80))
        self.KeypadButton_3.setFont(font)
        self.KeypadButton_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.KeypadButton_8 = QPushButton(self.Keypad)
        self.KeypadButton_8.setObjectName(u"KeypadButton_8")
        self.KeypadButton_8.setGeometry(QRect(244, 93, 80, 80))
        sizePolicy.setHeightForWidth(self.KeypadButton_8.sizePolicy().hasHeightForWidth())
        self.KeypadButton_8.setSizePolicy(sizePolicy)
        self.KeypadButton_8.setMaximumSize(QSize(80, 80))
        self.KeypadButton_8.setFont(font)
        self.KeypadButton_8.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.KeypadButton_6 = QPushButton(self.Keypad)
        self.KeypadButton_6.setObjectName(u"KeypadButton_6")
        self.KeypadButton_6.setGeometry(QRect(28, 93, 80, 80))
        sizePolicy.setHeightForWidth(self.KeypadButton_6.sizePolicy().hasHeightForWidth())
        self.KeypadButton_6.setSizePolicy(sizePolicy)
        self.KeypadButton_6.setMaximumSize(QSize(80, 80))
        self.KeypadButton_6.setFont(font)
        self.KeypadButton_6.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.LongStick_1 = QLabel(self.Keypad)
        self.LongStick_1.setObjectName(u"LongStick_1")
        self.LongStick_1.setGeometry(QRect(6, 10, 16, 160))
        self.LongStick_1.setPixmap(QPixmap(u"Images/boldStick.png"))
        self.LongStick_1.setAlignment(Qt.AlignCenter)
        self.LongStick_2 = QLabel(self.Keypad)
        self.LongStick_2.setObjectName(u"LongStick_2")
        self.LongStick_2.setGeometry(QRect(546, 10, 16, 160))
        self.LongStick_2.setPixmap(QPixmap(u"Images/boldStick.png"))
        self.LongStick_2.setAlignment(Qt.AlignCenter)
        self.ShortStick_1 = QLabel(self.Keypad)
        self.ShortStick_1.setObjectName(u"ShortStick_1")
        self.ShortStick_1.setGeometry(QRect(117, 10, 10, 74))
        self.ShortStick_1.setPixmap(QPixmap(u"Images/SharpStick.png"))
        self.ShortStick_1.setAlignment(Qt.AlignCenter)
        self.ShortStick_8 = QLabel(self.Keypad)
        self.ShortStick_8.setObjectName(u"ShortStick_8")
        self.ShortStick_8.setGeometry(QRect(441, 96, 10, 74))
        self.ShortStick_8.setPixmap(QPixmap(u"Images/SharpStick.png"))
        self.ShortStick_8.setAlignment(Qt.AlignCenter)
        self.ShortStick_4 = QLabel(self.Keypad)
        self.ShortStick_4.setObjectName(u"ShortStick_4")
        self.ShortStick_4.setGeometry(QRect(441, 10, 10, 74))
        self.ShortStick_4.setPixmap(QPixmap(u"Images/SharpStick.png"))
        self.ShortStick_4.setAlignment(Qt.AlignCenter)
        self.ShortStick_3 = QLabel(self.Keypad)
        self.ShortStick_3.setObjectName(u"ShortStick_3")
        self.ShortStick_3.setGeometry(QRect(333, 10, 10, 74))
        self.ShortStick_3.setPixmap(QPixmap(u"Images/SharpStick.png"))
        self.ShortStick_3.setAlignment(Qt.AlignCenter)
        self.ShortStick_2 = QLabel(self.Keypad)
        self.ShortStick_2.setObjectName(u"ShortStick_2")
        self.ShortStick_2.setGeometry(QRect(225, 10, 10, 74))
        self.ShortStick_2.setPixmap(QPixmap(u"Images/SharpStick.png"))
        self.ShortStick_2.setAlignment(Qt.AlignCenter)
        self.ShortStick_7 = QLabel(self.Keypad)
        self.ShortStick_7.setObjectName(u"ShortStick_7")
        self.ShortStick_7.setGeometry(QRect(333, 96, 10, 74))
        self.ShortStick_7.setPixmap(QPixmap(u"Images/SharpStick.png"))
        self.ShortStick_7.setAlignment(Qt.AlignCenter)
        self.ShortStick_6 = QLabel(self.Keypad)
        self.ShortStick_6.setObjectName(u"ShortStick_6")
        self.ShortStick_6.setGeometry(QRect(225, 96, 10, 74))
        self.ShortStick_6.setPixmap(QPixmap(u"Images/SharpStick.png"))
        self.ShortStick_6.setAlignment(Qt.AlignCenter)
        self.ShortStick_5 = QLabel(self.Keypad)
        self.ShortStick_5.setObjectName(u"ShortStick_5")
        self.ShortStick_5.setGeometry(QRect(117, 96, 10, 74))
        self.ShortStick_5.setPixmap(QPixmap(u"Images/SharpStick.png"))
        self.ShortStick_5.setAlignment(Qt.AlignCenter)
        self.MenuBar = QFrame(LogIn)
        self.MenuBar.setObjectName(u"MenuBar")
        self.MenuBar.setGeometry(QRect(0, 0, 800, 250))
        self.MenuBar.setStyleSheet(u"background-color: rgb(249, 138, 015);")
        self.MenuBar.setFrameShape(QFrame.StyledPanel)
        self.MenuBar.setFrameShadow(QFrame.Raised)
        self.ButtonNFC = QPushButton(self.MenuBar)
        self.ButtonNFC.setObjectName(u"ButtonNFC")
        self.ButtonNFC.setGeometry(QRect(700, 5, 80, 51))
        self.ButtonNFC.setLayoutDirection(Qt.RightToLeft)
        self.ButtonNFC.setStyleSheet(u"border-radius: 1px;\n"
"background-color: rgba(241, 145, 039, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
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
"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        icon1 = QIcon()
        icon1.addFile(u"Images/Document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonRegister.setIcon(icon1)
        self.ButtonRegister.setIconSize(QSize(32, 32))
        self.ButtonRegister.setAutoRepeat(False)
        self.MenuPageLabel = QLabel(self.MenuBar)
        self.MenuPageLabel.setObjectName(u"MenuPageLabel")
        self.MenuPageLabel.setGeometry(QRect(340, 5, 121, 60))
        font1 = QFont()
        font1.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50);
        self.MenuPageLabel.setFont(font1)
        self.MenuPageLabel.setStyleSheet(u"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        self.MenuPageLabel.setAlignment(Qt.AlignCenter)
        self.NumberDisplay_7 = QPushButton(self.MenuBar)
        self.NumberDisplay_7.setObjectName(u"NumberDisplay_7")
        self.NumberDisplay_7.setGeometry(QRect(580, 120, 70, 70))
        self.NumberDisplay_7.setFont(font1)
        self.NumberDisplay_7.setStyleSheet(u"border-radius: 16px;\n"
"background-color: rgb(199, 107, 5);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        self.NumberDisplay_5 = QPushButton(self.MenuBar)
        self.NumberDisplay_5.setObjectName(u"NumberDisplay_5")
        self.NumberDisplay_5.setGeometry(QRect(420, 120, 70, 70))
        self.NumberDisplay_5.setFont(font1)
        self.NumberDisplay_5.setStyleSheet(u"border-radius: 16px;\n"
"background-color: rgb(199, 107, 5);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        self.NumberDisplay_8 = QPushButton(self.MenuBar)
        self.NumberDisplay_8.setObjectName(u"NumberDisplay_8")
        self.NumberDisplay_8.setGeometry(QRect(660, 120, 70, 70))
        self.NumberDisplay_8.setFont(font1)
        self.NumberDisplay_8.setStyleSheet(u"border-radius: 16px;\n"
"background-color: rgb(199, 107, 5);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        self.NumberDisplay_1 = QPushButton(self.MenuBar)
        self.NumberDisplay_1.setObjectName(u"NumberDisplay_1")
        self.NumberDisplay_1.setGeometry(QRect(70, 120, 70, 70))
        self.NumberDisplay_1.setFont(font1)
        self.NumberDisplay_1.setStyleSheet(u"border-radius: 16px;\n"
"background-color: rgb(199, 107, 5);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        self.NumberDisplay_3 = QPushButton(self.MenuBar)
        self.NumberDisplay_3.setObjectName(u"NumberDisplay_3")
        self.NumberDisplay_3.setGeometry(QRect(230, 120, 70, 70))
        self.NumberDisplay_3.setFont(font1)
        self.NumberDisplay_3.setStyleSheet(u"border-radius: 16px;\n"
"background-color: rgb(199, 107, 5);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        self.NumberDisplay_4 = QPushButton(self.MenuBar)
        self.NumberDisplay_4.setObjectName(u"NumberDisplay_4")
        self.NumberDisplay_4.setGeometry(QRect(310, 120, 70, 70))
        self.NumberDisplay_4.setFont(font1)
        self.NumberDisplay_4.setStyleSheet(u"border-radius: 16px;\n"
"background-color: rgb(199, 107, 5);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        self.NumberDisplay_2 = QPushButton(self.MenuBar)
        self.NumberDisplay_2.setObjectName(u"NumberDisplay_2")
        self.NumberDisplay_2.setGeometry(QRect(150, 120, 70, 70))
        self.NumberDisplay_2.setFont(font1)
        self.NumberDisplay_2.setStyleSheet(u"border-radius: 16px;\n"
"background-color: rgb(199, 107, 5);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        self.NumberDisplay_6 = QPushButton(self.MenuBar)
        self.NumberDisplay_6.setObjectName(u"NumberDisplay_6")
        self.NumberDisplay_6.setGeometry(QRect(500, 120, 70, 70))
        self.NumberDisplay_6.setFont(font1)
        self.NumberDisplay_6.setStyleSheet(u"border-radius: 16px;\n"
"background-color: rgb(199, 107, 5);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";")
        self.DashStick = QLabel(self.MenuBar)
        self.DashStick.setObjectName(u"DashStick")
        self.DashStick.setGeometry(QRect(390, 147, 20, 16))
        self.DashStick.setPixmap(QPixmap(u"Images/Stick2.png"))
        self.DialogueShadow = QFrame(LogIn)
        self.DialogueShadow.setObjectName(u"DialogueShadow")
        self.DialogueShadow.setEnabled(True)
        self.DialogueShadow.setGeometry(QRect(0, 0, 800, 480))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DialogueShadow.sizePolicy().hasHeightForWidth())
        self.DialogueShadow.setSizePolicy(sizePolicy1)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 0, 0, 100))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.DialogueShadow.setPalette(palette1)
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
"background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(71, 71, 71);")
        self.DLabelName.setAlignment(Qt.AlignCenter)
        self.DLabelQ = QLabel(self.DialogueCheck)
        self.DLabelQ.setObjectName(u"DLabelQ")
        self.DLabelQ.setGeometry(QRect(0, 90, 400, 41))
        self.DLabelQ.setStyleSheet(u"font: 18pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(71, 71, 71);")
        self.DLabelQ.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_3 = QWidget(self.DialogueCheck)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 139, 401, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.DButtonYes = QPushButton(self.horizontalLayoutWidget_3)
        self.DButtonYes.setObjectName(u"DButtonYes")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DButtonYes.sizePolicy().hasHeightForWidth())
        self.DButtonYes.setSizePolicy(sizePolicy2)
        self.DButtonYes.setStyleSheet(u"font: 18pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(72, 112, 242);\n"
"background-color: rgb(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.DButtonYes)

        self.DButtonNo = QPushButton(self.horizontalLayoutWidget_3)
        self.DButtonNo.setObjectName(u"DButtonNo")
        sizePolicy2.setHeightForWidth(self.DButtonNo.sizePolicy().hasHeightForWidth())
        self.DButtonNo.setSizePolicy(sizePolicy2)
        self.DButtonNo.setStyleSheet(u"font: 18pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(232, 77, 33);\n"
"background-color: rgb(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.DButtonNo)


        self.retranslateUi(LogIn)

        QMetaObject.connectSlotsByName(LogIn)
    # setupUi

    def retranslateUi(self, LogIn):
        LogIn.setWindowTitle(QCoreApplication.translate("LogIn", u"Form", None))
        self.KeypadButton_9.setText(QCoreApplication.translate("LogIn", u"9", None))
        self.KeypadButton_1.setText(QCoreApplication.translate("LogIn", u"1", None))
        self.KeypadButton_4.setText(QCoreApplication.translate("LogIn", u"4", None))
        self.KeypadButton_0.setText(QCoreApplication.translate("LogIn", u"0", None))
        self.KeypadButton_5.setStyleSheet(QCoreApplication.translate("LogIn", u"QPushButton\n"
"{\n"
"	border-radius: 3px;\n"
"	font: 36pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"	color: rgb(255, 188, 50);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 188, 50);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(223, 163, 43);\n"
"	color: rgb(255, 255, 255);\n"
"}", None))
        self.KeypadButton_5.setText(QCoreApplication.translate("LogIn", u"5", None))
        self.KeypadButton_2.setText(QCoreApplication.translate("LogIn", u"2", None))
        self.KeypadButton_7.setText(QCoreApplication.translate("LogIn", u"7", None))
        self.KeypadButton_3.setText(QCoreApplication.translate("LogIn", u"3", None))
        self.KeypadButton_8.setText(QCoreApplication.translate("LogIn", u"8", None))
        self.KeypadButton_6.setText(QCoreApplication.translate("LogIn", u"6", None))
        self.LongStick_1.setText("")
        self.LongStick_2.setText("")
        self.ShortStick_1.setText("")
        self.ShortStick_8.setText("")
        self.ShortStick_4.setText("")
        self.ShortStick_3.setText("")
        self.ShortStick_2.setText("")
        self.ShortStick_7.setText("")
        self.ShortStick_6.setText("")
        self.ShortStick_5.setText("")
        self.ButtonNFC.setText(QCoreApplication.translate("LogIn", u"NFC", None))
        self.ButtonRegister.setText(QCoreApplication.translate("LogIn", u"\ub4f1\ub85d", None))
        self.MenuPageLabel.setText(QCoreApplication.translate("LogIn", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">\ubc88\ud638 \uc785\ub825</span></p></body></html>", None))
        self.DashStick.setText("")
#if QT_CONFIG(accessibility)
        self.DialogueShadow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.DLabelName.setText(QCoreApplication.translate("LogIn", u"\uc774\uc9c4\uc601 \ub2d8", None))
        self.DLabelQ.setText(QCoreApplication.translate("LogIn", u"\uc0ac\uc6a9\ud558\uc2dc\uaca0\uc2b5\ub2c8\uae4c?", None))
        self.DButtonYes.setText(QCoreApplication.translate("LogIn", u"\ud655\uc778", None))
        self.DButtonNo.setText(QCoreApplication.translate("LogIn", u"\ucde8\uc18c", None))
    # retranslateUi

