# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageSignUp.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(800, 480))
        self.actionSignUp = QAction(MainWindow)
        self.actionSignUp.setObjectName(u"actionSignUp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MebuBar = QGraphicsView(self.centralwidget)
        self.MebuBar.setObjectName(u"MebuBar")
        self.MebuBar.setEnabled(True)
        self.MebuBar.setGeometry(QRect(0, 0, 800, 60))
        self.MebuBar.setAutoFillBackground(False)
        self.MebuBar.setStyleSheet(u"background-color: rgb(241, 145, 39);")
        brush = QBrush(QColor(241, 145, 39, 255))
        brush.setStyle(Qt.SolidPattern)
        self.MebuBar.setBackgroundBrush(brush)
        self.MebuBar.setForegroundBrush(brush)
        self.MebuBar.setInteractive(True)
        self.MebuBar.setSceneRect(QRectF(20, 20, 400, 50))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 0, 240, 70))
        font = QFont()
        font.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50);
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(8, 5, 71, 51))
        palette = QPalette()
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush2 = QBrush(QColor(255, 152, 41, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush3)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        brush5 = QBrush(QColor(120, 120, 120, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush3)
        brush6 = QBrush(QColor(0, 0, 0, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.pushButton.setPalette(palette)
        font1 = QFont()
        font1.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font1.setPointSize(20)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 152, 41);")
        self.pushButton.setFlat(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 51, 40))
        font2 = QFont()
        font2.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font2.setPointSize(16)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 280, 120, 40))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 180, 101, 40))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.textEditName = QTextEdit(self.centralwidget)
        self.textEditName.setObjectName(u"textEditName")
        self.textEditName.setGeometry(QRect(30, 120, 200, 45))
        font3 = QFont()
        font3.setFamily(u"\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544")
        font3.setPointSize(18)
        self.textEditName.setFont(font3)
        self.textEditName.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEditName.setFrameShape(QFrame.WinPanel)
        self.textEditName.setFrameShadow(QFrame.Plain)
        self.textEditName_2 = QTextEdit(self.centralwidget)
        self.textEditName_2.setObjectName(u"textEditName_2")
        self.textEditName_2.setGeometry(QRect(30, 320, 231, 45))
        self.textEditName_2.setFont(font3)
        self.textEditName_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEditName_2.setInputMethodHints(Qt.ImhDigitsOnly)
        self.textEditName_2.setFrameShape(QFrame.WinPanel)
        self.textEditName_2.setFrameShadow(QFrame.Plain)
        self.textEditName_3 = QTextEdit(self.centralwidget)
        self.textEditName_3.setObjectName(u"textEditName_3")
        self.textEditName_3.setGeometry(QRect(30, 220, 80, 45))
        self.textEditName_3.setFont(font3)
        self.textEditName_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEditName_3.setInputMethodHints(Qt.ImhDigitsOnly)
        self.textEditName_3.setFrameShape(QFrame.WinPanel)
        self.textEditName_3.setFrameShadow(QFrame.Plain)
        self.textEditName_4 = QTextEdit(self.centralwidget)
        self.textEditName_4.setObjectName(u"textEditName_4")
        self.textEditName_4.setGeometry(QRect(150, 220, 110, 45))
        self.textEditName_4.setFont(font3)
        self.textEditName_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEditName_4.setInputMethodHints(Qt.ImhDigitsOnly)
        self.textEditName_4.setFrameShape(QFrame.WinPanel)
        self.textEditName_4.setFrameShadow(QFrame.Plain)
        self.textEditName_5 = QTextEdit(self.centralwidget)
        self.textEditName_5.setObjectName(u"textEditName_5")
        self.textEditName_5.setGeometry(QRect(300, 220, 110, 45))
        self.textEditName_5.setFont(font3)
        self.textEditName_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEditName_5.setInputMethodHints(Qt.ImhDigitsOnly)
        self.textEditName_5.setFrameShape(QFrame.WinPanel)
        self.textEditName_5.setFrameShadow(QFrame.Plain)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 230, 41, 31))
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 230, 41, 31))
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menubar.setNativeMenuBar(False)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSignUp.setText(QCoreApplication.translate("MainWindow", u"SignUp", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">\uc0ac\uc6a9\uc790 \ub4f1\ub85d</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ud648", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ud559\ubc88", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc804\ud654\ubc88\ud638", None))
        self.textEditName.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEditName_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEditName_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEditName_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEditName_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ubc30\ub2ec\uc758\ubbfc\uc871 \uc8fc\uc544'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"SignUp", None))
    # retranslateUi

