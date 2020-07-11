# from PySide2.QtCore import QRect, QSize, Qt
# from PySide2.QtGui import QBrush, QColor, QIcon, QPalette, QPixmap
# from PySide2.QtWidgets import QFrame, QPushButton
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiLogIn:
    def setupUi(self, widget):
        widget.resize(800, 480)

        self.frame_keypad = QFrame(widget)
        self.frame_keypad.setGeometry(QRect(116, 275, 568, 180))
        self.frame_keypad.setStyleSheet(
            "QPushButton { "
            "   font: 36pt 배달의민족 주아; "
            "   color: rgb(255, 188, 50); "
            "   background-color: white; "
            "   border-style: outset; "
            "   border-width: 5px; "
            "   border-radius: 12px; "
            "   border-color: rgb(225, 158, 20); "
            "} "
            "QPushButton:hover { "
            "   background-color: rgb(223, 163, 43); "
            "   color: white; "
            "} "
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
            "color: white; background-color: rgb(249, 138, 15);"
        )

        img_NFC = QPixmap("../../Images/icon_2_2.png")
        self.button_NFC = QPushButton(self.menu_bar)
        self.button_NFC.setGeometry(QRect(700, 5, 90, 50))
        self.button_NFC.setIcon(QIcon(img_NFC))
        self.button_NFC.setIconSize(QSize(32, 32))
        self.button_NFC.setText("NFC")
        self.button_NFC.setStyleSheet(
            "font: 20pt 배달의민족 주아; "
            "background-color: rgba(0, 0, 0, 0); "
            "border-radius: 5px; "
        )

        img_register = QPixmap("../../Images/Document.png")
        self.button_register = QPushButton(self.menu_bar)
        self.button_register.setGeometry(QRect(10, 5, 90, 50))
        self.button_register.setIcon(QIcon(img_register))
        self.button_register.setIconSize(QSize(32, 32))
        self.button_register.setText("등록")
        self.button_register.setStyleSheet(
            "font: 20pt 배달의민족 주아; "
            "background-color: rgba(0, 0, 0, 0); "
            "border-radius: 5px; "
        )

        self.label_menu = QLabel(self.menu_bar)
        self.label_menu.setGeometry(QRect(300, 5, 200, 60))
        self.label_menu.setText("번호 입력")
        self.label_menu.setAlignment(Qt.AlignCenter)
        self.label_menu.setStyleSheet("font: 24pt 배달의민족 주아;")

        self.display_number = []
        for i in range(8):
            display = QLabel(self.menu_bar)
            display.setGeometry(QRect(80 * i + (60 if i < 4 else 110), 120, 70, 70))
            display.setStyleSheet(
                "font: 24pt 배달의민족 주아; "
                "background-color: rgb(199, 107, 5); "
                "border-radius: 16px; "
            )
            self.display_number.append(display)

        self.label_dash = QLabel(self.menu_bar)
        self.label_dash.setGeometry(QRect(390, 145, 20, 20))
        self.label_dash.setPixmap(QPixmap("../../Images/Stick2.png"))
