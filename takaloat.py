import csv
csv.register_dialect('myDialect', delimiter = ',', skipinitialspace=True)

with open('takaloat.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    for row in reader:
        print(row)

csvFile.close()



#rowNum=input("Enter ID: ")
#product=input("Enter Product: ")
#hindrance=input("hindrance: ")


#row = [rowNum, hindrance, product]

with open('takaloat.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[2] = row

with open('takaloat.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()




import csv

from PyQt5 import QtCore, QtGui, QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self, fileName, parent=None):
        super(MyWindow, self).__init__(parent)
        self.fileName = fileName

        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.pushButtonLoad = QtWidgets.QPushButton(self)
        self.pushButtonLoad.setText("Load Corrupt Base")
        self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)

        self.pushButtonWrite = QtWidgets.QPushButton(self)
        self.pushButtonWrite.setText("Save")
        self.pushButtonWrite.clicked.connect(self.on_pushButtonWrite_clicked)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.pushButtonLoad)
        self.layoutVertical.addWidget(self.pushButtonWrite)

    def loadCsv(self, fileName):
        with open('takaloat.csv', "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    def writeCsv(self, fileName):
        with open(fileName, "w") as fileOutput:
            writer = csv.writer(fileOutput)
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber, columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(self.model.columnCount())
                ]
                writer.writerow(fields)


    def on_pushButtonWrite_clicked(self):
        self.writeCsv(self.fileName)


    def on_pushButtonLoad_clicked(self):
        self.loadCsv(self.fileName)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow("hindrance01.csv")
    main.show()

    sys.exit(app.exec_())
