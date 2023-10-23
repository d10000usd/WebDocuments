# **<span style="font-size: 35px; font-style: italic;">Insert HTML Tag.</span>**

당신이 원하는 것이 이 함수에서 `tagStyle`에 HTML을 삽입하는 것이라면, 주석 처리된 `const tagStyle`을 삭제하고 원하는 HTML을 `tagStyle` 변수에 할당하면 됩니다. 여기에 당신이 요청한 대로 HTML을 추가한 예시가 있습니다:

```javascript
function Seperator() {
    const tagStyle = `
    <div style="position: relative; text-align: center; color: white;">
        <br><br>
        <img src="./at.png" alt="이미지 설명" style="width:20%;">
        <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
        <br><br>
    </div>
    `;

    return `${tagStyle}\n\n`;
}
```

이렇게 하면 함수가 주어진 HTML을 반환할 것입니다. 주의할 점은 백틱 (`` ` ``)을 사용하여 여러 줄의 HTML 코드를 `tagStyle`에 할당해야 한다는 것입니다.

        <div style="position: relative; text-align: center; color: white;">
            <br><br>
            <img src="./at.png" alt="이미지 설명" style="width:20%;">
            <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
            <br><br>
        </div>
        



<div style="background-color: grey; height: 15px;"></div>

