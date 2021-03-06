# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_RegisterWindow(object):



    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(821, 607)
        RegisterWindow.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:14px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    background:rgba(0,0,0,0.8);\n"
"    border-radius:15px;\n"
"}\n"
"#RegisterWindow{\n"
"    border-image: url(:/pref0/images/InterfaceChoisie.jpeg);\n"
"\n"
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
"QRadioButton{\n"
"    background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 80, 431, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 40, 111, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 340, 261, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.insert_data)

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 150, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(100, 200, 101, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 190, 171, 31))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 140, 171, 31))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(100, 250, 71, 20))
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(240, 250, 41, 18))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 250, 41, 18))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 100, 171, 31))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(340, 60, 61, 41))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pref1/images/RegisterUserIcon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setObjectName("toolButton")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)


    def insert_data(self):
        try:
            mydb = mysql.connector.connect(
                host="",
                user="",
                password="",
                database="review_site"

            )

            mycursor = mydb.cursor()

            username = self.lineEdit_4.text()
            email = self.lineEdit_3.text()
            language = self.lineEdit_2.text()
            if self.radioButton.isChecked():
                handSite = True
            elif self.radioButton_2.isChecked():
                handSite = False

            add_user = ("INSERT INTO USAGER (NOMUS, EMAILUS, LANGUS, HANDYUS) VALUES (%s, %s, %s, %s)")
            value = (username, email, language, handSite)

            mycursor.execute(add_user, value)

            mydb.commit()
            self.pushButton.setText("Registered succeffuly")
            mycursor.close()
            mydb.close()

        except mysql.connector.Error as e:
            print("Error Inserting Data")


    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        RegisterWindow.setWhatsThis(_translate("RegisterWindow", "<html><head/><body><p>#ffb860;</p></body></html>"))
        self.label.setText(_translate("RegisterWindow", "REGISTER HERE"))
        self.pushButton.setText(_translate("RegisterWindow", "Register"))
        self.label_2.setText(_translate("RegisterWindow", "Username:"))
        self.label_3.setText(_translate("RegisterWindow", "Useremail:"))
        self.label_4.setText(_translate("RegisterWindow", "Userlanguage:"))
        self.lineEdit_2.setText(_translate("RegisterWindow", "language"))
        self.lineEdit_2.setPlaceholderText(_translate("RegisterWindow", "username"))
        self.lineEdit_3.setText(_translate("RegisterWindow", "email"))
        self.lineEdit_3.setPlaceholderText(_translate("RegisterWindow", "username"))
        self.label_5.setText(_translate("RegisterWindow", "Disabled:"))
        self.radioButton.setWhatsThis(_translate("RegisterWindow", "<html><head/><body><p>#717072;</p></body></html>"))
        self.radioButton.setText(_translate("RegisterWindow", "YES"))
        self.radioButton_2.setWhatsThis(_translate("RegisterWindow", "<html><head/><body><p>#ffb860;</p></body></html>"))
        self.radioButton_2.setText(_translate("RegisterWindow", "NO"))
        self.lineEdit_4.setText(_translate("RegisterWindow", "username"))
        self.lineEdit_4.setPlaceholderText(_translate("RegisterWindow", "username"))
import images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())
