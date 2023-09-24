PROMPT:

@app.route('/chart3') def notdash\_vue3(): fig = pchartmain.main(mode="코인", ticker="KRW-ETH", 주식이름="하나기술") graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) return graphJSON vue3 에서 받아서 보여주는 sciprt setup

RESPONSE:

To display the chart in Vue 3, you can follow these steps:

1. Create a new component in Vue 3 where you will display the chart. For example, let's name it `Chart3.vue`.

2. In the `<template>` section of `Chart3.vue`, add a `<div>` element with an id to serve as the container for the chart. For example:

```html
<template>
  <div>
    <div id="chart-container"></div>
  </div>
</template>
```

3. In the `<script>` section of `Chart3.vue`, import the necessary libraries and define the `setup` function:

```javascript
<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Plotly from 'plotly.js-dist';

export default {
  setup() {
    const chartContainer = ref(null);

    onMounted(() => {
      axios.get('/chart3')
        .then(response => {
          const graphJSON = response.data;
          Plotly.newPlot(chartContainer.value, JSON.parse(graphJSON));
        })
        .catch(error => {
          console.error(error);
        });
    });

    return {
      chartContainer,
    };
  },
};
</script>
```

4. Make sure you have installed the required dependencies. You can install them by running the following command in your Vue project directory:

```
npm install axios plotly.js-dist
```

5. Finally, you can use the `Chart3` component in your Vue application by importing and including it in your desired parent component's template.

Please note that in the code provided, we assume that you have a server-side route `/chart3` that returns the chart data in JSON format. Make sure to configure your server to handle this route and respond with the appropriate data.

Also, adjust the code as needed based on your project structure and requirements.