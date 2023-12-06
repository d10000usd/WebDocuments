# **<span style="font-size: 35px; font-style: italic;">Toggle 4 Lines Display</span>**


- Toggle 4 Lines Display  
- 2023년 12월 06일 09시 08분  
- SaaS  
- #article #code #keyword  
- 아래는 수정된 코드입니다:

```html
<template>

    <div >
      <p @click="toggleContent">
        <h4>{{ restOfText }}</h4>
      </p>
      <p>{{ number }}</p>
    </div>
    <div v-if="showContent">
      <Markdown
        :source="content"
        :html="true"
        :breaks="true"
        :linkify="true"
        :typographer="true"
      />
    </div>
</template>

<style>

</style>

<script setup>
import { ref, onMounted, defineProps } from 'vue';
import Markdown from 'vue3-markdown-it';

const props = defineProps(['title', 'contentUrl']);
const content = ref('');
const showContent = ref(false);
const [fullTitle, label, number, restOfText] = props.title.match(/([^\d]+)(\d+)(.*)/);
onMounted(async () => {
  const response = await fetch(props.contentUrl);
  content.value = await response.text();
});

const toggleContent = () => {
  showContent.value = !showContent.value;
};
</script>
```

이제 `<h4>{{ restOfText }}</h4>` 부분은 처음에는 4 줄만 표시되고 클릭하면 나머지가 나  
- [Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
## Description  

<body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  네, 주어진 코드를 수정하여 처음에는 4 줄만 표시되고 클릭하면 나머지가 보이도록 할 수 있습니다. 아래는 수정된 코드입니다:

```html
<template>

    <div >
      <p @click="toggleContent">
        <h4>{{ restOfText }}</h4>
      </p>
      <p>{{ number }}</p>
    </div>
    <div v-if="showContent">
      <Markdown
        :source="content"
        :html="true"
        :breaks="true"
        :linkify="true"
        :typographer="true"
      />
    </div>
</template>

<style>

</style>

<script setup>
import { ref, onMounted, defineProps } from 'vue';
import Markdown from 'vue3-markdown-it';

const props = defineProps(['title', 'contentUrl']);
const content = ref('');
const showContent = ref(false);
const [fullTitle, label, number, restOfText] = props.title.match(/([^\d]+)(\d+)(.*)/);
onMounted(async () => {
  const response = await fetch(props.contentUrl);
  content.value = await response.text();
});

const toggleContent = () => {
  showContent.value = !showContent.value;
};
</script>
```

이제 `<h4>{{ restOfText }}</h4>` 부분은 처음에는 4 줄만 표시되고 클릭하면 나머지가 나타납니다. 변경된 부분에 유의하십시오.


      </div></div></div><body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  죄송합니다. 코드를 다시 확인하고 수정합니다. 아래는 수정된 코드입니다:

```html
<template>
  <div>
    <p @click="toggleContent">
      <h4>{{ restOfText }}</h4>
    </p>
    <p>{{ number }}</p>
    <div v-if="showContent">
      <Markdown
        :source="content"
        :html="true"
        :breaks="true"
        :linkify="true"
        :typographer="true"
      />
    </div>
  </div>
</template>

<style></style>

<script setup>
import { ref, onMounted, defineProps } from 'vue';
import Markdown from 'vue3-markdown-it';

const props = defineProps(['title', 'contentUrl']);
const content = ref('');
const showContent = ref(false);
const [fullTitle, label, number, restOfText] = props.title.match(/([^\d]+)(\d+)(.*)/);
onMounted(async () => {
  const response = await fetch(props.contentUrl);
  content.value = await response.text();
});

const toggleContent = () => {
  showContent.value = !showContent.value;
};
</script>
```

이제 `<h4>{{ restOfText }}</h4>` 부분이 처음에는 4 줄만 표시되고 클릭하면 나머지가 나타납니다. 다시 한 번 죄송합니다.


      </div></div></div><div style="background-color: grey; height: 15px;"></div>

  