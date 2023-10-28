class ChartDrawer {
    constructor(options,ohlcdata) {
        this.options = options;
        this.ohlcdata = ohlcdata
    }
    async init() {
        const jsonData = await this.ohlcdata;
        if (jsonData) {
            
            this.generateTable(jsonData);
            this.drawCandleChart(jsonData, 'candle-chart');
            
            
        }
    }
    
    calculateMovingAverage(data, period) {
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

    drawCandleChart(data, containerId) {
        var modifiedData = data.map(function (item) {
            return {
                time: new Date(item.time * 1000).getTime() / 1000,
                open: item.open,
                high: item.high,
                low: item.low,
                close: item.close,
            };
        });

        var chart = LightweightCharts.createChart(document.getElementById(containerId), this.options);

        var candleSeries = chart.addCandlestickSeries();
        candleSeries.setData(modifiedData);

        var ma5Data = this.calculateMovingAverage(modifiedData, 5);
        var ma10Data = this.calculateMovingAverage(modifiedData, 10);

        var ma5Series = chart.addLineSeries(this.options.movingAverages.ma5);
        ma5Series.setData(ma5Data);

        var ma10Series = chart.addLineSeries(this.options.movingAverages.ma10);
        ma10Series.setData(ma10Data.map(item => ({ time: item.time, value: item.value })));
    }


    generateTable(data) {
        var tableHeaders = Object.keys(data[0]);
        var headerRow = document.getElementById("header-row");
        var bodyRowCount = data.length;
        var bodyRowCount = 12;
        for (var i = 0; i < tableHeaders.length && i < bodyRowCount; i++) {
            var headerCell = document.createElement("th");
            headerCell.innerHTML = tableHeaders[i];
            headerRow.appendChild(headerCell);
        }

        var tableBody = document.getElementById("table-body");
        for (var i = 0; i < bodyRowCount && i < data.length; i++) {
            var row = tableBody.insertRow(i);

            for (var j = 0; j < tableHeaders.length && j < bodyRowCount; j++) {
                var cell = row.insertCell(j);
                cell.innerHTML = data[i][tableHeaders[j]];
            }
        }
    }

    saveTableAsPNG() {
        var tableElement = document.querySelector(".table-responsive");
        html2canvas(tableElement, {
            width: tableElement.scrollWidth,
            height: tableElement.scrollHeight
        }).then(function (canvas) {
            var link = document.createElement('a');
            link.download = 'table.png';
            link.href = canvas.toDataURL("image/png");
            link.click();
        });
    }

    saveChartAsPNG() {
        var tableElement = document.querySelector("#candle-chart");
        html2canvas(tableElement, {
            width: tableElement.scrollWidth,
            height: tableElement.scrollHeight
        }).then(function (canvas) {
            var link = document.createElement('a');
            link.download = 'chart.png';
            link.href = canvas.toDataURL("image/png");
            link.click();
        });
    }
}
class DataFetcher {
    constructor() {
            this.options = {
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
                    'priceLineVisible': false,
                },
                "ma10": {
                    "color": "rgba(0, 0, 255, 1)",
                    "lineWidth": 12,
                    'priceLineVisible': false,
                }
            }
        };
    }


}
class DataLoader {
    async getJSONData() {
        try {
            const response = await fetch('https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/json/html_stock/086520.KQ.json');
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching JSON data:', error);
        }
    }
}
async function fetchDataFromURL(url) {
    const dataFetcher = new DataFetcher();
    const dataLoader = new DataLoader();

    const jsonData = await dataLoader.getJSONData(url);
    const chartDrawer = new ChartDrawer(dataFetcher.options, jsonData);

    await chartDrawer.init();
}

const externalUrl = 'https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/json/html_stock/086520.KQ.json';
fetchDataFromURL(externalUrl);