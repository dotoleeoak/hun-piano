# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_NewUser2.ui'
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


class Ui_NewUser2(object):
    def setupUi(self, NewUser2):
        if NewUser2.objectName():
            NewUser2.setObjectName(u"NewUser2")
        NewUser2.resize(800, 480)
        self.frameMenu = QFrame(NewUser2)
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
        self.MainFrame = QFrame(NewUser2)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(0, 60, 800, 420))
        self.MainFrame.setAutoFillBackground(False)
        self.MainFrame.setStyleSheet(u"QFrame#MainFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.labelError = QLabel(self.MainFrame)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setEnabled(False)
        self.labelError.setGeometry(QRect(230, 150, 220, 30))
        font3 = QFont()
        font3.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font3.setPointSize(14)
        self.labelError.setFont(font3)
        self.labelError.setStyleSheet(u"color: rgb(255, 0, 0);")
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
        self.editContact3 = QLineEdit(self.MainFrame)
        self.editContact3.setObjectName(u"editContact3")
        self.editContact3.setGeometry(QRect(490, 90, 100, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editContact3.sizePolicy().hasHeightForWidth())
        self.editContact3.setSizePolicy(sizePolicy)
        self.editContact3.setFont(font2)
        self.editContact3.setStyleSheet(u"QLineEdit\n"
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
        self.editContact3.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhNoPredictiveText)
        self.editContact3.setMaxLength(4)
        self.editContact3.setClearButtonEnabled(False)
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
        self.labelContact = QLabel(self.MainFrame)
        self.labelContact.setObjectName(u"labelContact")
        self.labelContact.setGeometry(QRect(230, 40, 121, 41))
        font4 = QFont()
        font4.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font4.setPointSize(22)
        self.labelContact.setFont(font4)
        self.labelContact.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.editContact1 = QLineEdit(self.MainFrame)
        self.editContact1.setObjectName(u"editContact1")
        self.editContact1.setGeometry(QRect(230, 90, 80, 50))
        sizePolicy.setHeightForWidth(self.editContact1.sizePolicy().hasHeightForWidth())
        self.editContact1.setSizePolicy(sizePolicy)
        self.editContact1.setFont(font2)
        self.editContact1.setStyleSheet(u"QLineEdit\n"
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
        self.editContact1.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhNoPredictiveText)
        self.editContact1.setMaxLength(3)
        self.editContact1.setClearButtonEnabled(False)
        self.lineLeft = QFrame(self.MainFrame)
        self.lineLeft.setObjectName(u"lineLeft")
        self.lineLeft.setGeometry(QRect(130, 50, 2, 80))
        self.lineLeft.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border: 0px;")
        self.lineLeft.setFrameShape(QFrame.VLine)
        self.lineLeft.setFrameShadow(QFrame.Sunken)
        self.lineRight = QFrame(self.MainFrame)
        self.lineRight.setObjectName(u"lineRight")
        self.lineRight.setGeometry(QRect(670, 50, 2, 80))
        self.lineRight.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border: 0px;")
        self.lineRight.setFrameShape(QFrame.VLine)
        self.lineRight.setFrameShadow(QFrame.Sunken)
        self.editContact2 = QLineEdit(self.MainFrame)
        self.editContact2.setObjectName(u"editContact2")
        self.editContact2.setGeometry(QRect(350, 90, 100, 50))
        sizePolicy.setHeightForWidth(self.editContact2.sizePolicy().hasHeightForWidth())
        self.editContact2.setSizePolicy(sizePolicy)
        self.editContact2.setFont(font2)
        self.editContact2.setStyleSheet(u"QLineEdit\n"
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
        self.editContact2.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhNoPredictiveText)
        self.editContact2.setMaxLength(4)
        self.editContact2.setClearButtonEnabled(False)
        self.labelDash2 = QLabel(self.MainFrame)
        self.labelDash2.setObjectName(u"labelDash2")
        self.labelDash2.setGeometry(QRect(450, 100, 40, 30))
        font5 = QFont()
        font5.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font5.setPointSize(18)
        self.labelDash2.setFont(font5)
        self.labelDash2.setAlignment(Qt.AlignCenter)
        self.labelDash1 = QLabel(self.MainFrame)
        self.labelDash1.setObjectName(u"labelDash1")
        self.labelDash1.setGeometry(QRect(310, 100, 40, 30))
        self.labelDash1.setFont(font5)
        self.labelDash1.setAlignment(Qt.AlignCenter)
        self.MainFrame.raise_()
        self.frameMenu.raise_()

        self.retranslateUi(NewUser2)

        QMetaObject.connectSlotsByName(NewUser2)
    # setupUi

    def retranslateUi(self, NewUser2):
        NewUser2.setWindowTitle(QCoreApplication.translate("NewUser2", u"Form", None))
        self.buttonHome.setText(QCoreApplication.translate("NewUser2", u"HH", None))
        self.labelMenu.setText(QCoreApplication.translate("NewUser2", u"\uc0ac\uc6a9\uc790 \ub4f1\ub85d", None))
        self.labelHome.setText(QCoreApplication.translate("NewUser2", u"\ud648", None))
        self.labelError.setText(QCoreApplication.translate("NewUser2", u"\uc804\ud654\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.buttonLeft.setText("")
        self.buttonRight.setText("")
        self.labelContact.setText(QCoreApplication.translate("NewUser2", u"\uc804\ud654\ubc88\ud638", None))
        self.labelDash2.setText(QCoreApplication.translate("NewUser2", u"-", None))
        self.labelDash1.setText(QCoreApplication.translate("NewUser2", u"-", None))
    # retranslateUi

