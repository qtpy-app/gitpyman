"use strict";

error;

// https://www.css-js.com/
/**
 * @return {number}
 */
function TIMEOUTE_TIMES(num = 8) {
    return num
}

function test() {
    window.Bridge.topy_callFromJs('123')
}


/*webShareObj 连接*/
function initBridge() {
    new QWebChannel(qt.webChannelTransport, function (channel) {
        // Bridge是QT对象
        window.Bridge = channel.objects.Bridge;

        // // 这里绑定窗口的标题变化信号（这个信号是由QWidget内部的）
        // Bridge.windowTitleChanged.connect(function (title) {
        //     showLog("标题被修改为：" + title);
        // });
        //
        // // 绑定自定义的信号customSignal
        // Bridge.customSignal.connect(function (text) {
        //     showLog("收到自定义信号内容：" + text);
        // });
    });

}



//<editor-fold desc="登录处理">
function login(uname, upwd) {
    console.log("执行登录");
    clearInterval(window.login_interval);

    let login_timer = window.login_interval = setInterval(() => {


        let user_input = $("input#login_field");
        let pwd_input  = $("input#password");
        let login_btn  = $("input[name='commit']");
        console.log(user_input, pwd_input, login_btn);
        if (login_btn.length === 1) {
            user_input.val(uname);
            pwd_input.val(upwd);
            login_btn.click();
            // setTimeout(autoAgree, 1500);
            clearInterval(login_timer)
        }
        // else {
        //     window.Bridge.topy_callFromJs("登录失败");
        // }
    }, 1000)


}


/*去除大厅广告*/
function removeAD() {
    let timer_id = setInterval(() => {
        try {
            $(".unsupported-browser").remove();
            $(".ad_float_SA").remove()
        } catch (e) {
        }
    }, 1500)

}

//</editor-fold>


function addDom_TextArea(TYPE, index, comment) {
    if (TYPE === 0) {
        addDom_TextArea_repositories(index, comment)
    }
    else if (TYPE === 10) {
        adddom_Textarea_stars(index, comment)
    }
    else if (TYPE === 20) {
        addDom_TextArea_following(index, comment)
    }
    else if (TYPE===30) {
        addDom_TextArea_Organizations(index,comment)
    }
}

function addDom_TextArea_repositories(index, comment) {
    let li         = $("#user-repositories-list ul").children()[index];
    let before_dom = $(li).find(">:eq(0)")
    before_dom.after("<div><textarea></textarea></div>");
    let dom_textxarea = $(before_dom).next();
    $(dom_textxarea).find("textarea").val(comment);
    // $(dom_textxarea)[0].val("hhh");
    // $(dom_textxarea).change();
    $(dom_textxarea)[0].pyindex = index;
    on_TextArea_Change(dom_textxarea)
}

function adddom_Textarea_stars(index, comment) {
    let li         = $("#js-pjax-container > div > div.col-lg-9.col-md-8.col-12.float-md-left.pl-md-2 > div.position-relative").children()[0];
    let new_index = 2+index
    let before_dom = $(li).find(`>div>div:nth-child(${new_index})>div.py-1`)
    before_dom.after("<div ><textarea style='width: 100%'></textarea></div>");
    let dom_textxarea = before_dom.next();
    $(dom_textxarea).find("textarea").val(comment);
    // $(dom_textxarea).change();
    $(dom_textxarea)[0].pyindex = index;
    on_TextArea_Change(dom_textxarea)
}

function addDom_TextArea_following(index, comment) {
    let li         = $("#js-pjax-container > div > div.col-lg-9.col-md-8.col-12.float-md-left.pl-md-2 > div.position-relative").children()[index];
    let before_dom = $(li).find(">:eq(1)")
    before_dom.after("<div style='float: right;'><textarea></textarea></div>");
    let dom_textxarea = before_dom.next();
    $(dom_textxarea).find("textarea").val(comment);
    // $(dom_textxarea).change();
    $(dom_textxarea)[0].pyindex = index;
    on_TextArea_Change(dom_textxarea)
}

function addDom_TextArea_Organizations(index, comment) {
    let li         = $("#org-repositories > div.col-8.d-inline-block > div > ul ").children()[index];
    let before_dom = $(li).find(">:eq(0)");
    before_dom.after("<div><textarea></textarea></div>");
    let dom_textxarea = before_dom.next();
    $(dom_textxarea).find("textarea").val(comment);
    // $(dom_textxarea).change();
    $(dom_textxarea)[0].pyindex = index;
    on_TextArea_Change(dom_textxarea)
}

function on_TextArea_Change(dom_textxarea) {
    dom_textxarea.on("change", e => {
        let index       = $(dom_textxarea)[0].pyindex;
        let new_comment = e.target.value;

        window.Bridge.topy_merge_comment(index, new_comment)
        // let textxarea_topDIV = e.target.parentNode.parentNode;
        // console.log($(textxarea_topDIV).find("a"))
        // console.log($(textxarea_topDIV.firstElementChild).find("a"))

        // window.Bridge.topy_eMsg(e.target.value)
    })
}
