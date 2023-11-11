# **Data Fetching and Manipulation**
Sure, to simplify the code and improve its readability, you can separate different functionalities into individual functions. Here's an example of how you could organize the provided code into separate functions:

```javascript
async function fetchAndAssignDataMod() {
	try {
		const trendlinedata = await this.getDataFromJSON('trendline.json');
		const financial = await this.getDataFromJSON('콜마비앤에이치_1.json');
		const ohlcdata = await this.getDataFromJSON('ohlc.json');
		const indicatorCalculator = new IndicatorCalculate();
		const dataFetcher = new DataFetcher(ohlcdata, trendlinedata, options, indicatorCalculator);

		const fluctuationRate = await this.calculateFluctuationRate(ohlcdata);
		const result = indicatorCalculator.calculateMovingAverage(ohlcdata, 250);

		const lastValue = result[result.length - 1].value;
		const seed = {
			'priceFormatter': {
				'currency': lastValue
			}
		};

		this.displayFluctuationRateInHTML(fluctuationRate, "005404.KS", "삼성전자", 'trendlineData', seed);

		displayFinancialData(financial);

		createCharts(dataFetcher, indicatorCalculator, ohlcdata, trendlinedata, options);
		createCharts(dataFetcher, indicatorCalculator, ohlcdata, trendlinedata, options1);
	} catch (error) {
		console.error("Error fetching data:", error);
	}
}

function displayFinancialData(financial) {
	const financialTableBody = document.getElementById("financialTableBody");
	for (const key in financial) {
		if (financial.hasOwnProperty(key)) {
			const data = financial[key];
			const row = document.createElement("tr");
			row.innerHTML = `<th scope="row">${key}</th>`;
			for (const prop in data) {
				if (data.hasOwnProperty(prop)) {
					row.innerHTML += `<td>${data[prop]}</td>`;
				}
			}
			financialTableBody.appendChild(row);
		}
	}
}

function createCharts(dataFetcher, indicatorCalculator, ohlcdata, trendlinedata, options) {
	const chartCreator = new ChartCreator(dataFetcher, indicatorCalculator);
	chartCreator.createChart();
}
```

In this refactoring, I've separated the code into three functions: `displayFinancialData`, `createCharts`, and `fetchAndAssignDataMod` to organize the code better and make it more manageable.




