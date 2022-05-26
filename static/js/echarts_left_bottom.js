var ec_left_bottom_selector = echarts.init(document.getElementById("left_bottom"), "dark");

var ec_left_bottom_option = {
    //标题样式
    title: {
        text: '全国新增趋势',
        left: 'left',
    },

    tooltip: {
        trigger: 'axis',
        //指示器
        axisPointer: {
            type: 'line',
            lineStyle: {
                color: "#7171C6",
            }
        },
    },
    legend: {
        data: ['新增确诊', '新增疑似'],
        left: "right",
    },

    //图形位置
    grid: {
        left: '4%',
        right: '6%',
        bottom: '4%',
        top: 50,//暂时没打%
        containLabel: true
    },
    xAxis: [{
        type: 'category',
        // boundaryGap: false,
        // nothing,just 王义松
        data: ['01.20', '01.21', '01.22']
    }],
    yAxis: [{
        type: 'value',
        //y轴字体设置
        axisLabel: {
            show: true,
            color: 'white',
            fontSize: 12,
            formatter: function (value) {
                if (value >= 1000) {
                    value = value / 1000 + 'k';
                }
                return value;
            }
        },
        //y轴线设置
        axisLine: {
            show: true,
        },
        splitLine: {
            show: true,
            lineStyle: {
                color: '#17273B',
                width: 1,
                type: 'solid',
            }

        }
    }],
    series: [
        {
            name: '新增确诊',
            type: 'line',
            smooth: true,
            data: [120, 132, 101]
        },
        {
            name: '新增疑似',
            type: 'line',
            smooth: true,
            data: [33, 16, 91]
        },
    ]
};
ec_left_bottom_selector.setOption(ec_left_bottom_option);