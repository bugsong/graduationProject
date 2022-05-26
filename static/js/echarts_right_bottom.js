var ec_right_bottom_selector = echarts.init(document.getElementById("right_bottom"), "dark");

var ec_right_bottom_data = [{ 'name': '肺炎', 'value': '123123' }, { 'name': '新冠', 'value': '123456' }, { 'name': 'Yisong Wang', 'value': '999999' }]
var ec_right_bottom_option = {
    title: {
        text: "今日疫情热搜",
        textStyle: {
            color: 'white',
        },
        left: 'left'
    },
    tooltip: {
        show: false
    },
    series: [{
        type: "wordCloud",
        gridSize: 1,
        sizeRange: [12, 55],
        rotationRange: [-45, 0, 45, 90],
        textStyle: {
            // normal: {//研究半天,手动修复了,不需要外边这个嵌套
            color: function () { //随机生成RGB颜色
                var r = Math.floor(Math.random() * 256); //随机生成256以内r值
                var g = Math.floor(Math.random() * 256); //随机生成256以内g值
                var b = Math.floor(Math.random() * 256); //随机生成256以内b值
                return 'rgb(' + r + ',' + g + ',' + b + ')'
            },
            // }
        },
        right: null,
        bottom: null,
        data: ec_right_bottom_data,
    }]
}
ec_right_bottom_selector.setOption(ec_right_bottom_option);