var ec_left_top_selector = echarts.init(document.getElementById("left_top"), "dark");

var ec_left_top_option = {
    //标题样式
    title: {
        text: '全国累计趋势',
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
        data: ['累计确诊', '现有疑似', '累计治愈', '累计死亡'],
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
            name: '累计确诊',
            type: 'line',
            smooth: true,
            data: [120, 132, 101]
        },
        {
            name: '现有疑似',
            type: 'line',
            smooth: true,
            data: [33, 16, 91]
        },
        {
            name: '累计治愈',
            type: 'line',
            smooth: true,
            data: [45, 37, 86]
        },
        {
            name: '累计死亡',
            type: 'line',
            smooth: true,
            data: [38, 43, 11]
        },
    ]
};
ec_left_top_selector.setOption(ec_left_top_option);