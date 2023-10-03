# **<span style="font-size: 35px; font-style: italic;">Refactor code to avoid globals</span>**

Sure, I can help you refactor the code to avoid using global functions and instead pass variables as parameters. Here's the modified code:

```javascript
function generateMarkdownContent(div, index) {
    const htmltag = Seperator();
    const mddiv = div.children[0];
    const fiberKey = Object.keys(mddiv).find(k => k.startsWith('__reactFiber$'));
    const origMd = mddiv[fiberKey].return.pendingProps.children;

    const titleStyle = '<span style="font-size: 35px; font-style: italic;">';
    const formattedTitle = `${titleStyle}${document.title}</span>`;
    
    return `${origMd}\n${formattedTitle}\n${htmltag}`;
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
    const titleStyle = '<span style="font-size: 35px; font-style: italic;">';
    const formattedTitle = `${titleStyle}${document.title}</span>`;
    return `# **${formattedTitle}**\n`;
}

function handleButtonClick(index, markdowns) {
    const titleMarkdown = MkTitle();
    const markdownContent = markdowns[`#${index + 1}`];
    const finalMarkdown = `${titleMarkdown}\n${markdownContent}`;

    const blob = new Blob([finalMarkdown], { type: "text/markdown" });
    const now = new Date();
    const dateString = `${now.getFullYear()}`;
    const fileName = `gpt-${document.title}-${dateString}.md`;
    const downloadLink = document.createElement("a");
    downloadLink.download = fileName;
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.click();
}

function removeSpecialCharacters(text) {
    text = text.replace(/(#{2,}|\*{2,})/g, "");
    return text.replace(/[#*]\s+/g, "");
}

function handleTextSaveButtonClick(index, markdowns) {
    const markdownContent = markdowns[`#${index + 1}`];
    const now = new Date();
    const dateString = `${now.getFullYear()}`;
    const fileName = `gpt-${document.title}-${dateString}.md`;

    const sanitizedContent = removeSpecialCharacters(markdownContent);
    const titleMarkdown = document.title
    const finalMarkdown = `Title - ${titleMarkdown}\n${sanitizedContent}`;
    const blob = new Blob([finalMarkdown], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function handleSaveAllButtonClick(markdowns) {
    let allMd = "";
    let idx = 1;
    Object.entries(markdowns).forEach(([key, value]) => {
        const ParagraphNum = idx;
        allMd += `> ## ${ParagraphNum}\n${value}\n\n`;
        idx = idx + 1;
    });
    const titleMarkdown = MkTitle();
    const finalMarkdown = `${titleMarkdown}\n${allMd}`;

    const now = new Date();
    const dateString = `${now.getFullYear()}`;
    const fileName = `gpt-All-${document.title}-${dateString}.md`;
    const blob = new Blob([finalMarkdown], { type: "text/markdown" });
    const downloadLink = document.createElement("a");
    downloadLink.download = fileName;
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.click();
}

function processMessages(markdowns) {
    const msgs = document.querySelectorAll("div.whitespace-pre-wrap");

    Array.from(msgs).forEach((div, index) => {
        if (div.children.length === 1 && (index + 1) % 2 === 0) {
            const markdownContent = generateMarkdownContent(div, index);
            markdowns[`#${index + 1}`] = markdownContent;

            const mdButton = createButton(`[${index + 1}] as Markdown`, () => handleButtonClick(index, markdowns));
            const textButton = createButton(`[${index + 1}] as Text`, () => handleTextSaveButtonClick(index, markdowns));

            div.appendChild(mdButton);
            div.appendChild(textButton);
        }
    });

    const saveAllButton = createButton("Save all as Markdown", () => handleSaveAllButtonClick(markdowns));
    const lastDiv = msgs[msgs.length - 1];
    lastDiv.appendChild(saveAllButton);
}

function reloadPage() {
    let msgs = document.querySelectorAll("div.whitespace-pre-wrap");
    let markdowns = {};
    console.log("refresh");
    processMessages(markdowns);
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

const targetElement = document.querySelector(".mb-1.flex.flex-row.gap-2");
const reloadButtonDiv = createReloadButton();
targetElement.parentElement.insertBefore(reloadButtonDiv, targetElement);
processMessages(markdowns);
```

I've made the necessary modifications to remove global functions and pass variables as parameters to ensure that the code maintains its functionality without relying on global variables.
*****

