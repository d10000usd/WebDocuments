# **Assigning Values to Variables**
물론, 다음은 각 변수를 다른 변수에 할당하는 예시입니다:

```vue
<script setup>
import tickersRaw from "@/assets/coinInfo/tickers.json";
import balances from "@/assets/coinInfo/balance_ticker.json";
import watches from "@/assets/coinInfo/tickers_watch.json";
import rankcoins from "@/assets/coinInfo/tickers_rating_order.json";

// tickersRaw를 다른 변수에 할당하는 예시
const otherVariable1 = tickersRaw;
const otherVariable2 = balances;
const otherVariable3 = watches;
const otherVariable4 = rankcoins;
</script>

<template>
  <!-- 템플릿 내용 -->
</template>
```

위 코드에서는 각각의 변수를 새로운 변수에 할당하는 방법을 보여주고 있습니다. `otherVariable1`, `otherVariable2`, `otherVariable3`, `otherVariable4`는 각각 `tickersRaw`, `balances`, `watches`, `rankcoins`와 동일한 데이터를 가지고 있습니다. 이를 통해 각 변수를 개별적으로 활용할 수 있습니다.




