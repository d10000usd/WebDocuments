# **<span style="font-size: 35px; font-style: italic;">Align Components Bootstrap Grid</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-34.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 4</div></div>
To align the `StaticsChart_realtimeOnly` to the left using Bootstrap and arrange the entire layout in two columns, you can use the following code structure:

```html
<div class="container">
  <div class="row">
    <div class="col-md-6">
      <!-- StaticsChart_realtimeOnly component here -->
      <StaticsChart_realtimeOnly/>
    </div>
    <div class="col-md-6">
      <div class="ml-1">
        <!-- Your existing code for the tab buttons and slider component -->
        <div class="tab-buttons">
          <button @click="changeTab('Hold')" :class="{ active: activeTab === 'Hold' }">Hold</button>
          <button @click="changeTab('WatchList')" :class="{ active: activeTab === 'WatchList' }">WatchList</button>
          <button @click="changeTab('RankList')" :class="{ active: activeTab === 'RankList' }">RankList</button>
        </div>
        <!-- Slider component with value display -->
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
      </div>
    </div>
  </div>
</div>
```

This code snippet creates a two-column layout using Bootstrap classes. The `StaticsChart_realtimeOnly` component is placed in the left column, and the rest of your existing code is in the right column. Adjust the classes and styles as needed to achieve the desired appearance.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-40.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 3</div></div>
슬라이더를 수직으로 표시하려면 몇 가지 CSS 스타일을 조정해야 합니다. 아래는 이를 구현하기 위한 예시 코드입니다.

```html
<style>
  .slider-container {
    writing-mode: bt-lr; /* 세로로 텍스트와 레이아웃을 배치합니다. */
    transform: rotate(180deg); /* 슬라이더를 180도 회전하여 수직으로 표시합니다. */
  }

  .slider-container input[type="range"] {
    writing-mode: bt-lr; /* 세로로 텍스트와 레이아웃을 배치합니다. */
    transform: rotate(180deg); /* 슬라이더를 180도 회전하여 수직으로 표시합니다. */
  }
</style>

<div class="container-xxl m-1 text-center slider-container"> <!-- text-center 클래스를 추가하여 가운데 정렬 -->
  <input type="range" v-model="sliderValue" min="0" max="5000" @input="updateCnt" class="w-100" />
  <!-- w-100 클래스를 추가하여 슬라이더의 가로 길이를 최대로 늘립니다. -->
  <p> [캔들갯수 {{ sliderValue }}] 상단차트는 설정값 차트, 하단은 7일기준 몫+나머지</p>
</div>
```

위의 CSS 스타일은 `slider-container` 클래스를 사용하여 슬라이더를 수직으로 배치합니다. 이 코드를 적용하면 슬라이더가 수직으로 표시될 것입니다.



<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-31.png)  
* Align Components Bootstrap Grid  
* 20231109085317  
* Description for dev  
* #keyword  
****
Adjust the classes and styles as needed to achieve the desired appearance.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-40.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 3</div></div>
슬라이더를 수직으로 표시하려면 몇 가지 CSS 스타일을 조정해야 합니다  
</div> 
