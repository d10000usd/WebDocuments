# 랜덤 알파벳 추가 코드

## 1)
아래의 코드는 현재 초 값을 가져와서 랜덤으로 알파벳 2글자를 추가하는 JavaScript 코드입니다.

```javascript
const now = new Date();
const alphabet = 'abcdefghijklmnopqrstuvwxyz';
const randomChars = alphabet[Math.floor(Math.random() * 26)] + alphabet[Math.floor(Math.random() * 26)];
const dateString = `${now.getSeconds().toString().padStart(2, '0')}${randomChars}`;
```

이 코드는 `alphabet` 문자열에서 랜덤한 두 개의 알파벳을 선택하여 `randomChars`에 저장하고, 현재 초 값을 가져와서 두 알파벳과 함께 이를 조합하여 `dateString`에 저장합니다.

또한, 이 코드의 알고리즘을 설명하면 다음과 같습니다:
1. 현재 시간을 나타내는 `now` 객체를 생성합니다.
2. 알파벳 문자열 `alphabet`을 정의합니다.
3. `Math.random()` 함수를 사용하여 0부터 25 사이의 난수를 생성하고, 이를 이용하여 `alphabet`에서 랜덤한 알파벳 두 개를 선택하여 `randomChars`에 저장합니다.
4. 현재 초 값을 가져와서 `padStart` 함수를 사용하여 두 자리 숫자로 변환한 후, `randomChars`와 함께 조합하여 `dateString`에 저장합니다.

다른 방식으로 이 문제를 해결하는 것은 어려운 부분이 없으며, 이 코드는 간단하고 효율적인 방법으로 문제를 해결합니다.