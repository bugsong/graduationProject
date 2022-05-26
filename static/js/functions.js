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

setInterval(get_center_top_data, 1000);

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
get_center_bottom_data();
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
get_left_top_data();

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
get_left_bottom_data();