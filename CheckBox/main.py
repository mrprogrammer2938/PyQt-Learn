from PyQt5.QtWidgets import *
from check import Ui_MainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Check Box")
        
        self.ui.check_1.toggled.connect(self.clicker)
        self.ui.check_2.toggled.connect(self.clicker)
        self.ui.check_3.toggled.connect(self.clicker)
        
    def clicker(self):
        if self.ui.check_1.isChecked():
           check = self.ui.check_1.text()
        else:
            check = ""
            
            
        if self.ui.check_2.isChecked():
            check_2 = self.ui.check_2.text()
        else:
            check_2 = ""
        if self.ui.check_3.isChecked():
            check_3 = self.ui.check_3.text()
        else:
            check_3 = ""
            
        text = f"{check} {check_2} {check_3}"
        
        self.ui.label.setText(text)
        
        
app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())

