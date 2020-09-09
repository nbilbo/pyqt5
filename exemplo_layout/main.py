import sys
from PyQt5.QtWidgets import (QWidget, QApplication, 
							QMainWindow, QVBoxLayout,
							QHBoxLayout)
from PyQt5.QtGui import QColor, QPalette


class Color(QWidget):
	def __init__(self, color, *args, **kwargs):
		super(Color, self).__init__(*args, **kwargs)
		self.setAutoFillBackground(True)

		palette = self.palette()
		palette.setColor(QPalette.Window, QColor(color))
		self.setPalette(palette)


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle('My Awesome App')
		self.resize(900, 500)

		layout1 = QHBoxLayout()
		layout2 = QVBoxLayout()
		layout3 = QVBoxLayout()

		layout2.addWidget(Color('red'))
		layout2.addWidget(Color('yellow'))
		layout2.addWidget(Color('purple'))

		layout3.addWidget(Color('red'))
		layout3.addWidget(Color('purple'))

		layout1.addLayout(layout2)
		layout1.addWidget(Color('green'))
		layout1.addLayout(layout3)

		layout1.setSpacing(1)
		layout1.setContentsMargins(10, 10, 10, 10)

		widget = QWidget()
		widget.setLayout(layout1)
		self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
