PROMPT:

dictsDf = df \[\['U\_pattern\_name','D\_pattern\_name','company', 'Count\_U', 'Count\_D', 'Sum\_UD'\]\] df = dictsDf.set\_index('company') dicts = df.to\_dict() 할때 인덱스, 컬럼을 스위칭

RESPONSE:

스위칭된 인덱스와 컬럼을 사용하여 `df.to_dict()`를 호출하려면 `transpose()` 메소드를 사용하여 DataFrame을 전치(transpose)해야 합니다. 아래는 코드 예시입니다:

```python
dictsDf = df[['U_pattern_name', 'D_pattern_name', 'company', 'Count_U', 'Count_D', 'Sum_UD']]
df = dictsDf.set_index('company')
dicts = df.transpose().to_dict()
```

이렇게 하면 `dicts`에는 전치된 DataFrame의 인덱스가 컬럼이 되고, 컬럼이 인덱스가 되는 딕셔너리가 저장됩니다.