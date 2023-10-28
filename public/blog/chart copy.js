var options = {
    "width": 1000,
    "height": 400,
    "timeScale": {
        "timeVisible": true,
        "secondsVisible": false
    },
    "priceScale": {
        "priceLineVisible": false
    },
    "movingAverages": {
        "ma5": {
            "color": "rgba(255, 0, 0, 1)",
            "lineWidth": 2,
            'priceLineVisible': false, // Hide the horizontal line
        },
        "ma10": {
            "color": "rgba(0, 0, 255, 1)",
            "lineWidth": 12,
            'priceLineVisible': false, // Hide the horizontal line
        }
    }
};

function calculateMovingAverage(data, period) {
    var result = [];
    for (var i = period - 1; i < data.length; i++) {
        var sum = 0;
        for (var j = 0; j < period; j++) {
            sum += data[i - j].close;
        }
        result.push({ time: data[i].time, value: sum / period });
    }
    return result;
}

function drawCandleChart(data, containerId) {
    var modifiedData = data.map(function (item) {
        return {
            time: new Date(item.time * 1000).getTime() / 1000,
            open: item.open,
            high: item.high,
            low: item.low,
            close: item.close,
        };
    });

    var chart = LightweightCharts.createChart(document.getElementById(containerId), options);

    var candleSeries = chart.addCandlestickSeries();
    candleSeries.setData(modifiedData);

    var ma5Data = calculateMovingAverage(modifiedData, 5);
    var ma10Data = calculateMovingAverage(modifiedData, 10);

    var ma5Series = chart.addLineSeries(options.movingAverages.ma5);
    ma5Series.setData(ma5Data);

    var ma10Series = chart.addLineSeries(options.movingAverages.ma10);
    ma10Series.setData(ma10Data.map(item => ({ time: item.time, value: item.value })));
}

