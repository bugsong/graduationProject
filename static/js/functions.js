function gettime() {
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

setInterval(gettime, 1000)

function get_center_data() {
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

setInterval(get_center_data, 1000)

