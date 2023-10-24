# **<span style="font-size: 35px; font-style: italic;">GitJsonRead Function Update</span>**


<div class="body-full">

Sure, here is the modified code:

```javascript
export async function GitJsonRead(localpath: string){
    try {
        const response = await fetch(`../${localpath}`);
        const text = await response.text();
        return text;
    } catch (error) {
        console.error(error);
        return Promise.reject(error);
    }
};
```

In this modified version, the catch block returns a rejected promise, ensuring that the function continues to propagate any errors that occur during the execution.


</div>