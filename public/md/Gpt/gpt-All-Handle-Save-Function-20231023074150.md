# **<span style="font-size: 35px; font-style: italic;">Handle Save Function</span>**

<div class="body-full">

해당 코드에서 `dateString` 변수를 `년월일시분초` 형식으로 변경하려면 JavaScript의 Date 객체를 사용하여 다음과 같이 수정할 수 있습니다.

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

    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    const dateString = `${year}${month}${day}${hours}${minutes}${seconds}`;

    const finalMarkdown = `${titleMarkdown}\n${allMd}`;

    const fileName = `gpt-All-${document.title}-${dateString}.md`;
    const blob = new Blob([finalMarkdown], { type: "text/markdown" });
    const downloadLink = document.createElement("a");
    downloadLink.download = fileName;
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.click();
}
```

위의 코드는 현재 날짜와 시간을 사용하여 `년월일시분초` 형식의 문자열을 만들고 해당 문자열을 `fileName` 변수에 추가하는 방법을 보여줍니다.

<div style="position: relative; text-align: center; color: white;">
    <br><br>
    <img src="./at.png" alt="이미지 설명" style="width:20%;">
    <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
    <br><br>
</div>

</div>

<div class="body-full">

물론, 아래는 간단하게 변경한 코드입니다.

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

    const now = new Date();
    const dateString = now.toISOString().replace(/[-T:]/g, "").slice(0, 14);

    const finalMarkdown = `${titleMarkdown}\n${allMd}`;

    const fileName = `gpt-All-${document.title}-${dateString}.md`;
    const blob = new Blob([finalMarkdown], { type: "text/markdown" });
    const downloadLink = document.createElement("a");
    downloadLink.download = fileName;
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.click();
}
```

이 코드는 현재 날짜와 시간을 `toISOString` 메서드를 사용하여 ISO 8601 형식으로 가져온 다음, 필요한 부분만 잘라서 `dateString`에 할당하는 방법을 보여줍니다.

<div style="position: relative; text-align: center; color: white;">
    <br><br>
    <img src="./at.png" alt="이미지 설명" style="width:20%;">
    <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
    <br><br>
</div>

</div>

<div class="body-full">

물론, 숫자로 표시하려면 간단히 년, 월, 일, 시, 분, 초를 각각 추출하면 됩니다. 아래는 그에 대한 예시입니다.

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

    const now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth() + 1;
    const day = now.getDate();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    const dateString = `${year}${month}${day}${hours}${minutes}${seconds}`;

    const finalMarkdown = `${titleMarkdown}\n${allMd}`;

    const fileName = `gpt-All-${document.title}-${dateString}.md`;
    const blob = new Blob([finalMarkdown], { type: "text/markdown" });
    const downloadLink = document.createElement("a");
    downloadLink.download = fileName;
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.click();
}
```

위의 코드는 각 변수에 년, 월, 일, 시, 분, 초를 추출하고 이를 하나의 문자열로 합쳐 `dateString`에 할당하는 방법을 보여줍니다.

<div style="position: relative; text-align: center; color: white;">
    <br><br>
    <img src="./at.png" alt="이미지 설명" style="width:20%;">
    <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
    <br><br>
</div>

</div>

<div class="body-full">

만약 UNIX 시간(에포크 시간) 형식으로 나타내고 싶다면, JavaScript에서 `Date` 객체를 사용하여 UNIX 시간을 얻을 수 있습니다. 아래는 그에 대한 예시입니다.

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

    const now = new Date();
    const unixTime = Math.floor(now.getTime() / 1000); // 초로 변환
    const dateString = `${unixTime}`;

    const finalMarkdown = `${titleMarkdown}\n${allMd}`;

    const fileName = `gpt-All-${document.title}-${dateString}.md`;
    const blob = new Blob([finalMarkdown], { type: "text/markdown" });
    const downloadLink = document.createElement("a");
    downloadLink.download = fileName;
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.click();
}
```

이 코드는 현재 시간을 초로 변환하여 UNIX 시간을 얻고, 이를 `dateString`에 할당하는 방법을 보여줍니다.

<div style="position: relative; text-align: center; color: white;">
    <br><br>
    <img src="./at.png" alt="이미지 설명" style="width:20%;">
    <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
    <br><br>
</div>

</div>

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

<div style="position: relative; text-align: center; color: white;">
    <br><br>
    <img src="./at.png" alt="이미지 설명" style="width:20%;">
    <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
    <br><br>
</div>

</div>

<div style="background-color: grey; height: 15px;"></div>

