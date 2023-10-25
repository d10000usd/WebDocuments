# **<span style="font-size: 35px; font-style: italic;">CSS Image Ratio Adjustment.</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-30.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 1</div></div>
이미지를 비율에 맞게 조정하기 위해 CSS를 사용하는 방법이 있습니다. 일반적으로 이미지의 최대 너비 또는 높이를 설정하여 이미지 비율을 유지하는 것이 좋습니다. 아래는 CSS를 사용하여 이미지를 비율에 맞게 조정하는 방법의 예시입니다:

```css
img {
  max-width: 100%;
  height: auto;
}
```

위 CSS는 이미지의 최대 너비를 부모 요소의 너비에 맞게 조정하고, 높이를 자동으로 조정하여 원래 비율을 유지합니다. 이렇게 하면 이미지가 비율에 맞게 조정되면서 부모 요소에 맞게 크기가 조정됩니다. 이 CSS를 해당 이미지를 보여주는 요소에 적용하면 됩니다.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-30.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
이미지를 가운데 정렬하려면 추가적인 CSS 속성이 필요합니다. 다음과 같이 `display`와 `margin` 속성을 활용하여 이미지를 가운데로 정렬할 수 있습니다:

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: auto;
}
```

위 CSS 코드는 이미지를 화면에서 가운데로 정렬시킵니다. `display: block;`은 이미지를 블록 레벨 요소로 설정하여 수평으로 가운데 정렬하는 데 도움이 됩니다. `margin: auto;`는 수평 방향으로 자동으로 마진을 설정하여 이미지를 가운데에 배치합니다. 이 CSS를 해당 이미지를 보여주는 요소에 적용하면 이미지가 비율에 맞게 가운데 정렬되면서 부모 요소에 맞게 크기가 조정됩니다.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-31.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 3</div></div>
옆에 있는 요소와 마진을 조정하려면, CSS의 `margin` 속성을 사용할 수 있습니다. 다음과 같이 해당 클래스에 `margin` 속성을 추가하여 옆에 있는 요소와 마진을 설정할 수 있습니다:

```css
.custom-card {
  margin-bottom: 0.1rem; /* 원하는 마진 크기 설정 */
  margin-right: 0.5rem; /* 옆에 있는 요소와의 마진 크기 설정 */
}
```

위 CSS 코드는 `custom-card` 클래스에 오른쪽에 있는 요소와의 마진을 0.5rem으로 설정합니다. 이렇게 함으로써 해당 요소와 옆에 있는 요소 사이에 원하는 간격을 만들 수 있습니다.



<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-33.png)  
- CSS Image Ratio Adjustment.  
- 20231025042257  
- gpt  
- #gpt #code #keyword  
- 일반적으로 이미지의 최대 너비 또는 높이를 설정하여 이미지 비율을 유지하는 것이 좋습니다,아래는 CSS를 사용하여 이미지를 비율에 맞게 조정하는 방법의 예시입니다:

```css
img {
  max-width: 100%;
  height: auto;
}
```

위 CSS는 이미지의 최대 너비를 부모 요소의 너비에 맞게 조정하고, 높이를 자동으로 조정하여 원래 비율을 유지합니다  
</div> 
