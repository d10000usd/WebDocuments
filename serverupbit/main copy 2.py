from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

async def send_numbers(websocket: WebSocket):
    # for number in range(1, 1000001):
    await websocket.send_text(str(number))
    await asyncio.sleep(1)  # Wait for 1 second

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await send_numbers(websocket)