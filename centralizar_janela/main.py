import sys
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, 
								QApplication, QPushButton)


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.resize(400, 200)
		button = QPushButton('Center', self)
		button.clicked.connect(self.center)
		self.center()

	def center(self):
		geometry = self.frameGeometry()
		center_position = QDesktopWidget().availableGeometry().center()
		geometry.moveCenter(center_position)
		self.move(geometry.topLeft())


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
