import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .path import PATH_IMG


class UiInUse:
    def setupUi(self, widget):
        widget.resize(800, 480)

        # TODO: Rename variables of InUse, LogIn, and SignUp to be consistent
        # Example: frame => frame_smth, label => label_smth

        self.background_frame = QFrame(widget)
        self.background_frame.setGeometry(QRect(0, 0, 800, 480))
        self.background_frame.setStyleSheet(
            "QFrame {"
            "   background-color: rgb(241, 168, 23);"
            "}"
            "QLabel {"
            "   font: 20pt 배달의민족 주아;"
            "   color: white;"
            "}"
        )

        self.piano_picture = QLabel(self.background_frame)
        self.piano_picture.setGeometry(QRect(320, 30, 160, 150))
        self.piano_picture.setPixmap(QPixmap(os.path.join(PATH_IMG, "Piano.png")))

        self.used_time = QLabel(self.background_frame)
        self.used_time.setGeometry(QRect(0, 180, 800, 40))
        self.used_time.setStyleSheet("font-size: 16pt;")
        self.used_time.setText("00:00:00")
        self.used_time.setAlignment(Qt.AlignCenter)

        self.username = QLabel(self.background_frame)
        self.username.setGeometry(QRect(0, 230, 800, 41))
        self.username.setStyleSheet("font-size: 20pt;")
        self.username.setText("홍길동")
        self.username.setAlignment(Qt.AlignCenter)

        self.in_use = QLabel(self.background_frame)
        self.in_use.setGeometry(QRect(0, 270, 800, 71))
        self.in_use.setStyleSheet("font-size: 32pt;")
        self.in_use.setText("사용 중")
        self.in_use.setAlignment(Qt.AlignCenter)

        self.button_quit = QPushButton(self.background_frame)
        self.button_quit.setGeometry(QRect(340, 360, 120, 60))
        self.button_quit.setText("종료")
        self.button_quit.setStyleSheet(
            "QPushButton {"
            "   font: 20pt 배달의민족 주아;"
            "   color: white;"
            "   background-color: rgb(255, 0, 0);"
            "   border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "   color: rgb(120, 120, 120);"
            "   background-color: rgb(120, 0, 0);"
            "}"
        )
