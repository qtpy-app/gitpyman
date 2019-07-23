# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import io
import os
import sys
# sys.path.insert(0,"../")
from PyQt5.QtWebChannel import QWebChannel

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineProfile
from PyQt5.QtWidgets import *

from util.BasePara import Signals
from UUI_WEB.webComponent import MyEngineView, MyWebEngineUrlRequest
from UUI_WEB.webControl import WebControl
from UUI_WEB.webSharedObject import MyWebSharedObject

# from PyQt5.QtWidgets import QMainWindow

try:
    from UUI.Ui_Serve import Ui_Form
except ImportError as e:
    print("--1 --", e)
    try:
        from Ui_Serve import Ui_Form
    except ImportError as e:
        print("--2 --", e)


class MainWebFrom(QWidget, Ui_Form, WebControl):
    """
    Class documentation goes here.
    """
    test_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        from util import BasePara

        super().__init__(parent)
        global DEBUG

        if isinstance(self, QWidget):
            BasePara.mw = self if BasePara.mw is None else BasePara.mw
            BasePara.DEBUG = DEBUG = True if BasePara.DEBUG is None else BasePara.DEBUG
            print("赋值1:", BasePara.mw, BasePara.DEBUG)
        else:
            BasePara.mw = self
            BasePara.DEBUG = DEBUG = True

        # -------------------------- ↑

        self.mw = parent
        self.setupUi(self)
        self.initUI()
        # web调试窗口 ,
        self.show_debug_web() if  DEBUG else None

    def initUI(self):
        # HIDE DEBUG
        from util import BasePara
        if DEBUG is False:
            self.debug_gp.setVisible(False)
        else:
            BasePara.mw.setWindowIcon(QApplication.style().standardIcon(2))
        # 设置浏览器
        self.browser = MyEngineView(self)
        self.Bridge = MyWebSharedObject(self)
        # 小注释 : 拦截设置
        # self.interceptor = MyWebEngineUrlRequest()
        # profile = QWebEngineProfile.defaultProfile()
        # profile.setRequestInterceptor(self.interceptor)

        # channel ,设置交互接口
        self.channel = QWebChannel(self)
        self.channel.registerObject('Bridge', self.Bridge)
        self.page().setWebChannel(self.channel)
        # 让浏览器相应url地址的变化
        self.browser.urlChanged.connect(self.renew_urlbar_slot)

        # 小注释 :
        # 指定打开界面的 URL
        # url = "http://93.hf666.net/"
        # url = "http://93.hf666.net/entrance.jsp?tpl=rf888"
        # url = "http://93.hf666.net/login_page.jsp?p=QWERTYUMTMwOTEzMDY1MT14ZWRuaV84ODhmciZuYz1YR05BTCY4ODhmcj1scHQ%253D"
        # self.browser.setUrl(QUrl(url))

        # 添加浏览器到窗口中
        self.verticalLayout.addWidget(self.browser)


        # self.verticalLayout.insertWidget(0, QPushButton('loadAll', clicked=self.test_clicked_signal.emit))
        # <editor-fold desc="导航栏">
        ## 使用QToolBar创建导航栏，并使用QAction创建按钮
        # 0.添加导航栏 , 设定图标的大小
        navigation_bar = QToolBar('Navigation')
        navigation_bar.setIconSize(QSize(16, 16))

        # 1.添加前进、后退、停止加载和刷新的按钮
        self.back_button = QAction('Back', self)
        self.next_button = QAction('Forward', self)
        self.stop_button = QAction('stop', self)
        self.reload_button = QAction('reload', self)
        self.web_zoom_sp = QtWidgets.QDoubleSpinBox(self.frame)
        self.web_zoom_sp.setMaximum(5.0)
        self.web_zoom_sp.setSingleStep(0.05)
        self.web_zoom_sp.setProperty("value", 1.0)
        self.web_zoom_sp.setObjectName("web_zoom_sp")
        self.web_zoom_sp.setPrefix("WebZoom: ")
        self.web_zoom_sp.setSuffix(" x")


        self.web_zoom_sp.valueChanged.connect(lambda v:self.browser.setZoomFactor(v))

        self.back_button.triggered.connect(self.browser.back)
        self.next_button.triggered.connect(self.browser.forward)
        self.stop_button.triggered.connect(self.browser.stop)
        # 小注释 : # self.reload_button.triggered.connect(self.browser.reload)
        try:
            self.reload_button.triggered.connect(BasePara.mw.on_relogin_triggered)
        except:
            pass

        # 2.添加URL地址栏 ,让地址栏能响应回车按键信号
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url_slot)
        # </editor-fold>

        # <editor-fold desc="导航栏布局">
        # 小注释 : # 添加导航栏到窗口中

        self.addToolBar(navigation_bar)
        # 小注释 :  将按钮添加到导航栏上
        navigation_bar.addAction(self.back_button)
        navigation_bar.addAction(self.next_button)
        navigation_bar.addAction(self.stop_button)
        navigation_bar.addAction(self.reload_button)

        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)
        navigation_bar.addWidget(self.web_zoom_sp)
        # </editor-fold>

    def navigate_to_url_slot(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)

    def renew_urlbar_slot(self, q):
        # 将当前网页的链接更新到地址栏
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def addToolBar(self, toolbar):
        if isinstance(self, QWidget):
            self.verticalLayout.insertWidget(0, toolbar)
        else:
            super().addToolBar(toolbar)

    def statusBar(self) -> QStatusBar:
        if isinstance(self, QWidget):
            return self.mw.statusBar()
        else:
            return super().statusBar()


if __name__ == "__main__":
    import traceback

    os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '9966'
    os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--disable-logging --log-level=4'
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))


    def excepthook(excType, excValue, tracebackobj):
        """ globals catch error / tb = traceback"""
        try:

            errmsg = '{0}: \n{1}'.format(str(excType), str(excValue))

            tbinfofile = io.StringIO()
            traceback.print_tb(tracebackobj, None, tbinfofile)
            tbinfofile.seek(0)

            tbinfo = tbinfofile.read()
            # emit
            error = errmsg + tbinfo
            # Signals.show_error_msg_signal.emit(error)
        except:
            pass
        sys.__excepthook__(excType, excValue, tracebackobj)


    sys.excepthook = excepthook

    ui = MainWebFrom()

    ui.show()
    sys.exit(app.exec_())
