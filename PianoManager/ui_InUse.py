# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_InUse.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
<<<<<<< HEAD
    QRect, QRectF, QSize, QUrl, Qt)
=======
    QRect, QSize, QUrl, Qt)
>>>>>>> LinkingPages
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_InUse(object):
    def setupUi(self, InUse):
        if InUse.objectName():
            InUse.setObjectName(u"InUse")
        InUse.resize(800, 480)
<<<<<<< HEAD
        self.label = QLabel(InUse)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(325, 30, 160, 150))
        self.label.setPixmap(QPixmap(u"Images/Piano.png"))
        self.label_4 = QLabel(InUse)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 180, 91, 41))
        self.label_4.setStyleSheet(u"font: 16pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);")
        self.viewMebuBar = QGraphicsView(InUse)
        self.viewMebuBar.setObjectName(u"viewMebuBar")
        self.viewMebuBar.setEnabled(True)
        self.viewMebuBar.setGeometry(QRect(0, 0, 800, 481))
        palette = QPalette()
        brush = QBrush(QColor(241, 168, 23, 255))
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
        self.viewMebuBar.setPalette(palette)
        self.viewMebuBar.setAutoFillBackground(True)
        self.viewMebuBar.setStyleSheet(u"background-color: rgb(241, 168, 23);")
        brush1 = QBrush(QColor(241, 145, 39, 255))
        brush1.setStyle(Qt.SolidPattern)
        self.viewMebuBar.setBackgroundBrush(brush1)
        self.viewMebuBar.setForegroundBrush(brush1)
        self.viewMebuBar.setInteractive(True)
        self.viewMebuBar.setSceneRect(QRectF(20, 20, 400, 50))
        self.pushButton = QPushButton(InUse)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 360, 111, 61))
        palette1 = QPalette()
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(255, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.NoBrush)
        self.pushButton.setPalette(palette1)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"font: 12pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"background-color: red")
        self.label_3 = QLabel(InUse)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 260, 360, 71))
        self.label_3.setStyleSheet(u"font: 32pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(InUse)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(345, 230, 111, 41))
        self.label_2.setStyleSheet(u"font: 20pt \"\ubc30\ub2ec\uc758\ubbfc\uc871 \ub3c4\ud604\";\n"
"color: rgb(255, 255, 255);")
        self.viewMebuBar.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
=======
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
>>>>>>> LinkingPages

        self.retranslateUi(InUse)

        QMetaObject.connectSlotsByName(InUse)
    # setupUi

    def retranslateUi(self, InUse):
        InUse.setWindowTitle(QCoreApplication.translate("InUse", u"Form", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("InUse", u"01:30:10", None))
<<<<<<< HEAD
        self.pushButton.setText(QCoreApplication.translate("InUse", u"\uc885\ub8cc", None))
        self.label_3.setText(QCoreApplication.translate("InUse", u"\ud604\uc7ac \uc0ac\uc6a9 \uc911\uc785\ub2c8\ub2e4", None))
        self.label_2.setText(QCoreApplication.translate("InUse", u"\uc774\uc9c4\uc601 \ub2d8", None))
=======
        self.label_2.setText(QCoreApplication.translate("InUse", u"\uc774\uc9c4\uc601 \ub2d8", None))
        self.label_3.setText(QCoreApplication.translate("InUse", u"\ud604\uc7ac \uc0ac\uc6a9 \uc911\uc785\ub2c8\ub2e4", None))
        self.pushButton.setText(QCoreApplication.translate("InUse", u"\uc885\ub8cc", None))
>>>>>>> LinkingPages
    # retranslateUi

