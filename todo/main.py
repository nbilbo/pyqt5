# coding: utf-8
# fonte de estudo: https://www.learnpyqt.com/courses/model-views/modelview-architecture/

import sys
from json import dump, load
from PyQt5.QtCore import Qt, QAbstractListModel
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                            QGridLayout, QPushButton, QLineEdit,
                            QListView)


class Model(QAbstractListModel):
    def __init__(self, data=None, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self._data = data or []
    
    def data(self, index, role):
        status, text = self._data[index.row()]
        
        if role == Qt.DisplayRole:
            return text
        
        if role == Qt.DecorationRole:
            if status:
                return QColor('green')
    
    def rowCount(self, index):
        return len(self._data)


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # configurando a janela
        self.settings()
        
        # central widget
        widget = QWidget()
        widget.setLayout(self.create_layout())
        self.setCentralWidget(widget)
        
        # load
        self.load()
    
    def settings(self):
        '''
        Configurar a janela.
        '''
        self.resize(550, 700)
        self.setWindowTitle('Todo')
    
    def create_layout(self):
        '''
        Criar um gridlayout e adicioanar widgets nele.
        '''
        #list
        self.model = Model()
        self.list = QListView()
        self.list.setModel(self.model)
        
        #input
        self.input_todo = QLineEdit()
        
        #buttons
        self.button_add = QPushButton(text='Adicionar')
        self.button_add.pressed.connect(self.add)
        
        self.button_remove = QPushButton(text='Remover')
        self.button_remove.pressed.connect(self.remove)
        
        self.button_complete = QPushButton(text='Completar')
        self.button_complete.pressed.connect(self.complete)
        
        # grid layout 
        layout = QGridLayout()
        layout.addWidget(self.input_todo, 0, 0)
        layout.addWidget(self.button_add, 1, 0)
        layout.addWidget(self.button_complete, 2, 0)
        layout.addWidget(self.list, 3, 0)
        layout.addWidget(self.button_remove, 4, 0)
        
        return layout
    
    def add(self):
        '''
        adicioanr uma nova linha.
        '''
        text = self.input_todo.text()
        if text:
            self.model._data.append((False, text))
            self.model.layoutChanged.emit()
            self.input_todo.setText('')
            
            # save
            self.save()
    
    def remove(self):
        '''
        remover a linha selecionada.
        '''
        indexes = self.list.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            del self.model._data[row]
            self.model.layoutChanged.emit()
            
            #save
            self.save()
    
    def complete(self):
        '''
        inverter o status da linha selecionada.
        '''
        indexes = self.list.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model._data[row]
            status = not status
            self.model._data[row] = (status, text)
            self.model.dataChanged.emit(index, index)
            
            #save
            self.save()
    
    def save(self):
        with open('todos.json', 'w') as f:
            dump(self.model._data, f)
    
    def load(self):
        try:
            with open('todos.json', 'r') as f:
                self.model._data = load(f)
        
        except Exception:
            pass


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont('Georgia, Arial'))
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    