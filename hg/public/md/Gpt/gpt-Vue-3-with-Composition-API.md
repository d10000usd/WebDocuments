Default (GPT-3.5)

PROMPT:

RESPONSE:

Sure, here's your Vue 3 code converted to use the Composition API with the `<script setup>` syntax:

```vue
<template>
  <div>
    <section>
      <!-- font size -->
      <h1>Trading View widget </h1>
      <p>https://www.tradingview.com/widget/</p>
      <!-- chart  -->
      <p>https://www.tradingview.com/widget/advanced-chart/</p>
      <Chart :key="selectedOption" :options="Chart_options" />
    </section>
    <section>
      <p>https://www.tradingview.com/widget/screener/</p>
      <Screener id="trdiv" :key="selectedOption" :options="Screener_options" />
    </section>
    <section>
      <p>https://www.tradingview.com/widget/fundamental-data/</p>
      <FundamentalData :key="selectedOption" :options="FundamentalData_options" />
    </section>
    <section>
      <p>https://www.tradingview.com/widget/crypto-mkt-screener/</p>
      <CryptoMarket :key="selectedOption" :options="CryptoMarket_options" />
    </section>
    <CompanyProfile />
    <ForexHeatMap />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import {
  Chart,
  FundamentalData,
  ForexHeatMap,
  CompanyProfile,
  Screener,
  CryptoMarket,
} from 'vue-tradingview-widgets';

const selectedOption = ref('BTCUSDT');

const CryptoMarket_options = computed(() => ({
  width: 1000,
  height: 490,
  defaultColumn: 'moving_averages',
  screener_type: 'crypto_mkt',
  displayCurrency: 'USD',
  colorTheme: 'light',
  locale: 'kr',
}));

const FundamentalData_options = computed(() => ({
  symbol: 'UPBIT:BTCKRW',
  colorTheme: 'light',
  isTransparent: false,
  largeChartUrl: '',
  displayMode: 'regular',
  width: 480,
  height: 830,
  locale: 'kr',
}));

const Screener_options = computed(() => ({
  width: 1200,
  height: 600,
  defaultColumn: 'moving_averages',
  defaultScreen: 'most_volatile',
  market: 'korea',
  showToolbar: true,
  colorTheme: 'light',
  locale: 'kr',
}));

const Chart_options = computed(() => ({
  width: 380,
  height: 610,
  symbol: 'UPBIT:BTCKRW',
  timezone: 'Asia/Seoul',
  theme: 'dark',
  style: '1',
  locale: 'kr',
  toolbar_bg: '#f1f3f6',
  enable_publishing: true,
  withdateranges: true,
  range: '1D',
  hide_side_toolbar: false,
  allow_symbol_change: true,
  details: true,
  hotlist: true,
  calendar: true,
  watchlist: ['AAPL', 'IBM', 'TSLA', 'AMD', 'MSFT', 'GOOG'],
  show_popup_button: true,
  popup_width: '1000',
  popup_height: '650',
  studies: [
    'STD;Advance%1Decline%1Ratio',
    'STD;Advance_Decline_Ratio_Bars',
    // ... (all the other studies)
  ],
}));

</script>
```

This code retains the functionality of your original Vue 3 code while using the Composition API and `<script setup>` syntax. Make sure to import the necessary `ref` and `computed` functions from the `vue` package for reactive data and computed properties.

PROMPT:

RESPONSE:

Yes, you can set the candlestick time interval for the TradingView chart using the `interval` property in your `Chart_options`. The `interval` property specifies the time interval for each candlestick on the chart.

Here's an example of how you can set the candlestick time interval to 15 minutes:

```javascript
const Chart_options = computed(() => ({
  // ... other options
  range: '1D', // Set the default range (e.g., 1 day)
  interval: '15', // Set the candlestick interval to 15 minutes
  // ... other options
}));
```

In the code above, I've added the `interval` property and set it to `'15'`, which represents a 15-minute candlestick interval. You can adjust this value to your desired time interval (e.g., `'1'` for 1 minute, `'5'` for 5 minutes, `'1D'` for 1 day, etc.).

Make sure to refer to the TradingView documentation or your specific chart library's documentation for more details on available interval options and formatting.

PROMPT:

RESPONSE:

I apologize for any confusion. It seems that the interval property may not be supported in the way I previously mentioned for the specific chart library you are using. If setting the interval directly in the `Chart_options` isn't working, it might be because the library you are using does not expose this as a configurable option through its Vue component.

To set the candlestick interval, you may need to refer to the documentation or support resources provided by the `vue-tradingview-widgets` library or check if there are specific props or methods available to configure the interval. The ability to set the candlestick interval depends on the capabilities of the library you are using.

If the library does not support setting the interval through its configuration options, you may need to explore other charting libraries or consider customizing the library's code to support the interval you require.

I recommend checking the official documentation or reaching out to the maintainers or community of the `vue-tradingview-widgets` library for specific guidance on setting the candlestick interval.

<button>?</button>