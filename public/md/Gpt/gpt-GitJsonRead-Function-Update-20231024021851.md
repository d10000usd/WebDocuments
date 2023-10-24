# **<span style="font-size: 35px; font-style: italic;">GitJsonRead Function Update</span>**


<div class="body-full">

위의 코드에서 발생하는 오류는 `ref`를 사용할 때 발생하는 문제입니다. `ref`를 사용할 때는 값을 설정할 때에는 `.value` 속성을 사용해야 합니다. 또한, `mk` 변수가 `ref`로 정의되었기 때문에 `.value`를 사용하여 값을 할당해야 합니다. 아래의 수정된 코드를 참고해 주세요.

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

이제 위의 수정된 코드를 사용하여 오류를 해결할 수 있어야 합니다.


</div>