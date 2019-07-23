from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtWidgets import QMainWindow


class FLAGS:
    loginFlag = False



def login_check(func, *args, **kwargs):
    def do(*args, **kwargs):
        if FLAGS.loginFlag is True:
            func(*args, **kwargs)
        else:
            Signals.show_error_msg_signal.emit("请先登录")

    return do


def NEXT_GENERATOR(generator):
    try:
        next(generator)
        return True
    except StopIteration:
        return False


# <editor-fold desc="1. color">

R = 0
G = 1
B = 2
Y = 3
K = 4
W = 5
S = 6


class COLOR:
    R = QColor(Qt.red)
    G = QColor(Qt.green)
    B = QColor(Qt.blue)
    Y = QColor(Qt.darkYellow)
    K = QColor(Qt.black)
    W = QColor(Qt.white)
    S = QColor(Qt.blue)


class PEN:
    R = QPen(Qt.red)
    G = QPen(Qt.green)
    B = QPen(Qt.blue)
    Y = QPen(Qt.darkYellow)
    K = QPen(Qt.black)
    W = QPen(Qt.white)
    S = QPen(Qt.blue)


class BRUSH:
    R = QBrush(COLOR.R)
    G = QBrush(COLOR.G)
    B = QBrush(COLOR.B)
    Y = QBrush(COLOR.Y)
    K = QBrush(COLOR.K)
    W = QBrush(COLOR.W)
    S = QBrush(COLOR.S)


# </editor-fold>

# <editor-fold desc="2. mwObj & settings">
mw: QMainWindow = None
DEBUG = True


# </editor-fold>

# <editor-fold desc="3. global signals">
class _Signals(QObject):
    # 显示错误框
    show_error_msg_signal = pyqtSignal(str)
    show_state_msg_signal = pyqtSignal(str,int)
    # 网页登录成功后信号
    loginSuccess_signal = pyqtSignal()

    # 输出
    debug_zjxx_signal = pyqtSignal(object)


Signals = _Signals()

# </editor-fold>
