import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication
from PyQt5.QtGui import QColor, QPalette


class Color(QWidget):
	def __init__(self, color, *args, **kwargs):
		super(Color, self).__init__()
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
		self.setWindowTitle('QHBoxLayout')
		self.resize(900, 500)

	def create_widgets(self):
		layout = QHBoxLayout()
		
		layout.addWidget(Color('#f00'))
		layout.addWidget(Color('#0f0'))
		layout.addWidget(Color('#00f'))

		self.setLayout(layout)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
