'''
Um programa que tira screenshots.
'''


import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, 
                                QLabel, QGridLayout, QFileDialog)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        self.settings()
        self.create_widgets()
        self.set_layout()
    
    def settings(self):
        self.resize(370, 300)
        self.setWindowTitle('Screenshoter')

    def create_widgets(self):
        self.img_preview = QLabel()
        self.img_preview.setPixmap(self.preview_screen.scaled(350, 350, 
                                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.btn_save_screenshot = QPushButton('Save screenshot')
        self.btn_new_screenshot = QPushButton('New screenshot')

        #signals
        self.btn_save_screenshot.clicked.connect(self.save_screenshot)
        self.btn_new_screenshot.clicked.connect(self.new_screenshot)
    
    def set_layout(self):
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.img_preview, 0, 0, 2, 0)
        self.main_layout.addWidget(self.btn_new_screenshot, 1, 0)
        self.main_layout.addWidget(self.btn_save_screenshot, 1, 1)
        self.setLayout(self.main_layout)
    
    def save_screenshot(self):
        img, _ = QFileDialog.getSaveFileName(self, 'Salvar Arquivo', 
                                            filter='PNG(*.png);; JPEG(*.jpg)')

        if img.endswith('png'):
            self.preview_screen.save(img, 'png')
        
        elif img.endswith('jpg'):
            self.preview_screen.save(img, 'jpg')         

    def new_screenshot(self):
        self.hide()
        #millissegundos
        delay = 1
        QTimer.singleShot(delay, self.take_screenshot)
    
    def take_screenshot(self):
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        self.img_preview.setPixmap(self.preview_screen.scaled(350, 350, 
                                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.show()
    



root = QApplication(sys.argv)
app = Window()
app.show()
sys.exit(root.exec_())

