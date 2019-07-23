# coding=utf-8

import json
from pprint import pprint as _print
from PyQt5.QtCore import pyqtSlot, QObject, Qt
from PyQt5.QtSql import (QSqlDatabase, QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel, QSqlQuery,
                         QSqlRelation,
                         QSqlRelationalDelegate
                         )
from PyQt5.QtWidgets import QDataWidgetMapper, QMessageBox, QTableView, QHBoxLayout, QWidget, QTabBar
from sqlalchemy import or_, and_

from sqlalchemy.sql import select
from sqlalchemy.dialects import sqlite

from UUI.Base_TableView import QQTableView
from UUI.Base_TableView_Delegate import URLDelegate
from UUI.main_db_control_util1 import DB_Util1
from UUI.main_db_model import (SqlalchemyDBControl, UserTable, WebSiteTable, USER_TABLE_NAME, WEBSITE_TABLE_NAME,
                               REPOSITORIES_TABLE_NAME, STARS_TABLE_NAME, FOLLOWING_TABLE_NAME,
                               WatchingTable,
                               WATCHING_TABLE_NAME,
                               getTable,
                               BaseComment
                               )
from util import github


# from gitpyman.UUI.main_db_model import sync_create_orgs_table


class DBControl(QObject, SqlalchemyDBControl, DB_Util1):
    def __init__(self, parent=None):
        super().__init__()

        import Client

        self.mw: Client.MainWindow = parent

        self.__initDB()
        self.__initUI()

    def __initDB(self):
        self._initDB()
        self._createDB()
        self._createModel()
        self._selectModel()

    # <editor-fold desc="qtdb">
    def _initDB(self):
        self.orm_db = self.create_session()
        self.qt_db = QSqlDatabase.addDatabase('QSQLITE')
        self.qt_db.setDatabaseName(self.db_path)
        if not self.qt_db.open():
            print("数据库连接失败")
            return False

        return self.qt_db

    def _createDB(self):
        self.create_table()
        print(self.qt_db.database().tables())

    def _createModel(self):
        def createModel(tbName):
            model = QSqlTableModel()
            # model.setEditStrategy(QSqlTableModel.OnFieldChange)
            model.setTable(tbName)
            model.select()
            setattr(self, tbName + "_model", model)  # here will create [self.watching_show_model ... ] and other model
            return model

        def createView(title, model, delegate=None):
            view = QQTableView(self.mw)
            view.setModel(model)
            view.setItemDelegateForColumn(0, delegate) if delegate is not None else None
            view.REMOVE_SIGNAL.connect(self.del_watching)
            return view

        def createTab(title):
            tab_form = self.mw.repo_tabWidget
            new_tab = QWidget()
            layout = QHBoxLayout(new_tab)
            layout.setContentsMargins(1,1,1,1)
            tab_form.addTab(new_tab, title)
            return layout

        def createItem(title):
            comb = self.mw.filter_cb

            comb.addItem(title)

        tables = self.qt_db.database().tables()
        for tableName in tables:
            if tableName[-4:] == "show":
                # print(tableName)
                model = createModel(tableName)
                delegate = URLDelegate(self)
                view_ = createView(tableName, model, delegate)
                new_tab = createTab(tableName)
                _ = createItem(tableName)
                new_tab.addWidget(view_)
        # modeln
        self.filterModel = QSqlTableModel()
        # model1
        self.urlTableModel = QSqlTableModel()
        self.urlTableModel.setTable(WEBSITE_TABLE_NAME)
        # model2
        self.unameTableModel = QSqlTableModel()
        self.unameTableModel.setTable(USER_TABLE_NAME) if isinstance(self.unameTableModel, QSqlTableModel) else None
        # model3
        self.upwdQueryModel = QSqlQueryModel(self)

        """

        ###self.url_mapper = QDataWidgetMapper()  # 数据映射
        ###self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit) # 提交策略
        ###self.url_mapper.setModel(self.urlQueryModel)  # 映射的模型源
        ###self.url_mapper.addMapping(self.mw.web_site_cb,0, b"currentIndex")
        ###self.mw.web_site_cb.setModel(self.urlQueryModel)


        # model4
        self.realationModel = QSqlRelationalTableModel(self)
        self.realationModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.realationModel.setTable(REPOSITORIES_TABLE_NAME)
        self.realationModel.setRelation(1, QSqlRelation(WEBSITE_TABLE_NAME, 'id', 'url'))
        # TW_TITLE = [""]
        # for i in range(len(TW_TITLE)):
        #     self.realationModel.setHeaderData(i + 1, Qt.Horizontal, TW_TITLE[i])

        self.realationModel.select()
        """

    def _selectModel(self):

        # <editor-fold desc="1">
        self.mw.web_site_cb.setModel(self.urlTableModel)

        # self.mw.web_user_cb.setModelColumn(1)
        # </editor-fold>

        # <editor-fold desc="2">
        self.mw.web_user_cb.setModel(self.unameTableModel)
        self.mw.web_user_cb.setModelColumn(1)
        # </editor-fold>

        # <editor-fold desc="3">
        self.upwd_mapper = QDataWidgetMapper()  # 数据映射
        self.upwd_mapper.setModel(self.upwdQueryModel)  # 映射的模型源
        self.upwd_mapper.addMapping(self.mw.web_pwd_le, 0)
        ## self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit) # 提交策略
        # </editor-fold>

        # <editor-fold desc="4">
        self.mw.filter_tv.setModel(self.filterModel)
        self.mw.filter_tv.setItemDelegateForColumn(0,URLDelegate())
        # </editor-fold>

    # </editor-fold>

    def __initUI(self):
        self._pre_url_ = "---"
        self._pre_uname_ = "---"

        # 1 .
        self.mw.web_site_cb.activated.connect(self.on_web_uname_query)
        self.mw.web_user_cb.activated.connect(self.on_web_upwd_query)

    def on_web_site_url_query(self):
        print("查网址")
        # self.urlTableModel.setQuery(QSqlQuery(self.ORM2SQL(select([WebSite.url]))))
        self.reloadTableModel(self.urlTableModel, False)
        self.mw.web_site_cb.setModelColumn(1)
        # 如果没有item, setCurrentIndex(0) #qtbug 是不起作用的, index还是-1
        self.mw.web_site_cb.setCurrentIndex(0)
        self.on_web_uname_query()

    def on_web_uname_query(self, index=None):
        """
        网址索引改变的时候触发.
        :return:
        """

        print("查用户")
        c_url = self.get_c_url()
        curl_id = self.get_curl_id(c_url)

        self.mw.web_pwd_le.setText("")
        # 有结果
        if curl_id is not None:
            print("查到用户")
            self.unameTableModel.setFilter(f"""user_info.url_id = {curl_id}""")
            self.reloadTableModel(self.unameTableModel)

            self.mw.web_user_cb.setCurrentIndex(0)
            self.on_web_upwd_query()
        # else:

    def on_web_upwd_query(self):
        print("查密码")
        c_url, c_uname, c_upwd, curl_id = self.get_c_all()

        self.upwdQueryModel.setQuery(QSqlQuery(
            self.ORM2SQL(
                select([UserTable.upwd])
                    .where(and_(UserTable.url_id == curl_id, UserTable.uname == c_uname))
            )
        ))
        # 设置密码UI
        self.upwd_mapper.toFirst()

        # loadtask

        self._set_pre_cb_text(c_url, c_uname)

    # -------------user------------- ↓
    def create_or_update_webInfo(self):
        c_url, c_uname, c_upwd, curl_id = self.get_c_all()
        if curl_id is None:
            model = self.urlTableModel

            row = model.rowCount()
            ret = model.insertRows(row, 1)
            print('insertRows=%s' % str(ret), model.columnCount())
            record_count = model.record().count()
            print(record_count)
            for col in range(model.columnCount()):
                index = model.index(row, col)
                # record = model.record(row)
                # field = record.field(col)
                field_col = self.urlTableModel.fieldIndex("url")
                if col == field_col:
                    model.setData(index, c_url)
            self.urlTableModel.submit()
            self.mw.web_site_cb.setModelColumn(1)
            # self.urlTableModel.select() # qt bug
            # web_obj = WebSite(url=c_url)
            # self.orm_db.add(web_obj)
            # self.orm_db.flush()
            # curl_id = web_obj.id

            curl_id = model.index(row, 0).data()
        # 法一: 双主键,  有则更新 , 无则创建
        # self.orm_db.merge(User(uname=c_uname, upwd=c_upwd, url_id=curl_id))
        # self.orm_db.commit()
        # 改变索引
        # self.reloadTableModel(self.urlTableModel)
        # self.reloadTableModel(self.unameTableModel)

        ## 法二
        model = self.unameTableModel
        row = model.rowCount()
        ret = model.insertRows(row, 1)
        print('insertRows=%s' % str(ret), model.columnCount())
        for col in range(model.columnCount()):
            index = model.index(row, col)

            if col == 0:
                model.setData(index, curl_id)
            elif col == 1:
                model.setData(index, c_uname)
            elif col == 2:
                model.setData(index, c_upwd)
            elif col == 3:
                model.setData(index, "{}")

        self.unameTableModel.submitAll()

    def delete_webInfo(self):
        """

        :return:
        """

        c_url, c_uname, c_upwd, curl_id = self.get_c_all()
        # 找到网址
        if curl_id is not None:
            # 删网址
            if c_uname == '' and c_upwd == '':
                obj = self.orm_db.query(WebSiteTable).filter_by(url=c_url).one()
                self.orm_db.delete(obj)
                self.orm_db.commit()
                self.on_web_site_url_query()

            # 删账户
            else:
                try:
                    obj = self.orm_db.query(UserTable).filter_by(uname=c_uname, upwd=c_upwd, url_id=curl_id).one()
                    self.orm_db.delete(obj)
                    self.orm_db.commit()
                    self.mw.web_pwd_le.setText("")
                    self.reloadTableModel(self.unameTableModel, False)

                    # self.mw.web_user_cb.setCurrentIndex(0)
                except:
                    pass

    # -------------user------------- ↑

    # -------------table query------------- ↓
    def get_watching(self):
        # try:
        WatchIterator = github.get_watching(self)
        self.mw.thread_pools.spawn(self.get_watching_querydb, WatchIterator)

    def get_watching_querydb(self, WatchIterator):
        for watched_repo in WatchIterator:
            query_field = "/" + watched_repo.full_name
            WatchingTable_obj: WatchingTable = self.orm_db.query(WatchingTable).filter_by(
                query_field=query_field).first()
            if WatchingTable_obj is None:
                uname = self.get_c_uname()
                self.orm_db.add(WatchingTable(query_field=query_field, uname=uname))
                self.orm_db.commit()
                model: QSqlTableModel = self.watching_show_model
                model.select()  # TODO:重新载入, 可能可以改成局部刷新.
            else:
                pass

    def del_watching(self, tv, data_dict):
        data = data_dict.get("data")  # type:list
        del_watching_repo = data[0]
        print(f"{del_watching_repo}")
        print(self.get_c_tableName())
        if self.get_c_tableName() == WATCHING_TABLE_NAME:
            print(f"delete")
            github.del_watching(del_watching_repo)
        else:
            pass

    # TODO:查数据库 ,可能用协程

    def re_select_model(self):
        model = self.get_c_model()
        model.select()

    def filterAll(self):
        """
        过滤
        :return:
        """
        query_fields = self.mw.filter_le.text().strip()  # 小注释 : e.g."py test "
        query_field_list = query_fields.split(" ")  # 小注释 : space split
        tableName = self.mw.filter_cb.currentText()

        # 小注释 : 单表
        if tableName != "All":
            TableClass = getTable(tableName)  ##type:BaseComment
            self.filterModel.setQuery(QSqlQuery(
                self.ORM2SQL(
                    select([TableClass])
                        .where(
                        or_(
                            *tuple(
                                map(lambda query_field: TableClass.comment.like(f'%{query_field}%'),
                                    query_field_list)
                            )
                            # 小注释 :
                            # TableClass.comment.like(f'%{query_field_list[0]}%'),
                            # TableClass.comment.like(f'%{query_field_list[1]}%'),
                            # TableClass.comment.like(f'%{query_field_list[2]}%'),
                        )
                    )
                )
            ))
        # 小注释 : 多表 union
        else:
            tw = self.mw.repo_tabWidget
            tabCount = tw.count()
            end = tabCount - 1
            sql =""
            for i in range(tabCount):
                tableName = tw.tabText(i)
                condition = " OR ".join(list(map(lambda query_field:f"""{tableName}.comment LIKE '%{query_field}%' """,query_field_list)))
                sql += f"""SELECT * From {tableName} WHERE {condition}"""
                if i != end:
                    sql+=" UNION ALL " if self.mw.filter_ckBox.isChecked() else " UNION "
            # print(sql)
            self.filterModel.setQuery(QSqlQuery(sql))

    # -------------table query------------- ↑

    def ORM2SQL(self, statement):
        """

        :param statement:
        :return:
        """
        query = statement.compile(dialect=sqlite.dialect())
        query_str = str(query)
        query_paras: dict = query.params
        query_raw_sql = query_str.replace('?', r"%r") % tuple(query_paras.values())
        # print("==query_raw_sql==↓:")
        # print(query_raw_sql)
        # print("==query_raw_sql==↑:")
        return query_raw_sql
