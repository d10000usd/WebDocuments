# **Vue.js Variable Declaration**
When using the `script setup` syntax in Vue 3, the way you define data properties is slightly different. Here's how you can define the `selectedCoinTicker` property within the `script setup` block:

```vue
<script setup>
import { ref } from 'vue';

// Define the selectedCoinTicker property using ref
const selectedCoinTicker = ref(null);

// Rest of your code...

</script>
```

By using the `ref` function from Vue, you can create a reactive reference to the `selectedCoinTicker` property. Make sure to include the rest of your code within the `script setup` block accordingly.




