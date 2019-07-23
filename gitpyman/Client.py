# -*- coding: utf-8 -*-

"""
三方库:
pip install js2py
pip install requests
pip install sqlalchemy
# pip install eventlet
# pip install httpretty
# pip install pysnooper
"""
import io
import sys,os
from threading import Thread

from PyQt5.QtWebEngineWidgets import QWebEngineProfile

from UUI_WEB.webComponent import MyWebEngineUrlRequest
from util import github
from util.Task import JF

from importlib import reload

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

try:
    from Ui_Client import Ui_MainWindow
except ImportError as e:
    print("--1 --", e)
    try:
        from .Ui_Client import Ui_MainWindow
    except ImportError as e:
        print("--2 --", e)

from UUI_WEB.webControl import WebControl
from UUI.main_db_control import DBControl
from util.BasePara import Signals, FLAGS

from eventlet.hubs import epolls, kqueue, poll, selects
import eventlet as __eventlet
import hgoldfish
from hgoldfish.utils import eventlet


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):

        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        from util import BasePara

        # -------------quick obj------------- ↓
        BasePara.mw = self
        global DEBUG
        self.DEBUG = BasePara.DEBUG = DEBUG = False
        if DEBUG:
            os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '9966'
            os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--disable-logging --log-level=4'

        print("赋值0:", BasePara.mw, BasePara.DEBUG)

        # -------------quick obj------------- ↑

        super().__init__(parent)

        self.setupUi(self)
        self.__initDB()
        self.__initUI()
        self.__Signal()
        if DEBUG:
            self.DEBUGOPTION()

    def __initDB(self):
        global DB
        DB = self.DB = DBControl(self)

    def __initUI(self):
        self.hm_dialog = QDialog()
        self.hm_dialog.resize(800, 600)
        hm_layout = QHBoxLayout(self.hm_dialog)
        self.hm_show_te = QTextEdit(self.hm_dialog)
        hm_layout.addWidget(self.hm_show_te)

        DB.on_web_site_url_query()

        self.wycz_tab__wid.web_zoom_sp.setValue(0.75)
        self.showMaximized()

        url = "https://github.com/login?return_to=%2Fjoin"
        self.browser.setUrl(QUrl(url))
    def __Signal(self):
        self.thread_pools = eventlet.GreenletGroup()
        # Signals.loginSuccess_signal.connect(lambda: [self.tjrw_btn.setEnabled(True),
        #                            self.tjrw_btn.setText("添加任务(最多15个)")])
        # Signals.sy_zjxx_signal.connect(self.on_play)
        pass

    def DEBUGOPTION(self):


        # <editor-fold desc="重载调试">
        from util import runTest
        self.reload_btn = QPushButton("重载")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.reload_btn.setSizePolicy(sizePolicy)
        # self.horizontalLayout_9.addWidget(self.reload_btn)
        self.run2_btn = QPushButton("run")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.run2_btn.setSizePolicy(sizePolicy)
        self.run2_btn.clicked.connect(self.wycz_tab__wid.run_btn.click)

        # self.horizontalLayout_9.addWidget(self.run2_btn)

        @pyqtSlot()
        def on_reload_btn_clicked():
            """
            Slot documentation goes here.
            """
            reload(runTest)
            runTest.RELOAD(self)

        self.__timer = QTimer()
        self.__timer.timeout.connect(on_reload_btn_clicked)
        self.__timer.start(1000)
        # </editor-fold>

        # 小注释 : 拦截设置
        # <editor-fold desc="get debug">
        # self.interceptor = MyWebEngineUrlRequest()
        # profile = QWebEngineProfile.defaultProfile()
        # profile.setRequestInterceptor(self.interceptor)
        # </editor-fold>

        # <editor-fold desc="生成web js 按钮">
        import re
        js_str = self.browser._web_script
        jfunc2btn = re.compile(r'function (\w+\(.*?\))', re.M)
        # res = [i for i in dGitHubMatch.findall(a) if i[0]!='(']
        res = jfunc2btn.findall(js_str)
        btn_widget = QWidget()
        layout = QVBoxLayout(btn_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        self.wycz_tab__wid.gridLayout.addWidget(btn_widget, 0, 2, 4, 1)
        for row, btn_bxt in enumerate(res):
            btn = QPushButton(btn_bxt)
            btn.clicked.connect(lambda: self.wycz_tab__wid.run_js_pe.appendPlainText(self.sender().text()))
            layout.addWidget(btn)
        # </editor-fold>

        # 调试: 启动全部任务
        # self.web_user_cb.setCurrentIndex(2)
        self.DB.on_web_upwd_query()

    def page(self):
        return self.wycz_tab__wid.page()

    @property
    def browser(self):
        return self.wycz_tab__wid.browser

    @pyqtSlot()
    def on_relogin_triggered(self):
        """Serve.py // reload_button.triggered连接 """
        self.browser.reload()
        # 重置
        self.__relogin_clear()

    def __relogin_clear(self):

        FLAGS.loginFlag = False
        FLAGS.first_login_Flag = True

    @pyqtSlot()
    def on_main_login_btn_clicked(self):
        """
        登录按钮: 1.检查是否为空;
                 2.1 更新/创建账号;
                 2.2 登录.
        """


        if self.web_site_cb.currentText() == "" \
                or self.web_user_cb.currentText() == "" \
                or self.web_pwd_le.text() == "":
            Signals.show_error_msg_signal.emit("网址/用户名/密码 不允许为空.")
        else:
            # <editor-fold desc="1.web登陆">
            # 更新/创建账号
            DB.create_or_update_webInfo()
            # 登录
            # self.tabWidget.setCurrentIndex(2)
            # 重置
            self.__relogin_clear()
            # 靠JS登录函数轮询登录
            url = DB.get_c_url()
            le_url = self.browser.url().url()
            if 'login' not in le_url:
                self.browser.setUrl(QUrl(url))
            uname, upwd, url = DB.get_c_uname(), DB.get_c_upwd(), DB.get_c_url()
            QTimer.singleShot(500, lambda: self.page().runJavaScript(JF.login(uname, upwd)))
            # </editor-fold>

            # <editor-fold desc="2. 模块登陆">
            t = Thread(target=github.login2github, args=(uname, upwd))
            t.start()
            # </editor-fold>

    @pyqtSlot()
    def on_main_del_user_btn_clicked(self):
        """
        删除用户.
        """
        print("delete")
        DB.delete_webInfo()

    def closeEvent(self, *args, **kwargs):
        sys.exit(0)

    @pyqtSlot()
    def on_get_watching_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        DB.get_watching()

    @pyqtSlot()
    def on_re_select_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        DB.re_select_model()

    @pyqtSlot()
    def on_filter_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        DB.filterAll()

    def sleep(self, time=0.1):
        eventlet.sleep(time)

def main():
    import sys, traceback

    app = QApplication(sys.argv)
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
            Signals.debug_zjxx_signal.emit([error])
            Signals.show_error_msg_signal.emit(error)
        except:
            pass
        sys.__excepthook__(excType, excValue, tracebackobj)

    sys.excepthook = excepthook

    ui = MainWindow()

    ui.show()
    # sys.exit(app.exec_())
    # eventlet.start_application()
    eventlet.start_application(quitOnLastWindowClosed=True)


if __name__ == "__main__":

    main()
