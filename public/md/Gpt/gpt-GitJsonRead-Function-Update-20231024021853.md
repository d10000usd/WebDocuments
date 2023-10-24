# **<span style="font-size: 35px; font-style: italic;">GitJsonRead Function Update</span>**


<div class="body-full">

오류가 발생한 이유는 `ref`가 `vue`에서 가져오지 않았기 때문입니다. Vue 3에서 `ref`를 사용하려면 해당 모듈을 가져와야 합니다. 아래 코드를 참고하여 수정해 보세요.

```vue
<template>
  <div>
    {{ path }}
    {{ mk }}
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { GitJsonRead } from '../ts/StaticLoadMarkdown';
import mkdocs_posts_nav from "../../public/md/mkdocs_posts_nav.json";

// Call the function
let path = mkdocs_posts_nav.Public.md[0].Gpt[1];
const mk = ref('');

const localpath = path; // Replace with your desired file path
GitJsonRead(localpath)
    .then(text => {
        console.log("Successfully fetched text:", text);
        mk.value = text; // Set the value using .value
        // Perform the desired operations using the fetched text
    })
    .catch(error => {
        console.error("Error occurred:", error);
        // Perform appropriate error handling in case of an error
    });
</script>
```

위 코드에서 `import { ref } from 'vue'`를 통해 `ref`를 가져오도록 했습니다. 이제 코드가 정상적으로 작동해야 합니다.


</div>