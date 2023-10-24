# **<span style="font-size: 35px; font-style: italic;">Extract Substring between Dots.</span>**


- 2023-10-24-12  
- Extract Substring between Dots.  
- gpt  
- #gpt,#code,#keyword  
        
To extract the substring between the first occurrence of the character "." and the second occurrence, you can use the following JavaScript code:

```javascript
let searchString = allMd;
let firstDotIndex = searchString.indexOf('.');
let secondDotIndex = searchString.indexOf('.', firstDotIndex + 1);

if (firstDotIndex !== -1 && secondDotIndex !== -1) {
    let result = searchString.substring(firstDotIndex + 1, secondDotIndex);
    console.log(result); // You can store or manipulate the extracted substring here
} else {
    console.log("Both '.' not found or only one '.' found.");
}
```

This code snippet finds the indices of the first and second occurrences of the dot (".") in the string `allMd` and then extracts the substring between them. Adjust the variable `allMd` to your specific string.




<div style="background-color: grey; height: 15px;"></div>

