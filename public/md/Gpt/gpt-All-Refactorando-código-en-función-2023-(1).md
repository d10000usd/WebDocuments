# **<span style="font-size: 35px; font-style: italic;">Refactorando código en función</span>**

> ## 1
Sure, I can help you refactor your code into a function. Here's the refactored code with a function:

```javascript
function createAndSaveMarkdown() {
    const targetElement = document.querySelector(".mb-1.flex.flex-row.gap-2");
    // Add the button before the target element
    const button = document.createElement('button');
    button.textContent = 'Save allmk';
    button.addEventListener('click', () => {
        // Log the allmk value to the console
        const allmk = extractChatGPTLogContent();
        let allMd = "";
        let idx = 1;
        Object.entries(allmk).forEach(([key, value]) => {
            const ParagraphNum = idx;
            allMd += `> ## ${ParagraphNum}\n${value}\n\n`;
            idx = idx + 1;
        });

        const finalMarkdown = `${allMd}`;

        const now = new Date();
        const dateString = `${now.getFullYear()}`;
        const fileName = `gpt-All-${dateString}.md`;
        const blob = new Blob([finalMarkdown], { type: "text/markdown" });
        const downloadLink = document.createElement("a");
        downloadLink.download = fileName;
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.click();

    });
    targetElement.parentNode.insertBefore(button, targetElement);
}

// Call the function to create and save markdown
createAndSaveMarkdown();
```

I've wrapped your code in the `createAndSaveMarkdown` function so that you can easily call it when needed. Just call `createAndSaveMarkdown()` whenever you want to create and save the markdown.
*****



