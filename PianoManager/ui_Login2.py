# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageLogin2.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QRectF, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Login(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(800, 480))
        font = QFont()
        font.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \ud55c\ub098\uccb4 Air")
        font.setPointSize(18)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        MainWindow.setAnimated(True)
        self.actionSignUp = QAction(MainWindow)
        self.actionSignUp.setObjectName(u"actionSignUp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.viewMebuBar = QGraphicsView(self.centralwidget)
        self.viewMebuBar.setObjectName(u"viewMebuBar")
        self.viewMebuBar.setEnabled(True)
        self.viewMebuBar.setGeometry(QRect(0, 0, 800, 60))
        self.viewMebuBar.setAutoFillBackground(False)
        self.viewMebuBar.setStyleSheet(u"background-color: rgb(241, 145, 39);")
        brush = QBrush(QColor(241, 145, 39, 255))
        brush.setStyle(Qt.SolidPattern)
        self.viewMebuBar.setBackgroundBrush(brush)
        self.viewMebuBar.setForegroundBrush(brush)
        self.viewMebuBar.setInteractive(True)
        self.viewMebuBar.setSceneRect(QRectF(20, 20, 400, 50))
        self.MenuPageLabel = QLabel(self.centralwidget)
        self.MenuPageLabel.setObjectName(u"MenuPageLabel")
        self.MenuPageLabel.setGeometry(QRect(280, 0, 240, 70))
        font1 = QFont()
        font1.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \ud55c\ub098\uccb4 Air")
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setWeight(75);
        self.MenuPageLabel.setFont(font1)
        self.MenuPageLabel.setAlignment(Qt.AlignCenter)
        self.ButtonRegister = QPushButton(self.centralwidget)
        self.ButtonRegister.setObjectName(u"ButtonRegister")
        self.ButtonRegister.setGeometry(QRect(20, 5, 80, 51))
        self.ButtonRegister.setStyleSheet(u"background-color: rgb(241, 145, 039, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ud55c\ub098\uccb4 Air\";")
        icon = QIcon()
        icon.addFile(u"images/Document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonRegister.setIcon(icon)
        self.ButtonRegister.setIconSize(QSize(32, 32))
        self.ButtonRegister.setAutoRepeat(False)
        self.ButtonNFC = QPushButton(self.centralwidget)
        self.ButtonNFC.setObjectName(u"ButtonNFC")
        self.ButtonNFC.setGeometry(QRect(700, 5, 80, 51))
        self.ButtonNFC.setLayoutDirection(Qt.RightToLeft)
        self.ButtonNFC.setStyleSheet(u"background-color: rgb(241, 145, 039, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ud55c\ub098\uccb4 Air\";")
        icon1 = QIcon()
        icon1.addFile(u"images/Phone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonNFC.setIcon(icon1)
        self.ButtonNFC.setIconSize(QSize(32, 32))
        self.KeypadWidget = QWidget(self.centralwidget)
        self.KeypadWidget.setObjectName(u"KeypadWidget")
        self.KeypadWidget.setGeometry(QRect(479, 60, 321, 421))
        palette = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(240, 182, 183, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.KeypadWidget.setPalette(palette)
        self.KeypadWidget.setAutoFillBackground(True)
        self.KeypadWidget.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(self.KeypadWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 301, 401))
        self.Keypad = QGridLayout(self.gridLayoutWidget)
        self.Keypad.setObjectName(u"Keypad")
        self.Keypad.setContentsMargins(0, 0, 0, 0)
        self.KeypadButton_9 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_9.setObjectName(u"KeypadButton_9")
        self.KeypadButton_9.setMaximumSize(QSize(80, 80))
        self.KeypadButton_9.setStyleSheet(u"border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_9, 2, 2, 1, 1)

        self.KeypadButton_8 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_8.setObjectName(u"KeypadButton_8")
        self.KeypadButton_8.setMaximumSize(QSize(80, 80))
        self.KeypadButton_8.setStyleSheet(u"border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_8, 2, 1, 1, 1)

        self.KeypadButton_1 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_1.setObjectName(u"KeypadButton_1")
        self.KeypadButton_1.setMaximumSize(QSize(80, 80))
        self.KeypadButton_1.setStyleSheet(u"border-radius: 40px;\n"
"font: 75 72pt \"Adobe Arabic\";\n"
"color: rgb(255, 188, 50);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_1, 0, 0, 1, 1)

        self.KeypadButton_2 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_2.setObjectName(u"KeypadButton_2")
        self.KeypadButton_2.setMaximumSize(QSize(80, 80))
        self.KeypadButton_2.setStyleSheet(u"border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_2, 0, 1, 1, 1)

        self.KeypadButton_3 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_3.setObjectName(u"KeypadButton_3")
        self.KeypadButton_3.setMaximumSize(QSize(80, 80))
        self.KeypadButton_3.setStyleSheet(u"border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_3, 0, 2, 1, 1)

        self.KeypadButton_4 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_4.setObjectName(u"KeypadButton_4")
        self.KeypadButton_4.setMaximumSize(QSize(80, 80))
        self.KeypadButton_4.setStyleSheet(u"border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_4, 1, 0, 1, 1)

        self.KeypadButton_5 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_5.setObjectName(u"KeypadButton_5")
        self.KeypadButton_5.setMaximumSize(QSize(80, 80))
        self.KeypadButton_5.setStyleSheet(u"border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_5, 1, 1, 1, 1)

        self.KeypadButton_7 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_7.setObjectName(u"KeypadButton_7")
        self.KeypadButton_7.setMaximumSize(QSize(80, 80))
        self.KeypadButton_7.setStyleSheet(u"border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_7, 2, 0, 1, 1)

        self.KeypadButton_6 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_6.setObjectName(u"KeypadButton_6")
        self.KeypadButton_6.setMaximumSize(QSize(80, 80))
        self.KeypadButton_6.setStyleSheet(u"border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_6, 1, 2, 1, 1)

        self.KeypadButton_0 = QPushButton(self.gridLayoutWidget)
        self.KeypadButton_0.setObjectName(u"KeypadButton_0")
        self.KeypadButton_0.setMaximumSize(QSize(80, 80))
        self.KeypadButton_0.setStyleSheet(u"border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-color: rgb(255, 188, 50);\n"
"")

        self.Keypad.addWidget(self.KeypadButton_0, 3, 1, 1, 1)

        self.roundDisplay_1 = QPushButton(self.centralwidget)
        self.roundDisplay_1.setObjectName(u"roundDisplay_1")
        self.roundDisplay_1.setGeometry(QRect(5, 210, 50, 50))
        self.roundDisplay_1.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"")
        self.roundDisplay_2 = QPushButton(self.centralwidget)
        self.roundDisplay_2.setObjectName(u"roundDisplay_2")
        self.roundDisplay_2.setGeometry(QRect(65, 210, 50, 50))
        self.roundDisplay_2.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"")
        self.roundDisplay_3 = QPushButton(self.centralwidget)
        self.roundDisplay_3.setObjectName(u"roundDisplay_3")
        self.roundDisplay_3.setGeometry(QRect(125, 210, 50, 50))
        self.roundDisplay_3.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"")
        self.roundDisplay_4 = QPushButton(self.centralwidget)
        self.roundDisplay_4.setObjectName(u"roundDisplay_4")
        self.roundDisplay_4.setGeometry(QRect(185, 210, 50, 50))
        self.roundDisplay_4.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"")
        self.roundDisplay_5 = QPushButton(self.centralwidget)
        self.roundDisplay_5.setObjectName(u"roundDisplay_5")
        self.roundDisplay_5.setGeometry(QRect(245, 210, 50, 50))
        self.roundDisplay_5.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"")
        self.roundDisplay_6 = QPushButton(self.centralwidget)
        self.roundDisplay_6.setObjectName(u"roundDisplay_6")
        self.roundDisplay_6.setGeometry(QRect(305, 210, 50, 50))
        self.roundDisplay_6.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"")
        self.roundDisplay_7 = QPushButton(self.centralwidget)
        self.roundDisplay_7.setObjectName(u"roundDisplay_7")
        self.roundDisplay_7.setGeometry(QRect(365, 210, 50, 50))
        self.roundDisplay_7.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"")
        self.roundDisplay_8 = QPushButton(self.centralwidget)
        self.roundDisplay_8.setObjectName(u"roundDisplay_8")
        self.roundDisplay_8.setGeometry(QRect(425, 210, 50, 50))
        self.roundDisplay_8.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(219, 117, 015);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSignUp.setText(QCoreApplication.translate("MainWindow", u"SignUp", None))
        self.MenuPageLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">\ubc88\ud638 \uc785\ub825</span></p></body></html>", None))
        self.ButtonRegister.setText(QCoreApplication.translate("MainWindow", u"\ub4f1\ub85d", None))
        self.ButtonNFC.setText(QCoreApplication.translate("MainWindow", u"NFC", None))
        self.KeypadButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.KeypadButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.KeypadButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.KeypadButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.KeypadButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.KeypadButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.KeypadButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.KeypadButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.KeypadButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.KeypadButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.roundDisplay_1.setText("")
        self.roundDisplay_2.setText("")
        self.roundDisplay_3.setText("")
        self.roundDisplay_4.setText("")
        self.roundDisplay_5.setText("")
        self.roundDisplay_6.setText("")
        self.roundDisplay_7.setText("")
        self.roundDisplay_8.setText("")
    # retranslateUi

