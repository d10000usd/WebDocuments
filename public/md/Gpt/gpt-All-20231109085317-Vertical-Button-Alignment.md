# **<span style="font-size: 35px; font-style: italic;">Vertical Button Alignment</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-36.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
버튼이 수직으로 들어가게 하려면 CSS를 사용하여 요소를 수직으로 배치해야 합니다. 아래는 예시 코드입니다. 이 코드를 해당 요소에 적용하여 수직 정렬을 구현할 수 있습니다.

```html
<style>
  .coin-card-container-wrapper {
    display: flex;
    flex-direction: column;
  }
</style>

<div class="coin-card-container-wrapper div-block-space-style">
  <div class="coin-card-container">
    <div v-for="(timeframeKey, index) in Object.keys(timeframe)" :key="index">
      <button @click="showTimeframe(timeframeKey)" class="btn-sm rounded-button btn-outline-primary">{{ removeMinutes(timeframeKey) }}</button>
    </div>
  </div>
</div>
```

위의 CSS 스타일은 `coin-card-container-wrapper` 클래스를 가진 요소를 수직으로 배치합니다. 이것은 버튼이 수직으로 배열되도록 합니다. 이 코드를 적용하면 버튼이 수직으로 정렬될 것입니다.





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
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-33.png)  
* Vertical Button Alignment  
* 20231109085317  
* Description for dev  
* #keyword  
****
이 코드를 해당 요소에 적용하여 수직 정렬을 구현할 수 있습니다.

```html
<style>
  .coin-card-container-wrapper {
    display: flex;
    flex-direction: column;
  }
</style>

<div class="coin-card-container-wrapper div-block-space-style">
  <div class="coin-card-container">
    <div v-for="(timeframeKey, index) in Object.keys(timeframe)" :key="index">
      <button @click="showTimeframe(timeframeKey)" class="btn-sm rounded-button btn-outline-primary">{{ removeMinutes(timeframeKey) }}</button>
    </div>
  </div>
</div>
```

위의 CSS 스타일은 `coin-card-container-wrapper` 클래스를 가진 요소를 수직으로 배치합니다  
</div> 
