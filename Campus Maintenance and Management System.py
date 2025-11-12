import os , sys
from PyQt6 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *


class SystemWindow(QMainWindow):
    
    def __init__(self, parent = None):
        """
        Initiate the main window
        """
        super().__init__(parent)
        self.show()


if __name__ == '__main__':
    #initialize
    app = QApplication(sys.argv)
    pet = SystemWindow()
    sys.exit(app.exec())