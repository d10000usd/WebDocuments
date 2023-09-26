# Bootstrap 버튼 컨테이너 생성

## 1
createButtonContainer(buttons) {
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

boostrap 으로 보기 좋게 수정해줘Download Conversation 1

## 2
createButtonContainer(buttons) {
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

함수 내에서 적용해줘Download Conversation 3