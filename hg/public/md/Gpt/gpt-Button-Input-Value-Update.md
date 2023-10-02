PROMPT:

<template> <div> <input v-model="inputValue" type="text" placeholder="Enter a value" /> <button class="btn btn-primary" @click="sendData(payload\_0)">Data Transfer {{ payload\_0\[1\] }} {{ inputValue.value }}</button> <button class="btn btn-primary" @click="sendData(payload\_1)">Data Transfer {{ payload\_1\[1\] }} {{ inputValue.value }}</button> <div>{{ inputValue }}</div> </div> <div> <div ref="chartContainer"></div> </div> </template> <script setup> import { onMounted, ref } from 'vue'; import axios from 'axios'; import Plotly from 'plotly.js-dist'; import { backendSchema } from '../utils/backendUtils' const chartContainer = ref(null); const inputValue = ref(''); const displayedValue = ref(''); const responseData = ref('') const parsingdata = ref('') const payload = ref(\['ChartComponent', 'plotlychart-coin'\]); const payload\_1 = ref(\['ChartComponent', 'plotlychart-stock'\]) const payload\_2 = ref(\['ChartComponent', 'getohlc'\]) const fetchData = async () => { try { const response = await axios.get(backendSchema.getUpdateChartRouteURL()); if (response) { responseData.value = response.data\['API'\] Plotly.newPlot(chartContainer.value, JSON.parse(chartData)); parsingdata.value = responseData.value\['fetch\_data'\]\[0\]\['action'\] } else { console.log('백엔드 호출 중 오류 발생: ' + String(error)) responseData.value = '응답이 없습니다.' } } catch (error) { console.log('백엔드 호출 중 오류 발생: ' + String(error)) if (error.message === 'Network Error') { responseData.value = error.config.url + '에서 백엔드가 실행 중인지 확인해주세요.' } else { responseData.value = '죄송합니다. 오류가 발생했습니다.' } } } const sendData = (payload) => { console.log(payload) axios .post(backendSchema.getUpdateChartRouteURL(), payload) .then(() => { fetchData() }) .catch((error) => { console.log('전송 중 오류 발생: ' + String(error)) }) } 버튼을 누르면 입력받은 값을 버튼별로 paload, payload 에 값을 추가 해서 sendData 를 실행할 수 있게 수정해줘

RESPONSE:

Sure! I can help you modify the code to add the input value to the payload when the buttons are clicked. Here's the updated code:

```html
<template>
  <div>
    <input v-model="inputValue" type="text" placeholder="Enter a value" />
    <button class="btn btn-primary" @click="sendData([...payload_0, inputValue])">
      Data Transfer {{ payload_0[1] }} {{ inputValue }}
    </button>
    <button class="btn btn-primary" @click="sendData([...payload_1, inputValue])">
      Data Transfer {{ payload_1[1] }} {{ inputValue }}
    </button>
    <div>{{ inputValue }}</div>
  </div>
  <div>
    <div ref="chartContainer"></div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import Plotly from 'plotly.js-dist';
import { backendSchema } from '../utils/backendUtils';

const chartContainer = ref(null);

const inputValue = ref('');
const displayedValue = ref('');

const responseData = ref('');
const parsingdata = ref('');
const payload_0 = ref(['ChartComponent', 'plotlychart-coin']);
const payload_1 = ref(['ChartComponent', 'plotlychart-stock']);
const payload_2 = ref(['ChartComponent', 'getohlc']);

const fetchData = async () => {
  try {
    const response = await axios.get(backendSchema.getUpdateChartRouteURL());

    if (response) {
      responseData.value = response.data['API'];
      Plotly.newPlot(chartContainer.value, JSON.parse(chartData));
      parsingdata.value = responseData.value['fetch_data'][0]['action'];
    } else {
      console.log('백엔드 호출 중 오류 발생: ' + String(error));
      responseData.value = '응답이 없습니다.';
    }
  } catch (error) {
    console.log('백엔드 호출 중 오류 발생: ' + String(error));
    if (error.message === 'Network Error') {
      responseData.value =
        error.config.url + '에서 백엔드가 실행 중인지 확인해주세요.';
    } else {
      responseData.value = '죄송합니다. 오류가 발생했습니다.';
    }
  }
};

const sendData = (payload) => {
  console.log(payload);
  axios
    .post(backendSchema.getUpdateChartRouteURL(), payload)
    .then(() => {
      fetchData();
    })
    .catch((error) => {
      console.log('전송 중 오류 발생: ' + String(error));
    });
};

onMounted(() => {
  fetchData();
});
</script>
```

In the updated code, I modified the button click handlers to pass the `inputValue` along with the existing payload values. The `sendData` function now receives the updated payload and sends it to the backend. Additionally, I added the `onMounted` lifecycle hook to automatically fetch data when the component is mounted.

Please note that I assumed the `chartData` variable is defined somewhere in your code, as it is used in the `Plotly.newPlot` function. Make sure to include that variable declaration and assignment as well.

Let me know if you need any further assistance!