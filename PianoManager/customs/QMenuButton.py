from PySide2.QtWidgets import *
from PySide2.QtGui import QPalette, QColor

import sys

class QMenuButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.originalPalette = self.palette()
        self.newPalette = QPalette(self.palette())
        self.newPalette.setColor(QPalette.Normal, QPalette.Base, QColor(241, 245, 039))

    def setColor
        
        
