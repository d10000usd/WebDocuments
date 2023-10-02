PROMPT:

<template> <MainLayoutComp> <div> <h2>Category: Gpt</h2> <ul> <li v-for="(item, index) in Gpt\_Items.Gpt" :key="index"> <a href="#" @click="selectItem(item)">{{ item }}</a> </li> </ul> <h2>Category: Post</h2> <ul> <li v-for="(item, index) in Post\_Items.Post" :key="index"> <a href="#" @click="selectItem(item)">{{ item }}</a> </li> </ul> <h2>Category: Usage</h2> <ul> <li v-for="(item, index) in Usage\_Items.Usage" :key="index"> <a href="#" @click="selectItem(item)">{{ extractFileName(item )}}</a> </li> </ul> </div> <Markdown :source="fileContent" v-if="selectedItem" /> </MainLayoutComp> </template> <script setup> import MainLayoutComp from './MainLayoutComp.vue' import Markdown from 'vue3-markdown-it'; import { ref, onMounted } from 'vue'; import hljs from 'highlight.js/lib/core'; import 'highlight.js/styles/github-dark-dimmed.css'; import mkdocs\_posts\_nav from "../../mkdocs\_posts\_nav.json"; import javascript from 'highlight.js/lib/languages/javascript'; hljs.registerLanguage('javascript', javascript); const Gpt\_Items = mkdocs\_posts\_nav.MD\[0\]; const Post\_Items = mkdocs\_posts\_nav.MD\[1\]; const Usage\_Items = mkdocs\_posts\_nav.MD\[2\]; const selectedCategory = ref(''); const selectedItem = ref(null); const fileContent = ref(''); const selectItem = (item) => { selectedCategory.value = getCategoryFromItem(item); selectedItem.value = item; loadMarkdownFile(item); }; const getCategoryFromItem = (item) => { if (Gpt\_Items.Gpt.includes(item)) { return 'Gpt'; } else if (Post\_Items.Post.includes(item)) { return 'Post'; } else if (Usage\_Items.Usage.includes(item)) { return 'Usage'; } return ''; }; const loadMarkdownFile = async (item) => { try { console.log(item); const response = await fetch(\`../public/${item}\`); const text = await response.text(); fileContent.value = text; } catch (error) { console.error(error); } }; onMounted(() => { fileContent.value = 'File content goes here'; }); </script> <style scoped> .container { margin-left: auto; margin-right: auto; } </style> extractFileName 파일이름만 분리해서 표시 하는 함수 추가 해줘

RESPONSE:

To extract only the file name from a given path and display it, you can add a function called `extractFileName` to your Vue component. Here's an updated version of your code with the `extractFileName` function added:

```vue
<template>
  <MainLayoutComp>
    <div>
      <h2>Category: Gpt</h2>
      <ul>
        <li v-for="(item, index) in Gpt_Items.Gpt" :key="index">
          <a href="#" @click="selectItem(item)">{{ item }}</a>
        </li>
      </ul>

      <h2>Category: Post</h2>
      <ul>
        <li v-for="(item, index) in Post_Items.Post" :key="index">
          <a href="#" @click="selectItem(item)">{{ item }}</a>
        </li>
      </ul>

      <h2>Category: Usage</h2>
      <ul>
        <li v-for="(item, index) in Usage_Items.Usage" :key="index">
          <a href="#" @click="selectItem(item)">{{ extractFileName(item) }}</a>
        </li>
      </ul>
    </div>

    <Markdown :source="fileContent" v-if="selectedItem" />
  </MainLayoutComp>
</template>

<script setup>
import MainLayoutComp from './MainLayoutComp.vue'
import Markdown from 'vue3-markdown-it';
import { ref, onMounted } from 'vue';
import hljs from 'highlight.js/lib/core';
import 'highlight.js/styles/github-dark-dimmed.css';
import mkdocs_posts_nav from "../../mkdocs_posts_nav.json";

import javascript from 'highlight.js/lib/languages/javascript';
hljs.registerLanguage('javascript', javascript);

const Gpt_Items = mkdocs_posts_nav.MD[0];
const Post_Items = mkdocs_posts_nav.MD[1];
const Usage_Items = mkdocs_posts_nav.MD[2];

const selectedCategory = ref('');
const selectedItem = ref(null);
const fileContent = ref('');

const selectItem = (item) => {
  selectedCategory.value = getCategoryFromItem(item);
  selectedItem.value = item;
  loadMarkdownFile(item);
};

const getCategoryFromItem = (item) => {
  if (Gpt_Items.Gpt.includes(item)) {
    return 'Gpt';
  } else if (Post_Items.Post.includes(item)) {
    return 'Post';
  } else if (Usage_Items.Usage.includes(item)) {
    return 'Usage';
  }
  return '';
};

const loadMarkdownFile = async (item) => {
  try {
    console.log(item);
    const response = await fetch(`../public/${item}`);
    const text = await response.text();
    fileContent.value = text;
  } catch (error) {
    console.error(error);
  }
};

const extractFileName = (item) => {
  const filePathParts = item.split('/');
  return filePathParts[filePathParts.length - 1];
};

onMounted(() => {
  fileContent.value = 'File content goes here';
});
</script>

<style scoped>
.container {
  margin-left: auto;
  margin-right: auto;
}
</style>
```

In the updated code, the `extractFileName` function takes an `item` as input, splits it by the forward slash ('/') to get an array of path segments, and then returns the last segment, which represents the file name. The `extractFileName` function is called within the `v-for` loop in the "Category: Usage" section to display only the file name instead of the full path.

Make sure to include the updated code in your Vue component and test it to see the file names extracted and displayed

PROMPT:

const extractFileName = (item) => { const filePathParts = item.split('/'); return filePathParts\[filePathParts.length - 1\]; }; 확장자도 빼고 이름만 출력되게 수정

RESPONSE:

To remove the file extension from the extracted file name, you can modify the `extractFileName` function as follows:

```javascript
const extractFileName = (item) => {
  const filePathParts = item.split('/');
  const fileNameWithExtension = filePathParts[filePathParts.length - 1];
  const fileName = fileNameWithExtension.split('.')[0]; // Remove the file extension
  return fileName;
};
```

In the updated code, after splitting the file path into segments, we retrieve the last segment, which includes the file name with the extension. Then, we further split this segment using the dot ('.') as the separator. The first element of the resulting array will be the file name without the extension. We return this file name from the `extractFileName` function.

By applying this modification, the `extractFileName` function will return only the file name without the extension when called within the Vue component's template.