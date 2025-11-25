import os, sys
from PyQt6 import *
from PyQt6 import QtCore
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
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir,"data.db")
        self.db = SQLProcessor(db_path)
        
        self.__initWindow()
        self.__initTab()
        # Tab one is useless, so I delete it
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
        
        # Time range selection
        timeGroup = QGroupBox("Time Range")
        timeLayout = QVBoxLayout()
        timeGroup.setLayout(timeLayout)
        
        # Any time checkbox
        self.anyTimeCheckbox = QCheckBox("Any Time")
        self.anyTimeCheckbox.stateChanged.connect(self.toggleDateRange)
        timeLayout.addWidget(self.anyTimeCheckbox)
        
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
        
        timeLayout.addLayout(dateLayout)
        formLayout.addWidget(timeGroup)
        
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

    def toggleDateRange(self, state):
        """Toggle date range fields based on Any Time checkbox"""
        if state == Qt.CheckState.Checked.value:
            # Any Time selected - disable date fields
            self.startDateEdit.setEnabled(False)
            self.endDateEdit.setEnabled(False)
            # Apply visual styling to show they are disabled
            self.startDateEdit.setStyleSheet("background-color: #F0F0F0; color: #A0A0A0;")
            self.endDateEdit.setStyleSheet("background-color: #F0F0F0; color: #A0A0A0;")
        else:
            # Specific time range - enable date fields
            self.startDateEdit.setEnabled(True)
            self.endDateEdit.setEnabled(True)
            # Reset styling
            self.startDateEdit.setStyleSheet("")
            self.endDateEdit.setStyleSheet("")

    def refreshQueryLocations(self):
        """Refresh location list for query tab"""
        self.queryLocationCombo.clear()
        locations = self.db.getLocations()
        for location in locations:
            self.queryLocationCombo.addItem(location[0])

    def refreshChemicalList(self):
        """Refresh chemical list"""
        self.chemicalList.clear()
        chemicals = self.db.getHarmfulChemicals()
        for chemical in chemicals:
            self.chemicalList.addItem(chemical)

    # ==========================Connect methods============================================

    def displayWorkerDistribution(self):
        """Display worker distribution report"""
        data = self.db.getWorkerDistribution()
        header = ["Name","ActivityCount"]
        self.displayReport(data, "Worker Distribution", header)

    def displayManagerWorkload(self):
        """Display manager workload report"""
        data = self.db.getManagerWorkload()
        header = ["Name","Locations","Activities"]
        self.displayReport(data, "Manager Workload", header)

    def displayOutSource(self):
        """Display outsource summary report"""
        data = self.db.getOutsourceSummary()
        header = ["Company Name","Contract Count", "Total Payment"]
        self.displayReport(data, "Outsource Summary", header)

    def displayReport(self, data, title, header):
        """Display a report in the results area"""
        # Clear previous results
        while self._resultTabLayout.count() > 1:
            item = self._resultTabLayout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()
        
        if data:
            table = QTableView()
            model = TableModel(data)
            model.setHeaderLabel(header)
            table.setModel(model)
            
            # 自动调整列宽
            table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            table.horizontalHeader().setStretchLastSection(True)  # 最后一列拉伸填充
            
            # 设置行高
            table.verticalHeader().setDefaultSectionSize(30)
            
            # 设置选择行为和网格线
            table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            table.setAlternatingRowColors(True)
            table.setShowGrid(True)
            
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
            success = self.db.readFile(file_path)
            
            if success:
                QMessageBox.information(self.mainWindow, "Success", "SQL file executed successfully!")
                
                # Refresh data in various tabs to reflect changes
                self.refreshQueryLocations()
                self.refreshChemicalList()
                    
            else:
                QMessageBox.critical(self.mainWindow, "Error", "Failed to execute SQL file.")
                
        except Exception as e:
            QMessageBox.critical(self.mainWindow, "Error", f"Error executing SQL file: {str(e)}")

    def runQuery(self):
        """Execute SQL query from text area"""
        query_text = self._queryArea.toPlainText().strip()
        if not query_text:
            return
            
        try:
            cursor = self.db.execute(query_text)
            if cursor:
                result = cursor.fetchall()
                column_names = [description[0] for description in cursor.description] if cursor.description else []
                
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
                    model = TableModel(result)
                    
                    if column_names:
                        model.setHeaderLabel(column_names)
                    else:
                        default_headers = [f"Column {i+1}" for i in range(len(result[0]))]
                        model.setHeaderLabel(default_headers)
                        
                    table.setModel(model)
                    
                    # 自动调整列宽
                    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
                    table.horizontalHeader().setStretchLastSection(True)
                    table.verticalHeader().setDefaultSectionSize(30)
                    table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
                    table.setAlternatingRowColors(True)
                    
                    resultLayout.addWidget(table)
                    
                    self._tableFrame = QWidget()
                    layout = QVBoxLayout()
                    self._tableFrame.setLayout(layout)
                    layout.addWidget(resultWidget)
                    self._tableFrame.show()
            else:
                QMessageBox.warning(self.mainWindow, "Query Error", "Failed to execute query")
                
        except Exception as e:
            QMessageBox.critical(self.mainWindow, "Query Error", f"Error executing query: {str(e)}")        
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
        # Clear previous results
        while self.resultsLayout.count() > 1:
            item = self.resultsLayout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()

        start_date = self.startDateEdit.date().toString("yyyy-MM-dd")
        end_date = self.endDateEdit.date().toString("yyyy-MM-dd")
        
        if location:
            chemicals = self.db.getHarmfulChemicals()
            if self.anyTimeCheckbox.isChecked():
                results = self.db.queryForActivity(location, chemicals)
            else:
                results = self.db.queryForActivityWithDate(location, start_date, end_date, chemicals)
            
            if results:
                table = QTableView()
                model = TableModel(results)
                model.setHeaderLabel(["AID", "Name", "Start Date", "End Date","Harmful Chemicals Count"])
                table.setModel(model)
                
                # 自动调整列宽
                table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
                table.horizontalHeader().setStretchLastSection(True)
                table.verticalHeader().setDefaultSectionSize(30)
                table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
                table.setAlternatingRowColors(True)
                
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
        
        self.setFixedSize(900, 700)
        
        self.condition_blocks = []
        self.column_types = {}
        
        self.initUI()
        
    def initUI(self):
        main_layout = QVBoxLayout(self)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        content_widget = QWidget()
        self.content_layout = QVBoxLayout(content_widget)
        
        # Table selection
        tableLayout = QHBoxLayout()
        tableLayout.addWidget(QLabel("Select Table:"))
        
        self.tableCombo = QComboBox()
        self.tableCombo.addItems(self.db.getTables())
        self.tableCombo.currentTextChanged.connect(self.tableChanged)
        tableLayout.addWidget(self.tableCombo)
        
        self.content_layout.addLayout(tableLayout)
        
        if self.operation == "delete":
            self.setupDeleteUI(self.content_layout)
        elif self.operation == "update":
            self.setupUpdateUI(self.content_layout)
        else:
            self.setupInsertUI(self.content_layout)
        
        # Buttons
        buttonLayout = QHBoxLayout()
        
        executeBtn = QPushButton("Execute")
        executeBtn.clicked.connect(self.executeOperation)
        buttonLayout.addWidget(executeBtn)
        
        cancelBtn = QPushButton("Cancel")
        cancelBtn.clicked.connect(self.reject)
        buttonLayout.addWidget(cancelBtn)
        
        self.content_layout.addLayout(buttonLayout)
        
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
        
        if self.tableCombo.count() > 0:
            self.tableChanged(self.tableCombo.currentText())
    
    def setupInsertUI(self, layout):
        """Setup UI for insert operation"""
        table_scroll = QScrollArea()
        table_scroll.setWidgetResizable(True)
        table_scroll.setMinimumHeight(300)
        
        self.dataTable = QTableWidget()
        table_scroll.setWidget(self.dataTable)
        
        layout.addWidget(table_scroll)
        
        addRowBtn = QPushButton("+ Add Row")
        addRowBtn.clicked.connect(self.addRow)
        layout.addWidget(addRowBtn)
        
        self.addRow()
    
    def setupDeleteUI(self, layout):
        """Setup UI for delete operation"""
        conditionWidget = QWidget()
        conditionLayout = QVBoxLayout()
        conditionWidget.setLayout(conditionLayout)
        
        conditionLabel = QLabel("WHERE Conditions (Blocks are ANDed, conditions within block are ORed):")
        conditionLayout.addWidget(conditionLabel)
        
        condition_scroll = QScrollArea()
        condition_scroll.setWidgetResizable(True)
        condition_scroll.setMinimumHeight(300)
        
        condition_blocks_widget = QWidget()
        self.conditionBlocksContainer = QVBoxLayout(condition_blocks_widget)
        condition_scroll.setWidget(condition_blocks_widget)
        
        conditionLayout.addWidget(condition_scroll)
        
        addBlockBtn = QPushButton("+ Add Condition Block")
        addBlockBtn.clicked.connect(self.addConditionBlock)
        conditionLayout.addWidget(addBlockBtn)
        
        layout.addWidget(conditionWidget)
        
        self.addConditionBlock()
    
    def setupUpdateUI(self, layout):
        """Setup UI for update operation"""
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        conditionWidget = QWidget()
        conditionLayout = QVBoxLayout(conditionWidget)
        
        conditionLabel = QLabel("WHERE Conditions (Blocks are ANDed, conditions within block are ORed):")
        conditionLayout.addWidget(conditionLabel)
        
        condition_scroll = QScrollArea()
        condition_scroll.setWidgetResizable(True)
        
        condition_blocks_widget = QWidget()
        self.conditionBlocksContainer = QVBoxLayout(condition_blocks_widget)
        condition_scroll.setWidget(condition_blocks_widget)
        
        conditionLayout.addWidget(condition_scroll)
        
        addBlockBtn = QPushButton("+ Add Condition Block")
        addBlockBtn.clicked.connect(self.addConditionBlock)
        conditionLayout.addWidget(addBlockBtn)
        
        updateWidget = QWidget()
        updateLayout = QVBoxLayout(updateWidget)
        
        updateLabel = QLabel("Update Values (unlock to change):")
        updateLayout.addWidget(updateLabel)
        
        table_scroll = QScrollArea()
        table_scroll.setWidgetResizable(True)
        
        self.updateTable = QTab
