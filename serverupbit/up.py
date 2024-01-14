
from threading import Thread
import json
import time
from websocket import WebSocketApp


class UpbitReal:
    def __init__(self, request, callback=print):
        self.request = request
        self.callback = callback
        self.msg = None
        self.ws = WebSocketApp(
            url="wss://api.upbit.com/websocket/v1",
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open,
        )
        self.running = False

    def on_message(self, _, msg):
        self.msg = json.loads(msg.decode('utf-8'))
        self.callback(self.msg)

    def on_error(self, _, msg):
        self.callback(msg)

    def on_close(self, _):
        self.callback("closed")
        self.running = False

    def on_open(self, _):
        th = Thread(target=self.activate, daemon=True)
        th.start()

    def activate(self):
        try:
            self.ws.send(self.request)
            while self.running:
                time.sleep(1)
        finally:
            self.ws.close()

    def start(self):
        self.running = True
        self.ws.run_forever()

if __name__ == "__main__":
    request1 = '[{"ticket":"test"},{"type":"ticker","codes":["KRW-BTC"]}]'
    real = UpbitReal(request=request1)
    real.start()
