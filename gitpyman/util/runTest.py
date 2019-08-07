# coding=utf-8
import functools
import json

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *




def RELOAD(mw_):
    from Client import MainWindow

    mw: MainWindow = mw_
    mw.rw_tb.on_control_rw = functools.partial(on_control_rw, mw.rw_tb)
