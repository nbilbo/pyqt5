import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
							QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.settings()
		self.create_button()

	def settings(self):
		#font used to render tooltips
		QToolTip.setFont(QFont('SansSerif', 14))
		#creating a tooltip
		self.setToolTip('This is a <b>QWidget</b> widget')
		self.setGeometry(0, 290, 1000, 500)
		self.setWindowTitle('Window')

	def create_button(self):
		btn = QPushButton('Button', self)
		#button font
		btn.setFont(QFont('SansSerif', 12))
		#creating a tooltip
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.move(50, 50)
		

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
