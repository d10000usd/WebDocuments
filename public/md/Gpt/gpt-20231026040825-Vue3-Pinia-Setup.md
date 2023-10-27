# **<span style="font-size: 35px; font-style: italic;">Vue3 Pinia Setup</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-40.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 5</div></div>
아래의 코드는 주어진 텍스트에서 띄어쓰기 단위로 가장 빈도수가 높은 상위 10개 단어를 찾아 배열에 넣는 방법을 보여줍니다.

```python
from collections import Counter

text = '''
## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-37.png)  
- Vue3 Pinia Setup  
- 20231026032643  
- gpt  
- #gpt #code #keyword  
****
'''

start = '## meta'
end = '****'

# 시작 문자열 이후, 끝 문자열 이전의 부분을 추출
extracted_text = text[text.find(start) + len(start):text.rfind(end)].strip()

# 띄어쓰기 단위로 단어 추출
words = extracted_text.split()

# 각 단어의 빈도수 계산
word_counts = Counter(words)

# 빈도수가 높은 상위 10개의 단어 추출
top_words = word_counts.most_common(10)

# 결과를 배열에 넣기
result_array = [word for word, count in top_words]
print(result_array)
```

이 코드를 사용하면 주어진 텍스트에서 띄어쓰기 단위로 가장 빈도수가 높은 상위 10개의 단어를 배열에 넣을 수 있습니다.







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-31.png)  
- Vue3 Pinia Setup  
- 20231026040825  
- gpt  
- #gpt #code #keyword  
****
undefined  
</div> 
