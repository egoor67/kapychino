# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 49, 800, 751))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.addBut = QtWidgets.QPushButton(Form)
        self.addBut.setGeometry(QtCore.QRect(30, 10, 93, 28))
        self.addBut.setObjectName("addBut")
        self.editBut = QtWidgets.QPushButton(Form)
        self.editBut.setGeometry(QtCore.QRect(160, 10, 93, 28))
        self.editBut.setObjectName("editBut")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addBut.setText(_translate("Form", "Add"))
        self.editBut.setText(_translate("Form", "edit"))
