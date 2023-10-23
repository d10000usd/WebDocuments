# **<span style="font-size: 35px; font-style: italic;">HTML CSS Box Design</span>**

```html
<!DOCTYPE html>
<html>
<head>
<style>
    .custom-box {
        background-color: red;
        border: 10px solid grey;
        border-radius: 10px;
        margin: 10px;
        text-align: center;
        font-size: 20px;
    }
</style>
</head>
<body>

<div class="custom-box">
  test car
</div>

</body>
</html>
```

> 위의 코드는 HTML과 CSS를 사용하여 설명한 내용을 구현한 것입니다. 이 코드는 빨간색 배경에 회색 테두리를 둥글게 적용하고, 테두리 마진은 10px로 설정되었습니다. 텍스트는 가운데 정렬되며 글자 크기는 20px로 설정되었습니다. 이 코드를 이용하여 웹 페이지에 해당 디자인을 표시할 수 있습니다.

<div style="position: relative; text-align: center; color: white;">
    <br><br>
    <img src="./ab.png" alt="이미지 설명" style="width:20%;">
    <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
    <br><br>
</div>

```html
<!DOCTYPE html>
<html>
<head>
<style>
    .custom-box {
        background-color: red;
        border: 10px solid grey;
        border-radius: 10px;
        margin: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px; /* 조정 가능한 높이 */
    }
    .custom-text {
        font-size: 20px;
    }
</style>
</head>
<body>

<div class="custom-box">
  <div class="custom-text">test car</div>
</div>

</body>
</html>
```

> 위의 수정된 코드는 텍스트를 가운데에 정렬하도록 수정한 것입니다. 이를 위해 `display: flex;`와 `justify-content: center;`, `align-items: center;`를 추가하였습니다. 이제 텍스트는 정중앙에 위치할 것입니다. 필요에 따라 높이를 조정할 수 있습니다.

<div style="position: relative; text-align: center; color: white;">
    <br><br>
    <img src="./ab.png" alt="이미지 설명" style="width:20%;">
    <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
    <br><br>
</div>

죄송합니다. 텍스트를 수직 및 수평으로 정확히 가운데로 정렬하려면 추가적인 CSS 속성이 필요합니다. 아래에 수정된 코드를 참조하세요.

```html
<!DOCTYPE html>
<html>
<head>
<style>
    .custom-box {
        background-color: red;
        border: 10px solid grey;
        border-radius: 10px;
        margin: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        width: 300px;
        height: 500px;
    }
    .custom-text {
        font-size: 80px;
    }
</style>
</head>
<body>

<div class="custom-box">
  <div class="custom-text">test car</div>
</div>

</body>
</html>
```

이 코드는 텍스트를 정확하게 가운데에 배치합니다. `display: flex;`, `justify-content: center;`, `align-items: center;`를 추가하여 가로 및 세로 중앙 정렬을 가능하게 했습니다. 이제 텍스트가 정중앙에 나타날 것입니다.

<div style="position: relative; text-align: center; color: white;">
    <br><br>
    <img src="./ab.png" alt="이미지 설명" style="width:20%;">
    <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
    <br><br>
</div>

<div style="background-color: grey; height: 15px;"></div>

