# **<span style="font-size: 35px; font-style: italic;">생성 ChatGPT 로그</span>**

> ## 1
아래는 주어진 코드를 함수로 래핑한 것입니다. 이 함수는 주어진 코드와 동일한 작업을 수행하며, 전체 코드를 함수 내에 포함하고 있습니다.

```javascript
function createChatGPTLog() {
    const msgs = document.querySelectorAll("div.whitespace-pre-wrap");
    const markdowns = {};

    Array.from(msgs).forEach((div, index) => {
        if (div.children.length === 1) {
            // This is a ChatGPT response.
            const mddiv = div.children[0];
            const fiberKey = Object.keys(mddiv).find(k => k.startsWith('__reactFiber$'));
            const origMd = mddiv[fiberKey].return.pendingProps.children;
            markdowns[`#${index + 1}`] = `## C\n${origMd}`;
        } else {
            // This is the user. The website doesn't Markdown-format
            // the user's text, but we assume that the user has been
            // using Markdown if they're running this script.
            // The user's email address is in the alt attribute of
            // their icon, but we don't use that.
            markdowns[`#${index + 1}`] = `## User\n${div.textContent}`;
        }
    });

    // Create a string to store the markdown content.
    let allMd = "";
    Object.entries(markdowns).forEach(([key, value]) => {
        allMd += `${key}\n\n${value}\n\n`;
    });

    // I use an ISO 8601 format of the local time. Since colons aren't
    // allowed in filenames, and everything else looks weird to me,
    // I just use the variant without punctuation.
    const now = new Date();
    const dateString = `${now.getFullYear()}${(now.getMonth() + 1).toString().padStart(2, '0')}${now.getDate().toString().padStart(2, '0')}T${now.getHours().toString().padStart(2, '0')}${now.getMinutes().toString().padStart(2, '0')}${now.getSeconds().toString().padStart(2, '0')}`;

    const fileName = `ChatGPT log - ${document.title} - ${dateString}.md`;
    const downloadLink = document.createElement("a");
    downloadLink.download = fileName;
    downloadLink.href = URL.createObjectURL(new Blob([allMd], { type: "text/markdown" }));
    downloadLink.click();

    return allMd;
}

// 호출하려면 아래와 같이 사용하세요.
// createChatGPTLog();
```

이제 코드를 `createChatGPTLog` 함수 내에 래핑하여 필요할 때 호출할 수 있습니다. 함수를 호출하면 전체 작업이 실행되고 마크다운 파일이 다운로드됩니다.
*****



