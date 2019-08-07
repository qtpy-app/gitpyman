# coding=utf-8
from copy import deepcopy
from PyQt5.QtCore import Qt, QAbstractItemModel, pyqtSignal, QModelIndex
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QTableView, QMenu, QAbstractItemView


class QQTableView(QTableView):
    REMOVE_SIGNAL = pyqtSignal(object, dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUI()

    def __initUI(self):
        # <editor-fold desc="1.menu">
        self.customContextMenuRequested.connect(self.__myListWidgetContext)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # </editor-fold>

        self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def __updateWidth(self, aver_type=1):
        """刷新宽度 和最大值 """
        # inner_scrollbar = self.verticalScrollBar()

        model = self.model()
        rowCount = model.rowCount()
        TW_COL = model.columnCount()
        if rowCount > 0:
            vBar_width = self.verticalHeader().defaultSectionSize()
        else:
            vBar_width = 0
        ## 1. 均分
        if aver_type == 1:
            averwidth_n = self.width() / TW_COL
            for col in range(TW_COL):
                self.setColumnWidth(col, averwidth_n)

        ## 2. 前占后隐 ,不均分
        elif aver_type == 2:
            dw = 0
            aver_p = 3
            averwidth_n = (self.width()) / aver_p
            other_width = 80
            self.setColumnWidth(0, averwidth_n + dw)
            self.setColumnWidth(1, averwidth_n - dw / 2)
            self.setColumnWidth(2, averwidth_n - dw / 2)
            for col in range(aver_p, TW_COL):
                self.setColumnWidth(col, other_width)
        ## 3. 完全自定义, 不均分
        else:


            cus_width = {
                # 0 : 20,
                # 1 : 80, # 网址
                2: 70,  # 用户

            }

            averwidth_n = (self.width()
                           - sum(cus_width.values())
                           - vBar_width) / (TW_COL - len(cus_width))

            for col in range(TW_COL):
                if col in cus_width:
                    self.setColumnWidth(col, cus_width[col])
                else:
                    self.setColumnWidth(col, averwidth_n)

    def resizeEvent(self, e, *args, **kwargs):
        self.__updateWidth(3)
        return super().resizeEvent(e)

    # -------------------------- ↓

    # 右键菜单

    def __myListWidgetContext(self):
        """右键菜单"""
        handle = self.__handleMenuRequest

        popMenu = QMenu()
        popMenu.addAction(u'delete', lambda: handle(0))
        popMenu.addSeparator()

        popMenu.exec_(QCursor.pos())  # 鼠标位置

    def __handleMenuRequest(self, type:int):
        """

        :param type:
            0: delete;
        :return:
        """
        index = self.currentIndex()
        row = index.row()
        if type == 0:
            self.__removeSelected()

    def __removeSelected(self):
        """
        Public method to remove the selected entries.
        """
        model = self.model()  # type:QAbstractItemModel
        if model is None or self.selectionModel() is None:
            # no models available
            return

        row = 0
        selectedRows = self.selectionModel().selectedRows()
        for selectedRow in reversed(selectedRows):
            row = selectedRow.row()
            colsCount = model.columnCount()
            cope_data_list = []
            emit_dict = {"data":cope_data_list}
            #
            for col in range(colsCount):
                # 小注释 : 需要删除掉的索引
                index = model.index(row, col) #type:QModelIndex
                data = index.data()
                print(f"id{index}-{data}")
                # 小注释 : 拷贝旧的索引数据
                copy_data = deepcopy(data)
                cope_data_list.append(copy_data)
            #
            model.removeRow(row, self.rootIndex())
            #
            self.hideRow(row)
            #
            self.REMOVE_SIGNAL.emit(self,emit_dict)
            # self.model().submitAll()
            # self.model_selectRow(row)
            # self.model_selectRow(row-1)
            # self.model_selectRow(row+1)

        # idx = self.model().index(row, 0, self.rootIndex())
        # if not idx.isValid():
        #     idx = self.model().index(row - 1, 0, self.rootIndex())
        # self.selectionModel().select(idx,QItemSelectionModel.SelectCurrent | QItemSelectionModel.Rows)
        # self.setCurrentIndex(idx)

    # -------------------------- ↑
    def model_selectRow(self, row):
        try:
            self.model().selectRow(row)
        except:
            pass
