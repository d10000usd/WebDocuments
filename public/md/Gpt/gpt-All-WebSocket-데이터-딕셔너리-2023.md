# **<span style="font-size: 35px; font-style: italic;">WebSocket 데이터 딕셔너리</span>**

> ## 1
당신이 제공한 코드를 딕셔너리로 수정하겠습니다. 딕셔너리를 사용하여 WebSocket 데이터를 저장하겠습니다.

```javascript
import { ref, onMounted, onUnmounted } from "vue";

// WebSocket 데이터 타입
interface WebSocketData {
  code: string;
  opening_price: number;
  low_price: number;
  high_price: number;
  trade_price: number;
  timestamp: number;
  trade_volume: number;
}

const UPBIT_URL: string = "wss://api.upbit.com/websocket/v1";

export default function useWebSocket(codes: string[]) {
  // 데이터를 딕셔너리로 저장
  const result = ref<{ [key: string]: WebSocketData }>({});

  let ws: WebSocket | null = null;

  const data = [
    { ticket: "nexoneunji" },
    { type: "ticker", codes, isOnlyRealtime: true },
  ];

  const setupWebSocket = () => {
    ws = new WebSocket(UPBIT_URL);

    ws.onopen = () => {
      ws?.send(JSON.stringify(data));
    };

    ws.onclose = () => {
      console.log("DISCONNECTED");
    };

    ws.onmessage = async (event) => {
      const text = await new Response(event.data).text();
      const message: WebSocketData = JSON.parse(text);
      updateResult(message);
    };

    ws.onerror = (event) => {
      console.log("Error", event);
      closeWebSocket();
    };
  };

  const closeWebSocket = () => {
    ws?.close();
  };

  const updateResult = (message: WebSocketData) => {
    // WebSocketData 인터페이스에 정의된 속성만 업데이트
    const updatedData: WebSocketData = {
      code: message.code,
      opening_price: message.opening_price,
      low_price: message.low_price,
      high_price: message.high_price,
      trade_price: message.trade_price,
      timestamp: message.timestamp,
      trade_volume: message.trade_volume,
    };

    // 코드가 이미 딕셔너리에 존재하는지 확인하고 새로운 데이터 업데이트
    result.value[message.code] = updatedData;
  };

  onMounted(() => {
    setupWebSocket();
  });

  onUnmounted(() => {
    closeWebSocket();
  });

  return { result };
}
```

이 코드는 WebSocket 데이터를 딕셔너리에 저장하고 업데이트하는 방식으로 변경되었습니다.
*****



> ## 2
1분 캔들을 만들 때 어느 쪽이 유리한지에 대해서는 다음 두 가지 방법을 고려해볼 수 있습니다:

1. 웹소켓 실시간 데이터:
   - 이 접근 방식은 웹소켓을 사용하여 실시간으로 거래 데이터를 수신하고 1분 캔들을 만드는 것입니다.
   - 이점:
     - 실시간 데이터를 받아들이므로 최신 거래 정보를 반영하는데 용이합니다.
     - 거래 데이터가 실시간으로 업데이트되므로 1분 캔들을 업데이트하는 데 거의 지연이 없습니다.
   - 단점:
     - 웹소켓 연결을 유지하기 위한 서버 및 클라이언트 측 로직이 필요합니다.
     - 서버 리소스를 사용하며, 연결 문제가 발생할 수 있습니다.

2. 누적 데이터 사용:
   - 이 접근 방식은 거래 데이터를 누적하여 1분 캔들을 만드는 것입니다. 일정 시간마다 거래 데이터를 합산하여 1분 캔들을 업데이트합니다.
   - 이점:
     - 데이터를 누적하기 때문에 별도의 웹소켓 연결이 필요하지 않습니다.
     - 서버 리소스를 절약할 수 있으며, 연결 문제에 민감하지 않습니다.
   - 단점:
     - 캔들이 실시간 데이터보다 지연될 수 있으며, 최신 거래 정보를 정확하게 반영하지 않을 수 있습니다.
     - 캔들 간의 간격을 조정해야 하며, 이를 위한 추가 로직이 필요합니다.

어떤 방법이 유리한지는 사용 사례 및 요구 사항에 따라 다를 수 있습니다. 실시간 데이터의 정확성과 지연 여부를 고려하여 선택하십시오.
*****



> ## 3
1분 봉 캔들을 만들어서 리턴하는 함수를 만들어 보겠습니다. 아래는 JavaScript로 작성된 예제 코드입니다. 이 코드는 입력으로 거래 데이터 배열을 받고, 해당 데이터에서 1분 봉 캔들을 생성한 후에 반환합니다.

```javascript
function create1MinuteCandles(tradeData) {
  // 거래 데이터를 1분 봉 캔들로 변환하는 함수
  function convertToCandle(data) {
    const candle = {
      timestamp: data[0],          // 캔들의 타임스탬프
      opening_price: data[1],     // 시작 가격
      low_price: data[2],         // 최저 가격
      high_price: data[3],        // 최고 가격
      closing_price: data[4],     // 종가
      volume: data[5],            // 거래량
    };
    return candle;
  }

  // 1분 봉 캔들 배열 초기화
  const oneMinuteCandles = [];

  // 1분 봉 캔들을 만드는 로직
  let currentCandle = null;  // 현재 1분 봉 캔들
  let currentMinute = null;  // 현재 분

  for (const trade of tradeData) {
    const tradeTimestamp = trade.timestamp;  // 거래의 타임스탬프

    // 타임스탬프에서 분을 추출
    const tradeMinute = new Date(tradeTimestamp).getMinutes();

    if (currentMinute === null) {
      // 최초 거래 처리
      currentMinute = tradeMinute;
      currentCandle = [
        tradeTimestamp,
        trade.trade_price,
        trade.trade_price,
        trade.trade_price,
        trade.trade_price,
        trade.trade_volume,
      ];
    } else if (tradeMinute === currentMinute) {
      // 같은 분 내의 거래를 계속해서 추가
      currentCandle[3] = Math.max(currentCandle[3], trade.trade_price);  // 최고 가격 업데이트
      currentCandle[2] = Math.min(currentCandle[2], trade.trade_price);  // 최저 가격 업데이트
      currentCandle[4] = trade.trade_price;  // 종가 업데이트
      currentCandle[5] += trade.trade_volume;  // 거래량 누적
    } else {
      // 새로운 분의 거래 시작
      oneMinuteCandles.push(convertToCandle(currentCandle));  // 이전 1분 봉 캔들 추가
      currentCandle = [
        tradeTimestamp,
        trade.trade_price,
        trade.trade_price,
        trade.trade_price,
        trade.trade_price,
        trade.trade_volume,
      ];
      currentMinute = tradeMinute;
    }
  }

  // 남은 데이터를 마지막 1분 봉 캔들로 추가
  if (currentCandle !== null) {
    oneMinuteCandles.push(convertToCandle(currentCandle));
  }

  return oneMinuteCandles;
}

// 사용 예시
const tradeData = [
  // 거래 데이터 예시 (timestamp, trade_price, ...)
  // ...
];

const oneMinuteCandles = create1MinuteCandles(tradeData);
console.log(oneMinuteCandles);
```

이 함수는 입력으로 거래 데이터를 받아 1분 봉 캔들로 변환하고 배열로 반환합니다. `tradeData` 배열에는 거래 데이터가 들어가야 합니다. 예제 코드에서는 각 거래 데이터가 `timestamp`, `trade_price`, 등의 속성을 가지고 있다고 가정하고 있습니다. 실제 데이터에 맞게 수정해 사용하십시오.
*****



> ## 4
전체 코드를 제공하겠습니다. 이 코드는 입력으로 거래 데이터를 받아 1분 봉 캔들로 변환하는 함수와 사용 예시를 포함하고 있습니다.

```javascript
function create1MinuteCandles(tradeData) {
  // 거래 데이터를 1분 봉 캔들로 변환하는 함수
  function convertToCandle(data) {
    const candle = {
      timestamp: data[0],          // 캔들의 타임스탬프
      opening_price: data[1],     // 시작 가격
      low_price: data[2],         // 최저 가격
      high_price: data[3],        // 최고 가격
      closing_price: data[4],     // 종가
      volume: data[5],            // 거래량
    };
    return candle;
  }

  // 1분 봉 캔들 배열 초기화
  const oneMinuteCandles = [];

  // 1분 봉 캔들을 만드는 로직
  let currentCandle = null;  // 현재 1분 봉 캔들
  let currentMinute = null;  // 현재 분

  for (const trade of tradeData) {
    const tradeTimestamp = trade.timestamp;  // 거래의 타임스탬프

    // 타임스탬프에서 분을 추출
    const tradeMinute = new Date(tradeTimestamp).getMinutes();

    if (currentMinute === null) {
      // 최초 거래 처리
      currentMinute = tradeMinute;
      currentCandle = [
        tradeTimestamp,
        trade.trade_price,
        trade.trade_price,
        trade.trade_price,
        trade.trade_price,
        trade.trade_volume,
      ];
    } else if (tradeMinute === currentMinute) {
      // 같은 분 내의 거래를 계속해서 추가
      currentCandle[3] = Math.max(currentCandle[3], trade.trade_price);  // 최고 가격 업데이트
      currentCandle[2] = Math.min(currentCandle[2], trade.trade_price);  // 최저 가격 업데이트
      currentCandle[4] = trade.trade_price;  // 종가 업데이트
      currentCandle[5] += trade.trade_volume;  // 거래량 누적
    } else {
      // 새로운 분의 거래 시작
      oneMinuteCandles.push(convertToCandle(currentCandle));  // 이전 1분 봉 캔들 추가
      currentCandle = [
        tradeTimestamp,
        trade.trade_price,
        trade.trade_price,
        trade.trade_price,
        trade.trade_price,
        trade.trade_volume,
      ];
      currentMinute = tradeMinute;
    }
  }

  // 남은 데이터를 마지막 1분 봉 캔들로 추가
  if (currentCandle !== null) {
    oneMinuteCandles.push(convertToCandle(currentCandle));
  }

  return oneMinuteCandles;
}

// 사용 예시
const tradeData = [
  // 거래 데이터 예시 (timestamp, trade_price, ...)
  // ...
];

const oneMinuteCandles = create1MinuteCandles(tradeData);
console.log(oneMinuteCandles);
```

위 코드는 1분 봉 캔들을 생성하는 함수와 사용 예시를 포함하고 있습니다. `tradeData` 배열에는 실제 거래 데이터를 입력해 사용하십시오.
*****



