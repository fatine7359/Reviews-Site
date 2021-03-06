# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from ListSiteInterface4 import Ui_ListSiteWindow
from ManageInterface3 import Ui_ManageWindow
from RegisterInterface4 import Ui_RegisterWindow
from review2 import Ui_Review
from reviewList2 import Ui_ReviewList


class Ui_HomeWindow(object):

    def openRegister(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openManage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ManageWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSiteList(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ListSiteWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openReviewList(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReviewList()
        self.ui.setupUi(self.window)
        self.window.show()

    def openReview(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Review()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(961, 710)
        HomeWindow.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:24px;\n"
"}\n"
"QFrame\n"
"{\n"
"    background:rgba(0,0,0,0.8);\n"
"    border-radius:15px\n"
"    \n"
"}\n"
"#HomeWindow{\n"
"    border-image: url(:/pref0/images/InterfaceChoisie.jpeg);\n"
"}\n"
"QToolButton\n"
"{\n"
"    background:#ffb860;\n"
"    border-radius:15px;\n"
"}\n"
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
"}")
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 130, 671, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 40, 71, 31))
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(60, 90, 81, 81))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pref1/images/AddReviewsIcon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(39, 39))
        self.toolButton.setObjectName("toolButton")

        self.toolButton.clicked.connect(self.openReview)

        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(260, 90, 81, 81))
        self.toolButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pref1/images/RegisterUserIcon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(39, 39))
        self.toolButton_2.setObjectName("toolButton_2")

        self.toolButton_2.clicked.connect(self.openRegister)

        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(150, 280, 81, 81))
        self.toolButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pref1/images/icon5.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(39, 39))
        self.toolButton_3.setObjectName("toolButton_3")

        self.toolButton_3.clicked.connect(self.openSiteList)

        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4.setGeometry(QtCore.QRect(460, 80, 81, 81))
        self.toolButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pref0/images/ManagerIcon1.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(65, 65))
        self.toolButton_4.setObjectName("toolButton_4")

        self.toolButton_4.clicked.connect(self.openManage)

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 190, 101, 31))
        self.label_5.setObjectName("label_5")
        self.toolButton_5 = QtWidgets.QToolButton(self.frame)
        self.toolButton_5.setGeometry(QtCore.QRect(370, 280, 81, 81))
        self.toolButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pref1/images/ReviewIcon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(60, 60))
        self.toolButton_5.setObjectName("toolButton_5")

        self.toolButton_5.clicked.connect(self.openReviewList)

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(260, 190, 131, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(460, 180, 121, 31))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(380, 380, 131, 31))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(170, 380, 91, 41))
        self.label_9.setObjectName("label_9")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(430, 80, 101, 81))
        self.toolButton_6.setStyleSheet("")
        self.toolButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pref1/images/HomeIcon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(65, 65))
        self.toolButton_6.setObjectName("toolButton_6")
        HomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "MainWindow"))
        self.label.setText(_translate("HomeWindow", "<html><head/><body><p>Home</p></body></html>"))
        self.label_5.setText(_translate("HomeWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Review</span></p></body></html>"))
        self.label_7.setText(_translate("HomeWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Register Here</span></p></body></html>"))
        self.label_8.setText(_translate("HomeWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Manage Site</span></p></body></html>"))
        self.label_6.setText(_translate("HomeWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Review List</span></p></body></html>"))
        self.label_9.setText(_translate("HomeWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Site List</span></p></body></html>"))
import HomePageIcon


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    HomeWindow.show()
    sys.exit(app.exec_())
