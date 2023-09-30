# Set Engineering Prompt

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