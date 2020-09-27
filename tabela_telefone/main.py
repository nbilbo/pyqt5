# coding: utf-8
# fonte estudo: https://www.learnpyqt.com/courses/model-views/qtableview-modelviews-numpy-pandas/

import sys
import pandas as pd

from PyQt5.QtCore import (Qt, QAbstractTableModel)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
                            QTableView, QTableWidget, QFormLayout, QComboBox,
                            QLabel, QLineEdit, QPushButton)


class Model(QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self._data = pd.DataFrame({'tipo':[], 'numero':[]})
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row()][index.column()]
            return str(value)
            
    def rowCount(self, index):
        return self._data.shape[0]
    
    def columnCount(self, index):
        return self._data.shape[1]
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.settings()
        widget = QWidget()
        widget.setLayout(self.create_layout())
        self.setCentralWidget(widget)
    
    def create_layout(self):
        # table
        self.model = Model()
        self.table = QTableView()
        self.table.setModel(self.model)
        
        # combobox
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItem('residencial')
        self.combo_tipo.addItem('comercial')
        self.combo_tipo.addItem('celular')
        
        # input
        self.input_numero = QLineEdit()
        
        # botao adicionar
        self.botao_add = QPushButton('Adicionar')
        self.botao_add.pressed.connect(self.add)
        
        # botao remover
        self.botao_remove = QPushButton('Remover')
        self.botao_remove.pressed.connect(self.remove)
        
        # form
        form = QFormLayout()
        form.addRow(QLabel('Tipo *'), self.combo_tipo)
        form.addRow(QLabel('Número *'), self.input_numero)
        form.addWidget(self.botao_add)        
        
        # layout 
        layout = QGridLayout()
        layout.addLayout(form, 0, 0)
        layout.addWidget(self.table, 1, 0)
        layout.addWidget(self.botao_remove, 2, 0)
        return layout
    
    def settings(self):
        self.resize(800, 400)
    
    def add(self):
        tipo = self.combo_tipo.currentText()
        numero = self.input_numero.text()
        
        if tipo and numero:
            self.model._data = self.model._data.append({'tipo': tipo, 'numero': numero}, ignore_index=True)
            self.model.layoutChanged.emit()
            self.input_numero.setText('')
            print(self.get_dict())
            
    def remove(self):
        indexes = self.table.selectedIndexes()
        if indexes:            
            selections = self.model._data.index[[index.row() for index in indexes]]
            self.model._data = self.model._data.drop(selections)
            self.model.layoutChanged.emit()
            print(self.get_dict())
    
    def get_dict(self):
        return self.model._data.to_dict()
            
    
def main():
    app = QApplication([])
    app.setFont(QFont('Georgia'))
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    