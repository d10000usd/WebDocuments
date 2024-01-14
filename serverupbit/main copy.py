from fastapi import FastAPI, WebSocket
import asyncio
import websockets

app = FastAPI()

async def send_btc_values(websocket: WebSocket):
    uri = "wss://api.upbit.com/websocket/v1"

    try:
        async with websockets.connect(uri) as upbit_websocket:
            subscribe_message = '{"type":"ticker","codes":["KRW-BTC"]}'
            await upbit_websocket.send(subscribe_message)

            while True:
                btc_value = await upbit_websocket.recv()
                await websocket.send_text(btc_value)
                await asyncio.sleep(1)
    except websockets.exceptions.ConnectionClosedError:
        # Handle the connection closed error
        pass

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await send_btc_values(websocket)
