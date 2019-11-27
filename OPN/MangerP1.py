from BootCampProject1.MangerWind import AddCoustmer1
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MangerP.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#Ui_Manger_Window
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from  OPN.AddCoustmer1 import Ui_Dialog
#from  OPN.AddProduct1 import Ui_Dialog1
def addcoustmer_button(self):
    addcoustmer_button.Ui_Dialog.set

class Ui_Manger_Window(object):
#ADD_COUSTMER_WINDOW
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
#ADD_PRODUCT_WINDOW
    def openWindow1(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window1)
        self.window1.show()

    def setupUi(self, Manger_Window):
        Manger_Window.setObjectName("Manger_Window")
        Manger_Window.resize(512, 434)
        self.pushButton = QtWidgets.QPushButton(Manger_Window)
        self.pushButton.setGeometry(QtCore.QRect(210, 190, 91, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Manger_Window)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 80, 91, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openWindow1)
        self.pushButton_3 = QtWidgets.QPushButton(Manger_Window)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 300, 91, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(Manger_Window)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 300, 91, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.openWindow1)
        self.pushButton_4 = QtWidgets.QPushButton(Manger_Window)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 80, 91, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Manger_Window)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 61))
        self.label.setObjectName("label")

        self.retranslateUi(Manger_Window)
        QtCore.QMetaObject.connectSlotsByName(Manger_Window)

    def retranslateUi(self, Manger_Window):
        _translate = QtCore.QCoreApplication.translate
        Manger_Window.setWindowTitle(_translate("Manger_Window", "Dialog"))
        self.pushButton.setText(_translate("Manger_Window", "Schedule"))
        self.pushButton_2.setText(_translate("Manger_Window", "Add Coustmer"))
        self.pushButton_3.setText(_translate("Manger_Window", "Add Problem"))
        self.pushButton_6.setText(_translate("Manger_Window", "Add Product"))
        self.pushButton_4.setText(_translate("Manger_Window", "Add Employee"))
        self.label.setText(_translate("Manger_Window", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">       Window Manger</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Manger_Window = QtWidgets.QDialog()
    ui = Ui_Manger_Window()
    ui.setupUi(Manger_Window)
    Manger_Window.show()
    sys.exit(app.exec_())
