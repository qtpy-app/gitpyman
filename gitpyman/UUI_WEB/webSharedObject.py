# coding=utf-8


from urllib.parse import urlparse
import requests
import js2py
from PyQt5.QtCore import QObject, pyqtSlot, QVariant, Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QMessageBox, QErrorMessage, QMainWindow

from util import BasePara
from util.BasePara import Signals, FLAGS
from util.Task import JF




class MyWebSharedObject(QObject):

    def __init__(self, mw):
        super().__init__()

        if isinstance(mw, QMainWindow):
            self.mw = mw
        else:
            self.mw = BasePara.mw
        #
        self.error_dialog = QErrorMessage(self.mw)

        Signals.show_error_msg_signal.connect(self.topy_eMsg)
        Signals.show_state_msg_signal.connect(lambda txt,time=2000:self.topy_sMsg(txt,time))


    @pyqtSlot()
    def topy_login(self):
        FLAGS.loginFlag = True
        Signals.loginSuccess_signal.emit()

    @pyqtSlot(str)
    def topy_callFromJs(self, txt):
        QMessageBox.information(None, "提示", txt)

    # @pyqtSlot(str)
    @pyqtSlot(str, int)
    def topy_sMsg(self, txt, msec=2000):
        print(f"msec{msec}")
        self.mw.statusBar().showMessage(txt, msec)

    @pyqtSlot(str)
    def topy_eMsg(self, error):
        print("show error msg ")
        self.error_dialog.showMessage(error)

    @pyqtSlot()
    def topy_relogin(self):
        self.mw.on_relogin_triggered()
        self.mw.tabWidget.setCurrentIndex(2)

    # -------------辅助函数------------- ↓
    def page(self) -> QWebEnginePage:
        return self.mw.page()

    @property
    def browser(self):
        return self.mw.browser

    @property
    def cookies(self):
        return self.mw.browser.DomainCookies

    # -------------辅助函数------------- ↑

    @pyqtSlot(int, QVariant)
    def topy_merge_comment(self, index, new_comment):
        self.browser.merge_comment(index, new_comment)
