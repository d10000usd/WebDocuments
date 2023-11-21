<html>
<head>
# **WebSocket Logic in Vue**
</head>
<body>
<p>It looks like you've shared a JavaScript module that defines a class `WebSocketLogic` and a function `useWebSocketLogic` using Vue.js and WebSocket communication. The class appears to handle the logic related to WebSocket data, sorting, and updating.

Is there anything specific you would like assistance with or any questions you have about this code?




</p>

<p>If you want to align the lines in your code for better readability, you can follow a consistent indentation style. Here's your code with indentation applied:

```javascript
import { sharedWebSocketService } from './WebSocketService';
import { ref } from 'vue';

class WebSocketLogic {
  constructor(keysToRetrieve, compname, reqCall, typesort, rankea, startpos) {
    this.keysToRetrieve = keysToRetrieve;
    this.compname = compname;
    this.reqCall = reqCall;
    this.typesort = typesort;
    this.rankea = rankea;
    this.startpos = startpos;
    this.sortedWsData = ref([]);
    this.isWebSocketSetup = false;
    this.keysOnlyData = ref([]);
    this.valueOnlyData = ref([]);
    this.updateWsData = this.updateWsData.bind(this);

    sharedWebSocketService.registerUpdateFunction(this.updateWsData);

    if (!WebSocketLogic.isWebSocketInitialized) {
      this.setupWebSocket(reqCall);
      WebSocketLogic.isWebSocketInitialized = true;
    }
  }

  static isWebSocketInitialized = false;

  countSignedChangeRate = (values) => {
    const greaterThanZeroCount = values.filter(([, value]) => value.signed_change_rate > 0).length;
    const lessThanZeroCount = values.filter(([, value]) => value.signed_change_rate < 0).length;
    return { greaterThanZeroCount, lessThanZeroCount };
  };

  sortValuesBy = (values, typesort) => {
    return values
      .filter(([, value]) => value !== undefined)
      .sort((a, b) => {
        const comparison = b[1][this.reqCall] - a[1][this.reqCall];
        return typesort === 'asc' ? comparison : -comparison;
      });
  };

  updateWsData = (data) => {
    if (!data) {
      console.warn('Received undefined data. Ignoring update.');
      return;
    }

    try {
      const retrievedValues = Object.fromEntries(
        this.keysToRetrieve.map((key) => [key, data.get(key)])
      );

      let sortedValues = this.sortValuesBy(Object.entries(retrievedValues), this.typesort);

      const keysToRetrieveLenth = this.keysToRetrieve.length;
      if (this.rankea >= 0 && keysToRetrieveLenth > 0) {
        sortedValues = Object.values(sortedValues).slice(this.startpos, this.startpos + this.rankea);
      } else if (this.rankea < 0) {
        sortedValues = Object.values(sortedValues).slice(this.rankea);
      }

      this.sortedWsData.value = Object.fromEntries(sortedValues);
      this.keysOnlyData.value = Object.keys(this.sortedWsData.value);
      this.valueOnlyData.value = Object.values(this.sortedWsData.value);
    } catch (error) {
      console.error('Error processing WebSocket data:', error);
    }
  };

  getFirstFourSortedData() {
    return this.sortedWsData.value.slice(0, 1);
  }

  setupWebSocket = (reqCall) => {
    return new Promise((resolve) => {
      if (!this.isWebSocketSetup) {
        sharedWebSocketService.setupWebSocket(reqCall).then(() => {
          this.isWebSocketSetup = true;
          resolve();
        });
      } else {
        resolve();
      }
    });
  };
}

const useWebSocketLogic = (keysToRetrieve, compname, reqCall, typesort, rankea, startpos) => {
  const logicInstance = new WebSocketLogic(keysToRetrieve, compname, reqCall, typesort, rankea, startpos);

  return {
    sortedWsData: logicInstance.sortedWsData,
    keysOnlyData: logicInstance.keysOnlyData,
    valueOnlyData: logicInstance.valueOnlyData,
    updateWsData: logicInstance.updateWsData,
  };
};

export { useWebSocketLogic, WebSocketLogic };
```

This indentation style is a common convention in JavaScript development. Adjustments can be made based on your team's or project's coding standards.




</p>


</body>
</html>