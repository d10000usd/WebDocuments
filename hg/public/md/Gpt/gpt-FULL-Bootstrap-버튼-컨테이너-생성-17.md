# Bootstrap 버튼 컨테이너 생성

## 1)
function createButtonContainer(buttons) {
    const buttonContainer = document.createElement("div");
    buttonContainer.style.backgroundColor = "rgba(0, 0, 0, 0)"; // 배경색을 투명으로 설정
    buttonContainer.style.color = "white"; // 폰트색을 흰색으로 설정
    buttonContainer.style.borderRadius = "10px";
    buttonContainer.style.padding = "0px";
    buttonContainer.style.margin = "5px";
    buttonContainer.style.border = "1px solid #ccc"; // 회색 테두리 추가

    buttons.forEach(button => {
        button.style.color = "white"; // 각 버튼의 폰트색을 흰색으로 설정
        button.style.backgroundColor = "rgba(0, 0, 0, 0)"; // 버튼의 배경색을 투명으로 설정
        buttonContainer.appendChild(button);
    });

    return buttonContainer;
}

boostrap 으로 보기 좋게 수정해줘저장 1

## 2)
아래는 Bootstrap을 사용하여 createButtonContainer 함수를 수정한 예제입니다. Bootstrap를 사용하려면 먼저 Bootstrap 라이브러리를 프로젝트에 추가해야 합니다.htmlCopy code<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.5.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0r3U1vagTpS2yFv5VZwL6I9z9NsfS6nIMqNzVtqI4Dr7f/ZJw8C95eLI5bwWfJ" crossorigin="anonymous">
    <title>Button Container</title>
</head>
<body>

<script>
function createButtonContainer(buttons) {
    const buttonContainer = document.createElement("div");
    buttonContainer.classList.add("container"); // Bootstrap container class 추가
    buttonContainer.classList.add("my-3"); // 상하 여백 추가
    buttonContainer.style.backgroundColor = "rgba(0, 0, 0, 0)"; // 배경색을 투명으로 설정

    buttons.forEach(button => {
        button.classList.add("btn", "btn-primary", "mx-2"); // Bootstrap 버튼 클래스 추가 및 좌우 여백 추가
        buttonContainer.appendChild(button);
    });

    return buttonContainer;
}

// 사용 예제
const button1 = document.createElement("button");
button1.textContent = "Button 1";

const button2 = document.createElement("button");
button2.textContent = "Button 2";

const button3 = document.createElement("button");
button3.textContent = "Button 3";

const buttons = [button1, button2, button3];

const container = createButtonContainer(buttons);
document.body.appendChild(container);
</script>

</body>
</html>
위의 코드는 Bootstrap 버전 5.5.0을 사용하고 있으며, Bootstrap의 클래스 및 스타일을 사용하여 버튼 컨테이너를 만들고 버튼을 추가합니다. Bootstrap의 클래스를 사용하면 버튼 및 컨테이너의 스타일을 쉽게 지정할 수 있습니다. 페이지의 <head> 부분에서 Bootstrap CSS 파일을 가져오는 것을 잊지 마세요.저장 2

## 3)
function createButtonContainer(buttons) {
    const buttonContainer = document.createElement("div");
    buttonContainer.style.backgroundColor = "rgba(0, 0, 0, 0)"; // 배경색을 투명으로 설정
    buttonContainer.style.color = "white"; // 폰트색을 흰색으로 설정
    buttonContainer.style.borderRadius = "10px";
    buttonContainer.style.padding = "0px";
    buttonContainer.style.margin = "5px";
    buttonContainer.style.border = "1px solid #ccc"; // 회색 테두리 추가

    buttons.forEach(button => {
        button.style.color = "white"; // 각 버튼의 폰트색을 흰색으로 설정
        button.style.backgroundColor = "rgba(0, 0, 0, 0)"; // 버튼의 배경색을 투명으로 설정
        buttonContainer.appendChild(button);
    });

    return buttonContainer;
}

함수 내에서 적용해줘저장 3

## 4)
아래는 함수 내에서 Bootstrap을 사용하여 createButtonContainer 함수를 수정한 예제입니다.javascriptCopy codefunction createButtonContainer(buttons) {
    const buttonContainer = document.createElement("div");
    buttonContainer.classList.add("container"); // Bootstrap container class 추가
    buttonContainer.style.backgroundColor = "transparent"; // 배경색을 투명으로 설정
    buttonContainer.style.color = "white"; // 폰트색을 흰색으로 설정
    buttonContainer.style.borderRadius = "10px";
    buttonContainer.style.padding = "0px";
    buttonContainer.style.margin = "5px";
    buttonContainer.style.border = "1px solid #ccc"; // 회색 테두리 추가

    buttons.forEach(button => {
        button.classList.add("btn", "btn-primary", "m-2"); // Bootstrap 버튼 클래스 추가 및 여백 추가
        button.style.color = "white"; // 각 버튼의 폰트색을 흰색으로 설정
        button.style.backgroundColor = "transparent"; // 버튼의 배경색을 투명으로 설정
        buttonContainer.appendChild(button);
    });

    return buttonContainer;
}

// 사용 예제
const button1 = document.createElement("button");
button1.textContent = "Button 1";

const button2 = document.createElement("button");
button2.textContent = "Button 2";

const button3 = document.createElement("button");
button3.textContent = "Button 3";

const buttons = [button1, button2, button3];

const container = createButtonContainer(buttons);
document.body.appendChild(container);
위의 코드에서는 Bootstrap 버튼 클래스와 여백 클래스(btn, btn-primary, m-2)를 각 버튼과 컨테이너에 추가하고, 배경색 및 폰트색을 함수 내에서 설정하도록 변경하였습니다. 이렇게 수정된 함수를 사용하면 Bootstrap 스타일을 적용한 버튼 컨테이너를 생성할 수 있습니다.저장 4