# **<span style="font-size: 35px; font-style: italic;">FastAPI News Server</span>**

>FastAPI News Server  
2023년 12월 06일 09시 42분  
SaaS  
#article #code #keyword  
[Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
Here’s a brief explanation read more
## Description  

<body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  This FastAPI application provides a web server with endpoints for handling news-related requests. Let's break down the code:

1. **Import Statements:**
   - The code starts by importing necessary modules, including `json`, `os`, `uvicorn`, `FastAPI`, and related components.

2. **FastAPI App Setup:**
   - An instance of the FastAPI app is created: `app = FastAPI()`.

3. **CORS Middleware Configuration:**
   - Cross-Origin Resource Sharing (CORS) middleware is added to the app using the `CORSMiddleware` class to handle cross-origin requests.

4. **Pydantic Models:**
   - Pydantic models (`Item`, `CommnadClientRequest`, `CommnadFastApiReturn`, and `ItemResponse`) are defined to validate request and response payloads.

5. **GET Endpoint ("/ping"):**
   - There is a GET endpoint at `/ping` defined by `@app.get("/ping")`. It reads a JSON file (`configdict.json`), calls the `main` function with a search term, and returns a JSON response containing the result.

6. **Main Function (`main`):**
   - The `main` function, called by the `/ping` endpoint, uses the `NewsDownload` class to download news related to a given search term and number of pages. It returns a parsed JSON response.

7. **PUT Endpoints ("/news/{item_id}" and "/blog/{item_id}"):**
   - There are two PUT endpoints (`/news/{item_id}` and `/blog/{item_id}`) defined for generating news and blog content. They call the `main` function with parameters from the request payload and return a JSON response containing the result.

8. **Run the FastAPI App:**
   - Finally, the app is run using `uvicorn.run` with a specified host and port.

Please note that the code assumes the existence of a `NewsDownload` class and related functionalities, which are not provided in the shared code snippet. Also, the IP address and port for running the server are set to `"127.30.1.102"` and `23`, respectively. Ensure that these values are appropriate for your environment.


  </div></div></div>

  <body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  This TypeScript code defines a Vue 3 composition function (`getFromServerData`) for making an asynchronous request to a backend server using Axios. Here's a breakdown of the code:

1. **Import Statements:**
   - The code begins by importing necessary modules: `axios` for making HTTP requests, and `ref`, `onMounted` from Vue for handling reactive data.

```typescript
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { backendSchema } from './backendUtils';
```

2. **Reactive Variables:**
   - Two reactive variables (`responseData` and `parsingdata`) are declared using the `ref` function. These variables will be used to store the response data from the server.

```typescript
const responseData = ref('');
const parsingdata = ref('');
```

3. **Fetch Data Function:**
   - The `fetchData` function is defined as an asynchronous function using `async/await` syntax. It makes an HTTP GET request to the backend server using Axios.

```typescript
const fetchData = async () => {
  try {
    const response = await axios.get(backendSchema.getPingRouteURL());

    if (response) {
      responseData.value = response.data.API;
      parsingdata.value = responseData.value;
    } else {
      console.log('백엔드 호출 중 오류 발생: ' + String(error));
      responseData.value = '응답이 없습니다.';
    }
  } catch (error) {
    console.log('백엔드 호출 중 오류 발생: ' + String(error));
    if (error.message === 'Network Error') {
      responseData.value = error.config.url + '에서 백엔드가 실행 중인지 확인해주세요.';
    } else {
      responseData.value = '죄송합니다. 오류가 발생했습니다.';
    }
  }
};
```

4. **Lifecycle Hook (`onMounted`):**
   - The `onMounted` lifecycle hook is used to trigger the `fetchData` function when the component is mounted.

```typescript
onMounted(async () => {
  // fetchData()
});
```

5. **Return Statement:**
   - The composition function returns an object with the reactive variables and the `fetchData` function, making them accessible in the component using this composition.

```typescript
return {
  responseData,
  parsingdata,
  fetchData,
};
```

Overall, this code sets up a mechanism for fetching data from the backend server and handling the response using Vue 3's reactivity system. Note that the `fetchData` function is currently commented out in the `onMounted` hook, so it won't be automatically called when the component is mounted. Uncommenting this line would trigger the data fetch on component mount.


  </div></div></div>

  <div style="background-color: grey; height: 15px;"></div>

  