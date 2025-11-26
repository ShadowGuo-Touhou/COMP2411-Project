from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class ConditionBlock(QWidget):
    """单个条件块控件"""
    
    conditionChanged = pyqtSignal()  # 条件改变信号
    requestExpansion = pyqtSignal(object)  # 请求扩展信号
    
    def __init__(self, parent=None, db=None, column_types=None, is_simple=True):
        super().__init__(parent)
        self.db = db
        self.column_types = column_types or {}
        self.is_simple = is_simple  # 标记是否为简单条件
        self.setupUI()
        
    def setupUI(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        
        # 添加边框和背景
        if self.is_simple:
            self.setStyleSheet("""
                ConditionBlock {
                    border: 2px solid #4CAF50;
                    border-radius: 8px;
                    background-color: #E8F5E8;
                }
            """)
        else:
            self.setStyleSheet("""
                ConditionBlock {
                    border: 2px solid #2196F3;
                    border-radius: 8px;
                    background-color: #E3F2FD;
                }
            """)
        
        # 列选择
        self.column_combo = QComboBox()
        self.column_combo.setMinimumWidth(120)
        self.column_combo.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 4px;
            }
        """)
        self.column_combo.currentTextChanged.connect(self.onConditionChanged)
        layout.addWidget(self.column_combo)
        
        # 操作符选择
        self.operator_combo = QComboBox()
        self.operator_combo.setMinimumWidth(80)
        operators = ["=", "!=", ">", ">=", "<", "<=", "LIKE", "IN", "IS NULL", "IS NOT NULL"]
        self.operator_combo.addItems(operators)
        self.operator_combo.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 4px;
            }
        """)
        self.operator_combo.currentTextChanged.connect(self.onOperatorChanged)
        self.operator_combo.currentTextChanged.connect(self.onConditionChanged)
        layout.addWidget(self.operator_combo)
        
        # 值输入
        self.value_edit = QLineEdit()
        self.value_edit.setPlaceholderText("值")
        self.value_edit.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 4px;
            }
        """)
        self.value_edit.textChanged.connect(self.onConditionChanged)
        layout.addWidget(self.value_edit)
        
        # 扩展按钮
        if self.is_simple:
            self.expand_btn = QPushButton("⊕")
            self.expand_btn.setFixedSize(25, 25)
            self.expand_btn.setToolTip("extend")
            self.expand_btn.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 3px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """)
            self.expand_btn.clicked.connect(lambda: self.requestExpansion.emit(self))
            layout.addWidget(self.expand_btn)
        
        # 初始状态
        self.onOperatorChanged(self.operator_combo.currentText())
        
    def onOperatorChanged(self, operator):
        """根据操作符更新值输入状态"""
        if operator in ["IS NULL", "IS NOT NULL"]:
            self.value_edit.setEnabled(False)
            self.value_edit.setPlaceholderText("NULL")
            self.value_edit.clear()
        else:
            self.value_edit.setEnabled(True)
            self.value_edit.setPlaceholderText("VALUE")
            
    def onConditionChanged(self):
        """条件改变时发出信号"""
        self.conditionChanged.emit()
        
    def setColumns(self, columns):
        """设置可选的列"""
        current = self.column_combo.currentText()
        self.column_combo.clear()
        self.column_combo.addItems(columns)
        if current in columns:
            self.column_combo.setCurrentText(current)
        
    def getCondition(self):
        """获取条件字符串"""
        column = self.column_combo.currentText()
        operator = self.operator_combo.currentText()
        value = self.value_edit.text().strip()
        
        if not column:
            return ""
            
        if operator in ["IS NULL", "IS NOT NULL"]:
            return f"{column} {operator}"
        elif value:
            col_type = self.column_types.get(column, "TEXT")
            if "TEXT" in col_type.upper():
                # 移除所有引号，然后加上SQL单引号
                value = value.replace('"', '').replace("'", "")
                value = value.replace("'", "''")
                return f"{column} {operator} '{value}'"
            else:
                return f"{column} {operator} {value}"
        
        return ""


class CompoundCondition(QGroupBox):
    """复合条件控件，包含两个条件和一个逻辑运算符"""
    
    conditionChanged = pyqtSignal()
    requestExpansion = pyqtSignal(object)  # 请求扩展特定条件块
    requestSimplify = pyqtSignal(object)   # 请求简化此复合条件
    
    def __init__(self, parent=None, db=None, column_types=None):
        super().__init__(parent)
        self.db = db
        self.column_types = column_types or {}
        self.setupUI()
        
    def setupUI(self):
        # 设置组框样式
        self.setStyleSheet("""
            CompoundCondition {
                border: 3px solid #FF9800;
                border-radius: 10px;
                background-color: #FFF3E0;
                margin-top: 5px;
                margin-bottom: 5px;
            }
            CompoundCondition::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #FF9800;
                font-weight: bold;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 20, 10, 10)
        
        self.condition_a = ConditionBlock(db=self.db, column_types=self.column_types, is_simple=True)
        self.condition_a.conditionChanged.connect(self.onConditionChanged)
        self.condition_a.requestExpansion.connect(self.expandSubCondition)
        layout.addWidget(self.condition_a)
        
        # 逻辑运算符行
        logic_layout = QHBoxLayout()
        logic_layout.addStretch()
        
        
        self.logic_combo = QComboBox()
        self.logic_combo.addItems(["AND", "OR"])
        self.logic_combo.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 4px;
                min-width: 80px;
            }
        """)
        self.logic_combo.currentTextChanged.connect(self.onConditionChanged)
        logic_layout.addWidget(self.logic_combo)
        
        # 简化按钮
        self.simplify_btn = QPushButton("⊖")
        self.simplify_btn.setFixedSize(25, 25)
        self.simplify_btn.setToolTip("simplify")
        self.simplify_btn.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                border: none;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        self.simplify_btn.clicked.connect(lambda: self.requestSimplify.emit(self))
        logic_layout.addWidget(self.simplify_btn)
        
        logic_layout.addStretch()
        layout.addLayout(logic_layout)
        
        self.condition_b = ConditionBlock(db=self.db, column_types=self.column_types, is_simple=True)
        self.condition_b.conditionChanged.connect(self.onConditionChanged)
        self.condition_b.requestExpansion.connect(self.expandSubCondition)
        layout.addWidget(self.condition_b)
        
    
    def expandSubCondition(self, condition):
        """扩展子条件"""
        # 找到要扩展的条件在布局中的位置
        if condition == self.condition_a:
            index = 0
            current_condition = self.condition_a
        else:
            index = 2
            current_condition = self.condition_b
        
        # 创建复合条件
        compound = CompoundCondition(db=self.db, column_types=self.column_types)
        compound.conditionChanged.connect(self.onConditionChanged)
        compound.requestExpansion.connect(self.expandSubCondition)
        compound.requestSimplify.connect(self.simplifySubCondition)
        
        # 将当前条件的值复制到新复合条件的第一个条件
        if current_condition.column_combo.count() > 0:
            compound.condition_a.column_combo.setCurrentText(current_condition.column_combo.currentText())
        compound.condition_a.operator_combo.setCurrentText(current_condition.operator_combo.currentText())
        compound.condition_a.value_edit.setText(current_condition.value_edit.text())
        
        # 设置列选项
        if hasattr(self, 'current_columns'):
            compound.setColumns(self.current_columns)
        
        # 替换布局中的控件
        if index == 0:
            self.layout().removeWidget(self.condition_a)
            self.condition_a.deleteLater()
            self.condition_a = compound
            self.layout().insertWidget(0, self.condition_a)
        else:
            self.layout().removeWidget(self.condition_b)
            self.condition_b.deleteLater()
            self.condition_b = compound
            self.layout().insertWidget(2, self.condition_b)
        
        self.onConditionChanged()
    
    def simplifySubCondition(self, compound):
        """简化子条件"""
        # 确定要简化的子条件位置
        if compound == self.condition_a:
            index = 0
        else:
            index = 2
        
        # 创建简单条件
        simple = ConditionBlock(db=self.db, column_types=self.column_types, is_simple=True)
        simple.conditionChanged.connect(self.onConditionChanged)
        simple.requestExpansion.connect(self.expandSubCondition)
        
        # 将复合条件的第一个条件的值复制到简单条件
        if hasattr(compound.condition_a, 'column_combo') and compound.condition_a.column_combo.count() > 0:
            simple.column_combo.setCurrentText(compound.condition_a.column_combo.currentText())
        if hasattr(compound.condition_a, 'operator_combo'):
            simple.operator_combo.setCurrentText(compound.condition_a.operator_combo.currentText())
        if hasattr(compound.condition_a, 'value_edit'):
            simple.value_edit.setText(compound.condition_a.value_edit.text())
        
        # 设置列选项
        if hasattr(self, 'current_columns'):
            simple.setColumns(self.current_columns)
        
        # 替换布局中的控件
        if index == 0:
            self.layout().removeWidget(self.condition_a)
            self.condition_a.deleteLater()
            self.condition_a = simple
            self.layout().insertWidget(0, self.condition_a)
        else:
            self.layout().removeWidget(self.condition_b)
            self.condition_b.deleteLater()
            self.condition_b = simple
            self.layout().insertWidget(2, self.condition_b)
        
        self.onConditionChanged()
        
    def onConditionChanged(self):
        """条件改变时发出信号"""
        self.conditionChanged.emit()
        
    def setColumns(self, columns):
        """设置可选的列"""
        self.current_columns = columns
        self.condition_a.setColumns(columns)
        self.condition_b.setColumns(columns)
        
    def getCondition(self):
        """获取条件字符串"""
        cond_a = self.condition_a.getCondition()
        cond_b = self.condition_b.getCondition()
        
        if not cond_a and not cond_b:
            return ""
        elif cond_a and not cond_b:
            return cond_a
        elif not cond_a and cond_b:
            return cond_b
        else:
            logic = self.logic_combo.currentText()
            return f"({cond_a} {logic} {cond_b})"