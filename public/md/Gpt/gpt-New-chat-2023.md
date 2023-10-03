# **<span style="font-size: 35px; font-style: italic;">New chat</span>**

Certainly, I can help you modify the code so that the `fetchData(url, imageUrl)` function is called for each URL in the `gitblobURL1` object. Here's the modified code:

```javascript
const gitblobURL1 = ref({
  "gpt-All-CSS로-NaviFooter-숨기기-2023.md": "https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/md/Gpt/gpt-All-CSS로-NaviFooter-숨기기-2023.md",
  "gpt-All-Divide-HTML-into-Columns-2023.md": "https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/md/Gpt/gpt-All-Divide-HTML-into-Columns-2023.md",
  // Add more URLs here as needed
});

onMounted(async () => {
  try {
    for (const url of Object.values(gitblobURL1.value)) {
      await fetchData(url, imageUrl);
    }
  } catch (error) {
    // Handle any errors here
  }
});
```

This code uses a `for...of` loop to iterate through the URLs in the `gitblobURL1` object and calls the `fetchData(url, imageUrl)` function for each URL. You can add more URLs to the `gitblobURL1` object as needed, and the code will automatically fetch data for all of them.
*****

