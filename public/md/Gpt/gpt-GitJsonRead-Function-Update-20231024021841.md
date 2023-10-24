# **<span style="font-size: 35px; font-style: italic;">GitJsonRead Function Update</span>**


<div class="body-full">

You can certainly return `text` in the catch block, but if you return `text` there, it will indicate a successful result even if there was an error. If you want to return the `text` in the catch block while still signaling that an error occurred, you can do it like this:

```javascript
export async function GitJsonRead(localpath: string){
    try {
        const response = await fetch(`../${localpath}`);
        const text = await response.text();
        return text;
    } catch (error) {
        console.error(error);
        return error; // Return the error object or message here.
    }
};
```

This way, you can access the error information if needed while still getting the text in case of success.


</div>