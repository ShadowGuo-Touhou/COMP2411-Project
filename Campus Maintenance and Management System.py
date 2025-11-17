import os , sys
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class SystemWindow():
    
    def __init__(self, parent = None):
        """
        Initialize the main window
        """
        self.__initWindow()
        self.__initTab()
        self.__initTabOne()
        self.__initTabTwo()
        self.mainWindow.show()

    def __initWindow(self):
        self.mainWindow = QMainWindow()
        # set window title
        self.mainWindow.setWindowTitle("Campus Maintenance and Management System")
        # set window size
        primaryScreenSize = QApplication.primaryScreen().size()
        self.mainWindow.setMinimumSize(primaryScreenSize.width()//2, primaryScreenSize.height()//2)

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
        self.mainWindow.setCentralWidget(self._displayTab)

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

    def __initTabTwo(self):
        # create layout
        reportTab = QWidget()
        reportTabLayout = QVBoxLayout()
        reportTab.setLayout(reportTabLayout)
        # titles
        title = QLabel("Generate System Reports")
        title.setObjectName("Title")
        reportTabLayout.addWidget(title)
        title = QLabel("Generate pre-defined reports for administrative review.")
        title.setObjectName("SecondaryText")
        reportTabLayout.addWidget(title)

        # sub Tab for buttons
        buttonTab = QWidget()
        buttonTabLayout = QHBoxLayout()
        buttonTab.setLayout(buttonTabLayout)
        buttonTab.setObjectName("SubTab2")
        # create buttons
        workDistribution = QPushButton("Worker Distribution")
        mangerWorkload = QPushButton("Manager Workload")
        outSource = QPushButton("Outsource Summary")
        # add buttons
        buttonTabLayout.addWidget(workDistribution)
        buttonTabLayout.addWidget(mangerWorkload)
        buttonTabLayout.addWidget(outSource)
        # add button connect function
        workDistribution.clicked.connect(self.displayWorkerDistribution)
        mangerWorkload.clicked.connect(self.displayMangerWorkload)
        outSource.clicked.connect(self.displayOutSource)

        # add subtab
        reportTabLayout.addWidget(buttonTab)
        # add to tab
        self._displayTab.addTab(reportTab, "Admin Report")

        # sub tab for results
        resultTab = QWidget()
        self._resultTabLayout = QVBoxLayout()
        resultTab.setLayout(self._resultTabLayout)
        resultTab.setObjectName("SubTab")
        # add text
        text = QLabel("Result")
        text.setObjectName("Title")
        self._resultTabLayout.addWidget(text)

        reportTabLayout.addWidget(resultTab)
        
        reportTabLayout.addStretch()


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
        data = self.query("fuck you")
        model = TableModel(data)
        table.setModel(model)
        table.setShowGrid(False)

        return table
  
    def query(self, query) -> list:
        """
        Send a query to database and returns a list
        Not completed yet
        """
        return [[1,2,3,4,5,6,7,8,9,10,11,12],[1,2,3,4,5,6,7,8,9,10,11,12],[1,2,3,4,5,6,7,8,9,10,11,12]]
#==========================Connect methods============================================
    def __buildingSelected(self, s):
        print(s)
    
    def displayWorkerDistribution(self)->QTableView:
        """
        Get worker in each activities
        Not COmpleted yet
        """
        table = QTableView()
        table.setModel(TableModel(self.query("fuck")))
        if self._resultTabLayout.count() == 2:
            self._resultTabLayout.takeAt(1)
        self._resultTabLayout.addWidget(table)
    
    def displayMangerWorkload(self)->QTableView:
        """
        Get worker in each activities
        Not COmpleted yet
        """
        table = QTableView()
        table.setModel(TableModel(self.query("fuck")))
        if self._resultTabLayout.count() == 2:
            self._resultTabLayout.takeAt(1)
        self._resultTabLayout.addWidget(table)
        
    def displayOutSource(self)->QTableView:
        """
        Get worker in each activities
        Not COmpleted yet
        """
        table = QTableView()
        table.setModel(TableModel(self.query("fuck")))
        if self._resultTabLayout.count() == 2:
            self._resultTabLayout.takeAt(1)
        self._resultTabLayout.addWidget(table)
  
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
    """)

    pet = SystemWindow()
    sys.exit(app.exec())