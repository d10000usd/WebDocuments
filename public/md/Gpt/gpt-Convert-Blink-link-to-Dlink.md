PROMPT:

blink= "https://raw.githubusercontent.com/jwasham/coding-interview-university/main/README.md" dlink = "https://github.com/jwasham/coding-interview-university/blob/main/README.md" blink 에서, dlink 형태로 변경하는 vue3 , script setup 에 함수 코드

RESPONSE:

Vue 3 with the `<script setup>` syntax allows you to write your component code more concisely. Here's an example of a function that converts a Blink link to a Dlink format:

```vue
<template>
  <div>
    <!-- Your template code here -->
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Function to convert Blink link to Dlink format
const convertLink = (blinkLink) => {
  const baseUrl = 'https://github.com'
  const pathRegex = /https?:\/\/github\.com\/([^/]+)\/([^/]+)\/blob\/([^/]+)\/(.+)/
  const [, user, repo, branch, filePath] = blinkLink.match(pathRegex)
  const dlink = `${baseUrl}/${user}/${repo}/${branch}/${filePath}`
  return dlink
}

// Usage example
const blink = ref("https://raw.githubusercontent.com/jwasham/coding-interview-university/main/README.md")
const dlink = ref(convertLink(blink.value))
</script>
```

In the code above, we define a function called `convertLink` that takes a Blink link as an argument and converts it to the Dlink format using regular expressions. We import the `ref` function from Vue for reactive properties.

Then, we create a `blink` reactive property with an initial value of your Blink link. We also create a `dlink` reactive property that calls the `convertLink` function with the `blink` value. The converted Dlink value will be stored in the `dlink` property.

Remember to replace the `<!-- Your template code here -->` placeholder with your actual template code. This code can be used inside a Vue 3 component using the `<script setup>` syntax.