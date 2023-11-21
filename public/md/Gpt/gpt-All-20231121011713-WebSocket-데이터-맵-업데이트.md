# **<span style="font-size: 35px; font-style: italic;">WebSocket 데이터 맵 업데이트</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-32.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 1</div></div>
Sure, if you want to store incoming data in a map, you can make a modification to the `handleWebSocketMessageIn` method. Here's an updated version of your `WebSocketService` class:

```typescript
// WebSocketService.ts
import { ref } from 'vue';

import tickers_raw from "@/assets/coinInfo/tickers.json";

class WebSocketService {
  ws: WebSocket | null = null;
  updateFunctions: ((data: any) => void)[] = [];
  dataMap: Map<string, any> = new Map(); // Add a Map to store incoming data

  constructor(updateFunction?: (data: any) => void) {
    if (updateFunction) {
      this.updateFunctions.push(updateFunction);
    }
  }

  registerUpdateFunction(updateFunction: (data: any) => void) {
    this.updateFunctions.push(updateFunction);
  }

  handleWebSocketMessageIn(payload: MessageEvent) {
    console.log('WebSocket message received:', payload.data);

    try {
      payload.data.text().then((text: any) => {
        const data = JSON.parse(text);
        this.updateFunctions.forEach((fn) => fn(data));

        // Store data in the map using a unique key (you can modify this key based on your data)
        this.dataMap.set(data.someUniqueKey, data);
      });
    } catch (error) {
      console.error('Error parsing WebSocket message:', error);
    }
  }

  setupWebSocket() {
    try {
      this.ws = new WebSocket('wss://api.upbit.com/websocket/v1');
      this.ws.onopen = () => {
        this.ws!.send(
          JSON.stringify([
            { ticket: 'test' },
            { type: 'ticker', codes: tickers_raw },
          ])
        );
      };
      this.ws.onclose = (e) => {
        console.error('WebSocket closed:', e);
      };

      this.ws.onmessage = (event) => this.handleWebSocketMessageIn(event);
    } catch (err) {
      console.error(err);
    }
  }
}

export const sharedWebSocketService = new WebSocketService();
```

This modification adds a `dataMap` property to the `WebSocketService` class, and in the `handleWebSocketMessageIn` method, it stores the incoming data in the map using a unique key. Adjust the key based on your data structure and requirements.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-36.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
The error you're encountering, "Failed to execute 'send' on 'WebSocket': Still in CONNECTING state," indicates that you're trying to send a message on the WebSocket before it has fully established a connection. WebSocket connections have a state machine, and you can only send messages once the connection is open.

To fix this issue, you should make sure that you're sending the initial message only when the WebSocket is in the open state. You can modify your `setupWebSocket` method to handle this:

```typescript
// WebSocketService.ts

// ... (your existing code)

class WebSocketService {
  // ... (your existing code)

  setupWebSocket() {
    try {
      this.ws = new WebSocket('wss://api.upbit.com/websocket/v1');
      
      this.ws.onopen = () => {
        // Move the sending of the initial message inside the onopen callback
        this.ws!.send(
          JSON.stringify([
            { ticket: 'test' },
            { type: 'ticker', codes: tickers_raw },
          ])
        );
      };

      this.ws.onclose = (e) => {
        console.error('WebSocket closed:', e);
      };

      this.ws.onmessage = (event) => this.handleWebSocketMessageIn(event);
    } catch (err) {
      console.error(err);
    }
  }
}

export const sharedWebSocketService = new WebSocketService();
```

This modification ensures that the initial message is only sent when the WebSocket connection is open. If you still face issues, please check for other parts of your code that might be attempting to send messages before the connection is fully established.



<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-34.png)  
- WebSocket 데이터 맵 업데이트  
- 20231121011713  
- gpt  
- #gpt #code #keyword  
- Here's an updated version of your `WebSocketService` class:

```typescript
// WebSocketService.ts
import { ref } from 'vue';

import tickers_raw from "@/assets/coinInfo/tickers.json";

class WebSocketService {
  ws: WebSocket | null = null;
  updateFunctions: ((data: any) => void)[] = [];
  dataMap: Map<string, any> = new Map(); // Add a Map to store incoming data

  constructor(updateFunction?: (data: any) => void) {
    if (updateFunction) {
      this.updateFunctions.push(updateFunction);
    }
  }

  registerUpdateFunction(updateFunction: (data: any) => void) {
    this.updateFunctions.push(updateFunction);
  }

  handleWebSocketMessageIn(payload: MessageEvent) {
    console.log('WebSocket message received:', payload.data);

    try {
      payload.data.text().then((text: any) => {
        const data = JSON.parse(text);
        this.updateFunctions.forEach((fn) => fn(data));

        // Store data in the map using a unique key (you can modify this key based on your data)
        this.dataMap.set(data.someUniqueKey, data);
      });
    } catch (error) {
      console.error('Error parsing WebSocket message:', error);
    }
  }

  setupWebSocket() {
    try {
      this.ws = new WebSocket('wss://api.upbit.com/websocket/v1');
      this.ws.onopen = () => {
        this.ws!.send(
          JSON.stringify([
            { ticket: 'test' },
            { type: 'ticker', codes: tickers_raw },
          ])
        );
      };
      this.ws.onclose = (e) => {
        console.error('WebSocket closed:', e);
      };

      this.ws.onmessage = (event) => this.handleWebSocketMessageIn(event);
    } catch (err) {
      console.error(err);
    }
  }
}

export const sharedWebSocketService = new WebSocketService();
```

This modification adds a `dataMap` property to the `WebSocketService` class, and in the `handleWebSocketMessageIn` method, it stores the incoming data in the map using a unique key,Adjust the key based on your data structure and requirements.





<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-36.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 2</div></div>
The error you're encountering, "Failed to execute 'send' on 'WebSocket': Still in CONNECTING state," indicates that you're trying to send a message on the WebSocket before it has fully established a connection  
</div> 
