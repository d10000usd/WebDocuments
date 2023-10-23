# **<span style="font-size: 35px; font-style: italic;">Mondrian Style Webpage.</span>**

```html
<!DOCTYPE html>
<html>
<head>
<style>
   :root {
        --text-color: #000000; /* Set your preferred text color here */
   }

   .custom-box {
        background-color: rgb(255, 255, 255);
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

위의 코드를 사용하면 도형이 들어간 몬드리안 스타일의 요소를 가진 웹 페이지를 만들 수 있습니다. 해당 코드는 사용자가 원하는 대로 텍스트 색상을 설정하고, 도형의 색상과 크기를 무작위로 생성합니다. 결과적으로, 가독성이 좋은 디자인을 가진 웹 페이지를 구현할 수 있습니다.



        <div style="position: relative; text-align: center; color: white;">
            <br><br>
            <img src="./at.png" alt="이미지 설명" style="width:20%;">
            <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
            <br><br>
        </div>
        



제가 제공한 코드는 도형이 들어간 몬드리안 스타일의 요소를 가진 웹 페이지를 생성할 수 있는 코드입니다. 제가 이해하건데, 웹 페이지가 변화하지 않았다면 아마도 브라우저가 캔버스를 지원하지 않는 것일 수 있습니다. 다음은 몇 가지 확인해야 할 사항입니다:

1. 브라우저의 호환성: 코드가 사용자가 사용하는 브라우저에서 올바르게 작동하는지 확인해보세요. 몇몇 구형 브라우저는 최신 기능을 지원하지 않을 수 있습니다.
2. 스크립트가 활성화되어 있는지 확인: 브라우저에서 자바스크립트가 활성화되어 있는지 확인하세요. 자바스크립트가 비활성화된 경우 스크립트가 작동하지 않을 수 있습니다.
3. 캔버스 지원 여부: 사용자가 사용하는 브라우저가 캔버스를 지원하는지 확인하세요. 몇몇 특정한 브라우저나 기기는 캔버스를 지원하지 않을 수 있습니다.

이러한 사항들을 확인한 후에도 여전히 문제가 지속된다면, 다른 브라우저를 시도해보거나 웹 페이지를 로컬 환경에서 실행해보세요. 그러면 문제를 파악하고 해결하는 데 도움이 될 수 있습니다.



        <div style="position: relative; text-align: center; color: white;">
            <br><br>
            <img src="./at.png" alt="이미지 설명" style="width:20%;">
            <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
            <br><br>
        </div>
        



도형이 움직이도록 구현하려면 자바스크립트를 사용하여 애니메이션을 추가해야 합니다. 다음은 코드를 수정하여 도형이 움직이도록 만드는 방법입니다. 이 코드는 캔버스에 무작위로 생성된 사각형과 원들을 움직이도록 구현할 것입니다. 

```html
<!DOCTYPE html>
<html>
<head>
<style>
   :root {
        --text-color: #000000; /* Set your preferred text color here */
   }

   .custom-box {
        background-color: rgb(255, 255, 255);
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
    }
    .custom-text {
        font-size: 80px;
        color: var(--text-color); /* Using the variable for text color */
    }
    
</style>
</head>
<body>

<div class="custom-box custom-text">
    가독성

</div>

<canvas id="myCanvas" width="800" height="500" style="position: absolute; top: 0; left: 0;"></canvas>

<script>
    var canvas = document.getElementById('myCanvas');
    var ctx = canvas.getContext('2d');

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

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
    }

    function animate() {
        draw();
        requestAnimationFrame(animate);
    }

    animate();

    // Custom JavaScript for text color
    var root = document.documentElement;
    root.style.setProperty('--text-color', 'black'); // Set your preferred text color here
</script>

</body>
</html>
```

위의 코드는 `draw` 함수를 사용하여 도형들을 그리고, `animate` 함수를 사용하여 애니메이션을 실행합니다. 이제 도형들이 화면에서 움직이는 것을 볼 수 있어야 합니다.



        <div style="position: relative; text-align: center; color: white;">
            <br><br>
            <img src="./at.png" alt="이미지 설명" style="width:20%;">
            <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
            <br><br>
        </div>
        



도형이 부드럽게 움직이도록 하려면 각 프레임 간의 변화를 조정하여 애니메이션을 부드럽게 만들어야 합니다. 이를 위해 애니메이션 프레임 간의 각 도형의 위치를 조정하고, 새로운 프레임을 그리기 전에 이전 프레임을 지우는 `requestAnimationFrame`을 사용할 수 있습니다. 아래 코드는 도형이 부드럽게 움직이도록 수정된 코드입니다.

```html
<!DOCTYPE html>
<html>
<head>
<style>
   :root {
        --text-color: #000000; /* Set your preferred text color here */
   }

   .custom-box {
        background-color: rgb(255, 255, 255);
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
    }
    .custom-text {
        font-size: 80px;
        color: var(--text-color); /* Using the variable for text color */
    }
    
</style>
</head>
<body>

<div class="custom-box custom-text">
    가독성

</div>

<canvas id="myCanvas" width="800" height="500" style="position: absolute; top: 0; left: 0;"></canvas>

<script>
    var canvas = document.getElementById('myCanvas');
    var ctx = canvas.getContext('2d');

    var shapes = [];

    for (var i = 0; i < 19; i++) {
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
            ctx.fillRect(shape.x, shape.y, shape.width, shape.height);
            ctx.beginPath();
            ctx.arc(shape.x, shape.y, shape.radius, 0, 2 * Math.PI);
            ctx.fill();

            shape.x += shape.dx;
            shape.y += shape.dy;

            if (shape.x > canvas.width || shape.x < 0) {
                shape.dx = -shape.dx;
            }
            if (shape.y > canvas.height || shape.y < 0) {
                shape.dy = -shape.dy;
            }
        });
    }

    function animate() {
        draw();
        requestAnimationFrame(animate);
    }

    animate();

    // Custom JavaScript for text color
    var root = document.documentElement;
    root.style.setProperty('--text-color', 'black'); // Set your preferred text color here
</script>

</body>
</html>
```

위의 코드를 사용하면 도형이 부드럽게 움직이는 것을 확인할 수 있어야 합니다. 이 코드는 각 도형의 위치를 조정하여 부드러운 애니메이션 효과를 만들어냅니다.



        <div style="position: relative; text-align: center; color: white;">
            <br><br>
            <img src="./at.png" alt="이미지 설명" style="width:20%;">
            <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
            <br><br>
        </div>
        



HTML의 구조를 수정하여 텍스트가 맨 앞에서 보이도록 할 수 있습니다. 아래 코드는 텍스트가 맨 앞에 표시되도록 수정된 코드입니다.

```html
<!DOCTYPE html>
<html>
<head>
<style>
   :root {
        --text-color: #000000; /* Set your preferred text color here */
   }

   .custom-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 500px;
    }

    .custom-box {
        background-color: rgb(255, 255, 255);
        border: 10px solid rgb(255, 255, 255);
        border-radius: 60px;
        margin: 10px;
        text-align: center;
        width: 800px;
        height: 500px;
        background-position: random;
        position: relative;
    }

    .custom-text {
        font-size: 80px;
        color: var(--text-color); /* Using the variable for text color */
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 1;
    }
    
</style>
</head>
<body>

<div class="custom-container">
    <div class="custom-box">
        <div class="custom-text">
            가독성
        </div>
    </div>
</div>

<canvas id="myCanvas" width="800" height="500" style="position: absolute; top: 0; left: 0;"></canvas>

<script>
    var canvas = document.getElementById('myCanvas');
    var ctx = canvas.getContext('2d');

    var shapes = [];

    for (var i = 0; i < 19; i++) {
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
            ctx.fillRect(shape.x, shape.y, shape.width, shape.height);
            ctx.beginPath();
            ctx.arc(shape.x, shape.y, shape.radius, 0, 2 * Math.PI);
            ctx.fill();

            shape.x += shape.dx;
            shape.y += shape.dy;

            if (shape.x > canvas.width || shape.x < 0) {
                shape.dx = -shape.dx;
            }
            if (shape.y > canvas.height || shape.y < 0) {
                shape.dy = -shape.dy;
            }
        });
    }

    function animate() {
        draw();
        requestAnimationFrame(animate);
    }

    animate();

    // Custom JavaScript for text color
    var root = document.documentElement;
    root.style.setProperty('--text-color', 'black'); // Set your preferred text color here
</script>

</body>
</html>
```

이제 텍스트가 화면의 가운데에 정렬되어 맨 앞에서 보이게 될 것입니다.



        <div style="position: relative; text-align: center; color: white;">
            <br><br>
            <img src="./at.png" alt="이미지 설명" style="width:20%;">
            <div style="color: aqua; font-size: 20px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Accent</div>
            <br><br>
        </div>
        



<div style="background-color: grey; height: 15px;"></div>

