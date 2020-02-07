# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageSignUp.ui'
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


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.setEnabled(True)
        SignUp.resize(800, 480)
        font = QFont()
        font.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font.setPointSize(20)
        SignUp.setFont(font)
        SignUp.setStyleSheet(u'''QLineEdit
{
	border: 2px solid #000000;
	border-radius: 10px;
}''')
        self.centralwidget = QWidget(SignUp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frameMenu = QFrame(self.centralwidget)
        self.frameMenu.setObjectName(u"frameMenu")
        self.frameMenu.setGeometry(QRect(0, 0, 800, 60))
        self.frameMenu.setFrameShape(QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QFrame.Raised)
        self.buttonHome = QPushButton(self.frameMenu)
        self.buttonHome.setObjectName(u"buttonHome")
        self.buttonHome.setGeometry(QRect(10, 5, 100, 50))
        font1 = QFont()
        font1.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font1.setPointSize(16)
        self.buttonHome.setFont(font1)
        self.buttonHome.setStyleSheet(u'''QPushButton
{
	color: rgba(255, 255, 255, 0);
	background-color: rgba(255, 255, 255, 0);
	border-radius: 15px;
	border: 3px solid #ffffff;
}

QPushButton:hover
{
	background-color: rgb(241, 219, 194);
}''')
        icon = QIcon()
        icon.addFile(u"Images/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonHome.setIcon(icon)
        self.buttonHome.setIconSize(QSize(40, 40))
        self.labelMenu = QLabel(self.frameMenu)
        self.labelMenu.setObjectName(u"labelMenu")
        self.labelMenu.setGeometry(QRect(0, 0, 800, 60))
        self.labelMenu.setStyleSheet(u'''color: rgb(255, 255, 255);
background-color: rgb(241, 145, 39);
font: 22pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";''')
        self.labelMenu.setAlignment(Qt.AlignCenter)
        self.labelHome = QLabel(self.frameMenu)
        self.labelHome.setObjectName(u"labelHome")
        self.labelHome.setGeometry(QRect(60, 10, 40, 45))
        self.labelHome.setFont(font1)
        self.labelHome.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.labelHome.setAlignment(Qt.AlignCenter)
        self.labelMenu.raise_()
        self.labelHome.raise_()
        self.buttonHome.raise_()
        self.labelName = QLabel(self.centralwidget)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(30, 75, 51, 40))
        self.labelName.setFont(font1)
        self.labelName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelID = QLabel(self.centralwidget)
        self.labelID.setObjectName(u"labelID")
        self.labelID.setGeometry(QRect(30, 275, 51, 40))
        self.labelID.setFont(font1)
        self.labelID.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelContact = QLabel(self.centralwidget)
        self.labelContact.setObjectName(u"labelContact")
        self.labelContact.setGeometry(QRect(30, 175, 91, 40))
        self.labelContact.setFont(font1)
        self.labelContact.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.buttonRegister = QPushButton(self.centralwidget)
        self.buttonRegister.setObjectName(u"buttonRegister")
        self.buttonRegister.setGeometry(QRect(370, 390, 111, 51))
        self.buttonRegister.setFont(font1)
        self.buttonRegister.setStyleSheet(u'''QPushButton
{
	color: rgb(255, 255, 255);
	background-color: rgb(70, 108, 234);
	border-radius: 15px;
}

QPushButton:hover
{
	background-color: rgb(38, 61, 129);
}''')
        self.editID = QLineEdit(self.centralwidget)
        self.editID.setObjectName(u"editID")
        self.editID.setGeometry(QRect(30, 315, 230, 45))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editID.sizePolicy().hasHeightForWidth())
        self.editID.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font2.setPointSize(18)
        self.editID.setFont(font2)
        self.editID.setCursor(QCursor(Qt.IBeamCursor))
        self.editID.setStyleSheet(u"")
        self.editID.setInputMethodHints(Qt.ImhDigitsOnly)
        self.editID.setMaxLength(10)
        self.editID.setClearButtonEnabled(True)
        self.editContact2 = QLineEdit(self.centralwidget)
        self.editContact2.setObjectName(u"editContact2")
        self.editContact2.setGeometry(QRect(155, 215, 110, 45))
        sizePolicy.setHeightForWidth(self.editContact2.sizePolicy().hasHeightForWidth())
        self.editContact2.setSizePolicy(sizePolicy)
        self.editContact2.setFont(font2)
        self.editContact2.setStyleSheet(u"")
        self.editContact2.setInputMethodHints(Qt.ImhDigitsOnly)
        self.editContact2.setMaxLength(4)
        self.editContact2.setClearButtonEnabled(True)
        self.editContact3 = QLineEdit(self.centralwidget)
        self.editContact3.setObjectName(u"editContact3")
        self.editContact3.setGeometry(QRect(305, 215, 110, 45))
        sizePolicy.setHeightForWidth(self.editContact3.sizePolicy().hasHeightForWidth())
        self.editContact3.setSizePolicy(sizePolicy)
        self.editContact3.setFont(font2)
        self.editContact3.setStyleSheet(u"")
        self.editContact3.setInputMethodHints(Qt.ImhDigitsOnly)
        self.editContact3.setMaxLength(4)
        self.editContact3.setClearButtonEnabled(True)
        self.buttonTemp = QPushButton(self.centralwidget)
        self.buttonTemp.setObjectName(u"buttonTemp")
        self.buttonTemp.setGeometry(QRect(30, 395, 40, 40))
        self.buttonTemp.setStyleSheet(u'''QPushButton
{
	background-color: rgb(255, 255, 255);
	border-radius: 10px;
	border: 3px solid black;
}

QPushButton:hover
{
	background-color: rgb(148, 148, 148);
}''')
        self.labelDash1 = QLabel(self.centralwidget)
        self.labelDash1.setObjectName(u"labelDash1")
        self.labelDash1.setGeometry(QRect(115, 225, 41, 31))
        self.labelDash1.setFont(font2)
        self.labelDash1.setAlignment(Qt.AlignCenter)
        self.editContact1 = QLineEdit(self.centralwidget)
        self.editContact1.setObjectName(u"editContact1")
        self.editContact1.setGeometry(QRect(30, 215, 85, 45))
        sizePolicy.setHeightForWidth(self.editContact1.sizePolicy().hasHeightForWidth())
        self.editContact1.setSizePolicy(sizePolicy)
        self.editContact1.setFont(font2)
        self.editContact1.setStyleSheet(u"")
        self.editContact1.setInputMethodHints(Qt.ImhDigitsOnly)
        self.editContact1.setMaxLength(3)
        self.editContact1.setClearButtonEnabled(True)
        self.labelDash2 = QLabel(self.centralwidget)
        self.labelDash2.setObjectName(u"labelDash2")
        self.labelDash2.setGeometry(QRect(265, 225, 41, 31))
        self.labelDash2.setFont(font2)
        self.labelDash2.setAlignment(Qt.AlignCenter)
        self.labelTemp = QLabel(self.centralwidget)
        self.labelTemp.setObjectName(u"labelTemp")
        self.labelTemp.setGeometry(QRect(80, 400, 250, 30))
        self.labelTemp.setFont(font1)
        self.editName = QLineEdit(self.centralwidget)
        self.editName.setObjectName(u"editName")
        self.editName.setGeometry(QRect(30, 115, 200, 45))
        sizePolicy.setHeightForWidth(self.editName.sizePolicy().hasHeightForWidth())
        self.editName.setSizePolicy(sizePolicy)
        self.editName.setFont(font2)
        self.editName.setStyleSheet(u"")
        self.editName.setInputMethodHints(Qt.ImhNone)
        self.editName.setMaxLength(20)
        self.editName.setClearButtonEnabled(True)
        SignUp.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"MainWindow", None))
        self.buttonHome.setText(QCoreApplication.translate("SignUp", u"HH", None))
        self.labelMenu.setText(QCoreApplication.translate("SignUp", u"\uc0ac\uc6a9\uc790 \ub4f1\ub85d", None))
        self.labelHome.setText(QCoreApplication.translate("SignUp", u"\ud648", None))
        self.labelName.setText(QCoreApplication.translate("SignUp", u"\uc774\ub984", None))
        self.labelID.setText(QCoreApplication.translate("SignUp", u"\ud559\ubc88", None))
        self.labelContact.setText(QCoreApplication.translate("SignUp", u"\uc804\ud654\ubc88\ud638", None))
        self.buttonRegister.setText(QCoreApplication.translate("SignUp", u"\ub4f1\ub85d", None))
#if QT_CONFIG(whatsthis)
        self.editContact3.setWhatsThis(QCoreApplication.translate("SignUp", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.buttonTemp.setText("")
        self.labelDash1.setText(QCoreApplication.translate("SignUp", u"-", None))
        self.labelDash2.setText(QCoreApplication.translate("SignUp", u"-", None))
        self.labelTemp.setText(QCoreApplication.translate("SignUp", u"\uc784\uc2dc \ub4f1\ub85d\uc744 \ud558\ub824 \ud569\ub2c8\ub2e4.", None))
    # retranslateUi

