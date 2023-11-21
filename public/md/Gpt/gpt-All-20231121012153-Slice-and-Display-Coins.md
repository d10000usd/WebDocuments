# **<span style="font-size: 35px; font-style: italic;">Slice and Display Coins</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-35.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 1</div></div>
To achieve this, you can use the `slice` method to extract the first 10 elements from the `rankcoins1` array. Here's the modified code:

```html
<template>
  <div class="c-custom-card">
    <div class="col-sm-12">
      <!-- Content in col-sm-12 -->
    </div>
    <!-- Use router-link to navigate and pass the selectedValue as a query parameter -->
    <h1>AA</h1>
    <div v-if="selectedValue !== null">
      Selected Value:
    </div>

    <TsWebsocket_table :message="slicedRankcoins1" />

  </div>
  <div class="c-custom-card">
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue';
import rankcoins1 from "@/assets/coinInfo/tickers_rating_order.json";
import { useWebSocketLogic } from '../stores/WebsocketConnector';

import TsWebsocket_table from "./TsWebsocket_table.vue"

const { sortedWsData: data } = useWebSocketLogic(rankcoins1, "TsWebsocket_all", 'signed_change_rate', "asc");

const selectedValue = ref({
  "Major Cryptocurrencies": [
    "KRW-BTG",
    "KRW-BSV"
  ]
});

// Slice the first 10 elements from rankcoins1
const slicedRankcoins1 = ref(rankcoins1.slice(0, 10));

</script>

<style scoped></style>
```

Now, `slicedRankcoins1` contains the first 10 elements of the `rankcoins1` array. This sliced array is then passed to the `TsWebsocket_table` component as the `message` prop.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-39.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
If you want to wait until `rankcoins1` is completely loaded before slicing the array, you should use the `watch` function to observe changes in the `rankcoins1` variable. Here's the modified code:

```html
<template>
  <div class="c-custom-card">
    <div class="col-sm-12">
      <!-- Content in col-sm-12 -->
    </div>
    <!-- Use router-link to navigate and pass the selectedValue as a query parameter -->
    <h1>AA</h1>
    <div v-if="selectedValue !== null">
      Selected Value:
    </div>

    <TsWebsocket_table :message="slicedRankcoins1" />

  </div>
  <div class="c-custom-card">
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import rankcoins1 from "@/assets/coinInfo/tickers_rating_order.json";
import { useWebSocketLogic } from '../stores/WebsocketConnector';

import TsWebsocket_table from "./TsWebsocket_table.vue"

const { sortedWsData: data } = useWebSocketLogic(rankcoins1, "TsWebsocket_all", 'signed_change_rate', "asc");

const selectedValue = ref({
  "Major Cryptocurrencies": [
    "KRW-BTG",
    "KRW-BSV"
  ]
});

const slicedRankcoins1 = ref([]);

onMounted(() => {
  // Watch for changes in rankcoins1 and update slicedRankcoins1 accordingly
  watch(() => rankcoins1, () => {
    slicedRankcoins1.value = rankcoins1.slice(0, 10);
  }, { deep: true });

  // Initial slicing after rankcoins1 is loaded
  slicedRankcoins1.value = rankcoins1.slice(0, 10);
});

</script>

<style scoped></style>
```

This code uses the `watch` function to observe changes in the `rankcoins1` variable. The initial slicing is done after the component is mounted (`onMounted` hook) to ensure that the data is fully loaded. The `deep: true` option is used to watch for changes deeply in the object, ensuring that nested properties are also observed.



<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-33.png)  
* Slice and Display Coins  
* 20231121012153  
* Description for dev  
* #keyword  
****
This sliced array is then passed to the `TsWebsocket_table` component as the `message` prop.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-39.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
If you want to wait until `rankcoins1` is completely loaded before slicing the array, you should use the `watch` function to observe changes in the `rankcoins1` variable  
</div> 
