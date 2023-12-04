# **<span style="font-size: 35px; font-style: italic;">Center Elements with Margin</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-38.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 1</div></div>
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



<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-35.png)  
* Center Elements with Margin  
* 20231204115304  
* Description for dev  
* #keyword  
****
Adjust the margin value as needed for your layout.



<div style="background-color: grey; height: 15px;"></div>

  
</div> 
