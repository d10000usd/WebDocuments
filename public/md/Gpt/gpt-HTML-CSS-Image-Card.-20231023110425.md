# **<span style="font-size: 35px; font-style: italic;">HTML CSS Image Card.</span>**


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

아래의 HTML과 CSS 코드를 사용하여 이미지 위에 텍스트를 포함하는 카드 형식을 만들 수 있습니다. 이 코드를 사용하면 이미지와 텍스트가 함께 표시되는 기본적인 카드 레이아웃을 만들 수 있습니다. 이를 통해 이미지 위에 텍스트를 자유롭게 배치할 수 있습니다.

```html
<!DOCTYPE html>
<html>
<head>
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.card img {
  width: 100%;
  height: auto;
}

.card-container {
  padding: 2px 16px;
}

.card-container p {
  color: black;
  font-size: 18px;
}
</style>
</head>
<body>

<div class="card">
  <img src="image.jpg" alt="Image" style="width:100%">
  <div class="card-container">
    <p>Some text to go on the card</p>
  </div>
</div>

</body>
</html>
```

이 코드를 사용하면 이미지와 텍스트가 포함된 카드가 생성됩니다. 여기서 "image.jpg"는 사용하려는 이미지의 파일 경로를 나타냅니다. 이 코드를 사용하면 웹 페이지에 이미지와 텍스트가 함께 표시됩니다.

위 코드는 기본적인 형태이며, 디자인에 따라 스타일을 추가로 변경할 수 있습니다.


</div>