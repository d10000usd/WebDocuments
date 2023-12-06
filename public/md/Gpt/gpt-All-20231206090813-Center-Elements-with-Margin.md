# **<span style="font-size: 35px; font-style: italic;">Center Elements with Margin</span>**


- Center Elements with Margin  
- 2023년 12월 06일 09시 08분  
- SaaS  
- #article #code #keyword  
- This class includes a `margin` property with `111px` at the top and `auto` for horizontal cente  
- [Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
## Description  

<body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  To center the elements inside the `<div>`, you can use the following modifications to your existing code:

```html
<template>

    <div class="div-flex spacing-mt"> <!-- Added spacing-mt class -->
      <p @click="toggleContent">
        <h4>{{ restOfText }}</h4>
      </p>
      <p class="right-aligned">{{ number }}</p>
    </div>

    <div v-if="showContent" class="spacing-mt"> <!-- Added spacing-mt class -->
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
.spacing-mt {
    margin: 111px auto; /* Added auto to center horizontally */
  }
.div-flex {
  display: flex;
  justify-content: space-between;
}

.right-aligned {
  margin-left: auto;
}
</style>
```

I added the `spacing-mt` class to both the main `div` and the content `div`. This class includes a `margin` property with `111px` at the top and `auto` for horizontal centering. Adjust the margin value as needed for your layout.


      </div></div></div><div style="background-color: grey; height: 15px;"></div>

  