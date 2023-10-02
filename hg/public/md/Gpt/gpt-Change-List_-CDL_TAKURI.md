PROMPT:

RESPONSE:

아래는 주어진 리스트에서 'takuri'를 'CDL\_TAKURI'로 일괄 변경하는 파이썬 코드 예시입니다:

```python
data_list = ['3whitesoldiers', 'takuri', '2crows', 'longline']

for index, item in enumerate(data_list):
    if item == 'takuri':
        data_list[index] = 'CDL_TAKURI'

print(data_list)
```

이 코드를 실행하면 `data_list` 리스트에서 'takuri'가 'CDL\_TAKURI'로 변경된 결과를 출력합니다.

PROMPT:

RESPONSE:

알겠습니다. 주어진 리스트에서 '3whitesoldiers', 'takuri', '2crows', 'longline'를 각각 'CDL\_3WHITESOLDIERS', 'CDL\_TAKURI', 'CDL\_2CROWS', 'CDL\_LONGLINE'으로 일괄 변경하는 파이썬 코드 예시는 다음과 같습니다:

```python
data_list = ['3whitesoldiers', 'takuri', '2crows', 'longline']

for index, item in enumerate(data_list):
    if item == '3whitesoldiers':
        data_list[index] = 'CDL_3WHITESOLDIERS'
    elif item == 'takuri':
        data_list[index] = 'CDL_TAKURI'
    elif item == '2crows':
        data_list[index] = 'CDL_2CROWS'
    elif item == 'longline':
        data_list[index] = 'CDL_LONGLINE'

print(data_list)
```

이 코드를 실행하면 `data_list` 리스트의 모든 항목이 해당하는 패턴에 따라 변경되어 'CDL\_' 접두사가 추가된 결과를 출력합니다.

PROMPT:

RESPONSE:

알겠습니다. 비교 없이 일괄적으로 변경하는 파이썬 코드 예시는 다음과 같습니다:

```python
data_list = ['3whitesoldiers', 'takuri', '2crows', 'longline']

# 변경 매핑 정의
name_mapping = {
    '3whitesoldiers': 'CDL_3WHITESOLDIERS',
    'takuri': 'CDL_TAKURI',
    '2crows': 'CDL_2CROWS',
    'longline': 'CDL_LONGLINE'
}

# 매핑에 따라 일괄적으로 변경
for index, item in enumerate(data_list):
    if item in name_mapping:
        data_list[index] = name_mapping[item]

print(data_list)
```

이 코드를 실행하면 `data_list` 리스트의 모든 항목이 `name_mapping`에 정의된 대응 관계에 따라 일괄적으로 변경됩니다. 더 이상 비교를 수행하지 않으며, 주어진 매핑에 따라 새로운 값으로 변경됩니다.