# coding=utf-8
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QPushButton, QItemDelegate, QAbstractItemDelegate


class URLDelegate(QItemDelegate):

    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        owner = str(index.data())
        combo = QPushButton(owner, parent)
        url = "https://github.com" + owner
        combo.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(url)))
        return combo

    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        # editor.setCurrentIndex(int(index.model().data(index)))
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.text())

    # @pyqtSlot()
    # def currentIndexChanged(self):
    #     self.commitData.emit(self.sender())
