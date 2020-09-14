import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, 
                                                QSlider, QSpinBox, QLabel, QListWidget, QPushButton)


class Sliders(QWidget):
    def __init__(self, parent=None):
        super(Sliders, self).__init__(parent)
        
        self.main_layout = QVBoxLayout()
        
        self.create_begin()
        self.create_end()
        self.create_step()
        
        self.setLayout(self.main_layout)
        
    
    def create_begin(self):
        layout = QHBoxLayout()
        label = QLabel('Begin')
        spin = QSpinBox(minimum=-100, maximum=100)
        self.slider_begin = QSlider(orientation=Qt.Horizontal, minimum=-100, maximum=100)
        
        spin.valueChanged.connect(self.slider_begin.setValue)
        self.slider_begin.valueChanged.connect(spin.setValue)
        
        layout.addWidget(label)
        layout.addWidget(self.slider_begin)
        layout.addWidget(spin)
        self.main_layout.addLayout(layout)
    
    def create_end(self):
        layout = QHBoxLayout()
        label = QLabel('End')
        spin = QSpinBox(minimum=-100, maximum=100)
        self.slider_end = QSlider(orientation=Qt.Horizontal, minimum=-100, maximum=100)
        
        spin.valueChanged.connect(self.slider_end.setValue)
        self.slider_end.valueChanged.connect(spin.setValue)
        
        layout.addWidget(label)
        layout.addWidget(self.slider_end)
        layout.addWidget(spin)
        self.main_layout.addLayout(layout)
    
    def create_step(self):
        layout = QHBoxLayout()
        label = QLabel('Step')
        spin = QSpinBox(minimum=-100, maximum=100)
        self.slider_step = QSlider(orientation=Qt.Horizontal, minimum=-100, maximum=100)
        
        spin.valueChanged.connect(self.slider_step.setValue)
        self.slider_step.valueChanged.connect(spin.setValue)
        
        layout.addWidget(label)
        layout.addWidget(self.slider_step)
        layout.addWidget(spin)
        self.main_layout.addLayout(layout)
    
    def get_values(self):
        return [self.slider_begin.value(), self.slider_end.value(), self.slider_step.value()]


class Output(QListWidget):
    def __init__(self, parent=None):
        super(Output, self).__init__(parent)
        


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        
        self.settings()
        main_layout = QGridLayout()
        self.sliders = Sliders()
        self.output = Output() 
        self.button = QPushButton(text='Calc')
        self.button.clicked.connect(self.gen_values)
        
        main_layout.addWidget(self.sliders, 0, 0)
        main_layout.addWidget(self.output, 0, 1, 2, 1)
        main_layout.addWidget(self.button, 1, 0)
        self.setLayout(main_layout)
    
    def settings(self):
        self.resize(800, 300)
        self.setWindowTitle('Contador')
    
    def gen_values(self):
        begin, end, step = self.sliders.get_values()
        
        if not step:
            step = 1
        
            self.sliders.slider_step.setValue(1)
        self.output.clear()
        
        for count in range(begin, end, step):
            self.output.addItem(str(count))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont('Georgia', 12))
    
    window = Window()
    window.show()
    
    sys.exit(app.exec_())
