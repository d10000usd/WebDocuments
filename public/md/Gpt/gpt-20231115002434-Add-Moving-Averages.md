# **<span style="font-size: 35px; font-style: italic;">Add Moving Averages</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-30.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 5</div></div>
Certainly! To add the moving average lines to your chart using `chartOptions.movingAverages`, you can modify your existing code like this:

```javascript
// ... your existing code ...

const chartOptions = {
  // ... your existing options ...

  "movingAverages": {
    "ma5": {
      "color": "rgba(255, 0, 0, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma35": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma65": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma95": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma125": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma155": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma185": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma215": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma245": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    }
  },

  // ... your existing options ...
};

// ... your existing code ...
```

In this modified code, the moving average lines are included under the "movingAverages" key within `chartOptions`. Adjust the color, line width, and other properties as needed for each moving average. Make sure to replace the existing `chartOptions` definition in your script with this modified version.







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-31.png)  
* Add Moving Averages  
* 20231115002434  
* Description for dev  
* #keyword  
****
your existing options ...

  "movingAverages": {
    "ma5": {
      "color": "rgba(255, 0, 0, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma35": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma65": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma95": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma125": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma155": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma185": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma215": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    },
    "ma245": {
      "color": "rgba(0, 244, 255, 1)",
      "lineWidth": 2,
      "priceLineVisible": false
    }
  },

  // ..  
</div> 
