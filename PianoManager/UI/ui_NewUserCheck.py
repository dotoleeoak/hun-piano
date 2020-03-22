# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_NewUserCheck.ui'
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


class Ui_NewUserCheck(object):
    def setupUi(self, NewUserCheck):
        if NewUserCheck.objectName():
            NewUserCheck.setObjectName(u"NewUserCheck")
        NewUserCheck.resize(800, 480)
        self.frameMenu = QFrame(NewUserCheck)
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
        self.MainFrame = QFrame(NewUserCheck)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(0, 60, 800, 420))
        self.MainFrame.setAutoFillBackground(False)
        self.MainFrame.setStyleSheet(u"QFrame#MainFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.buttonLeft = QPushButton(self.MainFrame)
        self.buttonLeft.setObjectName(u"buttonLeft")
        self.buttonLeft.setGeometry(QRect(30, 310, 80, 80))
        self.buttonLeft.setStyleSheet(u"QPushButton\n"
"{\n"
"	image: url(Images/arrow_left.png);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	image: url(Images/arrow_left_hover.png);\n"
"}")
        self.lineLeft = QFrame(self.MainFrame)
        self.lineLeft.setObjectName(u"lineLeft")
        self.lineLeft.setGeometry(QRect(130, 310, 2, 80))
        self.lineLeft.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border: 0px;")
        self.lineLeft.setFrameShape(QFrame.VLine)
        self.lineLeft.setFrameShadow(QFrame.Sunken)
        self.labelCheck = QLabel(self.MainFrame)
        self.labelCheck.setObjectName(u"labelCheck")
        self.labelCheck.setEnabled(False)
        self.labelCheck.setGeometry(QRect(0, 52, 800, 30))
        self.labelCheck.setFont(font)
        self.labelCheck.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.labelCheck.setAlignment(Qt.AlignCenter)
        self.labelGuideName = QLabel(self.MainFrame)
        self.labelGuideName.setObjectName(u"labelGuideName")
        self.labelGuideName.setGeometry(QRect(258, 95, 71, 41))
        font3 = QFont()
        font3.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font3.setPointSize(18)
        self.labelGuideName.setFont(font3)
        self.labelGuideName.setLayoutDirection(Qt.LeftToRight)
        self.labelGuideName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelUserName = QLabel(self.MainFrame)
        self.labelUserName.setObjectName(u"labelUserName")
        self.labelUserName.setGeometry(QRect(348, 95, 251, 41))
        font4 = QFont()
        font4.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font4.setPointSize(22)
        self.labelUserName.setFont(font4)
        self.labelUserName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelTemp = QLabel(self.MainFrame)
        self.labelTemp.setObjectName(u"labelTemp")
        self.labelTemp.setGeometry(QRect(320, 245, 220, 40))
        self.labelTemp.setFont(font)
        self.labelTemp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelUserContact = QLabel(self.MainFrame)
        self.labelUserContact.setObjectName(u"labelUserContact")
        self.labelUserContact.setGeometry(QRect(348, 143, 261, 41))
        self.labelUserContact.setFont(font4)
        self.labelUserContact.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelGuideContact = QLabel(self.MainFrame)
        self.labelGuideContact.setObjectName(u"labelGuideContact")
        self.labelGuideContact.setGeometry(QRect(228, 143, 101, 41))
        self.labelGuideContact.setFont(font3)
        self.labelGuideContact.setLayoutDirection(Qt.LeftToRight)
        self.labelGuideContact.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelUserID = QLabel(self.MainFrame)
        self.labelUserID.setObjectName(u"labelUserID")
        self.labelUserID.setGeometry(QRect(348, 192, 261, 41))
        self.labelUserID.setFont(font4)
        self.labelUserID.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelGuideID = QLabel(self.MainFrame)
        self.labelGuideID.setObjectName(u"labelGuideID")
        self.labelGuideID.setGeometry(QRect(258, 192, 71, 41))
        self.labelGuideID.setFont(font3)
        self.labelGuideID.setLayoutDirection(Qt.LeftToRight)
        self.labelGuideID.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.buttonTemp = QPushButton(self.MainFrame)
        self.buttonTemp.setObjectName(u"buttonTemp")
        self.buttonTemp.setGeometry(QRect(270, 245, 40, 40))
        self.buttonTemp.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 15px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Images/unchecked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonTemp.setIcon(icon1)
        self.buttonTemp.setIconSize(QSize(24, 24))
        self.buttonRegister = QPushButton(self.MainFrame)
        self.buttonRegister.setObjectName(u"buttonRegister")
        self.buttonRegister.setGeometry(QRect(340, 320, 120, 60))
        self.buttonRegister.setFont(font2)
        self.buttonRegister.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(70, 108, 234);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(38, 61, 129);\n"
"}")
        self.lineRight = QFrame(self.MainFrame)
        self.lineRight.setObjectName(u"lineRight")
        self.lineRight.setGeometry(QRect(670, 310, 2, 80))
        self.lineRight.setStyleSheet(u"background-color: rgb(176, 176, 176);\n"
"border: 0px;")
        self.lineRight.setFrameShape(QFrame.VLine)
        self.lineRight.setFrameShadow(QFrame.Sunken)
        self.buttonReturn = QPushButton(self.MainFrame)
        self.buttonReturn.setObjectName(u"buttonReturn")
        self.buttonReturn.setGeometry(QRect(695, 315, 70, 70))
        self.buttonReturn.setStyleSheet(u"QPushButton\n"
"{\n"
"	image: url(Images/Return.png);\n"
"	border: 0px;\n"
"}")
        self.DialogueShadow = QFrame(NewUserCheck)
        self.DialogueShadow.setObjectName(u"DialogueShadow")
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
        self.DialogueCheck.setGeometry(QRect(155, 110, 490, 260))
        self.DialogueCheck.setContextMenuPolicy(Qt.NoContextMenu)
        self.DialogueCheck.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px\n"
"")
        self.DLabelNFCTitle = QLabel(self.DialogueCheck)
        self.DLabelNFCTitle.setObjectName(u"DLabelNFCTitle")
        self.DLabelNFCTitle.setGeometry(QRect(0, 30, 491, 41))
        self.DLabelNFCTitle.setStyleSheet(u"font: 24pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(71, 71, 71);")
        self.DLabelNFCTitle.setAlignment(Qt.AlignCenter)
        self.DLabelNFCIcon = QLabel(self.DialogueCheck)
        self.DLabelNFCIcon.setObjectName(u"DLabelNFCIcon")
        self.DLabelNFCIcon.setGeometry(QRect(340, 82, 100, 100))
        self.DLabelNFCIcon.setStyleSheet(u"font: 18pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(71, 71, 71);")
        self.DLabelNFCIcon.setPixmap(QPixmap(u"Images/NFC_png.png"))
        self.DLabelNFCIcon.setScaledContents(True)
        self.DLabelNFCIcon.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_3 = QWidget(self.DialogueCheck)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 200, 491, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.DButtonSkip = QPushButton(self.horizontalLayoutWidget_3)
        self.DButtonSkip.setObjectName(u"DButtonSkip")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DButtonSkip.sizePolicy().hasHeightForWidth())
        self.DButtonSkip.setSizePolicy(sizePolicy1)
        self.DButtonSkip.setStyleSheet(u"font: 18pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"color: rgb(232, 77, 33);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.DButtonSkip)

        self.DLabelNFCGuide = QLabel(self.DialogueCheck)
        self.DLabelNFCGuide.setObjectName(u"DLabelNFCGuide")
        self.DLabelNFCGuide.setGeometry(QRect(50, 84, 231, 91))
        self.DLabelNFCGuide.setStyleSheet(u"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(71, 71, 71);")
        self.DLabelNFCGuide.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.MainFrame.raise_()
        self.frameMenu.raise_()
        self.DialogueShadow.raise_()

        self.retranslateUi(NewUserCheck)

        QMetaObject.connectSlotsByName(NewUserCheck)
    # setupUi

    def retranslateUi(self, NewUserCheck):
        NewUserCheck.setWindowTitle(QCoreApplication.translate("NewUserCheck", u"Form", None))
        self.buttonHome.setText(QCoreApplication.translate("NewUserCheck", u"HH", None))
        self.labelMenu.setText(QCoreApplication.translate("NewUserCheck", u"\uc0ac\uc6a9\uc790 \ub4f1\ub85d", None))
        self.labelHome.setText(QCoreApplication.translate("NewUserCheck", u"\ud648", None))
        self.buttonLeft.setText("")
        self.labelCheck.setText(QCoreApplication.translate("NewUserCheck", u"\uc544\ub798 \uc0ac\uc6a9\uc790\ub85c \ub4f1\ub85d\ud558\uc2dc\uaca0\uc2b5\ub2c8\uae4c?", None))
        self.labelGuideName.setText(QCoreApplication.translate("NewUserCheck", u"\uc774\ub984 :", None))
        self.labelUserName.setText(QCoreApplication.translate("NewUserCheck", u"\uc774\uc9c4\uc601", None))
        self.labelTemp.setText(QCoreApplication.translate("NewUserCheck", u"\uc774\ubc88\uc5d0\ub9cc \uc774\uc6a9\ud558\uaca0\uc2b5\ub2c8\ub2e4", None))
        self.labelUserContact.setText(QCoreApplication.translate("NewUserCheck", u"010 - 4047 - 9089", None))
        self.labelGuideContact.setText(QCoreApplication.translate("NewUserCheck", u"\uc804\ud654\ubc88\ud638 :", None))
        self.labelUserID.setText(QCoreApplication.translate("NewUserCheck", u"2019311737", None))
        self.labelGuideID.setText(QCoreApplication.translate("NewUserCheck", u"\ud559\ubc88 :", None))
        self.buttonTemp.setText("")
        self.buttonRegister.setText(QCoreApplication.translate("NewUserCheck", u"\ub4f1\ub85d", None))
        self.buttonReturn.setText("")
#if QT_CONFIG(accessibility)
        self.DialogueShadow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.DLabelNFCTitle.setText(QCoreApplication.translate("NewUserCheck", u"NFC \ub4f1\ub85d \uc911...", None))
        self.DLabelNFCIcon.setText("")
        self.DButtonSkip.setText(QCoreApplication.translate("NewUserCheck", u"SKIP", None))
        self.DLabelNFCGuide.setText(QCoreApplication.translate("NewUserCheck", u"NFC\ub97c \ucf1c\uace0\n"
"\ub2e8\ub9d0\uae30\uc5d0 \ud0dc\uadf8\ud574\uc8fc\uc138\uc694", None))
    # retranslateUi

