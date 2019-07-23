# coding=utf-8
"""
function about
"""
from UUI.main_db_model import (SqlalchemyDBControl, UserTable, WebSiteTable, USER_TABLE_NAME, WEBSITE_TABLE_NAME,
                               REPOSITORIES_TABLE_NAME, STARS_TABLE_NAME, FOLLOWING_TABLE_NAME,
                               )


class DB_Util1:
    def reloadTableModel(self, model, remember=True):
        """
        emit currentIndexChange.
        :param model:
        :param remember:
        :return:
        """
        model.select()
        # if model == self.urlTableModel:
        #     self.mw.web_site_cb.setModelColumn(1)

    # <editor-fold desc="辅助函数">
    def get_c_url(self):

        return self.mw.web_site_cb.currentText()

    def get_c_uname(self):
        return self.mw.web_user_cb.currentText()

    def get_c_upwd(self):
        return self.mw.web_pwd_le.text()

    def get_curl_id(self, c_url):
        curl_id = self.orm_db.query(WebSiteTable).filter_by(url=c_url).first()

        if curl_id:
            return curl_id.id
        else:
            return None

    def get_c_all(self, q_id=True):
        c_url = self.get_c_url()
        c_uname = self.get_c_uname()
        c_upwd = self.get_c_upwd()
        if q_id:
            curl_id = self.get_curl_id(c_url)
        else:
            curl_id = None
        return c_url, c_uname, c_upwd, curl_id

    # </editor-fold>

    def _get_pre_cb_text(self):
        return self._pre_url_, self._pre_uname_

    def _set_pre_cb_text(self, url, uname):

        self._pre_url_ = url
        self._pre_uname_ = uname

    def _is_same_pre(self):
        """
        防止combobox activate的是用一个任务. 相当于 currentIndexChange
        :return:
        """
        _pre_url_, _pre_uname_ = self._get_pre_cb_text()
        _c_url_ = self.mw.web_site_cb.currentText()
        _c_uname_ = self.mw.web_user_cb.currentText()

        if _c_url_ == _pre_url_ and _c_uname_ == _pre_uname_:
            return True
        else:
            return False

    def _restore_pre_text_(self):

        pass

    def get_c_tabName(self) -> str:
        tw = self.mw.repo_tabWidget
        index = tw.currentIndex()
        tabName = tw.tabText(index)
        return tabName

    def get_c_tableName(self) -> str:
        return self.get_c_tabName()

    def get_c_model(self):
        return getattr(self, self.get_c_tabName() + "_model")
#     else:
#         return False
# def on_web_site_cb_query_mousePressEvent(self, e):
#     self.urlTableModel.setQuery(QSqlQuery(self.ORM2SQL(select([WebSite.url]))))
#     self.urlTableModel.select()
#     return QComboBox.mousePressEvent(self.mw.web_site_cb, e)

# self.mw.web_site_cb.activated.connect(self.on_web_site_cb_activated)
# # ================================= codemodel =====================================#

# self.mw.web_site_cb.mouseReleaseEvent = lambda e: [print("e1:", e), print("e2:", e),
# QComboBox.mousePressEvent(self.mw.web_site_cb, e),
# print("444")] and None
# self.mw.web_site_cb.mousePressEvent = self.on_web_site_cb_query_mousePressEvent
# self.mw.web_site_cb.mouseReleaseEvent = lambda e: [print("123"),functools.partial(QComboBox.mousePressEvent,self.mw.web_site_cb,e)]

# -------------------------- ↓
# # model设置表
# self.initializeModel(self.codeModel, 'Mongo')
# # 设置编辑策略
# # self.codeModel.setEditStrategy(QSqlTableModel.OnFieldChange)
# # !!! 这里要注意 , 只能用这个策略 , 才可以实现自动提交
# self.codeModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

# # ================================ pushButton ==================================#
# # self.sub_btn.clicked.connect(self.mapper.submit)
# # self.sub_btn.clicked.connect(self.codeModel.submitAll)
# -------------------------- ↑
