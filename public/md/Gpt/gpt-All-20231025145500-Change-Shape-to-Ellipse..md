# **<span style="font-size: 35px; font-style: italic;">Change Shape to Ellipse.</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-37.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 1</div></div>
사각형을 원 모양 대신 타원으로 바꾸는 것은 가능합니다. 이를 수행하기 위해 다음 단계를 따를 수 있습니다:

1. HTML 및 Canvas 엘리먼트를 수정하지 않고 JavaScript 부분에서 변경합니다. 원을 그리는 부분을 수정합니다.

```javascript
shapes.forEach(function(shape) {
    ctx.fillStyle = 'rgb(' + shape.color + ', 0, ' + shape.color + ')';
    if (shape.width !== shape.height) {
        // Check if the width and height are not equal, which indicates it's not a perfect circle
        ctx.ellipse(
            shape.x + shape.width / 2, // x-coordinate of the center
            shape.y + shape.height / 2, // y-coordinate of the center
            shape.width / 2, // horizontal radius
            shape.height / 2, // vertical radius
            0, // rotation (0 for a circle)
            0, // start angle
            2 * Math.PI // end angle (draw a full circle)
        );
    } else {
        // Draw a rectangle if the width and height are equal
        ctx.fillRect(shape.x, shape.y, shape.width, shape.height);
    }

    shape.x += shape.dx;
    shape.y += shape.dy;

    if (shape.x > canvas.width || shape.x < 0) {
        shape.dx = -shape.dx;
    }
    if (shape.y > canvas.height || shape.y < 0) {
        shape.dy = -shape.dy;
    }
});
```

위의 코드는 원 모양 대신 타원(ellipse)으로 사각형을 그립니다. 타원의 가로축과 세로축을 조절하여 타원의 형태를 변경할 수 있습니다.

이렇게 하면 사각형 대신 타원 모양의 요소를 만들 수 있습니다.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-39.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
전체 코드를 제공하겠습니다. 사각형을 원 대신 타원으로 그리는 JavaScript 코드를 포함하여 HTML 전체 코드입니다:

```html
<!DOCTYPE html>
<html>
<head>
    <style id="dynamic-styles"></style>
</head>
<body>
    <div class="custom-box custom-box ">
        <canvas id="myCanvas" width="800" height="500" style="position: absolute; top: 0; left: 0; z-index: 0;"></canvas>
        <div class="custom-text">가독성</div>
    </div>

<script>
    var canvas = document.getElementById('myCanvas');
    var ctx = canvas.getContext('2d');

    var styles = `
        :root {
            --text-color: #000000; /* Set your preferred text color here */
        }
     
        .custom-box {
            background-color: rgba(247, 209, 209, 0.5); 
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
            position: relative;
            z-index: 1; /* Set z-index to bring it to the front */
            overflow: hidden; /* Hide overflowing content */
         }
         .custom-text {
             font-size: 80px;
             color: var(--text-color); /* Using the variable for text color */
             position: absolute;
             top: 50%; /* Adjust top and left values to position the text as desired */
             left: 50%;
             transform: translate(-50%, -50%); /* Center the text horizontally and vertically */
         }
    `;
    var styleSheet = document.getElementById('dynamic-styles');
    styleSheet.innerHTML = styles;

    var shapes = [];

    for (var i = 0; i < 39; i++) {
        var shape = {
            x: Math.random() * 800,
            y: Math.random() * 500,
            width: Math.random() * 400,
            height: Math.random() * 300,
            color: Math.floor(Math.random() * 255),
            radius: Math.random() * 150,
            dx: (Math.random() - 0.5) * 2, // random x velocity between -1 and 1
            dy: (Math.random() - 0.5) * 2 // random y velocity between -1 and 1
        };
        shapes.push(shape);
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        shapes.forEach(function(shape) {
            ctx.fillStyle = 'rgb(' + shape.color + ', 0, ' + shape.color + ')';
            if (shape.width !== shape.height) {
                // Check if the width and height are not equal, which indicates it's not a perfect circle
                ctx.ellipse(
                    shape.x + shape.width / 2, // x-coordinate of the center
                    shape.y + shape.height / 2, // y-coordinate of the center
                    shape.width / 2, // horizontal radius
                    shape.height / 2, // vertical radius
                    0, // rotation (0 for a circle)
                    0, // start angle
                    2 * Math.PI // end angle (draw a full circle)




<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-31.png)  
- Change Shape to Ellipse.  
- 20231025145500  
- gpt  
- #gpt #code #keyword  
- 이를 수행하기 위해 다음 단계를 따를 수 있습니다:

1,HTML 및 Canvas 엘리먼트를 수정하지 않고 JavaScript 부분에서 변경합니다  
</div> 
