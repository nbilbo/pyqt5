import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
from PyQt5.QtGui import QColor, QPalette

class Color(QWidget):
	def __init__(self, color, *args, **kwargs):
		super(Color, self).__init__(*args, **kwargs)
		self.setAutoFillBackground(True)

		palette = self.palette()
		palette.setColor(QPalette.Window, QColor(color))
		self.setPalette(palette)


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.settings()
		self.create_widgets()

	def settings(self):
		self.resize(500, 500)
		self.setWindowTitle('QVBoxLayout')

	def create_widgets(self):
		layout = QVBoxLayout()
		layout.addWidget(Color('red'))
		layout.addWidget(Color('green'))
		layout.addWidget(Color('blue'))
		self.setLayout(layout)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
