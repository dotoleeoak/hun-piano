from pathlib import Path

from PySide2.QtCore import QRect, Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QFrame, QLabel, QPushButton

PATH_IMG = Path(__file__).absolute().parents[1] / "image"


class UiInUse:
    def setupUi(self, widget):
        widget.resize(800, 480)

        self.frame_main = QFrame(widget)
        self.frame_main.setGeometry(QRect(0, 0, 800, 480))
        self.frame_main.setStyleSheet(
            "QFrame {"
            "   background-color: rgb(241, 168, 23);"
            "}"
            "QLabel {"
            "   font: 20pt 배달의민족 주아;"
            "   color: white;"
            "}"
        )

        self.picture_piano = QLabel(self.frame_main)
        self.picture_piano.setGeometry(QRect(320, 30, 160, 150))
        self.picture_piano.setPixmap(QPixmap(PATH_IMG / "Piano.png"))

        self.label_time = QLabel(self.frame_main)
        self.label_time.setGeometry(QRect(0, 180, 800, 40))
        self.label_time.setStyleSheet("font-size: 16pt;")
        self.label_time.setText("00:00:00")
        self.label_time.setAlignment(Qt.AlignCenter)

        self.label_name = QLabel(self.frame_main)
        self.label_name.setGeometry(QRect(0, 230, 800, 40))
        self.label_name.setStyleSheet("font-size: 20pt;")
        self.label_name.setText("홍길동")
        self.label_name.setAlignment(Qt.AlignCenter)

        self.label_in_use = QLabel(self.frame_main)
        self.label_in_use.setGeometry(QRect(0, 270, 800, 70))
        self.label_in_use.setStyleSheet("font-size: 32pt;")
        self.label_in_use.setText("사용 중")
        self.label_in_use.setAlignment(Qt.AlignCenter)

        self.button_quit = QPushButton(self.frame_main)
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
