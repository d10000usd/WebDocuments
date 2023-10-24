# **<span style="font-size: 35px; font-style: italic;">GitJsonRead Function Update</span>**


<div class="body-full">

당연히요. 아래 코드는 프로미스를 사용하여 `text` 값을 반환합니다.

```javascript
export async function GitJsonRead(localpath: string){
    return new Promise((resolve, reject) => {
        fetch(`../${localpath}`)
        .then(response => response.text())
        .then(text => resolve(text))
        .catch(error => {
            console.error(error);
            reject(error);
        });
    });
};
```

이렇게하면 함수가 프로미스를 반환하므로 호출 측에서 해당 프로미스를 처리할 수 있습니다.


</div>