# **Adjust Button Width**
Sure, to increase the length of the buttons, you can apply custom CSS to adjust the width. Here's an example of how you can modify the button width:

```html
<style>
  .tab-buttons button {
    width: 120px; /* Adjust the width as needed */
    /* Add any other custom styling here */
  }
</style>

<div class="tab-buttons">
  <button @click="changeTab('Hold')" :class="{ active: activeTab === 'Hold' }">Hold</button>
  <button @click="changeTab('WatchList')" :class="{ active: activeTab === 'WatchList' }">WatchList</button>
  <button @click="changeTab('RankList')" :class="{ active: activeTab === 'RankList' }">RankList</button>
</div>
```

Feel free to adjust the width value as per your requirements.




