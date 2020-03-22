# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_NewUser3.ui'
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


class Ui_NewUser3(object):
    def setupUi(self, NewUser3):
        if NewUser3.objectName():
            NewUser3.setObjectName(u"NewUser3")
        NewUser3.resize(800, 480)
        self.frameMenu = QFrame(NewUser3)
        self.frameMenu.setObjectName(u"frameMenu")
        self.frameMenu.setGeometry(QRect(0, 0, 800, 60))
        self.frameMenu.setFrameShape(QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QFrame.Raised)
        self.buttonHome = QPushButton(self.frameMenu)
        self.buttonHome.setObjectName(u"buttonHome")
        self.buttonHome.setGeometry(QRect(10, 5, 100, 50))
        font = QFont()
        font.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font.setPointSize(16)
        self.buttonHome.setFont(font)
        self.buttonHome.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(255, 255, 255, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 15px;\n"
"	border: 3px solid #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(241, 219, 194);\n"
"}")
        icon = QIcon()
        icon.addFile(u"Images/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonHome.setIcon(icon)
        self.buttonHome.setIconSize(QSize(40, 40))
        self.labelMenu = QLabel(self.frameMenu)
        self.labelMenu.setObjectName(u"labelMenu")
        self.labelMenu.setGeometry(QRect(0, 0, 800, 60))
        font1 = QFont()
        font1.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.labelMenu.setFont(font1)
        self.labelMenu.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(249, 138, 15);")
        self.labelMenu.setAlignment(Qt.AlignCenter)
        self.labelHom = QLabel(self.frameMenu)
        self.labelHom.setObjectName(u"labelHom")
        self.labelHom.setEnabled(True)
        self.labelHom.setGeometry(QRect(60, 10, 40, 45))
        font2 = QFont()
        font2.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font2.setPointSize(20)
        self.labelHom.setFont(font2)
        self.labelHom.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.labelHom.setAlignment(Qt.AlignCenter)
        self.labelMenu.raise_()
        self.labelHom.raise_()
        self.buttonHome.raise_()
        self.MainFrame = QFrame(NewUser3)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(0, 60, 800, 420))
        self.MainFrame.setAutoFillBackground(False)
        self.MainFrame.setStyleSheet(u"QFrame#MainFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.buttonRight = QPushButton(self.MainFrame)
        self.buttonRight.setObjectName(u"buttonRight")
        self.buttonRight.setGeometry(QRect(690, 50, 80, 80))
        self.buttonRight.setStyleSheet(u"QPushButton\n"
"{\n"
"	image: url(Images/arrow_right.png);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	image: url(Images/arrow_right_hover.png);\n"
"	border: 0px;\n"
"}")
        self.editID = QLineEdit(self.MainFrame)
        self.editID.setObjectName(u"editID")
        self.editID.setGeometry(QRect(310, 60, 255, 60))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editID.sizePolicy().hasHeightForWidth())
        self.editID.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font3.setPointSize(24)
        self.editID.setFont(font3)
        self.editID.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 3px solid #000000;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"	border-color: rgb(0, 85, 255);\n"
"	background-color: rgb(200, 200, 200);\n"
"}")
        self.editID.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhNoPredictiveText)
        self.editID.setMaxLength(10)
        self.editID.setClearButtonEnabled(False)
        self.lineRight = QFrame(self.MainFrame)
        self.lineRight.setObjectName(u"lineRight")
        self.lineRight.setGeometry(QRect(670, 50, 2, 80))
        self.lineRight.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border: 0px;")
        self.lineRight.setFrameShape(QFrame.VLine)
        self.lineRight.setFrameShadow(QFrame.Sunken)
        self.lineLeft = QFrame(self.MainFrame)
        self.lineLeft.setObjectName(u"lineLeft")
        self.lineLeft.setGeometry(QRect(130, 50, 2, 80))
        self.lineLeft.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border: 0px;")
        self.lineLeft.setFrameShape(QFrame.VLine)
        self.lineLeft.setFrameShadow(QFrame.Sunken)
        self.labelError = QLabel(self.MainFrame)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setEnabled(False)
        self.labelError.setGeometry(QRect(305, 140, 190, 30))
        font4 = QFont()
        font4.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font4.setPointSize(14)
        self.labelError.setFont(font4)
        self.labelError.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.labelError.setAlignment(Qt.AlignCenter)
        self.labelWarning = QLabel(self.MainFrame)
        self.labelWarning.setObjectName(u"labelWarning")
        self.labelWarning.setGeometry(QRect(175, 140, 450, 30))
        self.labelWarning.setFont(font4)
        self.labelWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.labelWarning.setAlignment(Qt.AlignCenter)
        self.buttonLeft = QPushButton(self.MainFrame)
        self.buttonLeft.setObjectName(u"buttonLeft")
        self.buttonLeft.setGeometry(QRect(30, 50, 80, 80))
        self.buttonLeft.setStyleSheet(u"QPushButton\n"
"{\n"
"	image: url(Images/arrow_left.png);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	image: url(Images/arrow_left_hover.png);\n"
"	border: 0px;\n"
"}")
        self.labelID = QLabel(self.MainFrame)
        self.labelID.setObjectName(u"labelID")
        self.labelID.setGeometry(QRect(220, 70, 71, 41))
        font5 = QFont()
        font5.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font5.setPointSize(22)
        self.labelID.setFont(font5)
        self.labelID.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.MainFrame.raise_()
        self.frameMenu.raise_()

        self.retranslateUi(NewUser3)

        QMetaObject.connectSlotsByName(NewUser3)
    # setupUi

    def retranslateUi(self, NewUser3):
        NewUser3.setWindowTitle(QCoreApplication.translate("NewUser3", u"Form", None))
        self.buttonHome.setText(QCoreApplication.translate("NewUser3", u"HH", None))
        self.labelMenu.setText(QCoreApplication.translate("NewUser3", u"\uc0ac\uc6a9\uc790 \ub4f1\ub85d", None))
        self.labelHom.setText(QCoreApplication.translate("NewUser3", u"\ud648", None))
        self.buttonRight.setText("")
        self.labelError.setText(QCoreApplication.translate("NewUser3", u"\ud559\ubc88\uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.labelWarning.setText(QCoreApplication.translate("NewUser3", u"\ud559\ubc88\uc774 \uc5c6\ub294 \uad50\ub0b4 \uad6c\uc131\uc6d0\uc740 \uc6b4\uc601\uc9c4\uc5d0\uac8c \ubb38\uc758\ud574\uc8fc\uc138\uc694.", None))
        self.buttonLeft.setText("")
        self.labelID.setText(QCoreApplication.translate("NewUser3", u"\ud559\ubc88", None))
    # retranslateUi

