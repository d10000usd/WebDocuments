# **<span style="font-size: 35px; font-style: italic;">Vue Code Update</span>**


- Vue Code Update  
- 2023년 12월 06일 09시 08분  
- SaaS  
- #article #code #keyword  
- 아래는 그에 대한 수정된 코드입니다:

```html
<template>
  <div class="card mb-2">
    <Markdown @click="toggleContent" :source="truncatedText" :html="true" :breaks="true" :linkify="true"
      :typographer="true" />
    <div v-if="showContent">
      <Markdown :source="remainingText" :html="true" :breaks="true" :linkify="true" :typographer="true" />
    </div>
  </div>
</template>

<style scoped>
</style>

<script setup>
import { ref, onMounted, defineProps, computed } from 'vue';
import Markdown from 'vue3-markdown-it';
import { staticLoadMarkdown } from '../../ts/StaticLoadMarkdown';

const props = defineProps(['title', 'contentUrl']);
const content = ref('');
const showContent = ref(false);
const [fullTitle, label, number, restOfText] = props.title.match(/([^\d]+)(\d+)(.*)/);

const consplit = 400;
const truncatedText = computed(() => {
  // Find the index of "Description" in the content and slice until that point
  const descriptionIndex = content.value.indexOf('Description');
  return content.value.slice(0, descriptionIndex !== -1 ? descriptionIndex : consplit);
});

const remainingText = computed(() => {
  // If "Description" is found, slice from that index, otherwise, slice from consplit
  const descriptionIndex = content.value.indexOf('Description');
  return content.value.slice(descriptionIndex !== -1 ? descriptionIndex : consplit);
});

onMounted(async () => {
  const response = await fetch(props.contentUrl);
  content.value = await response.text();
});

const toggleContent = () => {
  showContent.value = !showContent.value;
};
</script>
```

이 코드는 "Description"을 찾아 해당 부분까지를 표시하고, 그 이후는 남은 부분으로 표시합니다.


      </div></div></div><div style="background-color: grey; height: 15px;"></di  
- [Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
## Description  

<body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  당신의 코드에서 `content.value`에서 "Description" 문자열을 찾아 그 이전까지의 부분을 표시하는 computed 속성을 만들 수 있습니다. 아래는 그에 대한 수정된 코드입니다:

```html
<template>
  <div class="card mb-2">
    <Markdown @click="toggleContent" :source="truncatedText" :html="true" :breaks="true" :linkify="true"
      :typographer="true" />
    <div v-if="showContent">
      <Markdown :source="remainingText" :html="true" :breaks="true" :linkify="true" :typographer="true" />
    </div>
  </div>
</template>

<style scoped>
</style>

<script setup>
import { ref, onMounted, defineProps, computed } from 'vue';
import Markdown from 'vue3-markdown-it';
import { staticLoadMarkdown } from '../../ts/StaticLoadMarkdown';

const props = defineProps(['title', 'contentUrl']);
const content = ref('');
const showContent = ref(false);
const [fullTitle, label, number, restOfText] = props.title.match(/([^\d]+)(\d+)(.*)/);

const consplit = 400;
const truncatedText = computed(() => {
  // Find the index of "Description" in the content and slice until that point
  const descriptionIndex = content.value.indexOf('Description');
  return content.value.slice(0, descriptionIndex !== -1 ? descriptionIndex : consplit);
});

const remainingText = computed(() => {
  // If "Description" is found, slice from that index, otherwise, slice from consplit
  const descriptionIndex = content.value.indexOf('Description');
  return content.value.slice(descriptionIndex !== -1 ? descriptionIndex : consplit);
});

onMounted(async () => {
  const response = await fetch(props.contentUrl);
  content.value = await response.text();
});

const toggleContent = () => {
  showContent.value = !showContent.value;
};
</script>
```

이 코드는 "Description"을 찾아 해당 부분까지를 표시하고, 그 이후는 남은 부분으로 표시합니다.


      </div></div></div><div style="background-color: grey; height: 15px;"></div>

  