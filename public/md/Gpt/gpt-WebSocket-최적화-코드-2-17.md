# WebSocket 최적화 코드

## 2)
코드를 최적화하기 위해 몇 가지 개선할 수 있는 방법이 있습니다. 여기에 몇 가지 개선 사항을 제시하겠습니다:비동기 처리 최적화: handleWebSocketMessage 함수 내에서 비동기 작업을 수행하고 있습니다. 이를 최적화하기 위해 Promise.all을 사용하여 병렬로 처리할 수 있습니다. 이렇게 하면 성능이 향상됩니다.javascriptCopy codeconst handleWebSocketMessage = async (payload) => {
  const data = await new Response(payload.data).json();
  
  // 비동기 작업을 병렬로 처리
  await Promise.all([
    handleTickerData(data),
    handleBalanceData(data),
    handleWatchData(data),
    handleRankData(data)
  ]);
};

const handleTickerData = async (data) => {
  const tickerIndex = tickers.indexOf(data.code);
  if (data.code == 'KRW-ARK') {
    btcprice.trade_price = data.trade_price;
    const btcPriceData = { timestamp: data.trade_timestamp, price: btcprice.trade_price };
    const updatedCandles = updateCandle(preCandle_dict.value, candleOhl_dict.value, btcPriceData);
    console.log(updatedCandles);
  }
};

const handleBalanceData = async (data) => {
  const balanceIndex = balances.indexOf(data.code);
  if (balanceIndex != -1) {
    coins_hold.value[balanceIndex] = data;
  }
};

const handleWatchData = async (data) => {
  const watchIndex = watches.indexOf(data.code);
  if (watchIndex != -1) {
    coins_watch.value[watchIndex] = data;
  }
};

const handleRankData = async (data) => {
  const rankIndex = rankcoins.indexOf(data.code);
  if (rankIndex != -1) {
    coins_rank.value[rankIndex] = data;
  }
};
WebSocket 연결 관리: WebSocket 연결 관리를 최적화할 수 있습니다. onMounted 블록 내에서 WebSocket 연결을 열고 있으므로 페이지를 벗어날 때 연결을 닫는 코드를 추가해야 합니다.javascriptCopy codelet ws; // WebSocket 객체를 전역 변수로 선언

onMounted(async () => {
  try {
    ws = new WebSocket('wss://api.upbit.com/websocket/v1');
    ws.onopen = (e) => {
      ws.send(
        JSON.stringify([
          { ticket: "test" },
          { type: 'ticker', codes: tickers },
        ])
      );
    };
    ws.onmessage = handleWebSocketMessage;
  } catch (err) { }
});

// 페이지를 벗어날 때 WebSocket 연결을 닫음
onBeforeUnmount(() => {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.close();
  }
});
코드 최적화: 코드 내에서 반복되는 배열 검색을 최적화할 수 있습니다. Set 자료구조를 사용하여 배열 대신 집합으로 데이터를 관리하면 검색 성능이 향상됩니다.javascriptCopy code// 배열 대신 Set을 사용하여 데이터 관리
const tickerSet = new Set(tickers);
const balanceSet = new Set(balances);
const watchSet = new Set(watches);
const rankSet = new Set(rankcoins);

// 검색
const handleWebSocketMessage = async (payload) => {
  const data = await new Response(payload.data).json();
  
  await Promise.all([
    handleTickerData(data),
    handleBalanceData(data),
    handleWatchData(data),
    handleRankData(data)
  ]);
};

const handleTickerData = async (data) => {
  if (tickerSet.has(data.code)) {
    if (data.code == 'KRW-ARK') {
      btcprice.trade_price = data.trade_price;
      const btcPriceData = { timestamp: data.trade_timestamp, price: btcprice.trade_price };
      const updatedCandles = updateCandle(preCandle_dict.value, candleOhl_dict.value, btcPriceData);
      console.log(updatedCandles);
    }
  }
};

const handleBalanceData = async (data) => {
  if (balanceSet.has(data.code)) {
    coins_hold.value[balances.indexOf(data.code)] = data;
  }
};

const handleWatchData = async (data) => {
  if (watchSet.has(data.code)) {
    coins_watch.value[watches.indexOf(data.code)] = data;
  }
};

const handleRankData = async (data) => {
  if (rankSet.has(data.code)) {
    coins_rank.value[rankcoins.indexOf(data.code)] = data;
  }
};
이러한 최적화를 통해 코드의 성능과 가독성을 향상시킬 수 있습니다.저장 2