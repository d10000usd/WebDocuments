# **<span style="font-size: 35px; font-style: italic;">주식 차트 저항선 추가</span>**

> ## 1
당신이 원하는 것은 주식의 저항선 하단을 표시하는 JavaScript 코드일 것 같습니다. 이를 위해 주식 차트를 그리는 라이브러리를 사용할 수 있습니다. 아래는 주식 차트를 생성하고 저항선을 표시하는 간단한 JavaScript 코드의 예제입니다.

```javascript
// 필요한 라이브러리 가져오기
const { createChart, CrosshairMode } = require('lightweight-charts');

// 주식 데이터
const stockData = [
  { time: '2023-09-01', value: 100 },
  { time: '2023-09-02', value: 105 },
  { time: '2023-09-03', value: 110 },
  // ... 다른 주식 데이터 포인트
];

// 차트 생성
const container = document.getElementById('chart-container');
const chart = createChart(container, { width: 800, height: 400 });
const priceSeries = chart.addCandlestickSeries();

// 차트에 데이터 추가
priceSeries.setData(stockData);

// 저항선 추가
const resistanceLine = chart.createPriceLine({
  price: 115, // 저항선 가격
  color: 'red', // 저항선 색상
  lineWidth: 2, // 저항선 두께
  lineStyle: CrosshairMode.Normal, // 저항선 스타일
});

// 차트 렌더링
chart.timeScale().fitContent();
```

이 코드는 `lightweight-charts` 라이브러리를 사용하여 주식 차트를 만들고, 특정 가격에 대한 저항선을 추가하는 간단한 예제입니다. 여기서 `stockData` 배열에는 주식 가격 데이터가 포함되어 있으며, `resistanceLine`을 통해 저항선을 추가할 수 있습니다.

이 코드를 웹 페이지에 적용하려면 HTML에서 스크립트를 불러오고 적절한 `div` 요소를 만들어야 합니다. 또한 `lightweight-charts` 라이브러리를 설치해야 합니다.

저항선의 위치, 색상, 두께 등을 필요에 맞게 수정하여 사용할 수 있습니다.
*****



> ## 2
Apex 또는 ApexCharts는 JavaScript 차트 라이브러리로, Vue 3와 함께 사용할 수 있습니다. 아래는 Vue 3와 ApexCharts를 사용하여 간단한 차트를 생성하는 예제입니다.

먼저, Vue 3 프로젝트를 설정하고 ApexCharts를 설치해야 합니다. 아래는 이를 위한 스텝입니다.

1. Vue 3 프로젝트 생성:

   ```bash
   vue create my-apex-chart-app
   ```

2. 생성된 프로젝트 디렉토리로 이동:

   ```bash
   cd my-apex-chart-app
   ```

3. ApexCharts 설치:

   ```bash
   npm install apexcharts vue3-apexcharts
   ```

이제 ApexCharts를 Vue 3 프로젝트에서 사용하는 예제 코드를 제공합니다.

```vue
<template>
  <div>
    <apexchart :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue3-apexcharts';

export default {
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: 'line',
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        },
      },
      series: [
        {
          name: 'Sales',
          data: [30, 40, 35, 50, 49],
        },
      ],
    };
  },
};
</script>
```

이 코드는 Vue 3 컴포넌트에서 ApexCharts를 사용하는 예제입니다. `vue3-apexcharts` 라이브러리를 불러와서 `apexchart` 컴포넌트를 사용하고 있습니다. `chartOptions`와 `series` 데이터를 조정하여 원하는 차트를 생성하고 표시할 수 있습니다.

Vue 3와 ApexCharts를 사용하여 다양한 종류의 차트를 만들고 데이터를 시각화할 수 있습니다. 필요에 따라 `chartOptions` 및 `series` 데이터를 변경하여 원하는 차트를 만들어 보세요.
*****



