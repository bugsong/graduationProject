//时间更新部分
function get_time() {
    $.ajax({
        url: "/time",
        timeout: 10000,//设置超时时间为10秒
        success: function (data) {
            $("#time").html(data);//以服务器时间为准
        },
        error: function () {

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

        }
    })
}

setInterval(get_center_top_data, 1000);

// 地图数据部分
function get_center_bottom_data() {
    $.ajax({
        url: "/center_bottom",
        success: function (data_json_value) {
            ec_center_option.series[0].data = data_json_value.data;//从后台拿到数据
            ec_center_selector.setOption(ec_center_option);//丢在option里面重新渲染
        },
        error: function () {

        }
    })
}
get_center_bottom_data();
// 渲染一次即可