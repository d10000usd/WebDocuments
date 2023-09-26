# Set Engineering Prompt

## 1)
function setPromptEngneering() {
    const systemPrompt = [
        {
          "act": "form1", 
          "prompt": "Your job is now to read the recent conversation after any provided previous context and return a list of memories. Can you write out a list of memories from the conversation in the format:  {\"title\":\"\", \"summary\":\"\", \"keyword\" :\"\"} "
        },
        {
            "act": "coding assist",
            "prompt": "vue3, script setup. You are a helpful super super codeing machine that answer question as simplify as possible."
        },
        {
            "act": "JavaScript Console",
            "prompt": "vue3, script setup. I want you to act as a javascript console. I will type commands and you will reply with what the javascript console should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. my first command is console.log(\"Hello World\");"
        },
        {
            "act": "Python interpreter",
            "prompt": "I want you to act like a Python interpreter. I will give you Python code, and you will execute it. Do not provide any explanations. Do not respond with anything except the output of the code. The first code is: \"print('hello world!')\""
        }];

    // "helow"를 textarea의 값으로 설정합니다.
    var textarea = document.getElementById("prompt-textarea");

    // "helow"와 개행 문자 3개를 textarea의 값으로 설정합니다.
    if (textarea) {
        textarea.value = systemPrompt[2];
    }

    // 버튼 요소를 찾습니다.
    var button = document.querySelector("[data-testid='send-button']");

    // 버튼을 활성화합니다.
    if (button) {
        button.removeAttribute("disabled");
    }
}

안들어 가지는데 문법에 문제 있나?저장 1

## 2)
문제가 있는 부분을 확인해 보겠습니다. textarea.value에 값을 설정하려면 문자열 값을 사용해야 합니다. 그러나 systemPrompt[2]는 객체를 가리키는데, 이를 문자열로 변환해야 합니다. 아래는 수정된 코드입니다:javascriptCopy codevar textarea = document.getElementById("prompt-textarea");

if (textarea) {
    // systemPrompt[2]의 객체를 JSON 문자열로 변환하여 textarea의 값으로 설정합니다.
    textarea.value = JSON.stringify(systemPrompt[2]);
}
위의 코드에서 JSON.stringify() 함수를 사용하여 객체를 JSON 문자열로 변환하고, 그 값을 textarea의 값으로 설정하게 됩니다. 이렇게 하면 textarea에 JSON 형식의 문자열이 표시될 것입니다.저장 2

## 3)
{"act":"JavaScript Console","prompt":"vue3, script setup. I want you to act as 
a javascript console. I will type commands and you will reply with what the javascript console should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. my first command is console.log(\"Hello World\");"}저장 3

## 4)
제공해주신 JSON 데이터는 특정 동작(act) 및 프롬프트(prompt) 정보를 포함하고 있습니다. 이 데이터를 JavaScript 코드로 처리하고 해당 지침에 따라 JavaScript 콘솔처럼 동작하는 예제를 작성할 수 있습니다. 아래는 해당 JSON 데이터를 기반으로 작성한 JavaScript 코드 예제입니다:javascriptCopy code// JSON 데이터
const consoleSimulationData = {
    "act": "JavaScript Console",
    "prompt": "vue3, script setup. I want you to act as a javascript console. I will type commands and you will reply with what the javascript console should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. my first command is console.log(\"Hello World\");"
};

// JavaScript 콘솔 시뮬레이션 함수
function simulateJavaScriptConsole(command) {
    // 지정된 명령을 실행하고 결과를 얻습니다.
    let result = null;
    switch (command) {
        case 'console.log("Hello World");':
            result = "Hello World"; // 이 부분에서 결과를 생성하고 실제 콘솔에 표시하는 대신 문자열로 반환합니다.
            break;
        default:
            result = "Command not recognized"; // 알 수 없는 명령일 경우 오류 메시지 반환
            break;
    }

    // 결과를 지정된 형식으로 반환
    return `{
        "output": "${result}"
    }`;
}

// 이제 콘솔 시뮬레이션 함수를 사용하여 명령을 처리할 수 있습니다.
const command = 'console.log("Hello World");'; // JSON 데이터에서 명령을 추출하거나 직접 입력할 수 있습니다.
const consoleOutput = simulateJavaScriptConsole(command);
console.log(consoleOutput); // 결과를 콘솔에 표시
이 코드 예제에서는 simulateJavaScriptConsole 함수를 사용하여 지정된 명령을 실행하고 그 결과를 JSON 형식의 문자열로 반환합니다. 이것은 JavaScript 콘솔 시뮬레이션의 예시입니다.저장 4

## 5)
    if (textarea) {
        textarea.value = JSON.stringify(systemPrompt[2]);
    }

요거 뒤에다 개행문자 3개 붙여줘저장 5

## 6)
개행문자를 문자열 뒤에 추가하려면 JSON.stringify() 결과에 개행문자를 추가하면 됩니다. 아래는 수정된 코드입니다:javascriptCopy codevar textarea = document.getElementById("prompt-textarea");

if (textarea) {
    // systemPrompt[2]의 객체를 JSON 문자열로 변환하고 개행문자 3개를 추가하여 textarea의 값으로 설정합니다.
    textarea.value = JSON.stringify(systemPrompt[2], null, 3);
}
위 코드에서 JSON.stringify() 함수의 두 번째 인수로 null을 전달하고 세 번째 인수로 3을 전달하여 JSON 문자열을 읽기 쉽게 들여쓰기한 후 개행문자 3개를 추가하여 textarea의 값으로 설정합니다.저장 6

## 7)
(() => {
    let documentTitleUsed = false;

    // Helper function to save a conversation by its index
    function saveConversation(index, markdowns, documentTitle) {
        const conversationMd = markdowns[index - 1];
        if (conversationMd) {
            const now = new Date();
            const dateString = `${now.getSeconds().toString().padStart(4, '0')}`;
            const conversationFileName = `gpt-${documentTitle}-${index}-${dateString}.md`;
            createAndClickDownloadLink(conversationFileName, `# ${documentTitle}\n\n${conversationMd}`);
        }
    }

// Helper function to create and click a download link
function createAndClickDownloadLink(fileName, content) {
    if (content.length >= 12) {
        const downloadLink = document.createElement("a");
        downloadLink.download = fileName;
        downloadLink.href = URL.createObjectURL(new Blob([content], { type: "text/markdown" }));
        downloadLink.click();
    } else {
        console.log("Content is too short to save. more than 11");
    }
}

    // Helper function to save the entire conversation
    function saveEntireConversation(markdowns, documentTitle) {
        const allMarkdown = markdowns.join('\n\n');
        const now = new Date();
        const dateString = `${now.getSeconds().toString().padStart(4, '0')}`;
        const conversationFileName = `gpt-FULL-${documentTitle}-${dateString}.md`;
        createAndClickDownloadLink(conversationFileName, `# ${documentTitle}\n\n${allMarkdown}`);
    }


    // Helper function to save only even-indexed responses (answers) with sequential numbering
    function saveResponses(markdowns, documentTitle) {
        const responseMarkdowns = markdowns.filter((markdown, index) => (index % 2 === 1) && markdown.startsWith("## "));
        const now = new Date();
        const dateString = `${now.getSeconds().toString().padStart(4, '0')}`;
        const responseFileName = `gpt-RESPONSES-${documentTitle}-${dateString}.md`;

        // Add sequential numbering to responseMarkdowns without additional text
        const responseMarkdownsWithNumbers = responseMarkdowns.map((markdown, index) => {
            // Split the markdown string into an array using spaces
            const markdownParts = markdown.split(' ');
            // Remove the first three parts (##, index, and an extra space)
            markdownParts.splice(0, 2);
            // Join the remaining parts back into a string
            const cleanedMarkdown = markdownParts.join(' ');
            return `## ${index + 1}\n${cleanedMarkdown}`;
        });

        createAndClickDownloadLink(responseFileName, `# ${documentTitle}\n\n${responseMarkdownsWithNumbers.join('\n\n')}`);
    }
    // Helper function to add click event listener to download buttons
    function addClickListenerToDownloadButton(downloadButton, index) {
        downloadButton.addEventListener("click", () => {
            extractAndSaveConversations(index);
        });
    }

    // Function to create a download button
    function createDownloadButton(index, buttonText = `저장 ${index}`) {
        const downloadButton = document.createElement("button");
        downloadButton.textContent = buttonText;
        downloadButton.style.padding = "10px 20px";
        downloadButton.style.backgroundColor = "white"; // 흰색 배경색상
        downloadButton.style.color = "#007bff"; // 텍스트 색상
        downloadButton.style.border = "1px solid #ccc"; // 회색 테두리
        downloadButton.style.borderRadius = "5px";
        downloadButton.style.cursor = "pointer";

        // Add click event listener using the helper function
        addClickListenerToDownloadButton(downloadButton, index);

        return downloadButton;
    }

    // Helper function to extract conversations and return as an array of markdowns
    function extractConversations() {
        const msgs = document.querySelectorAll("div.whitespace-pre-wrap");
        const markdowns = [];
        let conversationCount = 0;
        let documentTitle = document.title;

        var textarea = document.getElementById("prompt-textarea");



        msgs.forEach((div, index) => {
            if (div.children.length === 1) {
                // This is a ChatGPT response.
                const mddiv = div.children[0];
                const fiberKey = Object.keys(mddiv).find(k => k.startsWith('__reactFiber$'));
                const origMd = mddiv[fiberKey]?.return?.pendingProps?.children;
                if (origMd) {
                    markdowns.push(`## ${++conversationCount})\n${origMd}`);
                }
            } else {
                // This is the user. Assume user is using Markdown.
                const userMessage = div.textContent;

                // Add documentTitle if it hasn't been added yet
                if (!documentTitleUsed) {
                    markdowns.push(`## ${documentTitle}\n`);
                    documentTitleUsed = true;
                }

                markdowns.push(`## ${++conversationCount})\n${userMessage}`);
            }
        });

        return { markdowns, documentTitle, conversationCount };
    }

    // Main function to extract and save conversations
    function extractAndSaveConversations(selectedConversationIndex) {
        const { markdowns, documentTitle, conversationCount } = extractConversations();

        if (selectedConversationIndex === 0) {
            saveEntireConversation(markdowns, documentTitle);
        } else if (selectedConversationIndex === -1) {
            saveResponses(markdowns, documentTitle);
        } else if (!isNaN(selectedConversationIndex) && selectedConversationIndex >= 1 && selectedConversationIndex <= conversationCount) {
            saveConversation(selectedConversationIndex, markdowns, documentTitle);
        } else {
            alert("Invalid input. Please enter a valid number between -1 and " + conversationCount);
        }
    }

// Function to add multiple download buttons with conversation indices
function addDownloadButtonsBetweenElements() {
    const whitespacePreWrapElements = document.querySelectorAll("div.whitespace-pre-wrap");
    let conversationIndex = 1;

    whitespacePreWrapElements.forEach((element, index) => {
        if (element.children.length === 1) {
            const downloadButton = createDownloadButton(conversationIndex);
            const buttonWrapper = document.createElement('span');
            buttonWrapper.style.display = 'inline'; // Make sure it's displayed inline
            buttonWrapper.appendChild(downloadButton);
            element.appendChild(buttonWrapper);
            conversationIndex++;
        }
    });

    if (whitespacePreWrapElements.length > 0) {
        const lastElement = whitespacePreWrapElements[whitespacePreWrapElements.length - 1];
        const saveAllButton = createDownloadButton(0, "전체저장");
        const saveResponsesButton = createDownloadButton(-1, "전체대답저장");

        const buttonWrapper = document.createElement('span');
        buttonWrapper.style.display = 'inline'; // Make sure it's displayed inline
        buttonWrapper.appendChild(saveAllButton);
        buttonWrapper.appendChild(saveResponsesButton);

        addClickListenerToDownloadButton(saveAllButton, 0); // Add click event listener
        addClickListenerToDownloadButton(saveResponsesButton, -1); // Add click event listener

        lastElement.appendChild(buttonWrapper);
    }
}

    // Call the function to add download buttons
    addDownloadButtonsBetweenElements();

// })();


// ////////////////////////////////////////////////////////////////////////////////////////////////////
//  프롬프트
// ////////////////////////////////////////////////////////////////////////////////////////////////////
// ////////////////////////////////////////////////////////////////////////////////////////////////////


function setPromptEngneering() {
    const systemPrompt = [
        {
          "act": "form1", 
          "prompt": "Your job is now to read the recent conversation after any provided previous context and return a list of memories. Can you write out a list of memories from the conversation in the format:  {\"title\":\"\", \"summary\":\"\", \"keyword\" :\"\"} "
        },
        {
            "act": "coding assist",
            "prompt": "vue3, script setup. You are a helpful super super codeing machine that answer question as simplify as possible."
        },
        {
            "act": "JavaScript Console",
            "prompt": "vue3, script setup. I want you to act as a javascript console. I will type commands and you will reply with what the javascript console should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. my first command is console.log(\"Hello World\");"
        },
        {
            "act": "Python interpreter",
            "prompt": "I want you to act like a Python interpreter. I will give you Python code, and you will execute it. Do not provide any explanations. Do not respond with anything except the output of the code. The first code is: \"print('hello world!')\""
        }];

    // "helow"를 textarea의 값으로 설정합니다.
    var textarea = document.getElementById("prompt-textarea");

    // "helow"와 개행 문자 3개를 textarea의 값으로 설정합니다.
    if (textarea) {
        // systemPrompt[2]의 객체를 JSON 문자열로 변환하고 개행문자 3개를 추가하여 textarea의 값으로 설정합니다.
        textarea.value = JSON.stringify(systemPrompt[2], null, 3);
    }

    // 버튼 요소를 찾습니다.
    var button = document.querySelector("[data-testid='send-button']");

    // 버튼을 활성화합니다.
    if (button) {
        button.removeAttribute("disabled");
    }
}
// Call the function to create download buttons within a single div container
setPromptEngneering()
// ////////////////////////////////////////////////////////////////////////////////////////////////////
//  상단 버튼
// ////////////////////////////////////////////////////////////////////////////////////////////////////
// ////////////////////////////////////////////////////////////////////////////////////////////////////

// Helper function to create a div wrapper for buttons
function createButtonContainer(buttons) {
    const buttonContainer = document.createElement("div");
    buttonContainer.classList.add("container-xxl"); // Bootstrap container class 추가
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

// Function to create download buttons and wrap them in a single div
// Function to create download buttons and wrap them in a single div
// Function to create download buttons and wrap them in a single div
// Helper function to create a div wrapper for buttons
function createButtonContainer(buttons) {
    const buttonContainer = document.createElement("div");
    buttonContainer.style.backgroundColor = "rgba(0, 0, 0, 0)"; // 배경색을 투명으로 설정
    buttonContainer.style.color = "white"; // 폰트색을 흰색으로 설정
    buttonContainer.style.borderRadius = "10px";
    buttonContainer.style.padding = "5px";
    buttonContainer.style.margin = "5px";
    buttonContainer.style.border = "1px solid #ccc"; // 회색 테두리 추가
    buttonContainer.style.display = "inline-flex"; // 버튼을 수평으로 정렬

    buttons.forEach(button => {
        button.style.color = "white"; // 각 버튼의 폰트색을 흰색으로 설정
        button.style.backgroundColor = "rgba(0, 0, 0, 0)"; // 버튼의 배경색을 투명으로 설정
        button.style.marginRight = "5px"; // 버튼 사이 간격 조정
        button.style.padding = "3px 5px"; // 버튼 내부 패딩 조정
        buttonContainer.appendChild(button);
    });

    return buttonContainer;
}

// Function to create download buttons and wrap them in a single div
function createDownloadButtonsInContainer() {
    const downloadButtons = [];
    const whitespacePreWrapElements = document.querySelectorAll("div.whitespace-pre-wrap");
    let conversationIndex = 1;

    whitespacePreWrapElements.forEach((element, index) => {
        if (element.children.length === 1) {
            const downloadButton = createDownloadButton(conversationIndex);
            downloadButtons.push(downloadButton);
            conversationIndex++;
        }
    });

    if (whitespacePreWrapElements.length >= 0) {
        const saveAllButton = createDownloadButton(0, "전체저장");
        downloadButtons.push(saveAllButton);

        const saveResponsesButton = createDownloadButton(-1, "전체대답저장");
        downloadButtons.push(saveResponsesButton);
    }

    const buttonContainer = createButtonContainer(downloadButtons);

    // 아래 부분을 수정하여 버튼이 들어갈 요소를 찾아주세요.
    const targetElement = document.querySelector(".mb-1.flex.flex-row.gap-2"); // 버튼을 추가할 대상 요소를 선택합니다.

    if (targetElement) {
        // 대상 요소의 상단에 버튼 컨테이너를 추가합니다.
        targetElement.parentElement.insertBefore(buttonContainer, targetElement);
    } else {
        console.error("Target element not found.");
    }
}

// Call the function to create download buttons within a single div container
createDownloadButtonsInContainer();
})();

기능은 유지 하고 최적화 할수 있는 부분을 알려줘저장 7

## 8)
코드를 최적화하고 기능을 유지하는 방법을 제안해드리겠습니다:코드 분리와 모듈화: 코드를 더 작은 함수와 모듈로 분리하여 가독성을 향상시킬 수 있습니다. 예를 들어, 파일 저장 및 버튼 생성과 관련된 기능을 별도의 함수로 분리할 수 있습니다.반복 코드 최소화: 코드에서 반복되는 부분을 최소화하고 코드 재사용성을 높일 수 있습니다. 일부 코드 조각은 여러 번 나타나는데, 이를 함수로 추상화하여 중복을 줄일 수 있습니다.코드 주석: 코드에 주석을 추가하여 각 부분의 역할을 설명하고, 코드를 이해하기 쉽도록 도움을 줄 수 있습니다.ES6+ 기능 활용: 최신 JavaScript 기능을 활용하여 코드를 더 간결하게 작성할 수 있습니다. 예를 들어, 화살표 함수와 템플릿 리터럴을 사용하여 문자열을 보다 간결하게 작성할 수 있습니다.이벤트 위임: 여러 요소에 대한 이벤트 리스너를 개별로 추가하는 대신, 이벤트 위임을 활용하여 부모 요소에서 이벤트를 처리할 수 있습니다.버튼 스타일 중복 제거: 버튼 스타일을 중복으로 설정하는 부분을 함수나 CSS 클래스로 추상화하여 중복을 최소화할 수 있습니다.아래는 위의 제안을 반영한 코드 예제입니다. 이 코드는 여러 부분을 함수로 분리하고 주석을 추가하여 가독성을 높였습니다. 또한 ES6+ 기능을 활용하고 중복 코드를 최소화했습니다:javascriptCopy code(() => {
    // Helper function to create and click a download link
    function createAndClickDownloadLink(fileName, content) {
        if (content.length >= 12) {
            const downloadLink = document.createElement("a");
            downloadLink.download = fileName;
            downloadLink.href = URL.createObjectURL(new Blob([content], { type: "text/markdown" }));
            downloadLink.click();
        } else {
            console.log("Content is too short to save. more than 11");
        }
    }

    // Helper function to create download button
    function createDownloadButton(index, buttonText) {
        const downloadButton = document.createElement("button");
        downloadButton.textContent = buttonText || `저장 ${index}`;
        downloadButton.classList.add("btn", "btn-primary", "m-2");
        downloadButton.style.color = "white";
        downloadButton.style.backgroundColor = "transparent";
        downloadButton.style.marginRight = "5px";
        downloadButton.style.padding = "3px 5px";
        return downloadButton;
    }

    // Helper function to add click event listener to download buttons
    function addClickListenerToDownloadButton(downloadButton, index) {
        downloadButton.addEventListener("click", () => {
            extractAndSaveConversations(index);
        });
    }

    // Function to create download buttons
    function createDownloadButtonsInContainer() {
        const downloadButtons = [];
        const whitespacePreWrapElements = document.querySelectorAll("div.whitespace-pre-wrap");
        let conversationIndex = 1;

        whitespacePreWrapElements.forEach((element, index) => {
            if (element.children.length === 1) {
                const downloadButton = createDownloadButton(conversationIndex);
                downloadButtons.push(downloadButton);
                addClickListenerToDownloadButton(downloadButton, conversationIndex);
                conversationIndex++;
            }
        });

        if (whitespacePreWrapElements.length >= 0) {
            const saveAllButton = createDownloadButton(0, "전체저장");
            downloadButtons.push(saveAllButton);
            addClickListenerToDownloadButton(saveAllButton, 0);

            const saveResponsesButton = createDownloadButton(-1, "전체대답저장");
            downloadButtons.push(saveResponsesButton);
            addClickListenerToDownloadButton(saveResponsesButton, -1);
        }

        const buttonContainer = createButtonContainer(downloadButtons);
        const targetElement = document.querySelector(".mb-1.flex.flex-row.gap-2");

        if (targetElement) {
            targetElement.parentElement.insertBefore(buttonContainer, targetElement);
        } else {
            console.error("Target element not found.");
        }
    }

    // Call the function to create download buttons within a single div container
    createDownloadButtonsInContainer();

    // Rest of your code...
})();
위 코드에서는 코드를 모듈화하고 중복을 제거하여 가독성과 유지 보수성을 개선했습니다. 이러한 변경 사항을 적용하면 코드가 더 관리하기 쉬워질 것입니다.저장 8전체저장전체대답저장