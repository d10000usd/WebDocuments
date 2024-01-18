# **<span style="font-size: 35px; font-style: italic;">Type Annotations, Property Declaration</span>**

>Type Annotations, Property Declaration  
2024년 01월 18일 11시 06분  
SaaS  
#article #code #keyword  
[Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
Here’s a brief explanation read more
## Description  

<body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  It looks like there are a few issues in your `DataFetcher.ts` file. Let's address each of them:

1. **Implicit 'any' Type for 'urlkey':**
   - Error: `Parameter 'urlkey' implicitly has an 'any' type.`
   - Solution: Add a type annotation for the `urlkey` parameter.

```typescript
constructor(urlkey: string) {
  // ...
}
```

2. **'globalurl' Property does not exist on type 'ApiUrl':**
   - Errors: 
     - `Property 'globalurl' does not exist on type 'ApiUrl'.` (both instances)
   - Solution: Declare the `globalurl` property within the `ApiUrl` class.

```typescript
export class ApiUrl {
  globalurl: Record<string, string>; // Declare globalurl property

  constructor(urlkey: string) {
    this.globalurl = {
      "historyhtml": 'http://172.30.1.10:1338/api/1/search.naver.historyhtml?sm=1&pages=2&search=삼성전자+ETF&where=extention',
      "history": 'http://172.30.1.10:1338/api/1/search.naver.history?sm=1&pages=2&search=삼성전자+ETF&where=extention'
    };
    // ...
  }
}
```

3. **Cannot Find Name 'apiData':**
   - Error: `Cannot find name 'apiData'.`
   - Solution: Declare `apiData` using `ref` at the beginning of your class.

```typescript
export class ApiUrl {
  globalurl: Record<string, string>;
  apiData = ref<string | null>(null); // Declare apiData

  constructor(urlkey: string) {
    // ...
  }
}
```

Make sure to include these changes in your `DataFetcher.ts` file. If you have any further questions or encounter issues, feel free to ask.


  </div></div></div>

  <body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  Certainly! Here's the modified `DataFetcher.ts` file with the suggested changes:

```typescript
// DataFetcher.ts

import { ref } from 'vue';

export class ApiUrl {
  globalurl: Record<string, string>;
  apiData = ref<string | null>(null);

  constructor(urlkey: string) {
    this.globalurl = {
      "historyhtml": 'http://172.30.1.10:1338/api/1/search.naver.historyhtml?sm=1&pages=2&search=삼성전자+ETF&where=extention',
      "history": 'http://172.30.1.10:1338/api/1/search.naver.history?sm=1&pages=2&search=삼성전자+ETF&where=extention'
    };

    const fetchData = async () => {
      try {
          const response = await fetch(this.globalurl.historyhtml);
          const data = await response.text(); // Use text() for HTML content
          this.apiData.value = data;
      } catch (error) {
          console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }
}
```

These changes should resolve the TypeScript errors in your code. If you have any more questions or if there's anything else I can help you with, feel free to ask!


  </div></div></div>

  <body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  To use the modified `DataFetcher.ts` file in a Vue 3 script, you can follow these steps:

1. **Import the `ApiUrl` class:**
   Import the `ApiUrl` class in your Vue component where you intend to use it.

   ```javascript
   import { ApiUrl } from 'path-to-your/DataFetcher';
   ```

   Replace `'path-to-your/DataFetcher'` with the actual path to your `DataFetcher.ts` file.

2. **Instantiate the `ApiUrl` class:**
   Create an instance of the `ApiUrl` class in your component.

   ```javascript
   export default {
     mounted() {
       const apiUrlInstance = new ApiUrl('your-url-key');
     },
   };
   ```

   Replace `'your-url-key'` with the desired value for the `urlkey` parameter.

3. **Accessing Data:**
   You can access the `apiData` property to retrieve the fetched data.

   ```javascript
   export default {
     mounted() {
       const apiUrlInstance = new ApiUrl('your-url-key');
       const fetchedData = apiUrlInstance.apiData.value;
       console.log('Fetched Data:', fetchedData);
     },
   };
   ```

Make sure to replace the placeholder values with your actual values. This approach assumes that you want to initiate the data fetching process when the component is mounted. Adjust the usage based on your specific requirements.

Remember to handle the asynchronous nature of fetching data in Vue components, possibly using lifecycle hooks or other mechanisms based on your application's needs.


  </div></div></div>

  <body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  Certainly! If you want to use the `script setup` syntax in Vue 3 and return the `apiData`, you can modify the `DataFetcher.ts` file and the component file as follows:

**DataFetcher.ts:**

```typescript
// DataFetcher.ts

import { ref } from 'vue';

export class ApiUrl {
  globalurl: Record<string, string>;
  apiData = ref<string | null>(null);

  constructor(urlkey: string) {
    this.globalurl = {
      "historyhtml": 'http://172.30.1.10:1338/api/1/search.naver.historyhtml?sm=1&pages=2&search=삼성전자+ETF&where=extention',
      "history": 'http://172.30.1.10:1338/api/1/search.naver.history?sm=1&pages=2&search=삼성전자+ETF&where=extention'
    };

    const fetchData = async () => {
      try {
        const response = await fetch(this.globalurl.historyhtml);
        const data = await response.text();
        this.apiData.value = data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }
}
```

**YourVueComponent.vue:**

```vue
<script setup>
import { ApiUrl } from 'path-to-your/DataFetcher';

const apiUrlInstance = new ApiUrl('your-url-key');
const apiData = apiUrlInstance.apiData;

// If you want to return apiData from the setup function
// return { apiData };
</script>

<template>
  <div>
    <!-- Access and use apiData in your template -->
    <p>{{ apiData }}</p>
  </div>
</template>
```

Make sure to replace `'path-to-your/DataFetcher'` with the actual path to your `DataFetcher.ts` file and adjust `'your-url-key'` with the desired value for the `urlkey` parameter.

In this example, the `apiData` is available directly in the template for usage. If you want to return it from the setup function, uncomment the `return { apiData };` line in the setup block.


  </div></div></div>

  <div style="background-color: grey; height: 15px;"></div>

  