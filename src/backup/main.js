// Function to generate a sample set of Candlestick datapoints
async function generateCandlestickData() {
  try {
    // const response = await fetch('https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/json/html_stock/lightdata_int_100.json');
    // const response = await fetch('https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/json/html_stock/lightdata.json');
    const response = await fetch('https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/json/html_stock/KAVAminutes240.json');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    console.log(data)
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    return []; // Return an empty array in case of an error
  }
}

generateCandlestickData().then((data) => {
  const candleStickData = data.map((datapoint) => {
    // map function is changing the color for the individual
    // candlestick points that close above 205
    if (datapoint.close < 1355) return datapoint;
    // we are adding 'color' and 'wickColor' properties to the datapoint.
    // Using spread syntax: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals
    return { ...datapoint, color: "orange", wickColor: "orange" };
  });

  // Create the Lightweight Chart within the container element
  const chart = LightweightCharts.createChart(
    document.getElementById('container'),
    {
      layout: {
        background: { color: "#222" },
        textColor: "#C3BCDB",
      },
      grid: {
        vertLines: { color: "#444" },
        horzLines: { color: "#444" },
      },
    }
  );

  // Setting the border color for the vertical axis
  chart.priceScale().applyOptions({
    borderColor: "#71649C",
  });

  // Setting the border color for the horizontal axis
  chart.timeScale().applyOptions({
    borderColor: "#71649C",
  });

  // Adjust the starting bar width (essentially the horizontal zoom)
  chart.timeScale().applyOptions({
    barSpacing: 10,
  });

  // Changing the font
  chart.applyOptions({
    layout: {
      fontFamily: "'Roboto', sans-serif",
    },
  });

  // Get the current user's primary locale
  const currentLocale = window.navigator.languages[0];
  // Create a number format using Intl.NumberFormat
  const myPriceFormatter = Intl.NumberFormat(currentLocale, {
    style: "currency",
    currency: "KRW", // Currency for data points
  }).format;

  // Apply the custom priceFormatter to the chart
  chart.applyOptions({
    localization: {
      priceFormatter: myPriceFormatter,
    },
  });

  // Customizing the Crosshair
  chart.applyOptions({
    crosshair: {
      // Change mode from default 'magnet' to 'normal'.
      // Allows the crosshair to move freely without snapping to datapoints
      mode: LightweightCharts.CrosshairMode.Normal,

      // Vertical crosshair line (showing Date in Label)
      vertLine: {
        width: 8,
        color: "#C3BCDB44",
        style: LightweightCharts.LineStyle.Solid,
        labelBackgroundColor: "#9B7DFF",
      },

      // Horizontal crosshair line (showing Price in Label)
      horzLine: {
        color: "#9B7DFF",
        labelBackgroundColor: "#9B7DFF",
      },
    },
  });

  // Add an area series to the chart,
  // Adding this before we add the candlestick chart
  // so that it will appear beneath the candlesticks
  const areaSeries = chart.addAreaSeries({
    lastValueVisible: false, // hide the last value marker for this series
    crosshairMarkerVisible: false, // hide the crosshair marker for this series
    lineColor: "transparent", // hide the line
    topColor: "rgba(56, 33, 110,0.6)",
    bottomColor: "rgba(56, 33, 110, 0.1)",
  });
  // Set the data for the Area Series
  areaSeries.setData(candleStickData);

  // Create the Main Series (Candlesticks)
  const mainSeries = chart.addCandlestickSeries();
  // Set the data for the Main Series
  mainSeries.setData(candleStickData);

  // Changing the Candlestick colors
  mainSeries.applyOptions({
    wickUpColor: "rgb(54, 116, 217)",
    upColor: "rgb(54, 116, 217)",
    wickDownColor: "rgb(225, 50, 85)",
    downColor: "rgb(225, 50, 85)",
    borderVisible: false,
  });

  // Adjust the options for the priceScale of the mainSeries
  mainSeries.priceScale().applyOptions({
    autoScale: true, // disables auto scaling based on visible content
    scaleMargins: {
      top: 0.1,
      bottom: 0.2,
    },
  });

  // Adding a window resize event handler to resize the chart when
  // the window size changes.
  // Note: for more advanced examples (when the chart doesn't fill the entire window)
  // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
  window.addEventListener("resize", () => {
    chart.resize(window.innerWidth, window.innerHeight);
  });
}).catch((error) => {
  console.error('Error fetching or processing data:', error);
});