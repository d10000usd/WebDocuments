# **<span style="font-size: 35px; font-style: italic;">Vue Router Variables</span>**


<style>
.body-full {
    overflow-x: hidden;
    margin: .21rem;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Apple SD Gothic Neo", Arial, sans-serif;
    font-weight: 500;
    position: relative;
    word-break: break-all;
    -webkit-text-size-adjust: none;
    background-color: #eaeef3;
    color: #474787;
    font-size: 16px;
    line-height: 19px;
    border-color: white;
    }
</style>
<div class="body-full">

`Body_view` 컴포넌트에서는 `props`를 사용하여 `RouterLink`로부터 전달된 데이터를 받을 수 있습니다. 다음은 `Body_view` 컴포넌트에서 `props`를 사용하는 방법에 대한 예제입니다:

```vue
<template>
  <div>
    <h2>Body View Component</h2>
    <p>This is the body view component.</p>
    <p>Received route name: {{ receivedRouteName }}</p>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

// Define props to receive data from RouterLink
const props = defineProps({
  receivedRouteName: String, // Define the type of data being received
})
</script>

<style scoped>

</style>
```

위 코드에서 `defineProps`를 사용하여 `receivedRouteName`이라는 이름으로 데이터를 받을 수 있도록 `props`를 정의합니다. 그런 다음 해당 데이터를 템플릿 부분에서 사용할 수 있습니다. 이제 `Body_view` 컴포넌트는 `RouterLink`로부터 전달된 데이터를 `receivedRouteName`으로 받게 됩니다. 이 데이터를 템플릿에서 필요한 곳에 적용할 수 있습니다.


</div>