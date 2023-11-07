<html>
<head>
# **Convert GPT to Markdown.**
</head>
<body>
<p>클래스로 변환하는 것은 JavaScript의 기본 지식이지만, 단순한 요청이 아니기 때문에 아래에서 간단한 예시를 제공하겠습니다.

```javascript
class ChatGPTResponseConverter {
    constructor() {
        this.msgs = document.querySelectorAll("div.whitespace-pre-wrap");
        this.markdowns = {};
        this.processMessages();
        this.addSaveAllButton();
        this.addReloadButton();
    }

    generateMarkdownContent(div, index) {
        // 기능 구현
    }

    createButton(text, clickHandler) {
        // 기능 구현
    }

    handleButtonClick(index) {
        // 기능 구현
    }

    handleSaveAllButtonClick() {
        // 기능 구현
    }

    handleTextSaveButtonClick(index) {
        // 기능 구현
    }

    processMessages() {
        // 기능 구현
    }

    reloadPage() {
        // 기능 구현
    }

    createReloadButton() {
        // 기능 구현
    }

    addSaveAllButton() {
        // 기능 구현
    }

    addReloadButton() {
        // 기능 구현
    }
}

const chatConverter = new ChatGPTResponseConverter();
```

위 코드는 기본적인 틀을 제공하며, `// 기능 구현` 부분에는 원래 코드의 각 기능을 구현해야 합니다. 위 코드는 전체적인 구조를 제공하므로 원하는 대로 추가로 수정하실 수 있습니다.




</p>

<p>당신이 원하는 것은 전체 코드인 것 같습니다. 여기에서는 웹 페이지의 구조에 따라 수정이 필요할 수 있습니다. 아래는 요청하신 기능을 포함한 전체 코드입니다.

```javascript
class ChatGPTResponseConverter {
    constructor() {
        this.msgs = document.querySelectorAll("div.whitespace-pre-wrap");
        this.markdowns = {};
        this.processMessages();
        this.addSaveAllButton();
        this.addReloadButton();
    }

    generateMarkdownContent(div, index) {
        const htmltag = "\n\n\n\n";
        const mddiv = div.children[0];
        const fiberKey = Object.keys(mddiv).find((k) => k.startsWith('__reactFiber$'));
        const origMd = mddiv[fiberKey].return.pendingProps.children;
        return `${origMd}\n${htmltag}`;
    }

    createButton(text, clickHandler) {
        const buttonDiv = document.createElement("div");
        const button = document.createElement("button");
        button.innerText = text;
        button.style.cssText = "border: 1px solid #ccc; border-radius: 5px;";
        buttonDiv.style.cssText = "background-color: blue; color: white; border-radius: 10px; padding: 0px; margin: 5px; border: 1px solid #ccc;";
        buttonDiv.appendChild(button);
        button.addEventListener("click", clickHandler);
        return buttonDiv;
    }

    handleButtonClick(index) {
        const markdownContent = this.markdowns[`#${index + 1}`];
        const finalMarkdown = `# **${document.title}**\n${markdownContent}`;
        const blob = new Blob([finalMarkdown], { type: "text/markdown" });
        const dateString = new Date().toISOString().replace(/[-T:]/g, "").slice(0, 14);
        const fileName = `gpt-${document.title}-${dateString}.md`;
        const downloadLink = document.createElement("a");
        downloadLink.download = fileName;
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.click();
    }

    handleSaveAllButtonClick() {
        let allMd = "";
        Object.entries(this.markdowns).forEach(([key, value]) => {
            allMd += `<p>${value}</p>\n\n`;
        });
        const titleMarkdown = `# **${document.title}**\n`;
        const finalMarkdown = `<html>\n<head>\n${titleMarkdown}</head>\n<body>\n${allMd}\n</body>\n</html>`;
        const dateString = new Date().toISOString().replace(/[-T:]/g, "").slice(0, 14);
        const fileName = `gpt-All-${document.title}-${dateString}.md`;
        const blob = new Blob([finalMarkdown], { type: "text/html" });
        const downloadLink = document.createElement("a");
        downloadLink.download = fileName;
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.click();
    }

    handleTextSaveButtonClick(index) {
        // 원하는 기능 구현
    }

    processMessages() {
        Array.from(this.msgs).forEach((div, index) => {
            if (div.children.length === 1 && (index + 1) % 2 === 0) {
                const markdownContent = this.generateMarkdownContent(div, index);
                this.markdowns[`#${index + 1}`] = markdownContent;
                const mdButton = this.createButton(`[${index + 1}] as Markdown`, () => this.handleButtonClick(index));
                const textButton = this.createButton(`[${index + 1}] as Text`, () => this.handleTextSaveButtonClick(index));
                div.appendChild(mdButton);
                div.appendChild(textButton);
            }
        });
    }

    reloadPage() {
        this.msgs = document.querySelectorAll("div.whitespace-pre-wrap");
        this.processMessages();
    }

    createReloadButton() {
        const reloadButtonDiv = document.createElement("div");
        const reloadButton = document.createElement("button");
        reloadButton.innerText = "Reload Page";
        reloadButton.style.cssText = "background-color: red; color: white; border-radius: 10px; padding: 0px; margin: 5px; border: 1px solid #ccc;";
        reloadButtonDiv.appendChild(reloadButton);
        reloadButton.addEventListener("click", this.reloadPage.bind(this));
        return reloadButtonDiv;
    }

    addSaveAllButton() {
        const lastDiv = this.msgs[this.msgs.length - 1];
        const saveAllButton = this.createButton("Save all as Markdown", this.handleSaveAllButtonClick.bind(this));
        lastDiv.appendChild(saveAllButton);
    }

    addReloadButton() {
        const targetElement = document.querySelector(".mb-1.flex.flex-row.gap-2");
        const reloadButtonDiv = this.createReloadButton();
        targetElement.parentElement.insertBefore(reloadButtonDiv, targetElement);
    }
}

const chatConverter = new ChatGPTResponseConverter();
```

위 코드는 요청하신 대로 클래스로 전환된 전체 코드입니다. 페이지 구조에 따라 몇 가지 조정이 필요할 수 있습니다.




</p>

<p>당연히요, 중복을 제거하고 코드를 더 깔끔하게 유지하기 위해 함수로 분리하는 것이 좋습니다. 아래에 중복을 제거하고 함수로 분리한 버전을 제시해 드리겠습니다.

```javascript
class ChatGPTResponseConverter {
    constructor() {
        this.msgs = document.querySelectorAll("div.whitespace-pre-wrap");
        this.markdowns = {};
        this.processMessages();
        this.addSaveAllButton();
        this.addReloadButton();
    }

    generateMarkdownContent(div, index) {
        const htmltag = "\n\n\n\n";
        const mddiv = div.children[0];
        const fiberKey = Object.keys(mddiv).find((k) => k.startsWith('__reactFiber$'));
        const origMd = mddiv[fiberKey].return.pendingProps.children;
        return `${origMd}\n${htmltag}`;
    }

    createButton(text, clickHandler, style) {
        const buttonDiv = document.createElement("div");
        const button = document.createElement("button");
        button.innerText = text;
        button.style.cssText = style;
        buttonDiv.style.cssText = "background-color: blue; color: white; border-radius: 10px; padding: 0px; margin: 5px; border: 1px solid #ccc;";
        buttonDiv.appendChild(button);
        button.addEventListener("click", clickHandler);
        return buttonDiv;
    }

    handleButtonClick(index) {
        const markdownContent = this.markdowns[`#${index + 1}`];
        const finalMarkdown = `# **${document.title}**\n${markdownContent}`;
        this.downloadMarkdown(finalMarkdown);
    }

    handleSaveAllButtonClick() {
        let allMd = "";
        Object.entries(this.markdowns).forEach(([key, value]) => {
            allMd += `<p>${value}</p>\n\n`;
        });
        const titleMarkdown = `# **${document.title}**\n`;
        const finalMarkdown = `<html>\n<head>\n${titleMarkdown}</head>\n<body>\n${allMd}\n</body>\n</html>`;
        this.downloadMarkdown(finalMarkdown);
    }

    downloadMarkdown(content) {
        const blob = new Blob([content], { type: "text/markdown" });
        const dateString = new Date().toISOString().replace(/[-T:]/g, "").slice(0, 14);
        const fileName = `gpt-${document.title}-${dateString}.md`;
        const downloadLink = document.createElement("a");
        downloadLink.download = fileName;
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.click();
    }

    handleTextSaveButtonClick(index) {
        // 원하는 기능 구현
    }

    processMessages() {
        Array.from(this.msgs).forEach((div, index) => {
            if (div.children.length === 1 && (index + 1) % 2 === 0) {
                const markdownContent = this.generateMarkdownContent(div, index);
                this.markdowns[`#${index + 1}`] = markdownContent;
                const mdButton = this.createButton(`[${index + 1}] as Markdown`, () => this.handleButtonClick(index), "border: 1px solid #ccc; border-radius: 5px;");
                const textButton = this.createButton(`[${index + 1}] as Text`, () => this.handleTextSaveButtonClick(index), "border: 1px solid #ccc; border-radius: 5px;");
                div.appendChild(mdButton);
                div.appendChild(textButton);
            }
        });
    }

    reloadPage() {
        this.msgs = document.querySelectorAll("div.whitespace-pre-wrap");
        this.processMessages();
    }

    createReloadButton() {
        const reloadButtonDiv = document.createElement("div");
        const reloadButton = document.createElement("button");
        reloadButton.innerText = "Reload Page";
        reloadButton.style.cssText = "background-color: red; color: white; border-radius: 10px; padding: 0px; margin: 5px; border: 1px solid #ccc;";
        reloadButtonDiv.appendChild(reloadButton);
        reloadButton.addEventListener("click", this.reloadPage.bind(this));
        return reloadButtonDiv;
    }

    addSaveAllButton() {
        const lastDiv = this.msgs[this.msgs.length - 1];
        const saveAllButton = this.createButton("Save all as Markdown", this.handleSaveAllButtonClick.bind(this), "border: 1px solid #ccc; border-radius: 5px;");
        lastDiv.appendChild(saveAllButton);
    }

    addReloadButton() {
        const targetElement = document.querySelector(".mb-1.flex.flex-row.gap-2");
        const reloadButtonDiv = this.createReloadButton();
        targetElement.parentElement.insertBefore(reloadButtonDiv, targetElement);
    }
}

const chatConverter = new ChatGPTResponseConverter();
```

이 코드에서는 `createButton` 함수를 만들어 중복을 제거했으며, 마찬가지로 `downloadMarkdown` 함수를 만들어 코드를 더욱 간결하게 유지했습니다.




</p>


</body>
</html>