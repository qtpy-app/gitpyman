# coding=utf-8

# <editor-fold desc="rw">



class CALC:
    """计算模块"""
    XH_SEP = "-"  # 选号分隔符
    BS_SEP = "/"  # 倍数分隔符
    SJ1FZ_SEP = ":"  # 1分钟时间


# </editor-fold>
class JF:
    # @formatter:off ↓
    initBridget = lambda: "initBridge()"
    removeAD    = lambda: "removeAD()"
    login       = lambda uname, upwd: f"login({uname!r},{upwd!r})"


    addDom_TextArea = lambda TYPE,index,comment:f"addDom_TextArea({TYPE},{index},{comment!r})"
    # @formatter:on  ↑