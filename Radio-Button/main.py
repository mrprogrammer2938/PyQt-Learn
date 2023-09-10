from PyQt5.QtWidgets import *
from radio import Ui_MainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("رستوران")
        
        self.ui.radio_1.toggled.connect(self.clicker)
        self.ui.radio_2.toggled.connect(self.clicker)
        self.ui.radio_3.toggled.connect(self.clicker)
    def clicker(self):
        if self.ui.radio_1.isChecked():
            text = self.ui.radio_1.text()
            self.ui.label.setText(text)
        if self.ui.radio_2.isChecked():
            text = self.ui.radio_2.text()
            self.ui.label.setText(text)
        if self.ui.radio_3.isChecked():
            text = self.ui.radio_3.text()
            self.ui.label.setText(text)
        
        
app = QApplication(sys.argv)
win = Window()
win.show()

sys.exit(app.exec_())
