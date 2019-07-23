# coding=utf-8
import functools
import json

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


TESTPARA = 3


def tjrw(self, wf_id, wf_name):
    print(wf_id, wf_name)

    self.on_add_rw(wf_id, wf_name)

    self.after_add_rw_clear(wf_id, wf_name)


def on_control_rw(self):
    # 分主动 和 被动 启动

    btn: QPushButton = self.sender()
    row, col = self._currentRow_FromWidget(btn)
    print("--",row)

    # 启动 -> 停止
    if btn.isChecked():
        # 判断是否开放下注
        # 判断时间是否允许
        btn.setText("请启动")
    # 停止 -> 启动
    else:
        # 改变TaskContrl状态
        btn.setText("已启动")



def RELOAD(mw_):
    from Client import MainWindow

    mw: MainWindow = mw_
    # mw.rw_tb.on_control_rw = functools.partial(on_control_rw, mw.rw_tb)
