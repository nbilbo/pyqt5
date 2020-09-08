import sys
from PyQt5.QtWidgets import QWidget, QApplication

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        
        self.setWindowTitle('Hello world')
        self.resize(500, 500)


root = QApplication(sys.argv)
app = Window()
app.show()
sys.exit(root.exec_())
