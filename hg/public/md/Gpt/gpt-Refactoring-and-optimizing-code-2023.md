# **<span style="font-size: 35px; font-style: italic;">Refactoring and optimizing code</span>**

> ## 1
Sure, I'll break down your code into smaller functions and optimize it for better performance. Here's the refactored code:

```javascript
function convertChatGPTResponsesToMarkdown() {
    let msgs = document.querySelectorAll("div.whitespace-pre-wrap");
    let markdowns = {};

    function generateMarkdownContent(div, index) {
        const htmltag = Seperator();
        const mddiv = div.children[0];
        const fiberKey = Object.keys(mddiv).find(k => k.startsWith('__reactFiber$'));
        const origMd = mddiv[fiberKey].return.pendingProps.children;

        const formattedTitle = formatTitle(document.title);
        return `${origMd}\n${htmltag}`;
    }

    function formatTitle(title) {
        const titleStyle = '<span style="font-size: 35px; font-style: italic;">';
        return `${titleStyle}${title}</span>`;
    }

    function createButton(text, clickHandler) {
        const buttonDiv = document.createElement("div");
        const button = document.createElement("button");
        button.innerText = text;
        button.style.border = "1px solid #ccc";
        button.style.borderRadius = "5px";
        buttonDiv.style.backgroundColor = "blue";
        buttonDiv.style.color = "white";
        buttonDiv.style.borderRadius = "10px";
        buttonDiv.style.padding = "0px";
        buttonDiv.style.margin = "5px";
        buttonDiv.style.border = "1px solid #ccc";
        buttonDiv.appendChild(button);
        button.addEventListener("click", clickHandler);
        return buttonDiv;
    }

    function Seperator() {
        const tagStyle = '*****'
        return `${tagStyle}\n\n`;
    }

    function MkTitle() {
        const titleMarkdown = formatTitle(document.title);
        return `# **${titleMarkdown}**\n`;
    }

    function handleButtonClick(index) {
        const titleMarkdown = MkTitle();
        const markdownContent = markdowns[`#${index + 1}`];
        const finalMarkdown = `${titleMarkdown}\n${markdownContent}`;
        downloadMarkdown(finalMarkdown);
    }

    function downloadMarkdown(content) {
        const blob = new Blob([content], { type: "text/markdown" });
        const now = new Date();
        const dateString = `${now.getFullYear()}`;
        const fileName = `gpt-${document.title}-${dateString}.md`;
        const downloadLink = document.createElement("a");
        downloadLink.download = fileName;
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.click();
    }

    function handleTextSaveButtonClick(index) {
        const markdownContent = markdowns[`#${index + 1}`];
        const now = new Date();
        const dateString = `${now.getFullYear()}`;
        const fileName = `gpt-${document.title}-${dateString}.md`;
        const sanitizedContent = removeSpecialCharacters(markdownContent);
        const titleMarkdown = formatTitle(document.title);
        const finalMarkdown = `Title - ${titleMarkdown}\n${markdownContent}`;
        downloadText(finalMarkdown, fileName);
    }

    function downloadText(content, fileName) {
        const blob = new Blob([content], { type: "text/plain" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = fileName;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }

    function removeSpecialCharacters(text) {
        return text.replace(/[#*]\s+/g, "");
    }

    function handleSaveAllButtonClick() {
        let allMd = "";
        let idx = 1;
        Object.entries(markdowns).forEach(([key, value]) => {
            const ParagraphNum = idx;
            allMd += `> ## ${ParagraphNum}\n${value}\n\n`;
            idx++;
        });
        const titleMarkdown = MkTitle();
        const finalMarkdown = `${titleMarkdown}\n${allMd}`;
        downloadMarkdown(finalMarkdown);
    }

    function processMessages() {
        Array.from(msgs).forEach((div, index) => {
            if (div.children.length === 1 && (index + 1) % 2 === 0) {
                const markdownContent = generateMarkdownContent(div, index);
                markdowns[`#${index + 1}`] = markdownContent;
                const mdButton = createButton(`[${index + 1}] as Markdown`, () => handleButtonClick(index));
                const textButton = createButton(`[${index + 1}] as Text`, () => handleTextSaveButtonClick(index));
                div.appendChild(mdButton);
                div.appendChild(textButton);
            }
        });

        const saveAllButton = createButton("Save all as Markdown", handleSaveAllButtonClick);
        const lastDiv = msgs[msgs.length - 1];
        lastDiv.appendChild(saveAllButton);
    }

    function reloadPage() {
        msgs = document.querySelectorAll("div.whitespace-pre-wrap");
        markdowns = {};
        console.log("refresh");
        processMessages();
    }

    function createReloadButton() {
        const reloadButtonDiv = document.createElement("div");
        const reloadButton = document.createElement("button");
        reloadButton.innerText = "Reload Page";
        reloadButton.style.backgroundColor = "red";
        reloadButton.style.color = "white";
        reloadButton.style.borderRadius = "10px";
        reloadButton.style.padding = "0px";
        reloadButton.style.margin = "5px";
        reloadButton.style.border = "1px solid #ccc";
        reloadButtonDiv.appendChild(reloadButton);
        reloadButton.addEventListener("click", reloadPage);
        return reloadButtonDiv;
    }

    processMessages();

    const targetElement = document.querySelector(".mb-1.flex.flex-row.gap-2");
    const reloadButtonDiv = createReloadButton();
    targetElement.parentElement.insertBefore(reloadButtonDiv, targetElement);
}

convertChatGPTResponsesToMarkdown();
```

I've organized your code into smaller functions to improve readability and maintainability. The main logic remains the same, but it's now easier to understand and modify.
*****



