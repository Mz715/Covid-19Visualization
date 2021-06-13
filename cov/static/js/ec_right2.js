var ec_right2 = echarts.init(document.getElementById('r2'), "dark");
var ec_right2_option = {
    title : {
	    text : "新增确诊top10",
	    textStyle : {
	        color : 'white',
	    },
	    left : 'left'
	},
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
	legend: {
        top: 'bottom'
    },
    toolbox: {
        show: true,
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    series: [
        {
            name: '当地新增',
            type: 'pie',
            radius: [10, 140],
            roseType: 'radius',
            itemStyle: {
                borderRadius: 5
            },
            label: {
                show: true
            },
            emphasis: {
                label: {
                    show: true
                }
            },
            data: []
        }
    ]
	  
};
ec_right2.setOption(ec_right2_option);