'''
encerrar a aplicação quando clicar no botão.
'''
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.settings()
		self.create_button()

	def settings(self):
		self.setGeometry(0, 0, 500, 500)
		self.setWindowTitle('Exemple')

	def create_button(self):
		button = QPushButton('Quit', self)
		button.clicked.connect(QApplication.instance().quit)
		button.move(50, 50)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
