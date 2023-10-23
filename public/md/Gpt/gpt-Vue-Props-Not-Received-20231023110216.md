# **<span style="font-size: 35px; font-style: italic;">Vue Props Not Received</span>**


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

프로프를 올바르게 받지 못하는 문제를 해결하려면 몇 가지 가능한 방법이 있습니다. Vue 3에서 프로프를 올바르게 받는 방법에 대해 설명하겠습니다.

1. **`defineProps`를 사용**:

   `setup` 블록에서 `props`를 정의할 때 `defineProps` 함수를 사용하여 props를 명시적으로 선언해야 합니다. 이렇게 하면 Vue가 프로프를 올바르게 추적하고 관리합니다.

   예를 들어, 다음과 같이 수정할 수 있습니다:

   ```vue
   <script setup>
     import { ref } from 'vue'
     import { defineProps } from 'vue'
     import GitGetOnlineUseUrl from "../components/body/GitGetOnlineUseUrl.vue"

     // Define props to receive data from RouterLink
     const props = defineProps({
       receivedRouteName: String, // Define the type of data being received
     })

     const selectNo = ref(38)
     const st = 'https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/md/Gpt/gpt-All-Divide-HTML-into-Columns-2023.md'
   </script>
   ```

2. **템플릿에서 props 사용**:

   템플릿 부분에서 `props`를 사용할 때 중괄호 `{}`로 감싸야 합니다. 이렇게 하면 Vue가 해당 변수를 props로 인식합니다. 예를 들어:

   ```vue
   <template>
     <p>Received route name: {{ props.receivedRouteName }}</p>
     <GitGetOnlineUseUrl :message="'넘버로 랜덤 선택'" :gitnum="Number(selectNo)" :burl="st" />
   </template>
   ```

위의 두 가지 수정을 통해 프로프를 올바르게 받아올 수 있어야 합니다. 만약 문제가 계속되면 추가 정보를 제공해 주시면 더 자세한 도움을 드릴 수 있습니다.


</div>