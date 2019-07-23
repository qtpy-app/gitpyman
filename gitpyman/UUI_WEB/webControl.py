# coding=utf-8


import sys

from PyQt5.QtCore import pyqtSlot, QUrl

from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

from util.BasePara import Signals
from util.Task import JF
from util import BasePara

class WebControl:

    @pyqtSlot()
    def on_reInject_btn_clicked(self):
        """
        Slot documentation goes here.
        """

        self.browser.reInject()

    @pyqtSlot()
    def on_run_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        cmd = self.run_js_pe.toPlainText()
        # print(cmd)
        self.page().runJavaScript(cmd)

    def page(self) -> QWebEnginePage:
        return self.browser.page()

    def show_debug_web(self):
        # 打开调试页面
        self.dw = QWebEngineView()
        self.dw.setWindowTitle('开发人员工具')
        self.dw.load(QUrl('http://127.0.0.1:9966'))
        self.dw.move(600, 100)
        self.dw.show()
        self.dw.closeEvent = lambda *a: self.show_debug_web()

    def closeEvent(self, *args, **kwargs):
        sys.exit(0)

