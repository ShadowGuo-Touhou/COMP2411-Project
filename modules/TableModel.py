from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

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

    def setHeaderData(self, section, orientation, value, role=Qt.ItemDataRole.EditRole):
            if orientation == Qt.Orientation.Horizontal and role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
                if 0 <= section < len(self._horizontal_headers):
                    self._horizontal_headers[section] = value
                    self.headerDataChanged.emit(orientation, section, section)
                    return True
            return super().setHeaderData(section, orientation, value, role)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
            if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
                if 0 <= section < len(self._horizontal_headers):
                    return self._horizontal_headers[section]

    def setHeaderLabel(self, header:list):
        for i in range(len(header)):    
            self.setHeaderData(i, Qt.Orientation.Horizontal, header[i])