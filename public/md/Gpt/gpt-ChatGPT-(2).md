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

<button>?</button>