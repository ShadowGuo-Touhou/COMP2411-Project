import os
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from .ConditionBuilder import ConditionBlock, CompoundCondition
from .TableModel import TableModel

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
        
        self.condition_container = QWidget()
        self.condition_layout = QVBoxLayout(self.condition_container)
        layout.addWidget(self.condition_container)
        
        self.addSimpleCondition()
        
    
        preview_group = QGroupBox("SQL condition preview")
        preview_layout = QVBoxLayout(preview_group)
        
        self.condition_preview = QTextEdit()
        self.condition_preview.setMaximumHeight(60)
        self.condition_preview.setReadOnly(True)
        preview_layout.addWidget(self.condition_preview)
        
        layout.addWidget(preview_group)
    
    def setupUpdateUI(self, layout):
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        condition_widget = QWidget()
        condition_layout = QVBoxLayout(condition_widget)
        
        
        self.condition_container = QWidget()
        self.condition_layout = QVBoxLayout(self.condition_container)
        condition_layout.addWidget(self.condition_container)
        
        self.addSimpleCondition()
        
        update_widget = QWidget()
        update_layout = QVBoxLayout(update_widget)
        
        update_label = QLabel("set updated values:")
        update_layout.addWidget(update_label)
        
        self.updateTable = QTableWidget()
        self.updateTable.setColumnCount(3)
        self.updateTable.setHorizontalHeaderLabels(["Column", "New Value", "Locked"])
        update_layout.addWidget(self.updateTable)
        
        splitter.addWidget(condition_widget)
        splitter.addWidget(update_widget)
        splitter.setSizes([400, 400])
        
        layout.addWidget(splitter)
        
        preview_group = QGroupBox("SQL condition preview")
        preview_layout = QVBoxLayout(preview_group)
        
        self.condition_preview = QTextEdit()
        self.condition_preview.setMaximumHeight(60)
        self.condition_preview.setReadOnly(True)
        preview_layout.addWidget(self.condition_preview)
        
        layout.addWidget(preview_group)
    
    def addSimpleCondition(self):
        condition = ConditionBlock(db=self.db, column_types=self.column_types, is_simple=True)
        condition.conditionChanged.connect(self.updateConditionPreview)
        condition.requestExpansion.connect(self.expandCondition)
        
        self.condition_blocks.append(condition)
        self.condition_layout.addWidget(condition)
        self.updateConditionPreview()
    
    def expandCondition(self, condition):
        index = self.condition_layout.indexOf(condition)
        
        compound = CompoundCondition(db=self.db, column_types=self.column_types)
        compound.conditionChanged.connect(self.updateConditionPreview)
        compound.requestExpansion.connect(self.expandCondition)
        compound.requestSimplify.connect(self.simplifyCondition)
        
        if condition.column_combo.count() > 0:
            compound.condition_a.column_combo.setCurrentText(condition.column_combo.currentText())
        compound.condition_a.operator_combo.setCurrentText(condition.operator_combo.currentText())
        compound.condition_a.value_edit.setText(condition.value_edit.text())
        
        if self.tableCombo.currentText():
            columns = self.db.getColumns(self.tableCombo.currentText())
            compound.setColumns(columns)
        
        self.condition_layout.removeWidget(condition)
        condition.deleteLater()
        self.condition_layout.insertWidget(index, compound)
        
        if condition in self.condition_blocks:
            idx = self.condition_blocks.index(condition)
            self.condition_blocks[idx] = compound
        
        self.updateConditionPreview()
    
    def simplifyCondition(self, compound):
        index = self.condition_layout.indexOf(compound)
        
        simple = ConditionBlock(db=self.db, column_types=self.column_types, is_simple=True)
        simple.conditionChanged.connect(self.updateConditionPreview)
        simple.requestExpansion.connect(self.expandCondition)
        
        if hasattr(compound.condition_a, 'column_combo') and compound.condition_a.column_combo.count() > 0:
            simple.column_combo.setCurrentText(compound.condition_a.column_combo.currentText())
        if hasattr(compound.condition_a, 'operator_combo'):
            simple.operator_combo.setCurrentText(compound.condition_a.operator_combo.currentText())
        if hasattr(compound.condition_a, 'value_edit'):
            simple.value_edit.setText(compound.condition_a.value_edit.text())
        
        if self.tableCombo.currentText():
            columns = self.db.getColumns(self.tableCombo.currentText())
            simple.setColumns(columns)
        
        self.condition_layout.removeWidget(compound)
        compound.deleteLater()
        self.condition_layout.insertWidget(index, simple)
        
        
        if compound in self.condition_blocks:
            idx = self.condition_blocks.index(compound)
            self.condition_blocks[idx] = simple
        
        self.updateConditionPreview()
    
    def updateConditionPreview(self):
        if hasattr(self, 'condition_preview'):
            condition_str = self.buildConditionString()
            self.condition_preview.setPlainText(f"WHERE {condition_str}")
    
    def tableChanged(self, table_name):
        columns = self.db.getColumns(table_name)
        
        self.column_types = self.getColumnTypes(table_name)
        
        for col in columns:
            if col not in self.column_types:
                self.column_types[col] = "TEXT"
        
        if self.operation == "insert":
            self.dataTable.setColumnCount(len(columns))
            self.dataTable.setHorizontalHeaderLabels(columns)
            self.dataTable.setRowCount(1)
            for col in range(len(columns)):
                self.dataTable.setItem(0, col, QTableWidgetItem(""))
            
            
            self.dataTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.dataTable.horizontalHeader().setStretchLastSection(True)
        
        elif self.operation == "update":
            for condition in self.condition_blocks:
                condition.setColumns(columns)
            
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
            
            self.updateTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.updateTable.horizontalHeader().setStretchLastSection(True)
        
        elif self.operation == "delete":
            for condition in self.condition_blocks:
                condition.setColumns(columns)
        
        if self.operation in ["update", "delete"]:
            self.updateConditionPreview()
    
    def toggleLockState(self, state, row):
        value_item = self.updateTable.item(row, 1)
        if state == Qt.CheckState.Checked.value:
            value_item.setFlags(value_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            value_item.setBackground(QColor(240, 240, 240))
        else:
            value_item.setFlags(value_item.flags() | Qt.ItemFlag.ItemIsEditable)
            value_item.setBackground(QColor(255, 255, 255))
    
    def addRow(self):
        row = self.dataTable.rowCount()
        self.dataTable.setRowCount(row + 1)
        for col in range(self.dataTable.columnCount()):
            self.dataTable.setItem(row, col, QTableWidgetItem(""))
    
    def getColumnTypes(self, table_name):
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
    
    def format_string_value(self, value):
        if not value:
            return "NULL"
        
        value = value.replace('"', '').replace("'", "")
        
        value = value.replace("'", "''")
        
        return f"{value}"

    def executeInsert(self, table):
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
                        data[header] = self.format_string_value(value)
                    else:
                        data[header] = value
            
            if data:
                success = self.db.insert(table, data)
                if not success:
                    raise Exception(f"Failed to insert row {row + 1}")

    def buildConditionString(self):
        if not self.condition_blocks:
            return "1=1"
        
        conditions = []
        for condition in self.condition_blocks:
            cond_str = condition.getCondition()
            if cond_str:
                conditions.append(cond_str)
        
        if not conditions:
            return "1=1"
        
        return " AND ".join(conditions)

    def executeUpdate(self, table):
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
                        changes[column] = self.format_string_value(value)
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
        condition = self.buildConditionString()
        success = self.db.delete(table, condition)
        
        if not success:
            raise Exception("Delete operation failed")