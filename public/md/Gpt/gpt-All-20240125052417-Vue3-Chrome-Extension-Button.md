# **<span style="font-size: 35px; font-style: italic;">Vue3 Chrome Extension Button</span>**

>Vue3 Chrome Extension Button  
2024년 01월 25일 05시 24분  
SaaS  
#article #code #keyword  
[Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
Here’s a brief explanation read more
## Description  

<body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  Sure, to achieve that using Vue 3 with the `script setup` syntax for a Chrome extension, you can follow these steps:

1. Create a new Vue component, let's say `Popup.vue`, and use the `script setup` syntax.

```vue
<template>
  <div>
    <!-- Your other components or elements here -->

    <button @click="insertRedButton">Insert Red Button</button>
  </div>
</template>

<script setup>
const insertRedButton = () => {
  const textarea = document.querySelector('textarea#prompt-textarea');

  // Check if the textarea exists before proceeding
  if (textarea) {
    const redButton = document.createElement('button');
    redButton.style.backgroundColor = 'red';
    redButton.innerText = 'Red Button';

    // You can customize the button styling further if needed

    // Append the button to the textarea's parent node
    textarea.parentNode.appendChild(redButton);
  }
};
</script>
```

2. Import and use this component in your `popup.html` or wherever your popup content is defined.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Your other head elements here -->
  </head>
  <body>
    <div id="app"></div>

    <!-- Include the compiled JavaScript file -->
    <script src="dist/build.js"></script>
  </body>
</html>
```

3. Make sure you set up your build process to compile the Vue component with the `script setup` syntax.

This code assumes you have a popup in your Chrome extension and that you want to insert a red button when the designated button is clicked. Adjust the component structure and styling as needed for your extension's specific requirements.


  </div></div></div>

  <div style="background-color: grey; height: 15px;"></div>

  