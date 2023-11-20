# **<span style="font-size: 35px; font-style: italic;">WebSocketService: Accessing Values</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-36.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 5</div></div>
Certainly! Here are 10 alternative ways to access the value with the key "KRW-BTC" from the map:

1. Using Array Destructuring:
   ```javascript
   const [coinData] = [...data].find(([key]) => key === "KRW-BTC") || [];
   ```

2. Using Object Destructuring:
   ```javascript
   const { 'KRW-BTC': coinData } = Object.fromEntries(data);
   ```

3. Using forEach:
   ```javascript
   let coinData;
   data.forEach((value, key) => {
     if (key === "KRW-BTC") coinData = value;
   });
   ```

4. Using Array Filter:
   ```javascript
   const coinData = [...data].filter(([key]) => key === "KRW-BTC")[0]?.[1];
   ```

5. Using for...of loop:
   ```javascript
   let coinData;
   for (const [key, value] of data) {
     if (key === "KRW-BTC") {
       coinData = value;
       break;
     }
   }
   ```

6. Using reduce:
   ```javascript
   const coinData = [...data].reduce((acc, [key, value]) => (key === "KRW-BTC" ? value : acc), undefined);
   ```

7. Using Map.entries and next:
   ```javascript
   const coinData = data.entries().next().value[1];
   ```

8. Using Map.forEach:
   ```javascript
   let coinData;
   data.forEach((value, key) => {
     if (key === "KRW-BTC") coinData = value;
   });
   ```

9. Using Map.keys and next:
   ```javascript
   const coinData = data.keys().next().value;
   ```

10. Using Map.values and next:
    ```javascript
    const coinData = data.values().next().value;
    ```

Choose the one that fits your coding style and preferences!







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-34.png)  
* WebSocketService: Accessing Values  
* 20231116052718  
* Description for dev  
* #keyword  
****
Using Object Destructuring:
   ```javascript
   const { 'KRW-BTC': coinData } = Object.fromEntries(data);
   ```

3  
</div> 
