# **Styling for Watched Coins.**
I apologize for any confusion. It seems there might be an issue with the implementation. Let me provide you with an updated version of the code. Please try using the following modified code:

```vue
<template>
  <!-- <StaticsChart_realtimeOnly :message="selectedCoinTicker"/> -->
  <div class="row">
    <div class="col-4 col-md-3">
      <div class="card">
        <button
          @click="toggleIframe"
          :class="{ active: showingIframe, yellowCode: isWatched(props.message.code) }"
          :style="{
            backgroundColor: props.message.signed_change_rate >= 0 ? 'rgba(255, 0, 0, 0.5)' : 'rgba(0, 0, 255, 0.5)',
            color: 'black',
            fontSize: '13px'
          }"
        >
          {{ showingIframe ? props.message.code : props.message.code.split('-')[1] }} {{ (props.message.signed_change_rate * 100).toFixed(2) }}
        </button>
      </div>
    </div>
  </div>
  <iframe :src="iframeSrc" width="100%" height="500" v-if="showingIframe" scrolling="no"></iframe>
</template>

<script setup>
import { ref, defineProps } from 'vue';
// import StaticsChart_realtimeOnly from "./StaticsChart.vue"
import { getUpbitCoinPrices } from './upibtCoinRatingOrder';

const props = defineProps({
  message: Object,
});

const watches = ["KRW-BTC", "KRW-ETH", "KRW-EGLD", "KRW-ARB", "KRW-MATIC", "KRW-SOL", "KRW-SUI"];

const isWatched = (code) => {
  return watches.includes(code);
};

const urlBase = "https://m.stock.naver.com/crypto/UPBIT/";
const token = props.message.code.split('-')[1];
const iframeSrc = ref(urlBase + token);
const showingIframe = ref(false);

const toggleIframe = () => {
  showingIframe.value = !showingIframe.value;
};
</script>

<style>
.yellowCode {
  color: yellow;
}
</style>
```

Please replace your existing code with this one and check if it works as intended. If you encounter any issues, please let me know, and I'll be glad to assist you further.




