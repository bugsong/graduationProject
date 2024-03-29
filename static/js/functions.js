//定义统一的刷新频率
fresh_all_except_time();

function fresh_all_except_time() {
    get_center_top_data();
    get_center_bottom_data();
    get_left_top_data();
    get_left_bottom_data();
    get_right_bottom_data();
    get_right_top_data();

}

setInterval(fresh_all_except_time, 10000)  //每隔多少毫秒刷新一次


//时间更新部分
function get_time() {
    $.ajax({
        url: "/time",
        timeout: 10000,//设置超时时间为10秒
        success: function (data) {
            $("#time").html(data);//以服务器时间为准
        },
        error: function () {
            alert("没拿到后台数据");
        }
    })
}

setInterval(get_time, 1000)

//中间数字部分
function get_center_top_data() {
    $.ajax({
        url: "/center_top",
        success: function (data_json_str) {
            $(".num h1").eq(0).text(data_json_str.confirm);
            $(".num h1").eq(1).text(data_json_str.suspect);
            $(".num h1").eq(2).text(data_json_str.heal);
            $(".num h1").eq(3).text(data_json_str.dead);
        },
        error: function () {
            alert("没拿到后台数据");
        }
    })
}


// 地图数据部分
function get_center_bottom_data() {
    $.ajax({
        url: "/center_bottom",
        success: function (data_json_value) {
            ec_center_bottom_option.series[0].data = data_json_value.data;//从后台拿到数据
            ec_center_bottom_selector.setOption(ec_center_bottom_option);//丢在option里面重新渲染
        },
        error: function () {
            alert("没拿到后台数据");
        }
    })
}

// 偷懒渲染一次即可

//左上部分
function get_left_top_data() {
    $.ajax({
        url: "/left_top",
        success: function (data_json_value) {
            ec_left_top_option.xAxis[0].data = data_json_value.day
            ec_left_top_option.series[0].data = data_json_value.confirm
            ec_left_top_option.series[1].data = data_json_value.suspect
            ec_left_top_option.series[2].data = data_json_value.heal
            ec_left_top_option.series[3].data = data_json_value.dead
            ec_left_top_selector.setOption(ec_left_top_option);//丢在option里面重新渲染
        },
        error: function () {
            alert("没拿到后台数据");
        }
    })
}


// 左下部分
function get_left_bottom_data() {
    $.ajax({
        url: "/left_bottom",
        success: function (data_json_value) {
            ec_left_bottom_option.xAxis[0].data = data_json_value.day
            ec_left_bottom_option.series[0].data = data_json_value.confirm_add
            ec_left_bottom_option.series[1].data = data_json_value.suspect_add

            ec_left_bottom_selector.setOption(ec_left_bottom_option);//丢在option里面重新渲染
        },
        error: function () {
            alert("没拿到后台数据");
        }
    })
}


// 右上部分
function get_right_top_data() {
    $.ajax({
        url: "/right_top",
        success: function (data_json_value) {
            ec_right_top_option.xAxis.data = data_json_value.city
            ec_right_top_option.series[0].data = data_json_value.confirm
            ec_right_top_selector.setOption(ec_right_top_option);//丢在option里面重新渲染
        },
        error: function () {
            alert("没拿到后台数据");
        }
    })
}


//右下部分
function get_right_bottom_data() {
    $.ajax({
        url: "/right_bottom",
        success: function (data_json_value) { //关注下面的数据类型
            ec_right_bottom_option.series[0].data = data_json_value.kws;
            ec_right_bottom_selector.setOption(ec_right_bottom_option);//丢在option里面重新渲染
        },
        error: function () {
            alert("没拿到后台数据");
        }
    })
}

