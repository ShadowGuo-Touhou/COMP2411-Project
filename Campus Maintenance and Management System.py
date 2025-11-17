import os , sys
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class SystemWindow(QMainWindow):
    
    def __init__(self, parent = None):
        """
        Initialize the main window
        """
        super().__init__(parent)
        self.__initWindow()
        self.__initTab()
        self.__initTabOne()
        self.show()

    def __initWindow(self):
        # set window title
        self.setWindowTitle("Campus Maintenance and Management System")
        # set window size
        primaryScreenSize = QApplication.primaryScreen().size()
        self.setMinimumSize(primaryScreenSize.width()//2, primaryScreenSize.height()//2)

    def __initTab(self):
        """
        Initialize the tab widget of main window. It provides the page-like view
        """
        # using table widget instead of stack layout, see: https://www.pythonguis.com/tutorials/pyqt6-layouts/
        self._displayTab = QTabWidget()
        # set the position of the tab on top of the screen
        self._displayTab.setTabPosition(QTabWidget.TabPosition.North)
        # make the position of tabs movable
        self._displayTab.setMovable(True)
        # make the position of of tab center of the main window
        self.setCentralWidget(self._displayTab)

    def __initTabOne(self):
        """
        This tab is for manage and check activities
        """
        # create activity tab
        activityTab = QWidget()
        # create table layout see: https://www.pythonguis.com/tutorials/pyqt6-layouts/
        activityTabLayout = QVBoxLayout()
        activityTab.setLayout(activityTabLayout)
        # create title
        title = QLabel("Activity list")
        # set name, for css style sheet
        title.setObjectName("Title")
        activityTabLayout.addWidget(title)
        # create sub title
        title = QLabel("Check for maintenance activities in a specific location")
        # set name, for css syle sheet
        title.setObjectName("SecondaryText")
        activityTabLayout.addWidget(title)

        # create widget that chose activities
        activityTable = QWidget()
        activityTable.setObjectName("SubTab")
        # create explanation text
        title = QLabel("Building/Location") 
        title.setObjectName("SubTitle")
        # create layout
        activityTableLayout = QVBoxLayout()
        activityTable.setLayout(activityTableLayout)
        # add text
        activityTableLayout.addWidget(title)
        # add table to tab
        activityTabLayout.addWidget(activityTable)
        # create combo box for activities, see: https://www.pythonguis.com/docs/qcombobox/
        buildingSelection = QComboBox()
        buildingSelection.setObjectName("ActivityComboBox")
        activityTableLayout.addWidget(buildingSelection)
        # add buildings to the combo box
        for building in self.getBuilding():
            buildingSelection.addItem(building)
        buildingSelection.currentTextChanged.connect(self.__buildingSelected)
        title = QLabel("Result")
        title.setObjectName("Title")
        activityTableLayout.addWidget(title)
        # add activites to container
        table = self.getActivities()
        activityTableLayout.addWidget(table)

        # push widgets to top
        activityTabLayout.addStretch()

        # add tab to the window
        self._displayTab.addTab(activityTab, "Activity list")

#===========================Functional methods===================================================
    def getBuilding(self)->list:
        """
        Get all buildings from database
        Not completed yet, need the colation from database
        """
        buildings = ["All", "one", "two", "tree"]
        return buildings

    def getActivities(self)->QTableView:
        """
        Get all activites from database
        Not Completed yet, can possible be modeled into an universal table generator
        """
        # create QTable view, see: https://www.pythonguis.com/tutorials/pyqt6-qtableview-modelviews-numpy-pandas/
        table = QTableView()
        data = [[1,2,3],[4,5,6],[7,8,9],["A", "B", "C"],["A", "B", "C"],["A", "B", "C"],["A", "B", "C"],["A", "B", "C"],["A", "B", "C"]]
        model = TableModel(data)
        table.setModel(model)
        table.setShowGrid(False)

        return table
#==========================Connect methods============================================
    def __buildingSelected(self, s):
        print(s)

#==========================Customer Classes===========================================
class TableModel(QAbstractTableModel):
    """
    Process database informations into QTableView data, see: https://www.pythonguis.com/tutorials/pyqt6-qtableview-modelviews-numpy-pandas/
    """
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # get the value from cell
            value = self._data[index.row()][index.column()]
            # format the value based on the type
            match value:
                case float():
                    # return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignLeft
                    return "%.2f" % value
                case int():
                    # return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignLeft
                    return value
                case str():
                    return "'%s'" % value
        
        
    def rowCount(self, index):
        """return the how many rows there are """
        return len(self._data)
    
    def columnCount(self, index):
        """return the length of first row, needs all row has the length"""
        return len(self._data[0])

if __name__ == '__main__':
    #initialize
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
        background-color: #D3D3D3;
        padding: 10px;
        margin-top: 10px;
    }
    QComboBox#ActivityComboBox{

    }
    QTableView {
        background-color: #EEEEEE;
    }
    QTableView::item {
        background-color: transparent;
    }
    QHeaderView::section {
        background-color: transparent;
        padding: 5px;
        border: 1px solid #D3D3D3;
        border-right: none;
    }
    QHeaderView::section:selected {
        background-color: #D3D3D3;
    }
    """)

    pet = SystemWindow()
    sys.exit(app.exec())