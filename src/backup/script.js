


// Call the init function when the window has finished loading
function loadJSON(callback) {
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/json");
  xobj.open('GET', 'https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/json/html/SUI_minutes240.json', true); // Replace 'path/to/your/file.json' with your file's path
  xobj.onreadystatechange = function () {
    if (xobj.readyState == 4 && xobj.status == "200") {
      callback(xobj.responseText);
    }
  };
  xobj.send(null);
}
function init() {
  loadJSON(function (response) {
    // Parse JSON string into object
    var data = JSON.parse(response);
    generateCandlestickData(data);
  });
}
// Call the init function when the window has finished loading
// window.onload = init;
////////
//////// chart area
chartOption = {

  layout: {
    background: { color: "#222" },
    textColor: "#C3BCDB",
    fontFamily: "'Roboto', sans-serif"
  },
  grid: {
    vertLines: { color: "#444" },
    horzLines: { color: "#444" },
  },
  crosshair: {
    mode: LightweightCharts.CrosshairMode.Normal,
    vertLine: {
      width: 8,
      color: "#C3BCDB44",
      style: LightweightCharts.LineStyle.Solid,

      labelBackgroundColor: "#9B7DFF",
    },
    horzLine: {
      color: "#9B7DFF",
      labelBackgroundColor: "#9B7DFF",
    },
  },


}
const chart = LightweightCharts.createChart(document.getElementById('container'), chartOption);

const areaSeries = chart.addAreaSeries({
  lastValueVisible: false,
  crosshairMarkerVisible: false,
  lineColor: "transparent",
  topColor: "rgba(56, 33, 110,0.6)",
  bottomColor: "rgba(56, 33, 110, 0.1)",
});
function calculatePriceData(data) {
  let minimumPrice = data[0].low;
  let maximumPrice = minimumPrice;
  let minimumDate = data[0].time;
  let maximumDate = data[0].time;
  for (let i = 1; i < data.length; i++) {
    const price = data[i].high;
    const date = data[i].time;
    if (price > maximumPrice) {
      maximumPrice = price;
      maximumDate = date;
    }
    if (price < minimumPrice) {
      minimumPrice = price;
      minimumDate = date;
    }
  }
  const avgPrice = (maximumPrice + minimumPrice) / 2;
  const avgDate = (maximumDate + minimumDate) / 2;
  return {
    minimum: { price: minimumPrice, date: minimumDate },
    maximum: { price: maximumPrice, date: maximumDate },
    average: { price: avgPrice, date: avgDate },
  };
}
function sortByDate(data) {
  return data.sort((a, b) => new Date(a.time) - new Date(b.time));
}





function generateCandlestickData(linedict,spl0, spl1, spl2) {
  const data = linedict
  spline0 = spl0
  spline1 = spl1
  spline2 = spl2
  const priceData = calculatePriceData(data);

  const candleStickData = data.map((datapoint) => {
    // map function is changing the color for the individual
    // candlestick points that close above 205
    if (datapoint.close < priceData.average.price) return datapoint;
    // we are adding 'color' and 'wickColor' properties to the datapoint.
    // Using spread syntax: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals
    return { ...datapoint, color: "orange", wickColor: "orange" };
  });

  const lineData = candleStickData.map((datapoint) => ({
    time: datapoint.time,
    value: (datapoint.close + datapoint.open) / 2.5,
  }));


  // lineLH = [
  //   { time: priceData.minimum.date, value: priceData.minimum.price },
  //   { time: priceData.maximum.date, value: priceData.maximum.price },

//   // ]

  lineOption = {
    'mainSeries': {
      'wickUpColor': "rgb(54, 116, 217)",
      'upColor': "rgb(54, 116, 217)",
      'wickDownColor': "rgb(225, 50, 85)",
      'downColor': "rgb(225, 50, 85)",
      'borderVisible': false,
    },
    'minPriceLine': {
      'price': priceData.minimum.price,
      'color': '#ef5350',
      'lineWidth': 12,
      'lineStyle': 2, // LineStyle.Dashed
      'axisLabelVisible': true,
      'title': '',
      'textAlign': 'left',
    },
    'avgPriceLine': {
      'price': priceData.average.price,
      'color': 'yellow',
      'lineWidth': 12,
      'lineStyle': 1, // LineStyle.Dotted
      'axisLabelVisible': true,
      'title': '평균가',
      'textAlign': 'left',
    },
    'maxPriceLine': {
      'price': priceData.maximum.price,
      'color': '#26a69a',
      'lineWidth': 12,
      'lineStyle': 2, // LineStyle.Dashed
      'axisLabelVisible': true,
      'title': '최고가',
      'textAlign': 'left',
    },
    'lineColor': {
      'priceScaleColor': {
        'borderColor': "#71649C",
      },
      'timeScaleColor': {
        'borderColor': "#71649C",
        'barSpacing': 110,
      }

    },
    'font': {
      'layout': {
        'fontFamily': "'Roboto', sans-serif",
      },
    },
    'priceScale': {
      'autoScale': true,
      'scaleMargins': {
        'top': 0.1,
        'bottom': 0.2,
      },
    },
    'priceFormatter': {
      'style': "currency",
      'currency': "KRW", // Currency for data points
    },
    'outlineOption': {
      'color': 'red',
      'lineStyle': 1,
      'lineWidth': 1,// 원하는 색상을 여기에 입력하세요.
    },
    'inlineOption': {
      'color': 'yellow',
      'lineStyle': 1,
      'lineWidth': 3,// 원하는 색상을 여기에 입력하세요.
    }

  };





  // areaSeries.setData(candleStickData);
  // areaSeries.setData(lineData);
  lineLH0 = spline0.support_line_c
  lineLH1 = spline0.resist_line_c
  lineLH2 = spline0.support_line
  lineLH3 = spline0.resist_line

  const mainSeries = chart.addCandlestickSeries();
  const lineSeries0 = chart.addLineSeries();
  const lineSeries1 = chart.addLineSeries();
  const lineSeries2 = chart.addLineSeries();
  const lineSeries3 = chart.addLineSeries();

  lineSeries0.setData((lineLH0));
  lineSeries1.setData((lineLH1));
  lineSeries2.setData((lineLH2));
  lineSeries3.setData((lineLH3));


  lineSeries2.applyOptions(lineOption.outlineOption);
  lineSeries3.applyOptions(lineOption.inlineOption);


// //////////////


  lineLH00 = spline1.support_line_c
  lineLH10 = spline1.resist_line_c
  lineLH20 = spline1.support_line
  lineLH30 = spline1.resist_line

  const mainSeries0 = chart.addCandlestickSeries();
  const lineSeries00 = chart.addLineSeries();
  const lineSeries10 = chart.addLineSeries();
  const lineSeries20 = chart.addLineSeries();
  const lineSeries30 = chart.addLineSeries();

  lineSeries00.setData((lineLH00));
  lineSeries10.setData((lineLH10));
  lineSeries20.setData((lineLH20));
  lineSeries30.setData((lineLH30));


  lineSeries20.applyOptions(lineOption.outlineOption);
  lineSeries30.applyOptions(lineOption.inlineOption);






  

  mainSeries.setData(candleStickData);


  mainSeries.applyOptions(lineOption.mainSeries);


  // mainSeries.applyOptions(lineOption.avgPriceLine);
  // mainSeries.applyOptions(lineOption.minPriceLine);
  // mainSeries.applyOptions(lineOption.maxPriceLine);

  mainSeries.createPriceLine(lineOption.minPriceLine);
  mainSeries.createPriceLine(lineOption.avgPriceLine);
  mainSeries.createPriceLine(lineOption.maxPriceLine);

  mainSeries.priceScale().applyOptions(lineOption.priceScale);
  chart.priceScale().applyOptions(lineOption.lineColor.priceScaleColor);
  chart.timeScale().applyOptions(lineOption.lineColor.timeScaleColor);
  chart.applyOptions(lineOption.font);

  const currentLocale = window.navigator.languages[0];
  const myPriceFormatter = Intl.NumberFormat(currentLocale, lineOption.priceFormatter).format;
  chart.applyOptions({
    localization: {
      priceFormatter: myPriceFormatter,
    },
  });

  chart.timeScale().fitContent();
}


window.addEventListener("resize", () => {
  chart.resize(window.innerWidth, window.innerHeight);
});
// document.getElementById('resetchart').addEventListener('click', resetChart);
// // document.getElementById('resetchart').addEventListener('click', function () {
// //   location.reload();
// // });




