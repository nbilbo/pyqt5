import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
							QSlider, QScrollBar, QPushButton,
							QVBoxLayout, QFormLayout, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Sliders(QWidget):
	def __init__(self, parent=None):
		super(Sliders, self).__init__(parent)
		self.main_layout = QVBoxLayout()
		self.create_sliders()
		self.create_equation()
		self.create_events()
		self.setLayout(self.main_layout)
		
	def create_sliders(self):
		form = QFormLayout()
		
		self.label_a = QLabel('<html style="color: green">a</html>')
		self.label_b = QLabel('<html style="color: red">b</html>')
		self.label_c = QLabel('<html style="color: blue">c</html>')

		self.slider_a = QScrollBar(orientation=Qt.Horizontal, minimum=-100, maximum=100)
		self.slider_b = QScrollBar(orientation=Qt.Horizontal, minimum=-100, maximum=100)
		self.slider_c = QScrollBar(orientation=Qt.Horizontal, minimum=-100, maximum=100)

		form.addRow(self.label_a, self.slider_a)
		form.addRow(self.label_b, self.slider_b)
		form.addRow(self.label_c, self.slider_c)

		self.main_layout.addLayout(form)
	
	def create_equation(self):
		self.equation = QLabel(alignment=Qt.AlignCenter)
		self.equation.setText('<html>&Delta; = b<sup>2</sup> - 4.a.c</html>')

		self.main_layout.addWidget(self.equation)
	
	def create_events(self):
		for slider in (self.slider_a, self.slider_b, self.slider_c):
			slider.valueChanged.connect(self.slider_change_value)
	
	def slider_change_value(self):
		a, b, c = self.get_sliders_values(type_=str)
		self.set_equation_values(b, a, c)
	
	def get_sliders_values(self, type_=int):
		return [type_(slider.value()) for slider in (self.slider_a, self.slider_b, self.slider_c)]
	
	def set_equation_values(self, *args):
		self.equation.setText('<html>&Delta; = <span style="color: red">{0}</span><sup>2</sup> - 4.<span style="color: green">{1}</span>.<span style="color: blue">{2}</sup></html>'.format(*args))


class OutPut(QWidget):
	def __init__(self, parent=None):
		super(OutPut, self).__init__(parent)
		main_layout = QGridLayout()

		self.outout_delta = QLabel(text='---', alignment=Qt.AlignRight)
		self.outout_raiz_a = QLabel(text='---', alignment=Qt.AlignRight)
		self.outout_raiz_b = QLabel(text='---', alignment=Qt.AlignRight)

		main_layout.addWidget(QLabel('<html>&Delta;</html>', alignment=Qt.AlignLeft), 0, 0)
		main_layout.addWidget(self.outout_delta, 0, 1)

		main_layout.addWidget(QLabel('<html>Primeira Raiz</html>', alignment=Qt.AlignLeft), 1, 0)
		main_layout.addWidget(self.outout_raiz_a, 1, 1)

		main_layout.addWidget(QLabel('<html>Segunda Raiz</html>', alignment=Qt.AlignLeft), 2, 0)
		main_layout.addWidget(self.outout_raiz_b, 2, 1)

		self.setLayout(main_layout)
	
	def set_output_values(self, delta='---', raiz_a='---', raiz_b='---'):
		self.outout_delta.setText(delta)
		self.outout_raiz_a.setText(raiz_a)
		self.outout_raiz_b.setText(raiz_b)


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.main_layout = QVBoxLayout()
		self.settings()
		self.create_sliders()
		self.create_button()
		self.create_output()
		self.create_events()
		self.setLayout(self.main_layout)

	def settings(self):
		self.resize(900, 300)
	
	def create_sliders(self):
		self.sliders = Sliders()
		self.sliders.set_equation_values('0', '0', '0')
		self.main_layout.addWidget(self.sliders)
	
	def create_button(self):
		self.calc_button = QPushButton(text='Calcular')
		self.main_layout.addWidget(self.calc_button)
	
	def create_output(self):
		self.outout = OutPut()		
		self.main_layout.addWidget(self.outout)
	
	def create_events(self):
		self.calc_button.clicked.connect(self.calcular)

	def calcular(self):
		a, b, c = self.sliders.get_sliders_values()
		delta = (b*b)-(4*a*c)
		raiz_a = '---'
		raiz_b = '---'

		#equação completa
		if a != 0 and b != 0 and c != 0:
			if delta >= 0:
				raiz_a = raiz_b = (-b + (delta**.5)) / (2*a)
			
			if delta > 0:
				raiz_b = (-b - (delta**.5)) / (2*a)			
		
		self.outout.set_output_values(delta=str(delta), raiz_a=str(raiz_a), raiz_b=str(raiz_b))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setFont(QFont('Georgia', 15))

	window = Window()
	window.show()
	
	sys.exit(app.exec_())
	