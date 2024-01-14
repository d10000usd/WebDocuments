# **<span style="font-size: 35px; font-style: italic;">Fetch and Display Data</span>**

>Fetch and Display Data  
2024년 01월 14일 06시 38분  
SaaS  
#article #code #keyword  
[Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
Here’s a brief explanation read more
## Description  

<body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  주어진 URL에서 데이터를 가져와 iframe으로 표시하는 것을 원하시는 것 같습니다. 아래는 JavaScript를 사용하여 이 작업을 수행하는 예제입니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IFrame 예제</title>
</head>
<body>

<!-- iframe을 담을 공간 -->
<iframe id="myIframe" width="100%" height="500px" frameborder="0"></iframe>

<script>
// XMLHttpRequest 객체를 사용하여 데이터를 가져오는 함수
function fetchData(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            callback(xhr.responseText);
        }
    };
    xhr.open("GET", url, true);
    xhr.send();
}

// URL에서 데이터 가져오기
var apiUrl = "http://172.30.1.10:7001/api/1/search.naver?sm=1&page=2&query=%ED%8F%AC%EC%8A%A4%EC%BD%94&where=extention";
fetchData(apiUrl, function(data) {
    // 데이터를 iframe에 삽입
    document.getElementById("myIframe").srcdoc = data;
});
</script>

</body>
</html>
```

이 코드는 XMLHttpRequest를 사용하여 주어진 URL에서 데이터를 가져오고, 가져온 데이터를 iframe의 srcdoc 속성을 통해 삽입합니다. 이렇게 하면 해당 데이터가 iframe에 표시됩니다.


  </div></div></div>

  <div style="background-color: grey; height: 15px;"></div>

  