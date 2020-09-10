'''
Calcular a idade apartir de um determinado ano.
'''
import sys
from PyQt5.QtWidgets import (QWidget, QApplication,QLabel, QSpinBox, QFormLayout, QPushButton, QGridLayout)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QPixmap, QIcon


def get_formated_date():
	now = QDate.currentDate()
	now = now.toString(Qt.DefaultLocaleLongDate)
	return now

def get_current_year():
	return QDate.currentDate().year()
	
class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.setWindowTitle('Calcular Idade')
		
		self.create_widgets()

		layout = QGridLayout()
		layout.addWidget(self.current_date, 0, 0, Qt.AlignTop)
		layout.addWidget(self.inupt_birth, 1, 0, Qt.AlignBottom)
		layout.addWidget(self.image, 1, 1, Qt.AlignRight)
		layout.addWidget(self.button, 2, 0, 1, 2)
		layout.addWidget(self.result, 3, 0, 1, 2, Qt.AlignCenter)

		self.setLayout(layout)

	def create_widgets(self):
		#current date
		label_date = QLabel(get_formated_date())
		self.current_date = label_date

		#input birth
		form_layout = QFormLayout()
		label_birth = QLabel('Ano de nascimento')
		spinbox_birth = QSpinBox()
		spinbox_birth.setRange(0, 9999)
		
		form_layout.addRow(label_birth, spinbox_birth)

		self.inupt_birth = QWidget()
		self.inupt_birth.setLayout(form_layout)

		#image
		self.image = QLabel()
		self.image.setPixmap(QPixmap('user.png'))

		#button
		self.button = QPushButton('Calcular')
		self.button.setIcon(QIcon('calc.png'))
		self.button.clicked.connect(self.button_click)

		#result
		self.result = QLabel('Resultado')

		for widget in (label_date, label_birth, spinbox_birth, self.button, self.result):
			widget.setFont(QFont('Georgia', 12))

	def button_click(self):
		current_year = get_current_year()
		years_old = current_year - self.inupt_birth.children()[2].value()
		self.result.setText(f'Você tem {years_old} anos de idade')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
