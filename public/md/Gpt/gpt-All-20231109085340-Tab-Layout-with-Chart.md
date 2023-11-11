# **<span style="font-size: 35px; font-style: italic;">Tab Layout with Chart</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-30.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 1</div></div>
To display the chart in two columns with the chart on the right, you can utilize CSS flexbox or grid. Here's an example of how you can achieve this using CSS grid:

```html
<div class="ml-1" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">

  <div class="tab-buttons">
    <button @click="changeTab('Hold')" :class="{ active: activeTab === 'Hold' }">Hold</button>
    <button @click="changeTab('WatchList')" :class="{ active: activeTab === 'WatchList' }">WatchList</button>
    <button @click="changeTab('RankList')" :class="{ active: activeTab === 'RankList' }">RankList</button>
  </div>

  <!-- Slider component with value display using Bootstrap classes -->
  <div class="d-flex align-items-center my-3">
    <input type="range" min="1" max="130" v-model="sliderValue" @input="updateSliceNumber" class="form-range" style="width: 100%" />
    <span class="mx-3 badge bg-secondary">{{ sliderValue }}</span>
  </div>

  <!-- Tab content -->
  <div class="coin-card-container-wrapper">
    <div class="coin-card-container">
      <div v-for="coinInfo in sortedActiveTabCoins" :key="coinInfo.code">
        <!-- {{ console.log(coinInfo.signed_change_rate) }} -->
        <PluginType_Tab :message="coinInfo"></PluginType_Tab>
      </div>
    </div>
  </div>

  <!-- Your chart component here -->
  <StaticsChart_realtimeOnly/>

</div>
```

In this example, the outermost `div` has a CSS style attribute that uses `display: grid` and `grid-template-columns` to create a two-column layout. The `gap` property adds space between the columns. Make sure to adjust the styling and dimensions according to your specific layout requirements.



<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-38.png)  
* Tab Layout with Chart  
* 20231109085340  
* Description for dev  
* #keyword  
****
The `gap` property adds space between the columns  
</div> 
