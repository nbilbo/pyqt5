import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QThread


class Loop(QThread):
    def run(self):
        while True:
            print('Estamos no loop')
            break


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.set_settings()
        self.set_widgets()

    
    def set_settings(self):
        self.resize(200, 200)

    def set_widgets(self):
        self.button = QPushButton('Iniciar loop', self)
        self.button.clicked.connect(self.start_loop)
    
    def start_loop(self):
        self.thread_loop = Loop()
        self.thread_loop.start()

root = QApplication(sys.argv)
app = Window()
app.show()
sys.exit(root.exec_())
