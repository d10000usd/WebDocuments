# **<span style="font-size: 35px; font-style: italic;">Vue3 Script KRW-NXM Key</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-35.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 1</div></div>
Vue 3 with script setup makes it easier to define properties in a more concise way. Here's an example of how you can output the key for "KRW-NXM" in your given data:

```vue
<template>
  <div>
    <p>{{ getKeyForToken("KRW-NXM") }}</p>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue';

const data = defineProps(['Hybrid Consensus Models', 'Quantum-Resistant Coins', 'Insurance and Risk Management']);

const getKeyForToken = (token) => {
  for (const category in data) {
    if (data[category].includes(token)) {
      return category;
    }
  }
  return "Token not found";
};
</script>
```

In this example, the `getKeyForToken` function takes a token as an argument and iterates through the categories in your data to find the key for the given token. The result is then displayed in the template.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-31.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
If you want to check the contents of the `DynamicCategorizing.json` file in JavaScript or Vue, you can use the following code:

```vue
<template>
  <div>
    <pre>{{ JSON.stringify(dynamicCategorizing, null, 2) }}</pre>
  </div>
</template>

<script setup>
import dynamicCategorizing from "@/assets/coinInfo/DynamicCategorizing.json";
</script>
```

This Vue 3 component uses the `JSON.stringify` method to convert the contents of `dynamicCategorizing` into a formatted string. The `pre` tag is used to display the string with proper formatting.

Make sure the path to your `DynamicCategorizing.json` file is correct. This example assumes that the `DynamicCategorizing.json` file is in the `@/assets/coinInfo/` directory. Adjust the path accordingly based on your project structure.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-36.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 3</div></div>
To extract the key associated with the value "KRW-CVC" in your `DynamicCategorizing.json` file, you can use the following code:

```vue
<template>
  <div>
    <p>{{ getKeyForToken("KRW-CVC") }}</p>
  </div>
</template>

<script setup>
import dynamicCategorizing from "@/assets/coinInfo/DynamicCategorizing.json";

const getKeyForToken = (token) => {
  for (const category in dynamicCategorizing) {
    if (dynamicCategorizing[category].includes(token)) {
      return category;
    }
  }
  return "Token not found";
};
</script>
```

This Vue 3 component defines a function `getKeyForToken` that takes a token (in this case, "KRW-CVC") and iterates through the categories in `DynamicCategorizing.json` to find the key associated with that token. The result is then displayed in the template. Adjust the path to `DynamicCategorizing.json` if needed based on your project structure.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-32.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 4</div></div>
Certainly! To display the entire array of values associated with a specific key in `DynamicCategorizing.json`, you can modify the previous code as follows:

```vue
<template>
  <div>
    <p>{{ getKeyForToken("KRW-CVC") }}</p>
    <ul>
      <li v-for="value in getValuesForKey('KRW-CVC')" :key="value">{{ value }}</li>
    </ul>
  </div>
</template>

<script setup>
import dynamicCategorizing from "@/assets/coinInfo/DynamicCategorizing.json";

const getKeyForToken = (token) => {
  for (const category in dynamicCategorizing) {
    if (dynamicCategorizing[category].includes(token)) {
      return category;
    }
  }
  return "Token not found";
};

const getValuesForKey = (key) => {
  return dynamicCategorizing[key] || [];
};
</script>
```

In this modified code, the `getValuesForKey` function is introduced, which takes a key (the result from `getKeyForToken`) and returns the array of values associated with that key. The template then iterates through this array and displays each value in an unordered list (`ul`). Adjust the path to `DynamicCategorizing.json` if needed based on your project structure.



<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-40.png)  
* Vue3 Script KRW-NXM Key  
* 20231112051215  
* Description for dev  
* #keyword  
****
The result is then displayed in the template.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-31.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
If you want to check the contents of the `DynamicCategorizing.json` file in JavaScript or Vue, you can use the following code:

```vue
<template>
  <div>
    <pre>{{ JSON.stringify(dynamicCategorizing, null, 2) }}</pre>
  </div>
</template>

<script setup>
import dynamicCategorizing from "@/assets/coinInfo/DynamicCategorizing.json";
</script>
```

This Vue 3 component uses the `JSON.stringify` method to convert the contents of `dynamicCategorizing` into a formatted string  
</div> 
