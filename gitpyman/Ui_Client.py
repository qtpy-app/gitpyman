# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.web_site_cb = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web_site_cb.sizePolicy().hasHeightForWidth())
        self.web_site_cb.setSizePolicy(sizePolicy)
        self.web_site_cb.setEditable(True)
        self.web_site_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.web_site_cb.setObjectName("web_site_cb")
        self.horizontalLayout_2.addWidget(self.web_site_cb)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.web_user_cb = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web_user_cb.sizePolicy().hasHeightForWidth())
        self.web_user_cb.setSizePolicy(sizePolicy)
        self.web_user_cb.setEditable(True)
        self.web_user_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.web_user_cb.setObjectName("web_user_cb")
        self.horizontalLayout_2.addWidget(self.web_user_cb)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.web_pwd_le = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web_pwd_le.sizePolicy().hasHeightForWidth())
        self.web_pwd_le.setSizePolicy(sizePolicy)
        self.web_pwd_le.setMinimumSize(QtCore.QSize(90, 0))
        self.web_pwd_le.setMaximumSize(QtCore.QSize(200, 16777215))
        self.web_pwd_le.setText("")
        self.web_pwd_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.web_pwd_le.setObjectName("web_pwd_le")
        self.horizontalLayout_2.addWidget(self.web_pwd_le)
        self.main_login_btn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_login_btn.sizePolicy().hasHeightForWidth())
        self.main_login_btn.setSizePolicy(sizePolicy)
        self.main_login_btn.setObjectName("main_login_btn")
        self.horizontalLayout_2.addWidget(self.main_login_btn)
        self.main_del_user_btn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_del_user_btn.sizePolicy().hasHeightForWidth())
        self.main_del_user_btn.setSizePolicy(sizePolicy)
        self.main_del_user_btn.setObjectName("main_del_user_btn")
        self.horizontalLayout_2.addWidget(self.main_del_user_btn)
        self.line_3 = QtWidgets.QFrame(self.groupBox_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.widget)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setStyleSheet("QSplitter::handle{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QSplitter::handle:vertical  {\n"
"    margin:3px;\n"
"}")
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.wycz_tab__wid = MainWebFrom()
        self.wycz_tab__wid.setObjectName("wycz_tab__wid")
        self.tabWidget.addTab(self.wycz_tab__wid, "")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.repo_frame = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.repo_frame.sizePolicy().hasHeightForWidth())
        self.repo_frame.setSizePolicy(sizePolicy)
        self.repo_frame.setObjectName("repo_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.repo_frame)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.get_watching_btn = QtWidgets.QPushButton(self.repo_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_watching_btn.sizePolicy().hasHeightForWidth())
        self.get_watching_btn.setSizePolicy(sizePolicy)
        self.get_watching_btn.setObjectName("get_watching_btn")
        self.gridLayout.addWidget(self.get_watching_btn, 0, 0, 1, 1)
        self.re_select_btn = QtWidgets.QPushButton(self.repo_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.re_select_btn.sizePolicy().hasHeightForWidth())
        self.re_select_btn.setSizePolicy(sizePolicy)
        self.re_select_btn.setObjectName("re_select_btn")
        self.gridLayout.addWidget(self.re_select_btn, 0, 1, 1, 1)
        self.repo_tabWidget = QtWidgets.QTabWidget(self.repo_frame)
        self.repo_tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.repo_tabWidget.setObjectName("repo_tabWidget")
        self.gridLayout.addWidget(self.repo_tabWidget, 1, 0, 1, 2)
        self.toolbar_frame = QtWidgets.QFrame(self.repo_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar_frame.sizePolicy().hasHeightForWidth())
        self.toolbar_frame.setSizePolicy(sizePolicy)
        self.toolbar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolbar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolbar_frame.setObjectName("toolbar_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.toolbar_frame)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolButton = QtWidgets.QToolButton(self.toolbar_frame)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_3.addWidget(self.toolButton, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.toolbar_frame, 0, 2, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.filter_le = QtWidgets.QLineEdit(self.groupBox_2)
        self.filter_le.setObjectName("filter_le")
        self.gridLayout_2.addWidget(self.filter_le, 1, 0, 1, 1)
        self.filter_tv = QtWidgets.QTableView(self.groupBox_2)
        self.filter_tv.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.filter_tv.setObjectName("filter_tv")
        self.gridLayout_2.addWidget(self.filter_tv, 2, 0, 1, 2)
        self.filter_btn = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_btn.sizePolicy().hasHeightForWidth())
        self.filter_btn.setSizePolicy(sizePolicy)
        self.filter_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.filter_btn.setObjectName("filter_btn")
        self.gridLayout_2.addWidget(self.filter_btn, 0, 1, 2, 1)
        self.frame = QtWidgets.QFrame(self.groupBox_2)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filter_cb = QtWidgets.QComboBox(self.frame)
        self.filter_cb.setObjectName("filter_cb")
        self.filter_cb.addItem("")
        self.horizontalLayout.addWidget(self.filter_cb)
        self.filter_ckBox = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_ckBox.sizePolicy().hasHeightForWidth())
        self.filter_ckBox.setSizePolicy(sizePolicy)
        self.filter_ckBox.setChecked(False)
        self.filter_ckBox.setObjectName("filter_ckBox")
        self.horizontalLayout.addWidget(self.filter_ckBox)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.repo_tabWidget.setCurrentIndex(-1)
        self.filter_le.returnPressed.connect(self.filter_btn.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.main_login_btn, self.web_site_cb)
        MainWindow.setTabOrder(self.web_site_cb, self.web_pwd_le)
        MainWindow.setTabOrder(self.web_pwd_le, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "UserInfo"))
        self.label_14.setText(_translate("MainWindow", "URL"))
        self.label_2.setText(_translate("MainWindow", "UserName"))
        self.label_3.setText(_translate("MainWindow", "PassWord"))
        self.main_login_btn.setText(_translate("MainWindow", "Login/Update"))
        self.main_del_user_btn.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wycz_tab__wid), _translate("MainWindow", "web_page"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.get_watching_btn.setText(_translate("MainWindow", "get/update watching repo"))
        self.re_select_btn.setText(_translate("MainWindow", "update current repo"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.filter_le.setPlaceholderText(_translate("MainWindow", "input query comment"))
        self.filter_btn.setText(_translate("MainWindow", "query"))
        self.filter_cb.setItemText(0, _translate("MainWindow", "All"))
        self.filter_ckBox.setText(_translate("MainWindow", "UNION ALL"))

from UUI.Serve import MainWebFrom
