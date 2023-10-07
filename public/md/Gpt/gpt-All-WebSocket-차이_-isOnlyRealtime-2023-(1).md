# **<span style="font-size: 35px; font-style: italic;">WebSocket 차이: isOnlyRealtime</span>**

> ## 1
# WebSocket 연결 및 실시간 데이터 처리

## 설명
위의 코드는 Vue.js 컴포넌트에서 `onMounted` 라이프사이클 훅에서 WebSocket을 이용하여 실시간 데이터를 받아오는 부분입니다. 주로 암호화폐 시세 데이터를 받아오는 경우에 사용됩니다.

### 코드 설명
1. `onMounted` 훅을 사용하여 컴포넌트가 마운트된 후에 실행되는 코드 블록입니다.
2. `try-catch` 블록을 사용하여 예외 처리를 수행합니다.
3. WebSocket 객체를 생성하고 `wss://api.upbit.com/websocket/v1` 주소로 연결합니다.
4. 연결이 열리면, `onopen` 이벤트 핸들러가 호출되어 초기 데이터를 서버에 요청합니다.
5. 요청은 JSON 형식으로 데이터를 패킷에 담아서 서버에 보내며, 이 패킷은 `ticker` 형식의 데이터를 요청합니다.
6. 서버에서 데이터가 도착하면 `onmessage` 이벤트 핸들러가 호출되고, `handleWebSocketMessage` 함수가 호출됩니다.

### `isOnlyRealtime` 차이
`isOnlyRealtime` 변수가 `true`일 때와 `false`일 때의 차이는 코드 내에서 주요한 정보로 나타나지 않습니다. 이 변수가 다른 곳에서 정의되고 사용되는 경우, 해당 코드 부분을 확인하여 두 경우 간의 차이를 이해할 수 있습니다. 코드 내에서 `isOnlyRealtime` 변수의 사용과 관련된 부분이 없으므로 추가 정보가 필요합니다.
*****



> ## 2
`isOnlyRealtime: true` 일 때와 `isOnlyRealtime: false` 일 때의 동작을 설명드리겠습니다.

1. `isOnlyRealtime: true`:
   - 이 설정이 `true`로 되어 있다면, 초기 연결 후에는 실시간으로 떨어지는 값을 받아옵니다. 즉, 초기 데이터 요청 이후에는 새로운 데이터만을 받아옵니다. 이 경우, 과거 데이터는 받아오지 않습니다.

2. `isOnlyRealtime: false`:
   - 이 설정이 `false`로 되어 있다면, 초기 연결 후에는 모든 데이터를 받아옵니다. 따라서 초기 데이터 요청 이후에도 과거 데이터와 함께 새로운 데이터를 계속해서 받아옵니다.

`isOnlyRealtime` 변수를 `true`로 설정하면 실시간으로 떨어지는 값만을 받고, `false`로 설정하면 초기 데이터와 실시간 데이터를 모두 받게 됩니다. 이 설정은 서버와의 통신 방식을 제어하며, 어떤 데이터를 받을지 여부를 조절할 때 사용됩니다.
*****



