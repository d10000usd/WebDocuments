const getData_ohlc = async () => {
  const res = await fetch('clos.csv');
  const resp = await res.text();
  const rows = resp.split('\n');
  const cdata = [];
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i].trim();
    if (row !== '') {
      const [date, open, high, low, close] = row.split(',');
      const rowData = {
        time: new Date(date).getTime() / 1000,
        open: parseFloat(open),
        high: parseFloat(high),
        low: parseFloat(low),
        close: parseFloat(close),
      };
      cdata.push(rowData);
    }
  }
  return cdata;
};
const getData_trendline_json = async () => {
    const res = await fetch('trendline.json');
    const resp = await res.text();
 
    
    return cdata;
  };

  const getData_ohlc_json = async () => {
    const res = await fetch('trendline.json');
    const resp = await res.text();
 
    
    return cdata;
  };

const displayChart = async () => {
  const chartProperties = {
    width: 1500,
    height: 600,
    timeScale: {
      timeVisible: true,
      secondsVisible: true,
    },
  };

  const domElement = document.getElementById('tvchart');
  const chartDip = LightweightCharts.createChart(domElement, chartProperties);
  const candleseries = chartDip.addCandlestickSeries();
  const klinedata = await getData_ohlc();
  candleseries.setData(klinedata);
 
  chartDip.applyOptions(options)
};

// displayChart();

options = {
    "width": 800,
    "height": 800,
    "timeScale": {
        "timeVisible": "true",
        "secondsVisible": "false"
    },
    "priceScale": {
        "autoScale": "true",
        "scaleMargins": {
            "top": 0.1,
            "bottom": 0.2
        }
    },
    "priceFormatter": {
        "style": "currency",
        "currency": "KRW"
    },
    "movingAverages": {
        "ma5": {
            "color": "rgba(255, 0, 0, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma10": {
            "color": "rgba(0, 0, 255, 1)",
            "lineWidth": 1,
            "priceLineVisible": "false"
        },
        "ma15": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma20": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma25": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma30": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma35": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma40": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma45": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma50": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma55": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma60": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma65": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma70": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma75": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma80": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma85": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma90": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma95": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma100": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 12,
            "priceLineVisible": "false"
        },
        "ma105": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma110": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma115": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma120": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma125": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma130": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma135": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma140": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma145": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma150": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma155": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma160": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma165": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma170": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma175": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma180": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma185": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma190": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma195": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma200": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma205": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma210": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma215": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma220": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma225": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma230": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma235": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma240": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma245": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma250": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma255": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma260": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma265": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma270": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma275": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma280": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma285": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma290": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma295": {
            "color": "rgba(0, 244, 255, 1)",
            "lineWidth": 2,
            "priceLineVisible": "false"
        },
        "ma300": {
            "color": "rgba(0, 0, 255, 1)",
            "lineWidth": 12,
            "priceLineVisible": "false"
        }
    },
    "crosshair": {
      "mode": LightweightCharts.CrosshairMode.Normal,
        "vertLine": {
            "width": 8,
            "color": "#C3BCDB44",
            "labelBackgroundColor": "#9B7DFF",
            "style": LightweightCharts.LineStyle.Solid,

        },
        "horzLine": {
            "color": "#9B7DFF",
            "labelBackgroundColor": "#9B7DFF"
        }
    }
}

options1 = {
  "width": 800,
  "height": 800,
  "timeScale": {
      "timeVisible": "true",
      "secondsVisible": "false"
  },
  "priceScale": {
      "autoScale": "true",
      "scaleMargins": {
          "top": 0.1,
          "bottom": 0.2
      }
  },
  "priceFormatter": {
      "style": "currency",
      "currency": "KRW"
  },
  "movingAverages": {
     
      "ma285": {
          "color": "rgba(0, 244, 255, 1)",
          "lineWidth": 2,
          "priceLineVisible": "false"
      },
      "ma290": {
          "color": "rgba(0, 244, 255, 1)",
          "lineWidth": 2,
          "priceLineVisible": "false"
      },
      "ma295": {
          "color": "rgba(0, 244, 255, 1)",
          "lineWidth": 2,
          "priceLineVisible": "false"
      },
      "ma300": {
          "color": "rgba(0, 0, 255, 1)",
          "lineWidth": 12,
          "priceLineVisible": "false"
      }
  },
  "crosshair": {
    "mode": LightweightCharts.CrosshairMode.Normal,
      "vertLine": {
          "width": 8,
          "color": "#C3BCDB44",
          "labelBackgroundColor": "#9B7DFF",
          "style": LightweightCharts.LineStyle.Solid,

      },
      "horzLine": {
          "color": "#9B7DFF",
          "labelBackgroundColor": "#9B7DFF"
      }
  }
}
