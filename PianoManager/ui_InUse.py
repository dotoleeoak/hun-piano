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
        self.frame = QFrame(InUse)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 800, 480))
        self.frame.setStyleSheet(u"background-color: rgb(241, 168, 23);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 30, 160, 150))
        self.label.setPixmap(QPixmap(u"Images/Piano.png"))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 180, 800, 40))
        self.label_4.setStyleSheet(u"font: 16pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 230, 800, 41))
        self.label_2.setStyleSheet(u"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 270, 800, 71))
        self.label_3.setStyleSheet(u"font: 32pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 360, 120, 60))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
        self.pushButton.setPalette(palette)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"font: 15pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"background-color: red")
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.label.raise_()

        self.retranslateUi(InUse)

        QMetaObject.connectSlotsByName(InUse)
    # setupUi

    def retranslateUi(self, InUse):
        InUse.setWindowTitle(QCoreApplication.translate("InUse", u"Form", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("InUse", u"01:30:10", None))
        self.label_2.setText(QCoreApplication.translate("InUse", u"\uc774\uc9c4\uc601 \ub2d8", None))
        self.label_3.setText(QCoreApplication.translate("InUse", u"\ud604\uc7ac \uc0ac\uc6a9 \uc911\uc785\ub2c8\ub2e4", None))
        self.pushButton.setText(QCoreApplication.translate("InUse", u"\uc885\ub8cc", None))
    # retranslateUi

