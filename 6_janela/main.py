import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.settings()

	def settings(self):
		self.resize(250, 150)
		self.move(0, 300)
		self.setWindowTitle('Simple')
		self.setWindowIcon(QIcon('img.png'))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
