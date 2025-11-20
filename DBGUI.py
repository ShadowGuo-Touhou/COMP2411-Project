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
        self.db = SQLProcessor("data.db")
        
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

    def displayWorkerDistribution(self):
        """Display worker distribution report"""
        query = """
        SELECT W.Name, COUNT(A.AID) as ActivityCount 
        FROM Worker W 
        LEFT JOIN Assigned A ON W.WID = A.WID 
        GROUP BY W.WID, W.Name
        """
        data = self.db.fetch_all(query)
        header = ["Name","ActivityCount"]
        self.displayReport(data, "Worker Distribution", header)

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
        header = ["Name","Locations","Activities"]
        self.displayReport(data, "Manager Workload", header)

    def displayOutSource(self):
        """Display outsource summary report"""
        query = """
        SELECT C.Name, COUNT(W.AID) as ContractCount, SUM(W.ContractedPayment) as TotalPayment
        FROM Company C 
        LEFT JOIN WorkOn W ON C.CompanyID = W.CompanyID
        GROUP BY C.CompanyID, C.Name
        """
        header = ["Company Name","Contract Count", "Total Payment"]
        data = self.db.fetch_all(query)
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
                model = TableModel(results)
                model.setHeaderLabel(["AID", "Location", "Start Date", "End Date"])
                table.setModel(model)
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
        
        # 设置固定大小
        self.setFixedSize(900, 700)
        
        self.condition_blocks = []  # 存储条件块
        self.column_types = {}  # 存储列数据类型
        
        self.initUI()
        
    def initUI(self):
        # 创建主布局和滚动区域
        main_layout = QVBoxLayout(self)
        
        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        # 创建内容部件
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
        
        # 根据操作类型显示不同界面
        if self.operation == "delete":
            self.setupDeleteUI(self.content_layout)
        elif self.operation == "update":
            self.setupUpdateUI(self.content_layout)
        else:  # insert
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
        
        # 将内容部件设置为滚动区域的部件
        scroll_area.setWidget(content_widget)
        
        # 将滚动区域添加到主布局
        main_layout.addWidget(scroll_area)
        
        # Initialize with first table
        if self.tableCombo.count() > 0:
            self.tableChanged(self.tableCombo.currentText())
    
    def setupInsertUI(self, layout):
        """Setup UI for insert operation"""
        # Data table with scroll area
        table_scroll = QScrollArea()
        table_scroll.setWidgetResizable(True)
        table_scroll.setMinimumHeight(300)
        
        self.dataTable = QTableWidget()
        table_scroll.setWidget(self.dataTable)
        
        layout.addWidget(table_scroll)
        
        addRowBtn = QPushButton("+ Add Row")
        addRowBtn.clicked.connect(self.addRow)
        layout.addWidget(addRowBtn)
        
        # Start with one empty row
        self.addRow()
    
    def setupDeleteUI(self, layout):
        """Setup UI for delete operation - 使用条件块"""
        # 条件构建器
        conditionWidget = QWidget()
        conditionLayout = QVBoxLayout()
        conditionWidget.setLayout(conditionLayout)
        
        conditionLabel = QLabel("WHERE Conditions (Blocks are ANDed, conditions within block are ORed):")
        conditionLayout.addWidget(conditionLabel)
        
        # 条件块容器 - 使用滚动区域
        condition_scroll = QScrollArea()
        condition_scroll.setWidgetResizable(True)
        condition_scroll.setMinimumHeight(300)
        
        condition_blocks_widget = QWidget()
        self.conditionBlocksContainer = QVBoxLayout(condition_blocks_widget)
        condition_scroll.setWidget(condition_blocks_widget)
        
        conditionLayout.addWidget(condition_scroll)
        
        # 添加条件块按钮
        addBlockBtn = QPushButton("+ Add Condition Block")
        addBlockBtn.clicked.connect(self.addConditionBlock)
        conditionLayout.addWidget(addBlockBtn)
        
        layout.addWidget(conditionWidget)
        
        # 初始添加一个条件块
        self.addConditionBlock()
    
    def setupUpdateUI(self, layout):
        """Setup UI for update operation - 使用条件块和更新表格"""
        # 使用分割器来分隔条件和更新部分，允许用户调整大小
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # 左侧条件部分
        conditionWidget = QWidget()
        conditionLayout = QVBoxLayout(conditionWidget)
        
        conditionLabel = QLabel("WHERE Conditions (Blocks are ANDed, conditions within block are ORed):")
        conditionLayout.addWidget(conditionLabel)
        
        # 条件块容器 - 使用滚动区域
        condition_scroll = QScrollArea()
        condition_scroll.setWidgetResizable(True)
        
        condition_blocks_widget = QWidget()
        self.conditionBlocksContainer = QVBoxLayout(condition_blocks_widget)
        condition_scroll.setWidget(condition_blocks_widget)
        
        conditionLayout.addWidget(condition_scroll)
        
        # 添加条件块按钮
        addBlockBtn = QPushButton("+ Add Condition Block")
        addBlockBtn.clicked.connect(self.addConditionBlock)
        conditionLayout.addWidget(addBlockBtn)
        
        # 右侧更新值部分
        updateWidget = QWidget()
        updateLayout = QVBoxLayout(updateWidget)
        
        updateLabel = QLabel("Update Values (unlock to change):")
        updateLayout.addWidget(updateLabel)
        
        # 更新值表格 - 使用滚动区域
        table_scroll = QScrollArea()
        table_scroll.setWidgetResizable(True)
        
        self.updateTable = QTableWidget()
        self.updateTable.setColumnCount(3)  # 列名，值，锁定状态
        self.updateTable.setHorizontalHeaderLabels(["Column", "New Value", "Locked"])
        table_scroll.setWidget(self.updateTable)
        
        updateLayout.addWidget(table_scroll)
        
        # 将左右部件添加到分割器
        splitter.addWidget(conditionWidget)
        splitter.addWidget(updateWidget)
        
        # 设置分割器初始比例
        splitter.setSizes([400, 400])
        
        layout.addWidget(splitter)
        
        # 初始添加一个条件块
        self.addConditionBlock()
    
    def addConditionBlock(self):
        """添加一个新的条件块"""
        block_widget = QWidget()
        block_widget.setStyleSheet("QWidget { border: 1px solid #CCCCCC; border-radius: 5px; padding: 5px; margin: 2px; }")
        block_layout = QVBoxLayout(block_widget)
        
        # 条件块标题
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
        
        # 条件容器
        conditions_layout = QVBoxLayout()
        block_layout.addLayout(conditions_layout)
        
        # 添加条件按钮
        add_condition_btn = QPushButton("+ Add Condition")
        add_condition_btn.clicked.connect(lambda: self.addCondition(conditions_layout))
        block_layout.addWidget(add_condition_btn)
        
        # 存储条件块信息
        block_info = {
            'widget': block_widget,
            'conditions_layout': conditions_layout,
            'conditions': []
        }
        self.condition_blocks.append(block_info)
        
        # 添加到容器 - 在块之间添加AND标志
        if len(self.condition_blocks) > 1:
            and_label = QLabel("AND")
            and_label.setStyleSheet("QLabel { font-weight: bold; color: #666666; background-color: #F0F0F0; padding: 5px; border-radius: 3px; }")
            and_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.conditionBlocksContainer.addWidget(and_label)
        
        self.conditionBlocksContainer.addWidget(block_widget)
        
        # 初始添加一个条件
        self.addCondition(conditions_layout)
    
    def removeConditionBlock(self, block_widget):
        """移除条件块"""
        # 找到要删除的块索引
        remove_index = -1
        for i, block_info in enumerate(self.condition_blocks):
            if block_info['widget'] == block_widget:
                remove_index = i
                break
        
        if remove_index == -1:
            return
        
        # 移除条件块及其前面的AND标签（如果有）
        if remove_index > 0:
            # 移除前面的AND标签
            and_widget = self.conditionBlocksContainer.itemAt(remove_index * 2 - 1).widget()
            if and_widget:
                and_widget.deleteLater()
        
        # 移除条件块
        self.condition_blocks.pop(remove_index)
        block_widget.deleteLater()
        
        # 重新编号条件块和AND标签
        self.renumberConditionBlocks()
    
    def renumberConditionBlocks(self):
        """重新编号条件块和AND标签"""
        # 清除所有现有的AND标签
        for i in reversed(range(self.conditionBlocksContainer.count())):
            item = self.conditionBlocksContainer.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                if isinstance(widget, QLabel) and widget.text() == "AND":
                    self.conditionBlocksContainer.removeWidget(widget)
                    widget.deleteLater()
        
        # 重新添加条件块和AND标签
        for i, block_info in enumerate(self.condition_blocks):
            if i > 0:
                and_label = QLabel("AND")
                and_label.setStyleSheet("QLabel { font-weight: bold; color: #666666; background-color: #F0F0F0; padding: 5px; border-radius: 3px; }")
                and_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.conditionBlocksContainer.addWidget(and_label)
            
            # 更新块标题
            block_label = block_info['widget'].layout().itemAt(0).itemAt(0).widget()
            block_label.setText(f"Condition Block {i + 1}")
            
            # 重新添加条件块
            self.conditionBlocksContainer.addWidget(block_info['widget'])
    
    def addCondition(self, conditions_layout):
        """在条件块中添加一个新条件"""
        condition_widget = QWidget()
        condition_widget.setStyleSheet("QWidget { background-color: #F5F5F5; border-radius: 3px; padding: 3px; }")
        condition_layout = QHBoxLayout(condition_widget)
        
        # 如果是第一个条件，添加OR标签占位符保持对齐
        if conditions_layout.count() > 0:
            or_label = QLabel("OR")
            or_label.setStyleSheet("QLabel { font-weight: bold; color: #666666; min-width: 30px; }")
            or_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            condition_layout.addWidget(or_label)
        else:
            # 添加空标签保持对齐
            empty_label = QLabel("")
            empty_label.setMinimumWidth(30)
            condition_layout.addWidget(empty_label)
        
        # 列选择
        column_combo = QComboBox()
        if self.tableCombo.currentText():
            columns = self.db.getColumns(self.tableCombo.currentText())
            column_combo.addItems(columns)
        column_combo.setMinimumWidth(120)
        condition_layout.addWidget(column_combo)
        
        # 运算符选择
        operator_combo = QComboBox()
        operator_combo.addItems(["=", "!=", ">", ">=", "<", "<=", "LIKE", "IN"])
        operator_combo.setMinimumWidth(80)
        condition_layout.addWidget(operator_combo)
        
        # 值输入
        value_edit = QLineEdit()
        value_edit.setPlaceholderText("Value")
        condition_layout.addWidget(value_edit)
        
        # 移除条件按钮
        remove_btn = QPushButton("Remove")
        remove_btn.setStyleSheet("QPushButton { background-color: #FFE6E6; }")
        remove_btn.clicked.connect(lambda: self.removeCondition(condition_widget, conditions_layout))
        condition_layout.addWidget(remove_btn)
        
        conditions_layout.addWidget(condition_widget)
        
        # 找到对应的条件块并存储条件
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
                
                # 重新添加OR标签
                self.readdOrLabels(conditions_layout)
                break
    
    def readdOrLabels(self, conditions_layout):
        """重新添加条件之间的OR标签"""
        # 获取所有条件部件
        condition_widgets = []
        for i in range(conditions_layout.count()):
            item = conditions_layout.itemAt(i)
            if item and item.widget():
                condition_widgets.append(item.widget())
        
        # 清除布局
        for widget in condition_widgets:
            conditions_layout.removeWidget(widget)
        
        # 重新添加条件，包括OR标签
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
            return "1=1"  # 默认条件
        
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
                
                # 处理值，根据数据类型决定是否加引号
                col_type = self.column_types.get(column, "TEXT")
                if "TEXT" in col_type.upper():
                    value = f"'{value.replace("'", "''")}'"  # 转义单引号
                
                condition_parts.append(f"{column} {operator} {value}")
            
            if condition_parts:
                block_conditions.append(f"({' OR '.join(condition_parts)})")
        
        if not block_conditions:
            return "1=1"
        
        return " AND ".join(block_conditions)
    
    def tableChanged(self, table_name):
        """当表选择改变时，更新界面"""
        # 获取列数据类型
        self.column_types = self.getColumnTypes(table_name)
        columns = list(self.column_types.keys())
        
        if self.operation == "insert":
            self.dataTable.setColumnCount(len(columns))
            self.dataTable.setHorizontalHeaderLabels(columns)
            self.dataTable.setRowCount(1)
            for col in range(len(columns)):
                self.dataTable.setItem(0, col, QTableWidgetItem(""))
        
        elif self.operation == "update":
            # 更新条件块中的列选择
            for block_info in self.condition_blocks:
                for condition_info in block_info['conditions']:
                    condition_info['column_combo'].clear()
                    condition_info['column_combo'].addItems(columns)
            
            # 更新更新值表格
            self.updateTable.setRowCount(len(columns))
            for i, column in enumerate(columns):
                # 列名
                col_name_item = QTableWidgetItem(column)
                col_name_item.setFlags(col_name_item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # 不可编辑
                self.updateTable.setItem(i, 0, col_name_item)
                
                # 值（初始为空，锁定）
                value_item = QTableWidgetItem("")
                value_item.setFlags(value_item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # 初始不可编辑
                self.updateTable.setItem(i, 1, value_item)
                
                # 锁定状态复选框
                lock_checkbox = QCheckBox()
                lock_checkbox.setChecked(True)  # 初始锁定
                lock_checkbox.stateChanged.connect(
                    lambda state, row=i: self.toggleLockState(state, row)
                )
                checkbox_widget = QWidget()
                checkbox_layout = QHBoxLayout(checkbox_widget)
                checkbox_layout.addWidget(lock_checkbox)
                checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                checkbox_layout.setContentsMargins(0, 0, 0, 0)
                self.updateTable.setCellWidget(i, 2, checkbox_widget)
        
        elif self.operation == "delete":
            # 更新条件块中的列选择
            for block_info in self.condition_blocks:
                for condition_info in block_info['conditions']:
                    condition_info['column_combo'].clear()
                    condition_info['column_combo'].addItems(columns)
    
    def toggleLockState(self, state, row):
        """切换锁定状态"""
        value_item = self.updateTable.item(row, 1)
        if state == Qt.CheckState.Checked.value:
            # 锁定 - 不可编辑
            value_item.setFlags(value_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            value_item.setBackground(QColor(240, 240, 240))  # 灰色背景表示锁定
        else:
            # 解锁 - 可编辑
            value_item.setFlags(value_item.flags() | Qt.ItemFlag.ItemIsEditable)
            value_item.setBackground(QColor(255, 255, 255))  # 白色背景表示可编辑
    
    def addRow(self):
        """为insert操作添加新行"""
        row = self.dataTable.rowCount()
        self.dataTable.setRowCount(row + 1)
        for col in range(self.dataTable.columnCount()):
            self.dataTable.setItem(row, col, QTableWidgetItem(""))
    
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
                
                # 处理空值
                if not value:
                    data[header] = "NULL"
                else:
                    # 只有TEXT类型才添加引号
                    if "TEXT" in self.column_types.get(header, "TEXT").upper():
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
    
    def executeUpdate(self, table):
        """执行update操作"""
        # 构建条件
        condition = self.buildConditionString()
        
        # 构建更新数据
        changes = {}
        for row in range(self.updateTable.rowCount()):
            column = self.updateTable.item(row, 0).text()
            value_item = self.updateTable.item(row, 1)
            lock_checkbox = self.updateTable.cellWidget(row, 2).findChild(QCheckBox)
            
            # 只处理解锁的列
            if not lock_checkbox.isChecked() and value_item:
                value = value_item.text().strip()
                
                if value:
                    # 根据数据类型处理值
                    col_type = self.column_types.get(column, "TEXT")
                    if "TEXT" in col_type.upper():
                        value = value.replace("'", "''")  # 转义单引号
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
