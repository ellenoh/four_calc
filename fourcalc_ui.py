# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p:/Ellen/workspace/gooey/fourcalc.ui'
#
# Created: Fri Oct 17 22:04:25 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(338, 233)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.output_le = QtGui.QLineEdit(Form)
        self.output_le.setObjectName(_fromUtf8("output_le"))
        self.verticalLayout.addWidget(self.output_le)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.k9_btn = QtGui.QPushButton(Form)
        self.k9_btn.setObjectName(_fromUtf8("k9_btn"))
        self.gridLayout.addWidget(self.k9_btn, 1, 2, 1, 1)
        self.k6_btn = QtGui.QPushButton(Form)
        self.k6_btn.setObjectName(_fromUtf8("k6_btn"))
        self.gridLayout.addWidget(self.k6_btn, 2, 2, 1, 1)
        self.minus_btn = QtGui.QPushButton(Form)
        self.minus_btn.setObjectName(_fromUtf8("minus_btn"))
        self.gridLayout.addWidget(self.minus_btn, 3, 3, 1, 1)
        self.k4_btn = QtGui.QPushButton(Form)
        self.k4_btn.setObjectName(_fromUtf8("k4_btn"))
        self.gridLayout.addWidget(self.k4_btn, 2, 0, 1, 1)
        self.k3_btn = QtGui.QPushButton(Form)
        self.k3_btn.setObjectName(_fromUtf8("k3_btn"))
        self.gridLayout.addWidget(self.k3_btn, 3, 2, 1, 1)
        self.multiply_btn = QtGui.QPushButton(Form)
        self.multiply_btn.setObjectName(_fromUtf8("multiply_btn"))
        self.gridLayout.addWidget(self.multiply_btn, 2, 3, 1, 1)
        self.k1_btn = QtGui.QPushButton(Form)
        self.k1_btn.setObjectName(_fromUtf8("k1_btn"))
        self.gridLayout.addWidget(self.k1_btn, 3, 0, 1, 1)
        self.clr_btn = QtGui.QPushButton(Form)
        self.clr_btn.setObjectName(_fromUtf8("clr_btn"))
        self.gridLayout.addWidget(self.clr_btn, 0, 1, 1, 1)
        self.back_btn = QtGui.QPushButton(Form)
        self.back_btn.setObjectName(_fromUtf8("back_btn"))
        self.gridLayout.addWidget(self.back_btn, 0, 0, 1, 1)
        self.k8_btn = QtGui.QPushButton(Form)
        self.k8_btn.setObjectName(_fromUtf8("k8_btn"))
        self.gridLayout.addWidget(self.k8_btn, 1, 1, 1, 1)
        self.k5_btn = QtGui.QPushButton(Form)
        self.k5_btn.setObjectName(_fromUtf8("k5_btn"))
        self.gridLayout.addWidget(self.k5_btn, 2, 1, 1, 1)
        self.k2_btn = QtGui.QPushButton(Form)
        self.k2_btn.setObjectName(_fromUtf8("k2_btn"))
        self.gridLayout.addWidget(self.k2_btn, 3, 1, 1, 1)
        self.divide_btn = QtGui.QPushButton(Form)
        self.divide_btn.setObjectName(_fromUtf8("divide_btn"))
        self.gridLayout.addWidget(self.divide_btn, 1, 3, 1, 1)
        self.k7_btn = QtGui.QPushButton(Form)
        self.k7_btn.setObjectName(_fromUtf8("k7_btn"))
        self.gridLayout.addWidget(self.k7_btn, 1, 0, 1, 1)
        self.decimal_btn = QtGui.QPushButton(Form)
        self.decimal_btn.setObjectName(_fromUtf8("decimal_btn"))
        self.gridLayout.addWidget(self.decimal_btn, 4, 2, 1, 1)
        self.add_btn = QtGui.QPushButton(Form)
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.gridLayout.addWidget(self.add_btn, 4, 3, 1, 1)
        self.k0_btn = QtGui.QPushButton(Form)
        self.k0_btn.setObjectName(_fromUtf8("k0_btn"))
        self.gridLayout.addWidget(self.k0_btn, 4, 0, 1, 2)
        self.equal_btn = QtGui.QPushButton(Form)
        self.equal_btn.setObjectName(_fromUtf8("equal_btn"))
        self.gridLayout.addWidget(self.equal_btn, 0, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.k9_btn.setText(_translate("Form", "9", None))
        self.k6_btn.setText(_translate("Form", "6", None))
        self.minus_btn.setText(_translate("Form", "-", None))
        self.k4_btn.setText(_translate("Form", "4", None))
        self.k3_btn.setText(_translate("Form", "3", None))
        self.multiply_btn.setText(_translate("Form", "*", None))
        self.k1_btn.setText(_translate("Form", "1", None))
        self.clr_btn.setText(_translate("Form", "C", None))
        self.back_btn.setText(_translate("Form", "BACK", None))
        self.k8_btn.setText(_translate("Form", "8", None))
        self.k5_btn.setText(_translate("Form", "5", None))
        self.k2_btn.setText(_translate("Form", "2", None))
        self.divide_btn.setText(_translate("Form", "/", None))
        self.k7_btn.setText(_translate("Form", "7", None))
        self.decimal_btn.setText(_translate("Form", ".", None))
        self.add_btn.setText(_translate("Form", "+", None))
        self.k0_btn.setText(_translate("Form", "0", None))
        self.equal_btn.setText(_translate("Form", "=", None))

