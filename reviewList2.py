# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reviewList1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_ReviewList(object):
    def setupUi(self, ReviewList):
        ReviewList.setObjectName("ReviewList")
        ReviewList.resize(800, 600)
        ReviewList.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:24px;\n"
"}\n"
"QFrame\n"
"{\n"
"    background:rgba(0,0,0,0.8);\n"
"    border-radius:15px\n"
"    \n"
"}\n"
"#ReviewList{\n"
"    border-image: url(:/pref0/images/InterfaceChoisie.jpeg);\n"
"}\n"
"QToolButton\n"
"{\n"
"    background:#ffb860;\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color:#ffb860;\n"
"    background:transparent;\n"
"}\n"
"QPushButton\n"
"{\n"
"    color:#333;\n"
"    border-radius:15px;\n"
"    background:#ffb860;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color:#333;\n"
"    border-radius:15px;\n"
"    background:white;\n"
"}\n"
"QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"font-size:14px;\n"
"}\n"
"\n"
"QTableWidget{\n"
"show-decoration-selected: 1;\n"
"border-bottom:1px solid #ffb860;\n"
"border-left: 1px solid #ffb860;\n"
"border-right:1px solid #ffb860;\n"
"border-top:1px solid #ffb860;\n"
"background:#ffb860;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ReviewList)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(210, 110, 441, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 20, 201, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(50, 65, 291, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(360, 80, 41, 21))
        self.toolButton_2.setStyleSheet("QToolButton\n"
"{\n"
"    background:#ffb860;\n"
"    border-radius:5px;\n"
"}")
        self.toolButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pref1/images/SearchIcon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.select_data)
        self.toolButton_2.clicked.connect(self.select_data)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(50, 120, 341, 251))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 47, 41))
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    color:#ffb860;\n"
"    background:transparent;\n"
"    font-size:14px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(380, 40, 111, 81))
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pref1/images/ReviewIcon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(70, 70))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(200, 100, 31, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/asus/PycharmProjects/web-review/pictures/homebdd.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.setVisible(False)
        ReviewList.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ReviewList)
        self.statusbar.setObjectName("statusbar")
        ReviewList.setStatusBar(self.statusbar)

        self.retranslateUi(ReviewList)
        QtCore.QMetaObject.connectSlotsByName(ReviewList)

    def select_data(self):
        try:
            mydb = mysql.connector.connect(
                host="",
                user="",
                password="",
                database="review_site"

            )
            mycursor1 = mydb.cursor()
            URL = self.lineEdit.text()
            desplay_user = (
                "Select NOMUS,COMSITE FROM USAGER JOIN REVIEWS ON REVIEWS.IDUSAGER=USAGER.IDUSAGER WHERE IDSITE = (SELECT IDSITE FROM SITES WHERE LIENSITE =%s)")
            url = (URL,)
            mycursor1.execute(desplay_user, url)

            result = mycursor1.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            mycursor1.close()
            mydb.close()
        except mysql.connector.Error as e:
            print("error occured")

    def retranslateUi(self, ReviewList):
        _translate = QtCore.QCoreApplication.translate
        ReviewList.setWindowTitle(_translate("ReviewList", "MainWindow"))
        self.label.setText(_translate("ReviewList", "Review List"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ReviewList", "Username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ReviewList", "Review"))
        self.label_2.setText(_translate("ReviewList", "URL:"))
        self.toolButton_3.setText(_translate("ReviewList", "..."))

import  images

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReviewList = QtWidgets.QMainWindow()
    ui = Ui_ReviewList()
    ui.setupUi(ReviewList)
    ReviewList.show()
    sys.exit(app.exec_())
