# coding=utf-8
# <editor-fold desc="js">
# @formatter:off ↓
## https://www.sojson.com/js.html
## https://www.css-js.com/
import os
from urllib.parse import urlparse
from xml.etree.ElementTree import Element
from PyQt5.QtGui import QContextMenuEvent, QDesktopServices
from PyQt5.QtWidgets import QMenu
from lxml import etree
from sqlalchemy.orm import sessionmaker

from UUI.main_db_model import (FOLLOWING_TABLE_NAME, STARS_TABLE_NAME, REPOSITORIES_TABLE_NAME, StarsTable,
                               RepositoriesTable,
                               FollowingTable,
                               BaseComment,
                               OrganizationsTable
                               )



# @formatter:on  ↑
# </editor-fold>

import json
from PyQt5.QtCore import QUrl, QByteArray, QFile, QIODevice, QTimer, QEventLoop, QPoint, QLocale
from PyQt5.QtNetwork import QNetworkCookie
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor, QWebEngineUrlRequestInfo

from util import BasePara
from util.Task import JF
from util import github
# from gitpyman.util import github # 吗的 bug了
import res_rc


class MyEngineView(QWebEngineView):
    DomainCookies = {}  # 存放domain的key-value
    PathCookies = {}  # 存放domain+path的key-value

    def __init__(self, parent=None):

        super().__init__(parent)
        self.__initUI()
        self.__initSignals()
        self.__initCookies()

    def __initUI(self):
        self._page = MyEnginePage(self.parent())
        self.setPage(self._page)
        #

        # self.__menu = QMenu(self)
        #
        self.hover_url = ''
        #
        self._channel_script = self.qt_readJS(':/Data/qwebchannel.js')
        self._jquery_script = self.qt_readJS(':/Data/jquery-3.3.1.min.js')
        self._web_script = self.readJS("Data/run_in_web.js")
        # 存储每次页面的 query_field
        self.query_field_list = []

    def __initSignals(self):
        self.page().loadFinished.connect(self.onLoadFinished)
        # replace createWindow

        self.page().linkHovered.connect(lambda url: setattr(self, 'hover_url', QUrl(url)))
        self.page().linkHovered.connect(lambda url: self.mw.statusBar().showMessage(url))
        ## https://www.sojson.com/js.html

    def __initCookies(self):
        # cookies
        webEngineProfile = QWebEngineProfile.defaultProfile()
        cookieStore = webEngineProfile.cookieStore()
        COOKIPATH = "./Cache"
        # if not os.path.exists(COOKIPATH):
        #     os.mkdir(COOKIPATH)
        webEngineProfile.setCachePath(COOKIPATH)
        webEngineProfile.setPersistentStoragePath(COOKIPATH)
        webEngineProfile.setPersistentCookiesPolicy(2)
        self.loadAllCookie()
        cookieStore.cookieAdded.connect(self.onCookieAdd)
        print(f"{webEngineProfile.persistentStoragePath(), webEngineProfile.persistentCookiesPolicy()}")
        # cookieStore.deleteAllCookies()
        # self.loadFinished.connect(self.onLoadFinished)

    # --------------------------

    def onLoadFinished(self):
        self.query_field_list = []
        self.onInjectStart()
        self.onSolveWeb()

    def onInjectStart(self):
        """

        :return:
        """
        # 绑定cookie被添加的信号槽

        page = self.page()

        page.runJavaScript(self._channel_script, )
        page.runJavaScript(self._jquery_script, )
        page.runJavaScript(self._web_script, )
        # if DEBUG:
        #     page.runJavaScript('console.log("注入 js 完成")', )
        #     page.runJavaScript('console.log(document.title)', )
        #     page.runJavaScript('console.log(this)', )

        page.runJavaScript(JF.initBridget())
        print("载入完成")
        page.runJavaScript(JF.removeAD())
        # DB = BasePara.mw.DB
        # uname, upwd, url = DB.get_c_uname(), DB.get_c_upwd(), DB.get_c_url()
        # page.runJavaScript(JF.login(uname, upwd))

    def onSolveWeb(self):

        self.page().toHtml(self.__do_paras_html)

    # import snoop
    # #snoop.install(out="snoop.log")
    # @snoop.snoop(depth=4)
    def __do_paras_html(self, qthtml):
        url = self.url().url()
        ParseResult = urlparse(url)
        querys = ParseResult.query
        if "tab=repositories" in querys:
            TYPE = 0
            QUERY_TABLE = RepositoriesTable

        elif "tab=stars" in querys:
            TYPE = 10
            QUERY_TABLE = StarsTable
        elif "tab=following" in querys:
            TYPE = 20
            QUERY_TABLE = FollowingTable
        elif len([org for org in github.get_organizations() if org in url]):
            TYPE = 30
            QUERY_TABLE = OrganizationsTable
        else:
            TYPE = -1
            QUERY_TABLE = ""
        if QUERY_TABLE != "":

            html = etree.HTML(qthtml)
            if TYPE == 0:
                dom_list = html.xpath('//*[@id="user-repositories-list"]/ul/li//h3/a')
            elif TYPE == 10:
                dom_list = html.xpath('//*[@id="js-pjax-container"]/div//h3/a')
            elif TYPE == 20:
                dom_list = html.xpath('// *[ @ id = "js-pjax-container"]/div//a/span[2]')
            elif TYPE == 30:
                dom_list = html.xpath('//*[@id="org-repositories"]/div[1]/div/ul//h3/a')
            else:
                dom_list = []

            for index, dom in enumerate(dom_list):  # type:int,Element
                # attrs: dict = dom.attrib
                if TYPE != 20:
                    query_field = dom.get("href")
                else:
                    query_field = dom.text
                # print(f"{TYPE},",dom.attrib,query_field)
                self.query_field_list.append(query_field)
                # 1.查数据库
                comment_obj = self.mw.DB.orm_db.query(QUERY_TABLE).filter_by(query_field=query_field).first()
                # comment_obj = None
                # 2.生成dom元素->赋值->监听
                if comment_obj:
                    comment = comment_obj.comment
                else:
                    comment = ""
                self.page().runJavaScript(JF.addDom_TextArea(TYPE, index, comment))

    def merge_comment(self, index, new_comment):
        url = self.url().url()
        ParseResult = urlparse(url)
        querys = ParseResult.query
        query_field = self.query_field_list[index]
        uname = self.mw.web_user_cb.currentText()
        if "tab=repositories" in querys:
            TABLE = RepositoriesTable
        elif "tab=stars" in querys:
            TABLE = StarsTable
        elif "tab=following" in querys:
            TABLE = FollowingTable
        elif len([org for org in github.get_organizations() if org in url]):
            TABLE = OrganizationsTable
        else:
            TABLE = ""
        if TABLE != "":  # type:BaseComment
            self.mw.DB.orm_db.merge(TABLE(uname=uname, query_field=query_field, comment=new_comment))
            self.mw.DB.orm_db.commit()

        print(f"{index}-{self.query_field_list[index]}")
        print(f"{new_comment}-")
        pass

    def reInject(self):
        page = self.page()
        try:
            self._web_script = self.readJS('Data/run_in_web.js')
            page.runJavaScript(self._web_script, lambda x: print('重载完成:', x))
        except:
            print(f"重载失败")

    def createWindow(self, type):
        """
        实现点击跳转链接。
        :param type:
        :return:
        """
        self.load(self.hover_url)
        # return self

    def readJS(self, path):

        with open(path, 'rb') as f:
            return f.read().decode()

    def qt_readJS(self, path):
        file = QFile(path)

        file.open(QIODevice.ReadOnly)
        txt = file.readAll().data().decode()

        file.close()
        return txt

    def closeEvent(self, event):

        super().closeEvent(event)

    # -------------------------- ↓

    # -------------------------- ↑

    def bytes2str(self, data):
        if isinstance(data, str):
            data = data
        elif isinstance(data, QByteArray):
            data = data.data()
        elif isinstance(data, bytes):
            data = data.decode(errors='ignore')
        else:
            data = str(data)
        return data

    def getAllDomainCookies(self):

        return json.dumps(self.DomainCookies, indent=4)

    def getDomainCookies(self, domain):
        return json.dumps(self.DomainCookies.get(domain, {}), indent=4)

    def getAllPathCookies(self):
        return json.dumps(self.PathCookies, indent=4)

    def getPathCookies(self, dpath):
        return json.dumps(self.PathCookies.get(dpath, {}), indent=4)

    def onCookieAdd(self, cookie: QNetworkCookie):
        """

        :param cookie: QNetworkCookie
        """
        domain = cookie.domain()  # '.hf666.net'
        path = cookie.path()  # '/'
        name = self.bytes2str(cookie.name().data())  # QByteArray-> (char)bytes
        value = self.bytes2str(cookie.value().data())
        self.DomainCookies[name] = value
        # if domain in self.DomainCookies:
        #     _cookie = self.DomainCookies[domain]
        #     _cookie[name] = value
        # else:
        #     self.DomainCookies[domain] = {
        #         name: value
        #     }
        # # -------------------------- ↓
        #
        # # -------------------------- ↑

        domain_path = domain + path
        if domain_path in self.PathCookies:
            _cookie = self.PathCookies[domain_path]
            _cookie[name] = value
        else:
            self.PathCookies[domain_path] = {
                name: value
            }
        # -------------------------- ↓

        # -------------------------- ↑

        # if domain in self.DomainCookies:
        #     _cookie = self.DomainCookies[domain]
        #     _cookie[name] = value
        # else:
        #     self.DomainCookies[domain] = {
        #         name: value
        #     }
        # # # -------------------------- ↓
        # #
        # # # -------------------------- ↑
        #
        # domain_path = domain + path
        # if domain_path in self.PathCookies:
        #     _cookie = self.PathCookies[domain_path]
        #     _cookie[name] = value
        # else:
        #     self.PathCookies[domain_path] = {
        #         name: value
        #     }

    def loadAllCookie(self):
        print("load all")
        webEngineProfile = QWebEngineProfile.defaultProfile()

        print(f"{webEngineProfile.persistentStoragePath(), webEngineProfile.persistentCookiesPolicy()}")

        QWebEngineProfile.defaultProfile().cookieStore().loadAllCookies()

    # -------------------------- ↓

    # -------------------------- ↑
    def contextMenuEvent(self, evt):
        """
        Protected method called to create a context menu.

        This method is overridden from QWebEngineView.

        @param evt reference to the context menu event object
            (QContextMenuEvent)
        """
        self.__menu = self.page().createStandardContextMenu()
        pos = evt.pos()
        reason = evt.reason()
        QTimer.singleShot(
            0,
            lambda: self._contextMenuEvent(QContextMenuEvent(reason, pos)))
        # needs to be done this way because contextMenuEvent is blocking
        # the main loop

    def _contextMenuEvent(self, evt):
        """
        Protected method called to create a context menu.

        This method is overridden from QWebEngineView.

        @param evt reference to the context menu event object
            (QContextMenuEvent)
        """

        self.__createPageContextMenu(self.__menu)

        if not self.__menu.isEmpty():
            pos = evt.globalPos()
            self.__menu.popup(QPoint(pos.x(), pos.y() + 1))

    def __createPageContextMenu(self, menu):
        """
        Private method to populate the basic context menu.

        @param menu reference to the menu to be populated
        @type QMenu
        """
        ##
        menu.addSeparator()
        menu.addAction(
            self.tr("Open native web"),
            lambda: QDesktopServices.openUrl(self.url())
        )
        ##
        language = QLocale.system().name()
        if not language:
            languages = []
        else:
            languages = MyEngineView.expand(QLocale(language).language())
        if languages:
            menu.addSeparator()
            language = languages[0]
            langCode = language.split("[")[1][:2]
            googleTranslatorUrl = QUrl.fromEncoded(
                b"http://translate.google.com/translate?sl=auto&tl=" +
                langCode.encode() +
                b"&u=" +
                QUrl.toPercentEncoding(bytes(self.url().toEncoded()).decode()))
            menu.addAction(
                self.tr("Google Translate"),
                lambda :self.load(googleTranslatorUrl)
                           )#TODO: maybe has google bug blank.

    @classmethod
    def expand(cls, language):
        """
        Class method to expand a language enum to a readable languages
        list.

        @param language language number (QLocale.Language)
        @return list of expanded language names (list of strings)
        """
        allLanguages = []
        countries = [l.country() for l in QLocale.matchingLocales(
            language, QLocale.AnyScript, QLocale.AnyCountry)]
        languageString = "{0} [{1}]" \
            .format(QLocale.languageToString(language),
                    QLocale(language).name().split('_')[0])
        allLanguages.append(languageString)
        for country in countries:
            languageString = "{0}/{1} [{2}]" \
                .format(QLocale.languageToString(language),
                        QLocale.countryToString(country),
                        '-'.join(QLocale(language, country).name()
                                 .split('_')).lower())
            if languageString not in allLanguages:
                allLanguages.append(languageString)

        return allLanguages
    # -------------------------- ↓

    # -------------------------- ↑
    @property
    def orm_db(self):

        return self.mw.DB.orm_db

    @property
    def mw(self):
        from util.BasePara import mw
        return mw


class MyEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        if level != 1:
            print('jsconsole=>:', f'leavel:{level} - {message}')
            if level == 2:
                if "$ is not defined" in message:
                    BasePara.Signals.debug_zjxx_signal.emit(["$ is not defined", ])
                    BasePara.mw.wycz_tab__wid.reload_button.activate(0)

            return QWebEnginePage.javaScriptConsoleMessage(self, level, message, lineNumber, sourceID)

    def runJavaScript(self, p_str, *__args):

        # print('JSFUNC==>:', p_str) if DEBUG else None
        return super().runJavaScript(p_str, *__args)

    def _runJavaScriptSync(self, js, timeout=500):
        """
        同步执行 , 不能与 qwebchannel一起使用
        :param js:
        :param timeout:
        :return:
        """
        result = None
        eventLoop = QEventLoop()
        called = False
        page = self

        def callback(val):
            nonlocal result, called
            result = val
            called = True
            eventLoop.quit()

        page.runJavaScript(js, callback)

        if not called:
            timer = QTimer()
            timer.setSingleShot(True)
            timer.timeout.connect(eventLoop.quit)
            timer.start(timeout)
            eventLoop.exec_()

        if not called:
            print('runJavaScriptSync() timed out')
        return result

    def acceptNavigationRequest(self, request, type, isMainFrame):
        # from pprint import pprint as _print
        # print(f"{request.url()}, {type}, {isMainFrame}")

        # print("frame:", [type, isMainFrame])
        # 自动登录
        # if self.parent().isLoginPage(isMainFrame, request.url()):
        #     self.parent().autoAgree()
        return super().acceptNavigationRequest(request, type, isMainFrame)

    def javaScriptConfirm(self, url, msg):
        try:
            BasePara.mw.statusBar().showMessage(msg)
        except:
            pass
        return True

    def javaScriptAlert(self, url, msg):

        BasePara.mw.statusBar().showMessage(msg)
        #
        #     print("alert:",msg)
        pass


class MyWebEngineUrlRequest(QWebEngineUrlRequestInterceptor):
    """拦截url"""

    def interceptRequest(self, info: QWebEngineUrlRequestInfo):
        # info.setHttpHeader("X-Frame-Options", "ALLOWALL")
        # print("interceptRequest")
        # print(info.requestUrl())
        url = info.requestUrl().url()
        r_type = info.resourceType()
        method = info.requestMethod()
        # vue hot-date
        # 拦截-http://127.0.0.1:8080/1.61bd9f235d8f0f9b1cbf.hot-update.js b'GET' 3
        print(f"拦截-{url}-{method}-{r_type}")
        # if r_type in [2, 3, 4, 5, 12]:
        #     pass
        # elif r_type == 13:
        #     if "getUserCash" in url:
        #         pass
        #     else:
        #         print(url, method, r_type)
        # else:
        #     print(url, method, r_type, )
        #     pass
