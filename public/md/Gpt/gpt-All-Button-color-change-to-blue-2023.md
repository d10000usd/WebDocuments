# **<span style="font-size: 35px; font-style: italic;">Button color change to blue</span>**

> ## 1
The code you provided appears to be a Vue.js template with some Bootstrap styling for buttons. It seems like you want to change the button color to blue when clicked. To achieve this, you can use Bootstrap's built-in classes for button states.

Here's how you can modify your code to make the buttons turn blue when clicked:

```vue
<template>
  <!-- ... (Your existing template code) ... -->
  <div class="coin-card-container-wrapper div-block-space-style">
    <div class="coin-card-container">
      <div v-for="(casad, index) in Object.values(rankcoins)" :key="index">
        <!-- Add the btn-primary class to change the button color to blue -->
        <button @click="showTicker(casad)" class="col-md-11 btn-sm rounded-button btn btn-outline-primary">{{
          removeKRW(casad) }}</button>
      </div>
    </div>
  </div>
  <!-- ... (The rest of your template) ... -->
</template>

<style scoped>
  /* ... (Your existing CSS styles) ... */

  /* Style for the clicked button (Active state) */
  .btn-outline-primary:active,
  .btn-outline-primary.active {
    background-color: blue; /* Change the background color to blue */
    color: white; /* Change the text color to white */
  }
</style>
```

In this code, I added the `btn btn-outline-primary` classes to the buttons inside your template. When a button is clicked, Bootstrap's `:active` and `.active` states will apply, which will change the background color to blue and the text color to white. This will give the appearance of a blue button when clicked.

Make sure to include Bootstrap's CSS and JavaScript in your project for this styling to work correctly.
*****



> ## 2
Certainly! Here's your Vue.js template with all the styles included:

```vue
<template>
  <div class="container-ml">
    <!-- Display Selected Values -->
    <StaticsModule :message="selectedCoinTicker" :key="selectedCoinTicker" />

    <div class="div-block-space-style">
      {{ selectedCode }}-{{ sliderValue }}-{{ selectedTimeframeKey }}
    </div>

    <!-- Buttons Container -->
    <div class="coin-card-container-wrapper div-block-space-style">
      <div class="coin-card-container">
        <div v-for="(timeframeKey, index) in Object.keys(timeframe)" :key="index">
          <button @click="showTimeframe(timeframeKey)" class="btn-sm rounded-button btn btn-outline-primary">{{ removeMinutes(timeframeKey) }}</button>
        </div>
      </div>
    </div>
    <div class="coin-card-container-wrapper div-block-space-style">
      <div class="coin-card-container">
        <div v-for="(casad, index) in Object.values(rankcoins)" :key="index">
          <button @click="showTicker(casad)" class="col-md-11 btn-sm rounded-button btn btn-outline-primary">{{ removeKRW(casad) }}</button>
        </div>
      </div>
    </div>
    <div class="coin-card-container-wrapper div-block-space-style">
      <div class="coin-card-container">
        <div v-for="(casad, index) in Object.values(balances)" :key="index">
          <button @click="showTicker(casad)" class="col-md-11 btn-sm rounded-button btn btn-outline-primary">{{ removeKRW(casad) }}</button>
        </div>
      </div>
    </div>

    <button @click="updateSelectedCoinTicker" class="btn-sm rounded-button btn btn-outline-primary">Update Coin Ticker</button>

    <!-- Slider Input -->
    <div class="container-xxl m-1 text-center">
      <input type="range" v-model="sliderValue" min="0" max="5000" @input="updateCnt" class="w-100" />
      <p>[캔들갯수 {{ sliderValue }}] 상단차트는 설정값 차트, 하단은 7일기준 몫+나머지</p>
    </div>
  </div>
</template>

<style scoped>
  .container-ml {
    /* Add your container styles here */
  }

  .div-block-space-style {
    text-align: center;
    font-size: 15px;
    background-color: #ebebeb;
    margin-top: 9px;
    margin-bottom: 9px;
    margin: 1 auto;
    /* Add your div styles here */
  }

  .coin-card-container-wrapper {
    overflow-x: scroll;
    white-space: nowrap;
    scrollbar-width: thin;
    scrollbar-color: transparent;
    -ms-overflow-style: none;
    display: flex;
    justify-content: left;
    /* Add your wrapper styles here */
  }

  .coin-card-container {
    display: inline-flex;
    flex-wrap: nowrap;
    margin-right: 0.1px;
    scrollbar-width: none;
    scrollbar-color: transparent;
    -ms-overflow-style: none;
    /* Add your container styles here */
  }

  /* Add more styles as needed */

  /* Style for the clicked button (Active state) */
  .btn-outline-primary:active,
  .btn-outline-primary.active {
    background-color: blue;
    color: white;
  }

  .rounded-button {
    border-radius: 13px;
    font-size: 174px;
    /* Add your button styles here */
  }

  .chart-container {
    width: 100%;
    height: 120%;
    background-color: #f0f0f0;
    border: 1px solid #000;
    /* Add your chart container styles here */
  }
</style>
```

You can customize the styles for each element by adding or modifying the CSS rules within the `<style>` section. Please replace the comments like `/* Add your container styles here */` with your desired styles.
*****



