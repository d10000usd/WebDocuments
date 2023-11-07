# **Image Density Categories**
주어진 `density_categories` 배열을 사용하여 `config` 딕셔너리에 있는 `"imgDict"` 및 `"imgDict1"`의 `"text"` 값들을 바꾸는 방법은 다음과 같습니다:

```python
config['imgDict']['text'] = density_categories[0]  # 첫 번째 카테고리로 설정
config['imgDict1']['text'] = density_categories[1]  # 두 번째 카테고리로 설정
```

이렇게 하면 `"imgDict"`와 `"imgDict1"`의 `"text"` 값이 `density_categories` 배열의 첫 번째와 두 번째 항목으로 변경됩니다. 이를 통해 각 이미지의 텍스트를 원하는 밀도 범주로 설정할 수 있습니다.




