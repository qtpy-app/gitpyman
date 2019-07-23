# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Serve.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(844, 546)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addWidget(self.frame)
        self.debug_gp = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debug_gp.sizePolicy().hasHeightForWidth())
        self.debug_gp.setSizePolicy(sizePolicy)
        self.debug_gp.setMaximumSize(QtCore.QSize(200, 16777215))
        self.debug_gp.setObjectName("debug_gp")
        self.gridLayout = QtWidgets.QGridLayout(self.debug_gp)
        self.gridLayout.setObjectName("gridLayout")
        self.reInject_btn = QtWidgets.QPushButton(self.debug_gp)
        self.reInject_btn.setObjectName("reInject_btn")
        self.gridLayout.addWidget(self.reInject_btn, 1, 1, 1, 1)
        self.run_btn = QtWidgets.QPushButton(self.debug_gp)
        self.run_btn.setObjectName("run_btn")
        self.gridLayout.addWidget(self.run_btn, 0, 1, 1, 1)
        self.run_js_pe = QtWidgets.QPlainTextEdit(self.debug_gp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_js_pe.sizePolicy().hasHeightForWidth())
        self.run_js_pe.setSizePolicy(sizePolicy)
        self.run_js_pe.setObjectName("run_js_pe")
        self.gridLayout.addWidget(self.run_js_pe, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.debug_gp)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.debug_gp.setTitle(_translate("Form", "DEBUG"))
        self.reInject_btn.setText(_translate("Form", "reInject"))
        self.run_btn.setText(_translate("Form", "run"))
        self.run_js_pe.setPlainText(_translate("Form", "console.log( )\n"
""))

