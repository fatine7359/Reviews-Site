# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListSiteInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_ListSiteWindow(object):
    def setupUi(self, ListSiteWindow):
        ListSiteWindow.setObjectName("ListSiteWindow")
        ListSiteWindow.resize(962, 653)
        ListSiteWindow.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:20px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    background:rgba(0,0,0,0.8);\n"
"    border-radius:15px;\n"
"}\n"
"#ListSiteWindow{\n"
"    border-image: url(:/pref0/images/InterfaceChoisie.jpeg);\n"
"}\n"
"QPushButton\n"
"{\n"
"background: #ffb860;\n"
"border-radius:30px;\n"
"}\n"
"QToolButton\n"
"{\n"
"background: #ffb860;\n"
"border-radius:15px;\n"
"}\n"
"QLabel\n"
"{\n"
"    color:#ffb860;\n"
"    background:transparent;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"color:black;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:#49ebff;\n"
"}\n"
"QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"QListView{\n"
"    \n"
"show-decoration-selected: 1;\n"
"border-bottom:1px solid #ffb860;\n"
"border-left: 1px solid #ffb860;\n"
"border-right:1px solid #ffb860;\n"
"border-top:1px solid #ffb860;\n"
"background-color:#ffb860;\n"
"background: transparent;\n"
"background: #ffb860;\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:#ffb860;\n"
"    \n"
"}\n"
"QToolButton\n"
"{\n"
"background: #ffb860;\n"
"border-radius:10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ListSiteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(180, 110, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(260, 50, 91, 31))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 140, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 200, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 131, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.display_data)

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(190, 130, 361, 241))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(440, 80, 81, 61))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pref1/images/icon5.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 30))
        self.toolButton.setObjectName("toolButton")
        ListSiteWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ListSiteWindow)
        self.statusbar.setObjectName("statusbar")
        ListSiteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListSiteWindow)
        QtCore.QMetaObject.connectSlotsByName(ListSiteWindow)

    def display_data(self):
        try:
            mydb = mysql.connector.connect(
                host="",
                user="",
                password="",
                database="review_site"

            )

            mycursor1 = mydb.cursor(buffered=True)
            mycursor2 = mydb.cursor(buffered=True)

            city = self.lineEdit.text()
            category = self.lineEdit_2.text()



            display_site = (
                "SELECT  LIENSITE FROM Sites INNER join categories on sites.CODECAT = categories.CODECAT WHERE VILLESITE = %s AND DESCAT= %s ")



            mycursor1.execute(display_site, (city, category))

            myresult1 = mycursor1.fetchall()

            for x in myresult1:
                display_notes = ("SELECT SITES.LIENSITE, AVG(NOTESITE) FROM Reviews INNER join Sites on sites.IDSITE = Reviews.IDSITE WHERE Sites.LIENSITE =%s GROUP BY Sites.LIENSITE ")
                mycursor2.execute(display_notes, x)
                myresult2 = mycursor2.fetchall()

                self.tableWidget.setRowCount(0)

                for row_number, row_data in enumerate(myresult2):
                    self.tableWidget.insertRow(row_number)

                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number,
                                                 column_number, QTableWidgetItem(str(data)))
                #for y in myresult2:
                    #print(x+y)



            mydb.commit()
            mycursor1.close()
            #mycursor2.close()
            mydb.close()

        except mysql.connector.Error as e:
            print("Error Displaying Data")

    def retranslateUi(self, ListSiteWindow):
        _translate = QtCore.QCoreApplication.translate
        ListSiteWindow.setWindowTitle(_translate("ListSiteWindow", "MainWindow"))
        self.label.setText(_translate("ListSiteWindow", "List Sites"))
        self.lineEdit.setText(_translate("ListSiteWindow", "City"))
        self.lineEdit_2.setText(_translate("ListSiteWindow", "category"))
        self.pushButton.setText(_translate("ListSiteWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ListSiteWindow", "Sites"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ListSiteWindow", "Notes Average"))
import images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListSiteWindow = QtWidgets.QMainWindow()
    ui = Ui_ListSiteWindow()
    ui.setupUi(ListSiteWindow)
    ListSiteWindow.show()
    sys.exit(app.exec_())
