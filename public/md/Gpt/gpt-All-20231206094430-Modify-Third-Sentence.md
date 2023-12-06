# **<span style="font-size: 35px; font-style: italic;">Modify Third Sentence</span>**

>Modify Third Sentence  
2023년 12월 06일 09시 44분  
SaaS  
#article #code #keyword  
[Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
Here’s a brief explanation read more
## Description  

<body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  ```javascript
function firstLineSeek(text) {
    // 문자열을 마침표로 분할하여 문장 배열을 생성
    const sentences = text.split('. ');

    const thirdSentence = sentences[2];
    // 문장 끝에서 5글자 제거
    const modifiedThirdSentence = thirdSentence.slice(0, -5);
    // 추출된 수정된 문장을 배열에 저장하고 리턴
    const result = [modifiedThirdSentence];

    return result;
}
```


  </div></div></div>

  <body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  It seems like the function is encountering an issue, likely because the third sentence is undefined. To handle this, you can add a check to ensure that `thirdSentence` exists before trying to manipulate it. Here's the updated code:

```javascript
function firstLineSeek(text) {
    // 문자열을 마침표로 분할하여 문장 배열을 생성
    const sentences = text.split('. ');

    // 세 번째 문장이 존재하는지 확인 후 추출
    const thirdSentence = sentences[2];
    
    if (thirdSentence) {
        // 문장 끝에서 5글자 제거
        const modifiedThirdSentence = thirdSentence.slice(0, -5);
        // 추출된 수정된 문장을 배열에 저장하고 리턴
        const result = [modifiedThirdSentence];
        return result;
    } else {
        // 세 번째 문장이 없을 경우 빈 배열 반환
        return [];
    }
}
```

This modification should prevent the TypeError by checking if `thirdSentence` exists before attempting to use the `slice` method.


  </div></div></div>

  <div style="background-color: grey; height: 15px;"></div>

  