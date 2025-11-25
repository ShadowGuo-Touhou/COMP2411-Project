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
        
        self.updateTable = QTableWidget()
        self.updateTable.setColumnCount(3)
        self.updateTable.setHorizontalHeaderLabels(["Column", "New Value", "Locked"])
        table_scroll.setWidget(self.updateTable)
        
        updateLayout.addWidget(table_scroll)
        
        splitter.addWidget(conditionWidget)
        splitter.addWidget(updateWidget)
        
        splitter.setSizes([400, 400])
        
        layout.addWidget(splitter)
        
        self.addConditionBlock()
    
    def addConditionBlock(self):
        """添加一个新的条件块"""
        block_widget = QWidget()
        block_widget.setStyleSheet("QWidget { border: 1px solid #CCCCCC; border-radius: 5px; padding: 5px; margin: 2px; }")
        block_layout = QVBoxLayout(block_widget)
        
        block_header = QHBoxLayout()
        block_label = QLabel(f"Condition Block {len(self.condition_blocks) + 1}")
        block_label.setStyleSheet("font-weight: bold;")
        block_header.addWidget(block_label)
        
        remove_block_btn = QPushButton("Remove Block")
        remove_block_btn.setStyleSheet("QPushButton { background-color: #FFCCCC; }")
        remove_block_btn.clicked.connect(lambda: self.removeConditionBlock(block_widget))
        block_header.addWidget(remove_block_btn)
        block_header.addStretch()
        
        block_layout.addLayout(block_header)
        
        conditions_layout = QVBoxLayout()
        block_layout.addLayout(conditions_layout)
        
        add_condition_btn = QPushButton("+ Add Condition")
        add_condition_btn.clicked.connect(lambda: self.addCondition(conditions_layout))
        block_layout.addWidget(add_condition_btn)
        
        block_info = {
            'widget': block_widget,
            'conditions_layout': conditions_layout,
            'conditions': []
        }
        self.condition_blocks.append(block_info)
        
        if len(self.condition_blocks) > 1:
            and_label = QLabel("AND")
            and_label.setStyleSheet("QLabel { font-weight: bold; color: #666666; background-color: #F0F0F0; padding: 5px; border-radius: 3px; }")
            and_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.conditionBlocksContainer.addWidget(and_label)
        
        self.conditionBlocksContainer.addWidget(block_widget)
        
        self.addCondition(conditions_layout)
    
    def removeConditionBlock(self, block_widget):
        """移除条件块"""
        remove_index = -1
        for i, block_info in enumerate(self.condition_blocks):
            if block_info['widget'] == block_widget:
                remove_index = i
                break
        
        if remove_index == -1:
            return
        
        if remove_index > 0:
            and_widget = self.conditionBlocksContainer.itemAt(remove_index * 2 - 1).widget()
            if and_widget:
                and_widget.deleteLater()
        
        self.condition_blocks.pop(remove_index)
        block_widget.deleteLater()
        
        self.renumberConditionBlocks()
    
    def renumberConditionBlocks(self):
        """重新编号条件块和AND标签"""
        for i in reversed(range(self.conditionBlocksContainer.count())):
            item = self.conditionBlocksContainer.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                if isinstance(widget, QLabel) and widget.text() == "AND":
                    self.conditionBlocksContainer.removeWidget(widget)
                    widget.deleteLater()
        
        for i, block_info in enumerate(self.condition_blocks):
            if i > 0:
                and_label = QLabel("AND")
                and_label.setStyleSheet("QLabel { font-weight: bold; color: #666666; background-color: #F0F0F0; padding: 5px; border-radius: 3px; }")
                and_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.conditionBlocksContainer.addWidget(and_label)
            
            block_label = block_info['widget'].layout().itemAt(0).itemAt(0).widget()
            block_label.setText(f"Condition Block {i + 1}")
            
            self.conditionBlocksContainer.addWidget(block_info['widget'])
    
    def addCondition(self, conditions_layout):
        """在条件块中添加一个新条件"""
        condition_widget = QWidget()
        condition_widget.setStyleSheet("QWidget { background-color: #F5F5F5; border-radius: 3px; padding: 3px; }")
        condition_layout = QHBoxLayout(condition_widget)
        
        if conditions_layout.count() > 0:
            or_label = QLabel("OR")
            or_label.setStyleSheet("QLabel { font-weight: bold; color: #666666; min-width: 30px; }")
            or_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            condition_layout.addWidget(or_label)
        else:
            empty_label = QLabel("")
            empty_label.setMinimumWidth(30)
            condition_layout.addWidget(empty_label)
        
        column_combo = QComboBox()
        if self.tableCombo.currentText():
            columns = self.db.getColumns(self.tableCombo.currentText())
            column_combo.addItems(columns)
        column_combo.setMinimumWidth(120)
        condition_layout.addWidget(column_combo)
        
        operator_combo = QComboBox()
        operator_combo.addItems(["=", "!=", ">", ">=", "<", "<=", "LIKE", "IN"])
        operator_combo.setMinimumWidth(80)
        condition_layout.addWidget(operator_combo)
        
        value_edit = QLineEdit()
        value_edit.setPlaceholderText("Value")
        condition_layout.addWidget(value_edit)
        
        remove_btn = QPushButton("Remove")
        remove_btn.setStyleSheet("QPushButton { background-color: #FFE6E6; }")
        remove_btn.clicked.connect(lambda: self.removeCondition(condition_widget, conditions_layout))
        condition_layout.addWidget(remove_btn)
        
        conditions_layout.addWidget(condition_widget)
        
        for block_info in self.condition_blocks:
            if block_info['conditions_layout'] == conditions_layout:
                condition_info = {
                    'widget': condition_widget,
                    'column_combo': column_combo,
                    'operator_combo': operator_combo,
                    'value_edit': value_edit
                }
                block_info['conditions'].append(condition_info)
                break
    
    def removeCondition(self, condition_widget, conditions_layout):
        """移除条件"""
        for block_info in self.condition_blocks:
            if block_info['conditions_layout'] == conditions_layout:
                for i, condition_info in enumerate(block_info['conditions']):
                    if condition_info['widget'] == condition_widget:
                        block_info['conditions'].pop(i)
                        condition_widget.deleteLater()
                        break
                
                self.readdOrLabels(conditions_layout)
                break
    
    def readdOrLabels(self, conditions_layout):
        """重新添加条件之间的OR标签"""
        condition_widgets = []
        for i in range(conditions_layout.count()):
            item = conditions_layout.itemAt(i)
            if item and item.widget():
                condition_widgets.append(item.widget())
        
        for widget in condition_widgets:
            conditions_layout.removeWidget(widget)
        
        for i, widget in enumerate(condition_widgets):
            if i > 0:
                or_label = QLabel("OR")
                or_label.setStyleSheet("QLabel { font-weight: bold; color: #666666; min-width: 30px; }")
                or_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                conditions_layout.addWidget(or_label)
            
            conditions_layout.addWidget(widget)
    
    def buildConditionString(self):
        """构建条件字符串"""
        if not self.condition_blocks:
            return "1=1"
        
        block_conditions = []
        
        for block_info in self.condition_blocks:
            if not block_info['conditions']:
                continue
                
            condition_parts = []
            for condition_info in block_info['conditions']:
                column = condition_info['column_combo'].currentText()
                operator = condition_info['operator_combo'].currentText()
                value = condition_info['value_edit'].text().strip()
                
                if not value:
                    continue
                
                col_type = self.column_types.get(column, "TEXT")
                if "TEXT" in col_type.upper():
                    value = f"'{value.replace("'", "''")}'"
                
                condition_parts.append(f"{column} {operator} {value}")
            
            if condition_parts:
                block_conditions.append(f"({' OR '.join(condition_parts)})")
        
        if not block_conditions:
            return "1=1"
        
        return " AND ".join(block_conditions)
    
    def tableChanged(self, table_name):
        """当表选择改变时，更新界面"""
        self.column_types = self.getColumnTypes(table_name)
        columns = list(self.column_types.keys())
        
        if self.operation == "insert":
            self.dataTable.setColumnCount(len(columns))
            self.dataTable.setHorizontalHeaderLabels(columns)
            self.dataTable.setRowCount(1)
            for col in range(len(columns)):
                self.dataTable.setItem(0, col, QTableWidgetItem(""))
            
            # 调整列宽
            self.dataTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.dataTable.horizontalHeader().setStretchLastSection(True)
        
        elif self.operation == "update":
            for block_info in self.condition_blocks:
                for condition_info in block_info['conditions']:
                    condition_info['column_combo'].clear()
                    condition_info['column_combo'].addItems(columns)
            
            self.updateTable.setRowCount(len(columns))
            for i, column in enumerate(columns):
                col_name_item = QTableWidgetItem(column)
                col_name_item.setFlags(col_name_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.updateTable.setItem(i, 0, col_name_item)
                
                value_item = QTableWidgetItem("")
                value_item.setFlags(value_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.updateTable.setItem(i, 1, value_item)
                
                lock_checkbox = QCheckBox()
                lock_checkbox.setChecked(True)
                lock_checkbox.stateChanged.connect(
                    lambda state, row=i: self.toggleLockState(state, row)
                )
                checkbox_widget = QWidget()
                checkbox_layout = QHBoxLayout(checkbox_widget)
                checkbox_layout.addWidget(lock_checkbox)
                checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                checkbox_layout.setContentsMargins(0, 0, 0, 0)
                self.updateTable.setCellWidget(i, 2, checkbox_widget)
            
            # 调整列宽
            self.updateTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.updateTable.horizontalHeader().setStretchLastSection(True)
        
        elif self.operation == "delete":
            for block_info in self.condition_blocks:
                for condition_info in block_info['conditions']:
                    condition_info['column_combo'].clear()
                    condition_info['column_combo'].addItems(columns)
    
    def toggleLockState(self, state, row):
        """切换锁定状态"""
        value_item = self.updateTable.item(row, 1)
        if state == Qt.CheckState.Checked.value:
            value_item.setFlags(value_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            value_item.setBackground(QColor(240, 240, 240))
        else:
            value_item.setFlags(value_item.flags() | Qt.ItemFlag.ItemIsEditable)
            value_item.setBackground(QColor(255, 255, 255))
    
    def addRow(self):
        """为insert操作添加新行"""
        row = self.dataTable.rowCount()
        self.dataTable.setRowCount(row + 1)
        for col in range(self.dataTable.columnCount()):
            self.dataTable.setItem(row, col, QTableWidgetItem(""))
    
    def getColumnTypes(self, table_name):
        """获取表的列信息，包括数据类型"""
        result = self.db.getTableSchema(table_name)
        
        if not result:
            return {}
        
        create_sql = result[0][0]
        column_types = {}
        
        start = create_sql.find('(')
        end = create_sql.rfind(')')
        if start == -1 or end == -1:
            return {}
        
        columns_def = create_sql[start+1:end]
        column_defs = [col.strip() for col in columns_def.split(',')]
        
        for col_def in column_defs:
            if col_def.upper().startswith(('PRIMARY', 'FOREIGN', 'CHECK', 'UNIQUE')):
                continue
            
            parts = col_def.split()
            if len(parts) >= 2:
                col_name = parts[0].strip('"\'')
                col_type = parts[1].upper()
                column_types[col_name] = col_type
        
        return column_types
    
    def executeOperation(self):
        """执行数据库操作"""
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
        """执行insert操作"""
        for row in range(self.dataTable.rowCount()):
            data = {}
            for col in range(self.dataTable.columnCount()):
                header = self.dataTable.horizontalHeaderItem(col).text()
                item = self.dataTable.item(row, col)
                value = item.text().strip() if item else ""
                
                if not value:
                    data[header] = "NULL"
                else:
                    if "TEXT" in self.column_types.get(header, "TEXT").upper():
                        value = value.replace('"', '').replace("'", "")
                        data[header] = f"'{value}'"
                    else:
                        data[header] = value
            
            if data:
                success = self.db.insert(table, data)
                if not success:
                    raise Exception(f"Failed to insert row {row + 1}")
    
    def executeUpdate(self, table):
        """执行update操作"""
        condition = self.buildConditionString()
        
        changes = {}
        for row in range(self.updateTable.rowCount()):
            column = self.updateTable.item(row, 0).text()
            value_item = self.updateTable.item(row, 1)
            lock_checkbox = self.updateTable.cellWidget(row, 2).findChild(QCheckBox)
            
            if not lock_checkbox.isChecked() and value_item:
                value = value_item.text().strip()
                
                if value:
                    col_type = self.column_types.get(column, "TEXT")
                    if "TEXT" in col_type.upper():
                        value = value.replace("'", "''")
                        changes[column] = f"'{value}'"
                    else:
                        changes[column] = value
                else:
                    changes[column] = "NULL"
        
        if not changes:
            raise Exception("No columns selected for update")
        
        success = self.db.update(table, changes, condition)
        
        if not success:
            raise Exception("Update operation failed")
    
    def executeDelete(self, table):
        """执行delete操作"""
        condition = self.buildConditionString()
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
        self._horizontal_headers = [""] * len(data[0]) if data else []
        self._vertical_headers = [""] * len(data) if data else []

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

    def setHeaderData(self, section, orientation, value, role=QtCore.Qt.ItemDataRole.EditRole):
            if orientation == QtCore.Qt.Orientation.Horizontal and role in (QtCore.Qt.ItemDataRole.DisplayRole, QtCore.Qt.ItemDataRole.EditRole):
                if 0 <= section < len(self._horizontal_headers):
                    self._horizontal_headers[section] = value
                    self.headerDataChanged.emit(orientation, section, section)
                    return True
            return super().setHeaderData(section, orientation, value, role)

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
            if orientation == QtCore.Qt.Orientation.Horizontal and role == QtCore.Qt.ItemDataRole.DisplayRole:
                if 0 <= section < len(self._horizontal_headers):
                    return self._horizontal_headers[section]

    def setHeaderLabel(self, header:list):
        for i in range(len(header)):    
            self.setHeaderData(i, Qt.Orientation.Horizontal, header[i])



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
