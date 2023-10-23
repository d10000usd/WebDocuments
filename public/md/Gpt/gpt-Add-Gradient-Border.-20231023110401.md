# **<span style="font-size: 35px; font-style: italic;">Add Gradient Border.</span>**


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

다음과 같이 코드를 수정하여 외곽 경계에 흰색 그라데이션을 추가할 수 있습니다. 이 코드는 변경 사항을 적용하여 도형 외곽에 흰색 그라데이션을 추가합니다.

```html
<!DOCTYPE html>
<html>
<head>
<style>
   :root {
        --text-color: #FFFFFF; /* Set your preferred text color here */
   }

   .custom-box {
        background-color: rgb(68, 171, 215);
        border: 10px solid rgb(255, 255, 255);
        border-radius: 60px;
        margin: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        width: 800px;
        height: 500px;
        background-position: random;
    }
    .custom-text {
        font-size: 80px;
        color: var(--text-color); /* Using the variable for text color */
    }
    .inner-box {
        border: 5px solid white;
        width: 750px;
        border-radius: 60px;
        height: 400px;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: Arial, sans-serif; /* Add your preferred font here */
        position: relative;
        background: linear-gradient(135deg, #00BFFF, #87CEFA);
        overflow: hidden; /* To hide overflow */
    }
    .custom-box::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.1)); /* Adjust the transparency as needed */
    }
    .custom-box::before {
        content: '';
        position: absolute;
        top: -10px;
        left: -10px;
        width: calc(100% + 20px);
        height: calc(100% + 20px);
        border: 10px solid white;
        border-radius: 70px;
        z-index: -1;
    }
</style>
</head>
<body>

<div class="custom-box custom-text">
    가독성

</div>

<canvas id="myCanvas" width="800" height="500" style="display: none;"></canvas>

<script>
    var canvas = document.getElementById('myCanvas');
    var ctx = canvas.getContext('2d');

    for (var i = 0; i < 19; i++) {
        var randomX = Math.floor(Math.random() * 500);
        var randomY = Math.floor(Math.random() * 300);
        var randomWidth = Math.floor(Math.random() * 400);
        var randomHeight = Math.floor(Math.random() * 300);

        var colorValue = 230; // Set the initial value for R
        ctx.fillStyle = 'rgb(' + colorValue + ',' + (i*10) + ',' + colorValue + ')';
        ctx.fillRect(randomX, randomY, randomWidth, randomHeight); // Rectangle

        var randomCircleX = Math.floor(Math.random() * 800);
        var randomCircleY = Math.floor(Math.random() * 500);
        var randomRadius = Math.floor(Math.random() * 150);

        ctx.beginPath();
        ctx.arc(randomCircleX, randomCircleY, randomRadius, 0, 2 * Math.PI); // Circle
        ctx.fill();
    }

    // Convert canvas to image and set as background
    var dataURL = canvas.toDataURL();
    document.getElementsByClassName('custom-box')[0].style.backgroundImage = "url('" + dataURL + "')";

    // Custom JavaScript for text color
    var root = document.documentElement;
    root.style.setProperty('--text-color', 'black'); // Set your preferred text color here
</script>

</body>
</html>
```

위의 수정된 코드는 `::before` 선택자를 사용하여 외곽 경계에 흰색 그라데이션 효과를 추가합니다. 수정된 코드를 적용하여 원하는 외곽 경계 스타일을 얻을 수 있을 것입니다.


</div>