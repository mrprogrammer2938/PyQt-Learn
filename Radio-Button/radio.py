# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radio_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_1.setGeometry(QtCore.QRect(150, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_1.setFont(font)
        self.radio_1.setObjectName("radio_1")
        self.radio_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_2.setGeometry(QtCore.QRect(150, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_2.setFont(font)
        self.radio_2.setObjectName("radio_2")
        self.radio_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_3.setGeometry(QtCore.QRect(150, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_3.setFont(font)
        self.radio_3.setObjectName("radio_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 180, 281, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radio_1.setText(_translate("MainWindow", "پیتزا اورجینال"))
        self.radio_2.setText(_translate("MainWindow", "پیتزا پپرونی"))
        self.radio_3.setText(_translate("MainWindow", "پیتزا قارچ"))
        self.label_2.setText(_translate("MainWindow", "پیتزا"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())