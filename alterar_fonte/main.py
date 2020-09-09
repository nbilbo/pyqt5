import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
#This
from PyQt5.QtGui import QFont


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.resize(500, 500)
		label = QLabel('Label', self)
		#Set Font
		label.setFont(QFont('Georgia', 15))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
