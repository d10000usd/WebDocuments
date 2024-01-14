from fastapi import FastAPI, WebSocket

app = FastAPI()

async def send_numbers(websocket: WebSocket):
    for number in range(1, 11111111111111):
        try:
            await websocket.send_text(str(number))
            # 여기서 다른 작업을 수행할 수도 있습니다.
        except Exception as e:
            # WebSocket 연결이 끊어진 경우에 대한 예외 처리
            print(f"WebSocket connection closed: {e}")
            break

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await send_numbers(websocket)