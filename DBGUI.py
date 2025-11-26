import os, sys
from PyQt6.QtWidgets import QApplication
from modules.SystemWindow import SystemWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QLabel#Title{
        font-size: 16px;
        font-weight: bold;
    }
    QLabel#SubTitle{
        font-size: 12px;
        font-weight: bold;
    }
    QLabel#SecondaryText{
        font-size: 12px;
        color: gray;
    }
    QWidget#SubTab{
        border-radius: 10px;
        background-color: #EEEEEE;
        padding: 10px;
        margin-top: 10px;
    }
    QWidget#SubTab2{
        border-radius: 10px;
        background-color: #EEEEEE;
        padding-top: 20px;
    }
    QTableView {
        background-color: #EFEFEF;
    }
    QTableView::item {
        background-color: transparent;
    }
    QHeaderView::section {
        background-color: transparent;
        padding: 5px;
        border: 1px solid #EEEEEE;
        border-right: none;
    }
    QHeaderView::section:selected {
        background-color: #EEEEEE;
    }
    QTableCornerButton::section { 
        background: transparent;
    }
    QPushButton{
        border-radius: 5px;
        background-color: #EEEEEE;
        border: 2px solid #BBBBBB;
        padding: 10px;
    }         
    QPushButton::hover{
        background-color: #DDDDDD;
        color: #555555;
    }
    QPushButton::pressed{
        border: 2px solid #999999;
        background-color: #DDDDDD;
        color: #555555;
    }
    QListWidget {
        background-color: white;
        border: 1px solid #CCCCCC;
        border-radius: 5px;
    }
    QLineEdit {
        padding: 5px;
        border: 1px solid #CCCCCC;
        border-radius: 3px;
    }
    QDateEdit {
        padding: 5px;
        border: 1px solid #CCCCCC;
        border-radius: 3px;
    }
    QComboBox {
        padding: 5px;
        border: 1px solid #CCCCCC;
        border-radius: 3px;
    }
    QTextEdit {
        border: 1px solid #CCCCCC;
        border-radius: 3px;
        padding: 5px;
    }

    """)

    window = SystemWindow()
    sys.exit(app.exec())