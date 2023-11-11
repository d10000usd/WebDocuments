# **Dynamic Upbit Coin Fetch**
```html
<template>
  <div class="row">
    <div class="col-4 col-md-3"> <!-- This sets up a 5-column layout on medium-sized screens (col-md-3) -->
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">{{ showingIframe ? message.code : props.message.code.split('-')[1] }}</h5>
          <p class="card-text">Change Rate: {{ (props.message.signed_change_rate * 100).toFixed(2) }}%</p>
          <p class="card-text">Accumulated Ask Volume: {{ props.message.acc_ask_volume.toFixed(2) }}</p>
          <!-- Include more information here if needed -->
          <p class="card-text">Trade Price: {{ props.message.trade_price }}</p>
          <p class="card-text">Opening Price: {{ props.message.opening_price }}</p>
          <p class="card-text">Highest 52-week Price: {{ props.message.highest_52_week_price }}</p>
          <p class="card-text">Lowest 52-week Price: {{ props.message.lowest_52_week_price }}</p>
          <p class="card-text">Trade Volume: {{ props.message.trade_volume.toFixed(2) }}</p>
          <p class="card-text">Type: {{ props.message.type }}</p>
          <p class="card-text">Timestamp: {{ props.message.timestamp }}</p>
          <!-- Add more fields if needed -->
        </div>
      </div>
    </div>
  </div>
</template>
```

This modified code uses Bootstrap to style and structure the card layout for displaying the information from `props.message`. Adjust the fields displayed as needed, and add more fields if required to accommodate the data appropriately.




