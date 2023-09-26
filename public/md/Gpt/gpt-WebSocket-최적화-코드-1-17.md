# WebSocket 최적화 코드

## 1)

const handleWebSocketMessage = async (payload) => {
  const data = await new Response(payload.data).json();

  const tickerIndex = tickers.indexOf(data.code);

  if (data.code == 'KRW-ARK') {
    btcprice.trade_price = data.trade_price;

    const btcPriceData = { timestamp: data.trade_timestamp, price: btcprice.trade_price };
    const updatedCandles = updateCandle(preCandle_dict.value, candleOhl_dict.value, btcPriceData);

    console.log(updatedCandles);
  }

  const balanceIndex = balances.indexOf(data.code);
  if (balanceIndex != -1) {
    coins_hold.value[balanceIndex] = data;
  }

  const watchIndex = watches.indexOf(data.code);
  if (watchIndex != -1) {
    coins_watch.value[watchIndex] = data;
  }

  const rankIndex = rankcoins.indexOf(data.code);
  if (rankIndex != -1) {
    coins_rank.value[rankIndex] = data;
  }
};

onMounted(async () => {
  try {
    const ws = new WebSocket('wss://api.upbit.com/websocket/v1')
    ws.onopen = (e) => {
      ws.send(
        JSON.stringify([
          { ticket: "test" },
          { type: 'ticker', codes: tickers },
        ])
      )
    }
    ws.onmessage = handleWebSocketMessage;
  } catch (err) { }
})

const btcprice = ref({
  signed_change_rate: 0,
});
</script>
이부분을 최적화 해줘저장 1