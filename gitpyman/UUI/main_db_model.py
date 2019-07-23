# coding=utf-8
import datetime
import os
from os.path import join

from sqlalchemy import Column, Integer, String, create_engine, TypeDecorator, event, DateTime, func
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import ForeignKey
import json


class Json(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        return json.loads(value)


# -------------------------- ↓
# 创建对象的基类:
Model = declarative_base()

# @formatter:off ↓
WEBSITE_TABLE_NAME       = "website_info"
USER_TABLE_NAME          = "user_info"
REPOSITORIES_TABLE_NAME  = "repositories_show"
STARS_TABLE_NAME         = "stars_show"
FOLLOWING_TABLE_NAME     = "following_show"
WATCHING_TABLE_NAME      = "watching_show"
ORGANIZATIONS_TABLE_NAME = "organizations_show"

# @formatter:on  ↑
# -------------------------- ↑


class WebSiteTable(Model):
    __tablename__ = WEBSITE_TABLE_NAME
    # 表的字段
    id = Column(Integer, autoincrement=True, primary_key=True)
    url = Column(String(300), unique=True, nullable=False)
    # DATA = Column(Json(5000))


class UserTable(Model):
    __tablename__ = USER_TABLE_NAME
    # 表的字段
    # id = Column(Integer, autoincrement=True, primary_key=True, )
    url_id = Column(Integer, ForeignKey('website_info.id'), primary_key=True, )
    webs = relationship('WebSiteTable', backref=backref('urls'))  # 反向引用backref  找到该作者做的所有文章
    uname = Column(String(50), unique=False, nullable=False, primary_key=True, )
    upwd = Column(String(50), nullable=False)
    tasks = Column(Json(50000))


class BaseComment(Model):
    __abstract__ = True

    @declared_attr
    def uname(cls):
        return Column(String(50), ForeignKey('user_info.uname'), primary_key=True, )

    query_field = Column(String(350), nullable=False, primary_key=True)
    comment = Column(String(350), nullable=True)


class RepositoriesTable(BaseComment):
    __tablename__ = REPOSITORIES_TABLE_NAME


class StarsTable(BaseComment):
    __tablename__ = STARS_TABLE_NAME


class FollowingTable(BaseComment):
    __tablename__ = FOLLOWING_TABLE_NAME


class WatchingTable(BaseComment):
    __tablename__ = WATCHING_TABLE_NAME


class OrganizationsTable(BaseComment):
    __tablename__ = ORGANIZATIONS_TABLE_NAME


def getTable(tableName: str):
    try:
        TableClass = tableName.split("_")[0].capitalize()
        return globals()[TableClass + "Table"]
    except Exception as e:
        print("getTable Error", e)
        return None


# -------------------------- ↓
db_path = join(os.getcwd(), 'database.db')
engine_path = "sqlite:///" + db_path

engine = create_engine(engine_path, )


# -------------------------- ↑


class SqlalchemyDBControl:
    def __init__(self, parent=None):
        super().__init__()
        self.db_path = db_path
        self.engine = engine
        self.con = self.engine.connect()
        event.listen(self.engine, "do_execute", self.__do_execute)
        #

    def create_session(self):
        # 创建session对象:
        db_session = sessionmaker(bind=self.engine)
        self.db_session = db_session()
        return self.db_session

    # @event.listen(engine, "do_execute")
    def __do_execute(self, cursor, statement, parameters, context, **kw):
        """

        :param kw: cursor, statement, parameters, context
        :return:
        """
        # conn.info.setdefault('query_start_time', []).append(time.time())
        # print(cursor.mogrify(statement, parameters))
        pre_suffix = statement.split(" ")[0]

        if pre_suffix == "PRAGMA":
            pass
        else:
            return False  # DEBUG
            print("*" * 8 + "do_execute" + "*" * 8 + "↓", )
            print(statement.replace('?', r"%r") % parameters)
            print("*" * 8 + "do_execute" + "*" * 8 + "↑")

        return False

    def create_table(self, sync_tables=None):
        if isinstance(sync_tables,list):
            for org in sync_tables:
                # 创建类,
                new_table = type(org, (BaseComment,), {
                    "__tablename__": org
                })
            print(Model.metadata.tables.keys())

        # -------------------------- ↑

        Model.metadata.create_all(self.engine)  # 创建表结构
