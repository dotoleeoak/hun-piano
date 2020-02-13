# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_InUse.ui'
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

class Ui_InUse(object):
    def setupUi(self, InUse):
        if InUse.objectName():
            InUse.setObjectName(u"InUse")
        InUse.resize(800, 480)
        self.BackgroundFrame = QFrame(InUse)
        self.BackgroundFrame.setObjectName(u"BackgroundFrame")
        self.BackgroundFrame.setGeometry(QRect(0, 0, 800, 480))
        self.BackgroundFrame.setStyleSheet(u"background-color: rgb(241, 168, 23);")
        self.BackgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QFrame.Raised)
        self.PianoPic = QLabel(self.BackgroundFrame)
        self.PianoPic.setObjectName(u"PianoPic")
        self.PianoPic.setGeometry(QRect(320, 30, 160, 150))
        self.PianoPic.setPixmap(QPixmap(u"Images/Piano.png"))
        self.UsedTime = QLabel(self.BackgroundFrame)
        self.UsedTime.setObjectName(u"UsedTime")
        self.UsedTime.setGeometry(QRect(0, 180, 800, 40))
        self.UsedTime.setStyleSheet(u"font: 16pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);")
        self.UsedTime.setAlignment(Qt.AlignCenter)
        self.UserName = QLabel(self.BackgroundFrame)
        self.UserName.setObjectName(u"UserName")
        self.UserName.setGeometry(QRect(0, 230, 800, 41))
        self.UserName.setStyleSheet(u"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);")
        self.UserName.setAlignment(Qt.AlignCenter)
        self.InUseLabel = QLabel(self.BackgroundFrame)
        self.InUseLabel.setObjectName(u"InUseLabel")
        self.InUseLabel.setGeometry(QRect(0, 270, 800, 71))
        self.InUseLabel.setStyleSheet(u"font: 32pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);")
        self.InUseLabel.setAlignment(Qt.AlignCenter)
        self.ButtonQuit = QPushButton(self.BackgroundFrame)
        self.ButtonQuit.setObjectName(u"ButtonQuit")
        self.ButtonQuit.setGeometry(QRect(340, 360, 120, 60))
        self.ButtonQuit.setStyleSheet(u"font: 16pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"background-color: red")
        self.UsedTime.raise_()
        self.UserName.raise_()
        self.InUseLabel.raise_()
        self.ButtonQuit.raise_()
        self.PianoPic.raise_()

        self.retranslateUi(InUse)

        QMetaObject.connectSlotsByName(InUse)
    # setupUi

    def retranslateUi(self, InUse):
        InUse.setWindowTitle(QCoreApplication.translate("InUse", u"Form", None))
        self.PianoPic.setText("")
        self.UsedTime.setText(QCoreApplication.translate("InUse", u"01:30:10", None))
        self.UserName.setText(QCoreApplication.translate("InUse", u"\uc774\uc9c4\uc601 \ub2d8", None))
        self.InUseLabel.setText(QCoreApplication.translate("InUse", u"\ud604\uc7ac \uc0ac\uc6a9 \uc911\uc785\ub2c8\ub2e4", None))
        self.ButtonQuit.setText(QCoreApplication.translate("InUse", u"\uc885\ub8cc", None))
    # retranslateUi

