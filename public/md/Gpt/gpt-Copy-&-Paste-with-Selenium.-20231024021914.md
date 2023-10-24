# **<span style="font-size: 35px; font-style: italic;">Copy & Paste with Selenium.</span>**


<div class="body-full">

이 코드에서 발생한 오류는 클립보드에 복사할 때 바이트 형식의 데이터를 사용했기 때문에 발생한 것으로 보입니다. pyperclip은 문자열, 정수, 부동 소수점, 불리언 값만 클립보드로 복사할 수 있습니다.

해결책으로는 바이너리 데이터를 문자열로 변환하여 클립보드에 복사하는 것입니다. 아래는 수정된 코드입니다.

```python
from selenium import webdriver
import pyperclip

# 맥에서 이미지를 클립보드로 복사하는 방법은 이미지를 파일로 저장한 후 pyperclip을 사용하여 복사할 수 있습니다.
# 아래 코드는 주어진 경로에 있는 이미지를 클립보드로 복사합니다.
image_path = '/Users/hg/DEV/naverblog/dt.png'
with open(image_path, 'rb') as image_file:
    image_data = image_file.read()
    pyperclip.copy(str(image_data))  # 바이너리 데이터를 문자열로 변환하여 클립보드에 복사합니다.

# 이후 셀레니움을 사용하여 붙여넣기 할 수 있습니다.
driver = webdriver.Chrome()  # Chrome 드라이버를 사용하겠지만, 다른 드라이버를 사용할 수도 있습니다.
driver.get('URL_여기에_넣으세요')  # 붙여넣기할 페이지의 URL을 여기에 넣어주세요.
element = driver.find_element_by_xpath('XPATH_여기에_넣으세요')  # 붙여넣기할 요소의 XPATH를 여기에 넣어주세요.
element.send_keys(pyperclip.paste())  # 클립보드의 내용을 붙여넣습니다.

# 이 코드는 클립보드에 있는 이미지를 맥에서 가져와 셀레니움으로 붙여넣는 과정을 보여줍니다. 
```

위 코드는 클립보드로 복사할 때 바이너리 데이터를 문자열로 변환하여 복사하고, 이후 셀레니움을 사용하여 붙여넣기하는 과정을 보여줍니다. 주어진 코드는 이미지 경로와 페이지 URL, 그리고 XPATH에 따라 적절하게 수정되어야 합니다.


</div>