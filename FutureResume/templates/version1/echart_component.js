 
import ec from 'echarts/build/dist/echarts.js' 
        // 路径配置
        require.config({
            paths: {
                //echarts: "{% static 'echarts/build/dist' %}"
                echarts: "echarts/build/dist"
            }
        });
        
        // 使用
        require(
            [
                'echarts',
                'echarts/chart/bar', // 使用柱状图就加载bar模块，按需加载
                'echarts/chart/line', 
                'echarts/chart/scatter',
                'echarts/chart/k',
                'echarts/chart/pie',
                'echarts/chart/radar',
                'echarts/chart/force',
                'echarts/chart/chord',
                'echarts/chart/gauge',
                'echarts/chart/funnel',
                'echarts/chart/eventRiver',
                'echarts/chart/venn',
                'echarts/chart/treemap',
                'echarts/chart/tree',
                'echarts/chart/wordCloud',
                'echarts/chart/heatmap',
            ],
            function (ec) {

                var myChart3 = ec.init(document.getElementById('main3')); 
                var option3 = {

                    title : {
                        text: 'Yield Trend',
                        subtext: 'kent',
                        x:'center',
                        textStyle: {
                            fontWeight: 'normal',
                            color: '#fff'          // 主标题文字颜色
                        }
                    },


                    tooltip : {
                        trigger: 'item',
                        formatter : function (params) {
                            var date = new Date(params.value[0]);
                            data = date.getFullYear() + '-'
                                   + (date.getMonth() + 1) + '-'
                                   + date.getDate() + ' '
                                   + date.getHours() + ':'
                                   + date.getMinutes();
                            return data + '<br/>'
                                   + params.value[1] + ', ' 
                                   + params.value[2];
                        }
                    },
                    /*
                    toolbox: {
                        show : true,
                        feature : {
                            mark : {show: true},
                            dataView : {show: true, readOnly: false},
                            restore : {show: true},
                            saveAsImage : {show: true}
                        }
                    },
                    */

                    dataZoom: {
                        show: true,
                        start : 70
                    },



                    legend: {
                        x : 'center',
                        y : 'bottom',
                        textStyle: {
                        color: '#ccc'          // 图例文字颜色
                        },
                        data:['series1']
                    },


                    grid: {
                        y2: 80
                    },

                    color: ['#F4E001','#B5C334'],
                    xAxis : [
                        {
                            type : 'time',
                            splitNumber:10
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    series : [
                        {
                            name: 'series1',
                            type: 'line',
                            showAllSymbol: true,
                            symbolSize: function (value){
                                return Math.round(value[2]/10) + 2;
                            },
                            data: (function () {
                                var d = [];
                                var len = 0;
                                var now = new Date();
                                var value;
                                while (len++ < 200) {
                                    d.push([
                                        new Date(2014, 9, 1, 0, len * 10000),
                                        (Math.random()*30).toFixed(2) - 0,
                                        (Math.random()*100).toFixed(2) - 0
                                    ]);
                                }
                                return d;
                            })()
                        }
                    ]
                };
                        
                // 为echarts对象加载数据 
                myChart3.setOption(option3); 