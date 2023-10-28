
// 캔들 차트를 생성하는 함수
<<<<<<< HEAD
function drawCandleChart(data, containerId) {
=======
export function drawCandleChart(data, containerId) {
>>>>>>> 299f6630910204435ae21a0d6d28c230f83e6149
    // 옵션 데이터 설정
    var options = {
        width: 1000,
        height: 400,
        timeScale: {
            timeVisible: true,
            secondsVisible: false,
        },
    };
    var modifiedData = data.map(function (item) {
        return {
            time: new Date(item.time * 1000).getTime() / 1000,
            open: item.open,
            high: item.high,
            low: item.low,
            close: item.close,
        };
    });
<<<<<<< HEAD
    // 차트 생성
    var chart = LightweightCharts.createChart(document.getElementById(containerId), options);
    // 시리즈 생성
    var candleSeries = chart.addCandlestickSeries();
    // 캔들 데이터를 차트에 추가
    candleSeries.setData(modifiedData);
}
=======

    // 차트 생성
    var chart = LightweightCharts.createChart(document.getElementById(containerId), options);

    // 시리즈 생성
    var candleSeries = chart.addCandlestickSeries();

    // 캔들 데이터를 차트에 추가
    candleSeries.setData(modifiedData);
}

>>>>>>> 299f6630910204435ae21a0d6d28c230f83e6149
// JSON 데이터를 가져오는 함수
async function getJSONData() {
    try {
        // https://github.com/d10000usd/WebDocuments/blob/main/public/json/html_stock/086520.KQ.json
        const response = await fetch('https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/json/html_stock/086520.KQ.json');
        const data = await response.json();
        return data
<<<<<<< HEAD
        // drawCandleChart(data, 'candle-chart');
=======
        
>>>>>>> 299f6630910204435ae21a0d6d28c230f83e6149
    } catch (error) {
        console.error('Error fetching JSON data:', error);
    }
}
<<<<<<< HEAD
=======

>>>>>>> 299f6630910204435ae21a0d6d28c230f83e6149
async function init() {
    const jsonData = await getJSONData();
    if (jsonData) {
        generateTable(jsonData)
        drawCandleChart(jsonData, 'candle-chart');
        document.getElementById("jsondata").innerHTML = JSON.stringify(jsonData);
<<<<<<< HEAD

    }
}
// JSON 데이터를 사용하여 HTML 테이블 생성
function generateTable(data) {
    var tableHeaders = Object.keys(data[0]);
    var headerRow = document.getElementById("header-row");
    var bodyRowCount = data.length; // 테이블에 표시할 데이터 수
    var bodyRowCount = 2;
=======
    }
}






// JSON 데이터를 사용하여 HTML 테이블 생성

function generateTable(data) {
    var tableHeaders = Object.keys(data[0]);
    var headerRow = document.getElementById("header-row");
    // var bodyRowCount = data.length; // 테이블에 표시할 데이터 수
    var bodyRowCount = 2; // 테이블에 표시할 데이터 수

>>>>>>> 299f6630910204435ae21a0d6d28c230f83e6149
    // 헤더 셀 생성
    for (var i = 0; i < tableHeaders.length && i < bodyRowCount; i++) {
        var headerCell = document.createElement("th");
        headerCell.innerHTML = tableHeaders[i];
        headerRow.appendChild(headerCell);
    }

    var tableBody = document.getElementById("table-body");
<<<<<<< HEAD
=======

>>>>>>> 299f6630910204435ae21a0d6d28c230f83e6149
    // 데이터 셀 생성
    for (var i = 0; i < bodyRowCount && i < data.length; i++) {
        var row = tableBody.insertRow(i);

        for (var j = 0; j < tableHeaders.length && j < bodyRowCount; j++) {
            var cell = row.insertCell(j);
            cell.innerHTML = data[i][tableHeaders[j]];
        }
    }
}
<<<<<<< HEAD
=======
function saveChartAsPNG() {
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

>>>>>>> 299f6630910204435ae21a0d6d28c230f83e6149
function saveTableAsPNG() {
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
init();
<<<<<<< HEAD

=======
generateTable(jsonData);

document.getElementById("jsondata").innerHTML = JSON.stringify(jsonData);
>>>>>>> 299f6630910204435ae21a0d6d28c230f83e6149
