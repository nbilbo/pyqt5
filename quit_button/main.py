'''
encerrar a aplicação quando clicar no botão.
'''
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtWidgets import QMessageBox


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

	def closeEvent(self, event):
		
		reply = QMessageBox.question(self, 'Message', 
									'Are you sure to quit?',
									QMessageBox.Yes | QMessageBox.No, 
									QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
