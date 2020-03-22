# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_NewUser1.ui'
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


class Ui_NewUser1(object):
    def setupUi(self, NewUser1):
        if NewUser1.objectName():
            NewUser1.setObjectName(u"NewUser1")
        NewUser1.resize(800, 480)
        self.frameMenu = QFrame(NewUser1)
        self.frameMenu.setObjectName(u"frameMenu")
        self.frameMenu.setGeometry(QRect(0, 0, 800, 60))
        self.frameMenu.setFrameShape(QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QFrame.Raised)
        self.labelMenu = QLabel(self.frameMenu)
        self.labelMenu.setObjectName(u"labelMenu")
        self.labelMenu.setGeometry(QRect(0, 0, 800, 60))
        font = QFont()
        font.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelMenu.setFont(font)
        self.labelMenu.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(249, 138, 15);")
        self.labelMenu.setAlignment(Qt.AlignCenter)
        self.buttonHome = QPushButton(self.frameMenu)
        self.buttonHome.setObjectName(u"buttonHome")
        self.buttonHome.setGeometry(QRect(10, 5, 100, 50))
        font1 = QFont()
        font1.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font1.setPointSize(16)
        self.buttonHome.setFont(font1)
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
        self.labelHome = QLabel(self.frameMenu)
        self.labelHome.setObjectName(u"labelHome")
        self.labelHome.setEnabled(True)
        self.labelHome.setGeometry(QRect(60, 10, 40, 45))
        font2 = QFont()
        font2.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font2.setPointSize(20)
        self.labelHome.setFont(font2)
        self.labelHome.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.labelHome.setAlignment(Qt.AlignCenter)
        self.labelMenu.raise_()
        self.labelHome.raise_()
        self.buttonHome.raise_()
        self.MainFrame = QFrame(NewUser1)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(0, 60, 800, 420))
        self.MainFrame.setAutoFillBackground(False)
        self.MainFrame.setStyleSheet(u"QFrame#MainFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.lineRight = QFrame(self.MainFrame)
        self.lineRight.setObjectName(u"lineRight")
        self.lineRight.setGeometry(QRect(670, 50, 2, 80))
        self.lineRight.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border: 0px;")
        self.lineRight.setFrameShape(QFrame.VLine)
        self.lineRight.setFrameShadow(QFrame.Sunken)
        self.editName = QLineEdit(self.MainFrame)
        self.editName.setObjectName(u"editName")
        self.editName.setGeometry(QRect(310, 60, 250, 60))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editName.sizePolicy().hasHeightForWidth())
        self.editName.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font3.setPointSize(24)
        self.editName.setFont(font3)
        self.editName.setStyleSheet(u"QLineEdit\n"
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
        self.editName.setInputMethodHints(Qt.ImhNoPredictiveText)
        self.editName.setMaxLength(20)
        self.editName.setClearButtonEnabled(False)
        self.labelError = QLabel(self.MainFrame)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setEnabled(False)
        self.labelError.setGeometry(QRect(320, 130, 200, 30))
        font4 = QFont()
        font4.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font4.setPointSize(14)
        self.labelError.setFont(font4)
        self.labelError.setStyleSheet(u"color: rgb(255, 0, 0);")
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
"}")
        self.labelName = QLabel(self.MainFrame)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(220, 70, 71, 41))
        font5 = QFont()
        font5.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font5.setPointSize(22)
        self.labelName.setFont(font5)
        self.labelName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.MainFrame.raise_()
        self.frameMenu.raise_()

        self.retranslateUi(NewUser1)

        QMetaObject.connectSlotsByName(NewUser1)
    # setupUi

    def retranslateUi(self, NewUser1):
        NewUser1.setWindowTitle(QCoreApplication.translate("NewUser1", u"Form", None))
        self.labelMenu.setText(QCoreApplication.translate("NewUser1", u"\uc0ac\uc6a9\uc790 \ub4f1\ub85d", None))
        self.buttonHome.setText(QCoreApplication.translate("NewUser1", u"HH", None))
        self.labelHome.setText(QCoreApplication.translate("NewUser1", u"\ud648", None))
        self.labelError.setText(QCoreApplication.translate("NewUser1", u"\uc774\ub984\uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.buttonRight.setText("")
        self.labelName.setText(QCoreApplication.translate("NewUser1", u"\uc774\ub984", None))
    # retranslateUi

