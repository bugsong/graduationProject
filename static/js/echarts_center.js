var ec_center_selector = echarts.init(document.getElementById("center_bottom"), "dark");
var mydata = [{ 'name': '西藏', 'value': 318 }, { 'name': '新疆', 'value': 162 }];

var ec_center_option = {
    title: {
        text: '',
        subtext: '',
        x: 'left',
    },
    tooltip: {
        trigger: 'item'
    },
    // 左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{ start: 1, end: 9 },
        { start: 10, end: 99 },
        { start: 100, end: 999 },
        { start: 1000, end: 9999 },
        { start: 10000 }],
        color: ['#8A3310', '#c64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },
    // 配置属性
    series: [{
        name: '累计确诊人数',
        type: 'map',
        mapType: 'china',
        roma: false,
        itemStyle: {
            normal: {
                borderWidth: 3,// 区域边框宽度
                borderColor: '#4b0082',// 区域边框颜色
                areaColor: '#ffefd5',// 区域颜色 
            },
            emphasis: { // 鼠标划过地图高亮相关
                borderWidth: .5,
                borderColor: '#4b0082',
                areaColor: '#fff',
            },
        },
        label: {
            normal: {
                show: true,//省份名称
                fontSize: 10,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data: mydata//数据

    }]
};
ec_center_selector.setOption(ec_center_option);