# **<span style="font-size: 35px; font-style: italic;">Handle Save Function</span>**


<style>
.body-full {
    overflow-x: hidden;
    margin: .21rem;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Apple SD Gothic Neo", Arial, sans-serif;
    font-weight: 500;
    position: relative;
    word-break: break-all;
    -webkit-text-size-adjust: none;
    background-color: #eaeef3;
    color: #474787;
    font-size: 16px;
    line-height: 19px;
    border-color: white;
    }
</style>
<div class="body-full">

UNIX 시간을 일반적인 시간 형식으로 표시하려면 JavaScript의 `Date` 객체를 사용하여 변환해야 합니다. 아래는 UNIX 시간을 일반적인 시간 형식으로 변환하는 예시입니다.

```javascript
function handleSaveAllButtonClick() {
    let allMd = "";
    let idx = 1;
    Object.entries(markdowns).forEach(([key, value]) => {
        const ParagraphNum = idx;
        allMd += `> ## ${ParagraphNum}\n${value}\n\n`;
        idx = idx + 1;
    });
    const titleMarkdown = MkTitle();

    const unixTime = 1698028137; // 여기에 UNIX 시간을 삽입하세요.
    const dateObj = new Date(unixTime * 1000); // UNIX 시간을 밀리초로 변환하여 Date 객체 생성
    const dateString = dateObj.toISOString(); // ISO 문자열로 변환

    const finalMarkdown = `${titleMarkdown}\n${allMd}`;

    const fileName = `gpt-All-${document.title}-${dateString}.md`;
    const blob = new Blob([finalMarkdown], { type: "text/markdown" });
    const downloadLink = document.createElement("a");
    downloadLink.download = fileName;
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.click();
}
```

위의 코드는 `1698028137`와 같은 UNIX 시간을 JavaScript `Date` 객체를 사용하여 ISO 문자열로 변환하는 방법을 보여줍니다.


</div>