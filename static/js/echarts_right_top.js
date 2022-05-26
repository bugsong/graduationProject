var ec_right_top_selector = echarts.init(document.getElementById("right_top"), "dark");
var ec_right_top_option = {
    title: {
        text: "非湖北地区城市确诊TOP5",
        textStyle: {
            color: 'white',
        },
        left: 'left'

    },
    color: ['#3398DB'],
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    xAxis: {
        type: 'category',
        data: ['重庆', '温州', '北京', '广州', '上海']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [525, 200, 150, 80, 90],
        type: 'bar',
        barMaxWidth: "50"

    }]
};
ec_right_top_selector.setOption(ec_right_top_option);