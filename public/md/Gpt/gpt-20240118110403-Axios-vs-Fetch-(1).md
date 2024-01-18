# **<span style="font-size: 35px; font-style: italic;">Axios vs Fetch</span>**

>Axios vs Fetch  
2024년 01월 18일 11시 04분  
SaaS  
#article #code #keyword  
[Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
Here’s a brief explanation read more
## Description  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  두 함수 간의 주요 차이를 간단하게 설명하겠습니다.

1. **fetchData1 함수 (fetch API 사용)**:

```javascript
async fetchData1() {
  try {
    const response = await fetch(this.globalurl[this.urlkey]);
    const data = await response.text();
    this.apiData.value = data;
    return this.apiData.value;
  } catch (error) {
    console.error('데이터를 가져오는 중 오류 발생:', error);
  }
}
```

2. **fetchData 함수 (Axios 사용)**:

```javascript
async fetchData() {
  try {
    const response = await axios.get(this.globalurl[this.urlkey]);
    this.apiData.value = response.data;
    return this.apiData.value;
  } catch (error) {
    console.error('데이터를 가져오는 중 오류 발생:', error);
  }
}
```

**차이점**:

- **라이브러리**: `fetchData1`는 기본 Fetch API를 사용하고, `fetchData`는 Axios 라이브러리를 사용합니다.

- **데이터 형식**: `fetchData1`는 `response.text()`를 사용하여 텍스트 데이터를 가져오고, `fetchData`는 Axios의 `response.data`를 사용하여 데이터를 가져옵니다. Axios는 주로 JSON 데이터를 자동으로 파싱합니다.

두 함수는 비슷한 기능을 하지만 사용된 라이브러리와 데이터 형식에서 차이가 있습니다. 선택은 프로젝트 요구사항 및 개발자 선호도에 따라 이루어질 수 있습니다.
