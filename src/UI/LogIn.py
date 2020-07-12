import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .path import PATH_IMG


class UiLogIn:
    def setupUi(self, widget):
        widget.resize(800, 480)

        self.frame_keypad = QFrame(widget)
        self.frame_keypad.setGeometry(QRect(116, 275, 568, 180))
        self.frame_keypad.setStyleSheet(
            "QPushButton {"
            "   font: 36pt 배달의민족 주아;"
            "   color: rgb(255, 188, 50);"
            "   background-color: white;"
            "   border: 5px outset rgb(255, 158, 20);"
            "   border-radius: 16px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgb(223, 163, 43);"
            "   color: white;"
            "}"
        )

        self.button_keypad = []
        for i in range(10):
            button = QPushButton(self.frame_keypad)
            button.setGeometry(QRect(28 + 108 * (i % 5), 100 * (i // 5), 80, 80))
            button.setText(str(i))
            self.button_keypad.append(button)

        self.menu_bar = QFrame(widget)
        self.menu_bar.setGeometry(QRect(0, 0, 800, 250))
        self.menu_bar.setStyleSheet(
            "QFrame {"
            "   background-color: rgb(249, 138, 15);"
            "}"
            "QLabel {"
            "   color: white;"
            "   background-color: rgba(0, 0, 0, 0);"
            "   font: 24pt 배달의민족 주아;"
            "}"
            "QPushButton {"
            "   font: 16pt 배달의민족 주아;"
            "   color: white;"
            "   background-color: rgba(0, 0, 0, 0);"
            "   border: none;"
            "   border-radius: 16px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgb(241, 219, 194);"
            "}"
        )

        img_NFC = QPixmap(os.path.join(PATH_IMG, "icon_2_2.png"))
        self.button_NFC = QPushButton(self.menu_bar)
        self.button_NFC.setGeometry(QRect(680, 5, 110, 50))
        self.button_NFC.setIcon(QIcon(img_NFC))
        self.button_NFC.setIconSize(QSize(32, 32))
        self.button_NFC.setText(" NFC")

        img_register = QPixmap(os.path.join(PATH_IMG, "Document.png"))
        self.button_register = QPushButton(self.menu_bar)
        self.button_register.setGeometry(QRect(10, 5, 110, 50))
        self.button_register.setIcon(QIcon(img_register))
        self.button_register.setIconSize(QSize(32, 32))
        self.button_register.setText(" 등록")

        self.label_menu = QLabel(self.menu_bar)
        self.label_menu.setGeometry(QRect(300, 5, 200, 60))
        self.label_menu.setText("번호 입력")
        self.label_menu.setAlignment(Qt.AlignCenter)

        self.display_number = []
        for i in range(8):
            display = QLabel(self.menu_bar)
            display.setGeometry(QRect(80 * i + (60 if i < 4 else 110), 120, 70, 70))
            display.setStyleSheet(
                "background-color: rgb(199, 107, 5);" "border-radius: 16px;"
            )
            self.display_number.append(display)

        self.label_dash = QLabel(self.menu_bar)
        self.label_dash.setGeometry(QRect(390, 145, 20, 20))
        self.label_dash.setPixmap(QPixmap(os.path.join(PATH_IMG, "Stick2.png")))
