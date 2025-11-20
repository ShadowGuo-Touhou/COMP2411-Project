import os, sys
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from datetime import datetime, date

from sqlprocessor import SQLProcessor

class SystemWindow():
    
    def __init__(self, parent=None):
        """
        Initialize the main window
        """
        # Initialize database
        self.db = SQLProcessor("data.db")
        
        self.__initWindow()
        self.__initTab()
        self.__initTabOne()  # Activity list
        self.__initTabTwo()  # Admin Report
        self.__initTabThree()  # Data Management
        self.__initTabFour()   # Chemical Management
        self.__initTabFive()   # Activity Query
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
        Initialize the tab widget of main window.
        """
        self._displayTab = QTabWidget()
        self._displayTab.setTabPosition(QTabWidget.TabPosition.North)
        self._displayTab.setMovable(True)
        self.mainWindow.setCentralWidget(self._displayTab)

    def __initTabOne(self):
        """
        This tab is for manage and check activities
        """
        activityTab = QWidget()
        activityTabLayout = QVBoxLayout()
        activityTab.setLayout(activityTabLayout)
        
        # Title
        title = QLabel("Activity list")
        title.setObjectName("Title")
        activityTabLayout.addWidget(title)
        
        subtitle = QLabel("Check for maintenance activities in a specific location")
        subtitle.setObjectName("SecondaryText")
        activityTabLayout.addWidget(subtitle)

        # Building selection
        buildingWidget = QWidget()
        buildingWidget.setObjectName("SubTab")
        buildingLayout = QVBoxLayout()
        buildingWidget.setLayout(buildingLayout)
        
        buildingLabel = QLabel("Building/Location") 
        buildingLabel.setObjectName("SubTitle")
        buildingLayout.addWidget(buildingLabel)
        
        self.buildingSelection = QComboBox()
        self.buildingSelection.setObjectName("ActivityComboBox")
        buildingLayout.addWidget(self.buildingSelection)
        
        # Add buildings to combo box
        self.refreshBuildings()
        self.buildingSelection.currentTextChanged.connect(self.__buildingSelected)
        
        # Results section
        resultLabel = QLabel("Result")
        resultLabel.setObjectName("Title")
        buildingLayout.addWidget(resultLabel)
        
        self.activityTable = self.getActivities()
        buildingLayout.addWidget(self.activityTable)

        activityTabLayout.addWidget(buildingWidget)
        activityTabLayout.addStretch()
        # self._displayTab.addTab(activityTab, "Activity list")

    def __initTabTwo(self):
        reportTab = QWidget()
        reportTabLayout = QVBoxLayout()
        reportTab.setLayout(reportTabLayout)
        
        # Titles
        title = QLabel("Generate System Reports")
        title.setObjectName("Title")
        reportTabLayout.addWidget(title)
        
        subtitle = QLabel("Generate pre-defined reports for administrative review.")
        subtitle.setObjectName("SecondaryText")
        reportTabLayout.addWidget(subtitle)

        # Buttons
        buttonTab = QWidget()
        buttonTabLayout = QHBoxLayout()
        buttonTab.setLayout(buttonTabLayout)
        buttonTab.setObjectName("SubTab2")
        
        workDistribution = QPushButton("Worker Distribution")
        managerWorkload = QPushButton("Manager Workload")
        outSource = QPushButton("Outsource Summary")
        
        buttonTabLayout.addWidget(workDistribution)
        buttonTabLayout.addWidget(managerWorkload)
        buttonTabLayout.addWidget(outSource)
        
        workDistribution.clicked.connect(self.displayWorkerDistribution)
        managerWorkload.clicked.connect(self.displayManagerWorkload)
        outSource.clicked.connect(self.displayOutSource)

        reportTabLayout.addWidget(buttonTab)

        # Results area
        resultTab = QWidget()
        self._resultTabLayout = QVBoxLayout()
        resultTab.setLayout(self._resultTabLayout)
        resultTab.setObjectName("SubTab")
        
        resultLabel = QLabel("Result")
        resultLabel.setObjectName("Title")
        self._resultTabLayout.addWidget(resultLabel)

        reportTabLayout.addWidget(resultTab)
        reportTabLayout.addStretch()
        self._displayTab.addTab(reportTab, "Admin Report")

    def __initTabThree(self):
        queryTab = QWidget()
        queryTabLayout = QVBoxLayout()
        queryTab.setLayout(queryTabLayout)
        
        # Title
        title = QLabel("Data Management")
        title.setObjectName("Title")
        queryTabLayout.addWidget(title)
        
        subtitle = QLabel("Insert, update, or delete data from database tables")
        subtitle.setObjectName("SecondaryText")
        queryTabLayout.addWidget(subtitle)

        # Operation buttons
        opButtonTab = QWidget()
        opButtonLayout = QHBoxLayout()
        opButtonTab.setLayout(opButtonLayout)
        opButtonTab.setObjectName("SubTab2")
        
        insertBtn = QPushButton("Insert Data")
        updateBtn = QPushButton("Update Data")
        deleteBtn = QPushButton("Delete Data")
        
        opButtonLayout.addWidget(insertBtn)
        opButtonLayout.addWidget(updateBtn)
        opButtonLayout.addWidget(deleteBtn)
        
        insertBtn.clicked.connect(self.showInsertDialog)
        updateBtn.clicked.connect(self.showUpdateDialog)
        deleteBtn.clicked.connect(self.showDeleteDialog)
        
        queryTabLayout.addWidget(opButtonTab)
        
        # SQL File Execution section
        sqlFileWidget = QWidget()
        sqlFileWidget.setObjectName("SubTab")
        sqlFileLayout = QVBoxLayout()
        sqlFileWidget.setLayout(sqlFileLayout)
        
        sqlFileTitle = QLabel("Execute SQL File")
        sqlFileTitle.setObjectName("SubTitle")
        sqlFileLayout.addWidget(sqlFileTitle)
        
        # File selection area
        fileSelectionLayout = QHBoxLayout()
        
        self.sqlFilePathLabel = QLabel("No file selected")
        self.sqlFilePathLabel.setStyleSheet("color: gray;")
        fileSelectionLayout.addWidget(self.sqlFilePathLabel)
        
        browseFileBtn = QPushButton("Browse SQL File")
        browseFileBtn.clicked.connect(self.browseSqlFile)
        fileSelectionLayout.addWidget(browseFileBtn)
        
        sqlFileLayout.addLayout(fileSelectionLayout)
        
        # Execute button
        executeFileBtn = QPushButton("Execute SQL File")
        executeFileBtn.clicked.connect(self.executeSqlFile)
        sqlFileLayout.addWidget(executeFileBtn)
        
        queryTabLayout.addWidget(sqlFileWidget)
        
        # SQL Query section
        sqlWidget = QWidget()
        sqlWidget.setObjectName("SubTab")
        sqlLayout = QVBoxLayout()
        sqlWidget.setLayout(sqlLayout)
        
        sqlTitle = QLabel("Run SQL Query")
        sqlTitle.setObjectName("SubTitle")
        sqlLayout.addWidget(sqlTitle)
        
        self._queryArea = QTextEdit()
        self._queryArea.setPlaceholderText("Enter SQL query here...")
        sqlLayout.addWidget(self._queryArea)
        
        queryButton = QPushButton("Run Query")
        queryButton.clicked.connect(self.runQuery)
        sqlLayout.addWidget(queryButton)
        
        queryTabLayout.addWidget(sqlWidget)
        queryTabLayout.addStretch()
        
        self._displayTab.addTab(queryTab, "Data Management")

    def __initTabFour(self):
        """Tab for managing harmful chemicals"""
        chemicalTab = QWidget()
        chemicalLayout = QVBoxLayout()
        chemicalTab.setLayout(chemicalLayout)
        
        # Title
        title = QLabel("Harmful Chemicals Management")
        title.setObjectName("Title")
        chemicalLayout.addWidget(title)
        
        subtitle = QLabel("View, add, or remove harmful chemicals")
        subtitle.setObjectName("SecondaryText")
        chemicalLayout.addWidget(subtitle)

        # Chemical management widget
        chemWidget = QWidget()
        chemWidget.setObjectName("SubTab")
        chemMainLayout = QVBoxLayout()
        chemWidget.setLayout(chemMainLayout)
        
        # Current chemicals
        currentLabel = QLabel("Current Harmful Chemicals")
        currentLabel.setObjectName("SubTitle")
        chemMainLayout.addWidget(currentLabel)
        
        self.chemicalList = QListWidget()
        self.refreshChemicalList()
        chemMainLayout.addWidget(self.chemicalList)
        
        # Add/Remove chemicals
        chemOpLayout = QHBoxLayout()
        
        self.newChemicalInput = QLineEdit()
        self.newChemicalInput.setPlaceholderText("Enter new chemical name")
        chemOpLayout.addWidget(self.newChemicalInput)
        
        addChemicalBtn = QPushButton("Add Chemical")
        addChemicalBtn.clicked.connect(self.addChemical)
        chemOpLayout.addWidget(addChemicalBtn)
        
        removeChemicalBtn = QPushButton("Remove Selected")
        removeChemicalBtn.clicked.connect(self.removeChemical)
        chemOpLayout.addWidget(removeChemicalBtn)
        
        chemMainLayout.addLayout(chemOpLayout)
        chemicalLayout.addWidget(chemWidget)
        chemicalLayout.addStretch()
        
        self._displayTab.addTab(chemicalTab, "Chemical Management")

    def __initTabFive(self):
        """Tab for querying activities by location and date"""
        queryTab = QWidget()
        queryLayout = QVBoxLayout()
        queryTab.setLayout(queryLayout)
        
        # Title
        title = QLabel("Activity Query")
        title.setObjectName("Title")
        queryLayout.addWidget(title)
        
        subtitle = QLabel("Query activities by location and date range")
        subtitle.setObjectName("SecondaryText")
        queryLayout.addWidget(subtitle)

        # Query form
        formWidget = QWidget()
        formWidget.setObjectName("SubTab")
        formLayout = QVBoxLayout()
        formWidget.setLayout(formLayout)
        
        # Location selection
        locationLayout = QHBoxLayout()
        locationLabel = QLabel("Location:")
        locationLayout.addWidget(locationLabel)
        
        self.queryLocationCombo = QComboBox()
        self.refreshQueryLocations()
        locationLayout.addWidget(self.queryLocationCombo)
        formLayout.addLayout(locationLayout)
        
        # Date range
        dateLayout = QHBoxLayout()
        
        startDateLayout = QVBoxLayout()
        startDateLabel = QLabel("Start Date:")
        startDateLayout.addWidget(startDateLabel)
        self.startDateEdit = QDateEdit()
        self.startDateEdit.setDate(QDate.currentDate())
        self.startDateEdit.setCalendarPopup(True)
        startDateLayout.addWidget(self.startDateEdit)
        dateLayout.addLayout(startDateLayout)
        
        endDateLayout = QVBoxLayout()
        endDateLabel = QLabel("End Date:")
        endDateLayout.addWidget(endDateLabel)
        self.endDateEdit = QDateEdit()
        self.endDateEdit.setDate(QDate.currentDate().addDays(30))
        self.endDateEdit.setCalendarPopup(True)
        endDateLayout.addWidget(self.endDateEdit)
        dateLayout.addLayout(endDateLayout)
        
        formLayout.addLayout(dateLayout)
        
        # Query button
        queryBtn = QPushButton("Query Activities")
        queryBtn.clicked.connect(self.queryActivities)
        formLayout.addWidget(queryBtn)
        
        queryLayout.addWidget(formWidget)
        
        # Results area
        resultsWidget = QWidget()
        resultsWidget.setObjectName("SubTab")
        self.resultsLayout = QVBoxLayout()
        resultsWidget.setLayout(self.resultsLayout)
        
        resultsLabel = QLabel("Query Results")
        resultsLabel.setObjectName("Title")
        self.resultsLayout.addWidget(resultsLabel)
        
        queryLayout.addWidget(resultsWidget)
        queryLayout.addStretch()
        
        self._displayTab.addTab(queryTab, "Activity Query")

    def refreshBuildings(self):
        """Refresh building list from database"""
        self.buildingSelection.clear()
        buildings = self.db.getBuildings()
        for building in buildings:
            self.buildingSelection.addItem(building[0])

    def refreshQueryLocations(self):
        """Refresh location list for query tab"""
        self.queryLocationCombo.clear()
        buildings = self.db.getBuildings()
        for building in buildings:
            self.queryLocationCombo.addItem(building[0])

    def refreshChemicalList(self):
        """Refresh chemical list"""
        self.chemicalList.clear()
        chemicals = self.db.getHarmfulChemicals()
        for chemical in chemicals:
            self.chemicalList.addItem(chemical)

    def getActivities(self):
        """
        Get all activities from database
        """
        table = QTableView()
        # Get activities for the first building by default
        if self.buildingSelection.count() > 0:
            building = self.buildingSelection.currentText()
            data = self.db.select("Activity", "*", f"AID IN (SELECT AID FROM HoldIn WHERE LocationName='{building}')")
        else:
            data = self.db.select("Activity")
        
        model = TableModel(data)
        table.setModel(model)
        table.setShowGrid(False)
        return table

    def query(self, query_text):
        """
        Execute a query and return results
        """
        try:
            return self.db.fetch_all(query_text)
        except Exception as e:
            print(f"Query error: {e}")
            return []

    # ==========================Connect methods============================================
    def __buildingSelected(self, s):
        """When building is selected, refresh activities"""
        if hasattr(self, 'activityTable'):
            # Remove old table and create new one
            parent = self.activityTable.parent()
            layout = parent.layout()
            layout.removeWidget(self.activityTable)
            self.activityTable.deleteLater()
            
            self.activityTable = self.getActivities()
            layout.addWidget(self.activityTable)

    def displayWorkerDistribution(self):
        """Display worker distribution report"""
        query = """
        SELECT W.Name, COUNT(A.AID) as ActivityCount 
        FROM Worker W 
        LEFT JOIN Assigned A ON W.WID = A.WID 
        GROUP BY W.WID, W.Name
        """
        data = self.db.fetch_all(query)
        self.displayReport(data, "Worker Distribution")

    def displayManagerWorkload(self):
        """Display manager workload report"""
        query = """
        SELECT M.Name, COUNT(DISTINCT L.Name) as Locations, COUNT(DISTINCT A.AID) as Activities
        FROM Manager M 
        LEFT JOIN Location L ON M.MID = L.Supervisor
        LEFT JOIN Activity A ON M.MID = A.AID  -- Assuming AID relates to manager
        GROUP BY M.MID, M.Name
        """
        data = self.db.fetch_all(query)
        self.displayReport(data, "Manager Workload")

    def displayOutSource(self):
        """Display outsource summary report"""
        query = """
        SELECT C.Name, COUNT(W.AID) as ContractCount, SUM(W.ContractedPayment) as TotalPayment
        FROM Company C 
        LEFT JOIN WorkOn W ON C.CompanyID = W.CompanyID
        GROUP BY C.CompanyID, C.Name
        """
        data = self.db.fetch_all(query)
        self.displayReport(data, "Outsource Summary")

    def displayReport(self, data, title):
        """Display a report in the results area"""
        # Clear previous results
        while self._resultTabLayout.count() > 1:
            item = self._resultTabLayout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()
        
        if data:
            table = QTableView()
            model = TableModel(data)
            table.setModel(model)
            self._resultTabLayout.addWidget(table)
        else:
            label = QLabel("No data found")
            self._resultTabLayout.addWidget(label)

    def showInsertDialog(self):
        """Show insert data dialog"""
        dialog = DataOperationDialog(self.db, "insert", self.mainWindow)
        dialog.exec()

    def showUpdateDialog(self):
        """Show update data dialog"""
        dialog = DataOperationDialog(self.db, "update", self.mainWindow)
        dialog.exec()

    def showDeleteDialog(self):
        """Show delete data dialog"""
        dialog = DataOperationDialog(self.db, "delete", self.mainWindow)
        dialog.exec()

    def browseSqlFile(self):
        """Browse for SQL file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self.mainWindow,
            "Select SQL File",
            "",
            "SQL Files (*.sql);;All Files (*)"
        )
        
        if file_path:
            self.sqlFilePathLabel.setText(file_path)
            self.sqlFilePathLabel.setStyleSheet("color: black;")

    def executeSqlFile(self):
        """Execute the selected SQL file"""
        file_path = self.sqlFilePathLabel.text()
        
        if not file_path or file_path == "No file selected":
            QMessageBox.warning(self.mainWindow, "Warning", "Please select a SQL file first.")
            return
        
        try:
            # Use the SQL processor's readFile method
            success = self.db.readFile(file_path)
            
            if success:
                QMessageBox.information(self.mainWindow, "Success", "SQL file executed successfully!")
                
                # Refresh data in various tabs to reflect changes
                self.refreshBuildings()
                self.refreshQueryLocations()
                self.refreshChemicalList()
                
                # Refresh activity table if it exists
                if hasattr(self, 'activityTable') and self.buildingSelection.count() > 0:
                    self.__buildingSelected(self.buildingSelection.currentText())
                    
            else:
                QMessageBox.critical(self.mainWindow, "Error", "Failed to execute SQL file.")
                
        except Exception as e:
            QMessageBox.critical(self.mainWindow, "Error", f"Error executing SQL file: {str(e)}")

    def runQuery(self):
        """Execute SQL query from text area"""
        query_text = self._queryArea.toPlainText().strip()
        if not query_text:
            return
            
        result = self.query(query_text)
        
        # Find and clear previous result
        for i in reversed(range(self._displayTab.currentWidget().layout().count())):
            item = self._displayTab.currentWidget().layout().itemAt(i)
            if item and hasattr(item, 'widget') and item.widget() and item.widget().objectName() == "QueryResult":
                item.widget().deleteLater()
        
        if isinstance(result, list) and result:
            resultWidget = QWidget()
            resultWidget.setObjectName("QueryResult")
            resultLayout = QVBoxLayout()
            resultWidget.setLayout(resultLayout)
            
            title = QLabel("Query Result")
            title.setObjectName("Title")
            resultLayout.addWidget(title)
            
            table = QTableView()
            table.setModel(TableModel(result))
            resultLayout.addWidget(table)
            
            self._displayTab.currentWidget().layout().addWidget(resultWidget)

    def addChemical(self):
        """Add a new harmful chemical"""
        chemical = self.newChemicalInput.text().strip()
        if chemical and self.db.addHarmfulChemical(chemical):
            self.refreshChemicalList()
            self.newChemicalInput.clear()

    def removeChemical(self):
        """Remove selected harmful chemical"""
        current_item = self.chemicalList.currentItem()
        if current_item:
            chemical = current_item.text()
            if self.db.removeHarmfulChemical(chemical):
                self.refreshChemicalList()

    def queryActivities(self):
        """Query activities based on location and date range"""
        location = self.queryLocationCombo.currentText()
        start_date = self.startDateEdit.date().toString("yyyy-MM-dd")
        end_date = self.endDateEdit.date().toString("yyyy-MM-dd")
        
        # Clear previous results
        while self.resultsLayout.count() > 1:
            item = self.resultsLayout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()
        
        if location:
            chemicals = self.db.getHarmfulChemicals()
            results = self.db.queryForActivity(location, start_date, end_date, chemicals)
            
            if results:
                table = QTableView()
                table.setModel(TableModel(results))
                self.resultsLayout.addWidget(table)
            else:
                label = QLabel("No activities found for the selected criteria")
                self.resultsLayout.addWidget(label)


class DataOperationDialog(QDialog):
    """Dialog for insert, update, and delete operations"""
    
    def __init__(self, db, operation, parent=None):
        super().__init__(parent)
        self.db = db
        self.operation = operation
        self.setWindowTitle(f"{operation.title()} Data")
        self.setModal(True)
        self.resize(600, 400)
        
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Table selection
        tableLayout = QHBoxLayout()
        tableLayout.addWidget(QLabel("Select Table:"))
        
        self.tableCombo = QComboBox()
        self.tableCombo.addItems(self.db.getTables())
        self.tableCombo.currentTextChanged.connect(self.tableChanged)
        tableLayout.addWidget(self.tableCombo)
        
        layout.addLayout(tableLayout)
        
        # Data table
        self.dataTable = QTableWidget()
        layout.addWidget(self.dataTable)
        
        # Operation specific widgets
        if self.operation == "insert":
            self.setupInsertUI(layout)
        elif self.operation == "update":
            self.setupUpdateUI(layout)
        elif self.operation == "delete":
            self.setupDeleteUI(layout)
        
        # Buttons
        buttonLayout = QHBoxLayout()
        
        executeBtn = QPushButton("Execute")
        executeBtn.clicked.connect(self.executeOperation)
        buttonLayout.addWidget(executeBtn)
        
        cancelBtn = QPushButton("Cancel")
        cancelBtn.clicked.connect(self.reject)
        buttonLayout.addWidget(cancelBtn)
        
        layout.addLayout(buttonLayout)
        
        # Initialize with first table
        if self.tableCombo.count() > 0:
            self.tableChanged(self.tableCombo.currentText())
    
    def setupInsertUI(self, layout):
        """Setup UI for insert operation"""
        addRowBtn = QPushButton("+ Add Row")
        addRowBtn.clicked.connect(self.addRow)
        layout.addWidget(addRowBtn)
        
        # Start with one empty row
        self.addRow()
    
    def setupUpdateUI(self, layout):
        """Setup UI for update operation"""
        conditionLayout = QHBoxLayout()
        conditionLayout.addWidget(QLabel("WHERE Condition:"))
        
        self.conditionEdit = QLineEdit()
        self.conditionEdit.setPlaceholderText("e.g., ID=1")
        conditionLayout.addWidget(self.conditionEdit)
        
        layout.addLayout(conditionLayout)
    
    def setupDeleteUI(self, layout):
        """Setup UI for delete operation"""
        conditionLayout = QHBoxLayout()
        conditionLayout.addWidget(QLabel("WHERE Condition:"))
        
        self.conditionEdit = QLineEdit()
        self.conditionEdit.setPlaceholderText("e.g., ID=1 (leave empty to delete all)")
        conditionLayout.addWidget(self.conditionEdit)
        
        layout.addLayout(conditionLayout)
    
    def tableChanged(self, table_name):
        """When table selection changes, update the data table"""
        columns = self.db.getColumns(table_name)
        self.dataTable.setColumnCount(len(columns))
        self.dataTable.setHorizontalHeaderLabels(columns)
        
        if self.operation == "insert":
            self.dataTable.setRowCount(1)
            for col in range(len(columns)):
                self.dataTable.setItem(0, col, QTableWidgetItem(""))
    
    def addRow(self):
        """Add a new row for insert operation"""
        row = self.dataTable.rowCount()
        self.dataTable.setRowCount(row + 1)
        for col in range(self.dataTable.columnCount()):
            self.dataTable.setItem(row, col, QTableWidgetItem(""))
    
    def executeOperation(self):
        """Execute the database operation"""
        table = self.tableCombo.currentText()
        
        try:
            if self.operation == "insert":
                self.executeInsert(table)
            elif self.operation == "update":
                self.executeUpdate(table)
            elif self.operation == "delete":
                self.executeDelete(table)
                
            QMessageBox.information(self, "Success", f"{self.operation.title()} operation completed successfully!")
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Operation failed: {str(e)}")
    
    def executeInsert(self, table):
        """Execute insert operation"""
        # 获取表的列信息（包括数据类型）
        column_info = self.getColumnTypes(table)
        
        for row in range(self.dataTable.rowCount()):
            data = {}
            for col in range(self.dataTable.columnCount()):
                header = self.dataTable.horizontalHeaderItem(col).text()
                item = self.dataTable.item(row, col)
                value = item.text().strip() if item else ""
                
                # 获取该列的数据类型
                col_type = column_info.get(header, "TEXT")  # 默认为TEXT
                
                # 处理空值
                if not value:
                    data[header] = "NULL"
                else:
                    # 只有TEXT类型才添加引号
                    if "TEXT" in col_type.upper():
                        # 移除用户输入中可能包含的引号，然后加上引号
                        value = value.replace('"', '').replace("'", "")
                        data[header] = f"'{value}'"
                    else:
                        # 对于非TEXT类型（如INTEGER, REAL等），直接使用值
                        data[header] = value
            
            if data:
                success = self.db.insert(table, data)
                if not success:
                    raise Exception(f"Failed to insert row {row + 1}")

    def getColumnTypes(self, table_name):
        """获取表的列信息，包括数据类型"""
        # 查询sqlite_master表获取表定义
        query = f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        result = self.db.fetch_all(query)
        
        if not result:
            return {}
        
        # 解析CREATE TABLE语句来获取列定义
        create_sql = result[0][0]
        column_types = {}
        
        # 简单的解析逻辑，提取列名和类型
        # 找到括号内的列定义部分
        start = create_sql.find('(')
        end = create_sql.rfind(')')
        if start == -1 or end == -1:
            return {}
        
        columns_def = create_sql[start+1:end]
        # 分割各个列定义
        column_defs = [col.strip() for col in columns_def.split(',')]
        
        for col_def in column_defs:
            # 跳过约束定义（如PRIMARY KEY, FOREIGN KEY等）
            if col_def.upper().startswith(('PRIMARY', 'FOREIGN', 'CHECK', 'UNIQUE')):
                continue
            
            # 提取列名和类型
            parts = col_def.split()
            if len(parts) >= 2:
                col_name = parts[0].strip('"\'')  # 移除可能的引号
                col_type = parts[1].upper()
                column_types[col_name] = col_type
        
        return column_types
    
    def executeUpdate(self, table):
        """Execute update operation"""
        if self.dataTable.rowCount() == 0:
            raise Exception("No data to update")
            
        changes = {}
        for col in range(self.dataTable.columnCount()):
            header = self.dataTable.horizontalHeaderItem(col).text()
            item = self.dataTable.item(0, col)
            value = item.text().strip() if item else ""
            
            if value:
                value = value.replace('"', '').replace("'", "")
                changes[header] = f"'{value}'"
        
        condition = self.conditionEdit.text().strip() or "1=1"
        success = self.db.update(table, changes, condition)
        
        if not success:
            raise Exception("Update operation failed")
    
    def executeDelete(self, table):
        """Execute delete operation"""
        condition = self.conditionEdit.text().strip() or "1=1"
        success = self.db.delete(table, condition)
        
        if not success:
            raise Exception("Delete operation failed")


class TableModel(QAbstractTableModel):
    """
    Process database information into QTableView data
    """
    def __init__(self, data):
        super().__init__()
        self._data = data if data else []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if index.row() < len(self._data) and index.column() < len(self._data[0]):
                value = self._data[index.row()][index.column()]
                if value is None:
                    return ""
                elif isinstance(value, float):
                    return "%.2f" % value
                else:
                    return str(value)
        return None
        
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0]) if self._data else 0


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
