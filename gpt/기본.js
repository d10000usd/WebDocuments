(() => {
    const msgs = document.querySelectorAll("div.whitespace-pre-wrap");
    const markdowns = {};

    // Function to generate Markdown content for a ChatGPT response
    function generateMarkdownContent(div, index) {
        const mddiv = div.children[0];
        const fiberKey = Object.keys(mddiv).find(k => k.startsWith('__reactFiber$'));
        const origMd = mddiv[fiberKey].return.pendingProps.children;

        // Define formatting for the title
        const titleStyle = '<span style="font-size: 18px; font-style: italic;">';
        // Apply formatting to the document.title
        const formattedTitle = `${titleStyle}${document.title}</span>`;
        // Create the Markdown content
        return `# **${formattedTitle}**\n${origMd}`;
    }

    // Function to create a button with specified text and click handler
    function createButton(text, clickHandler) {
        const button = document.createElement("button");
        button.innerText = text;

        // Add styles for gray border and rounded corners
        button.style.border = "1px solid #ccc";
        button.style.borderRadius = "5px";

        button.addEventListener("click", clickHandler);
        return button;
    }

    // Function to handle the button click and save markdown
    function handleButtonClick(index) {
        const markdownContent = markdowns[`#${index + 1}`];
        const blob = new Blob([markdownContent], { type: "text/markdown" });
        const now = new Date();
        const dateString = `${now.getFullYear()}${(now.getMonth() + 1).toString().padStart(2, '0')}${now.getDate().toString().padStart(2, '0')}${now.getHours().toString().padStart(2, '0')}${now.getMinutes().toString().padStart(2, '0')}${now.getSeconds().toString().padStart(2, '0')}`;

        const fileName = `gpt-All-${dateString}-${document.title.replace(/\s+/g, '-')}.md`;
        const downloadLink = document.createElement("a");
        downloadLink.download = fileName;
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.click();
    }

    // Function to handle the button click and save all content to one file
    function handleSaveAllButtonClick() {
        let allMd = "";
        Object.entries(markdowns).forEach(([key, value]) => {
            allMd += `${key}\n\n${value}\n\n`;
        });

        const now = new Date();
        const dateString = `${now.getFullYear()}${(now.getMonth() + 1).toString().padStart(2, '0')}${now.getDate().toString().padStart(2, '0')}${now.getHours().toString().padStart(2, '0')}${now.getMinutes().toString().padStart(2, '0')}${now.getSeconds().toString().padStart(2, '0')}`;

        // gpt-20231206094446-Python-Fasapi-Example
        // ChatGPT-log---백그라운드-메시지-수신---20240206T115247
        // 20240206T115247
        // 20231206094251
        
        // gpt-All-20231206094251-FastAPI-News-Server
        const fileName = `gpt-All-${dateString}-${document.title.replace(/\s+/g, '-')}.md`;
        const blob = new Blob([allMd], { type: "text/markdown" });
        const downloadLink = document.createElement("a");
        downloadLink.download = fileName;
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.click();
    }

    Array.from(msgs).forEach((div, index) => {
        if (div.children.length === 1 && (index + 1) % 2 === 0) {
            // This is a ChatGPT response for even indices.
            const markdownContent = generateMarkdownContent(div, index);
            markdowns[`#${index + 1}`] = markdownContent;

            // Create a button for even indices with index number inside square brackets
            const button = createButton(`[${index + 1}] Save Index ${index + 1} as Markdown`, () => handleButtonClick(index));
            div.appendChild(button);
        }
    });
    const lastDiv = msgs[msgs.length - 1];

    // Create a button to save all content to one file
    const saveAllButton = createButton("Save All as One Markdown File", handleSaveAllButtonClick);
    lastDiv.appendChild(saveAllButton);

})();
