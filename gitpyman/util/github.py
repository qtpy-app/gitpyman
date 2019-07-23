from pprint import pprint

import requests
import json
from github3 import login

# from github3.decorators import (
# #     requires_auth,
# #     requires_basic_auth,
# #     requires_app_credentials
# # )
from util.BasePara import Signals

headers = {
    'Connection'               : 'keep-alive',
    'Cache-Control'            : 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent'               : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Accept'                   : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding'          : 'gzip, deflate, br',
    'Accept-Language'          : 'zh-CN,zh;q=0.9',
    'If-None-Match'            : 'W/"c59fd8a30c13e5524e4fb6bc0cbd3103"',
}

global me
global organizations


# pprint(globals().keys())
def requires_auth(func, *args, **kwargs):
    def do(*args, **kwargs):
        # print(globals(), "me" is globals(),"me" is globals().keys())
        if 'me' in globals():
            return func(*args, **kwargs)
        else:
            Signals.show_error_msg_signal.emit("Requires authentication")
            return []

    return do


def login2github(uname, upwd):
    gh = login(uname, upwd)

    global me
    me = gh.me()
    me.uname = uname
    me.upwd = upwd

    Signals.show_state_msg_signal.emit("login success", 3000)

    #
    get_orgs_and_set()


def get_me():
    return globals()["me"]


@requires_auth
def get_watching(*a, **kw):
    #
    # response = requests.get(
    #     f'https://api.github.com/users/{login_name}/subscriptions',
    #     headers=headers,
    #
    # )
    # print(response.status_code)
    # return response
    me = get_me()
    # login_name = me.login
    # list(me.subscriptions())
    # print(me, login_name, list(me.subscriptions()),me.subscriptions())
    WatchIterator = me.subscriptions()
    return WatchIterator


@requires_auth
def del_watching(full_name):
    me = get_me()
    api_url = 'https://api.github.com/user/subscriptions' + full_name
    print(api_url)
    response = requests.delete(api_url,headers=headers, auth=(me.uname, me.upwd))
    # print(response)


# -------------------------- ↓

@requires_auth
def get_orgs_and_set() -> list:
    me = get_me()
    # orgs_iter = me.organizations()
    api_url = 'https://api.github.com/user/orgs'

    res =   requests.get(api_url,headers=headers, auth=(me.uname, me.upwd))

    global organizations
    # orgs = []
    # for org in orgs_iter:
    #     orgs.append(orgs_iter.login)
    if res.status_code==200:
        res_list = json.loads(res.content.decode())
        orgs = list(map(lambda res_list_oneDict:res_list_oneDict.get('login'),res_list))
        organizations = orgs
    # print("set organizations:",globals().get("organizations",'没有'))
    return organizations



def get_organizations() -> list:

    return globals().get("organizations",[])
