# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 225)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 511, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.title = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.title.setObjectName("title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.title)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.roast_degree = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.roast_degree.setObjectName("roast_degree")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roast_degree)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.type = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.type.setObjectName("type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.type)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.taste = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.taste.setObjectName("taste")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taste)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.price = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.price.setObjectName("price")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.price)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.V = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.V.setObjectName("V")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.V)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 10, 93, 181))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "title"))
        self.label_2.setText(_translate("MainWindow", "roast_degree"))
        self.label_3.setText(_translate("MainWindow", "type"))
        self.label_4.setText(_translate("MainWindow", "taste"))
        self.label_5.setText(_translate("MainWindow", "price"))
        self.label_6.setText(_translate("MainWindow", "V"))
        self.pushButton.setText(_translate("MainWindow", "Ок"))
