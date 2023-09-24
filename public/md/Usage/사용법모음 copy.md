
# vue3
## vite

 - npm init vite@latest
 - vue create markdown-sidebar-client

  ```
  Virtual script "/Users/hg/DEV/Web/markdown-sidebar-client/src/components/HelloWorld.vue.js"  
  not found, may missing <script lang="ts"> / "allowJs": true / jsconfig.json.v
  ```
  ``` json
  tsconfig.json 안에다 추가     "allowJs": true,
    "compilerOptions": {
      "target": "esnext",
      "module": "esnext",
      "strict": true,
      "jsx": "preserve",
      "moduleResolution": "node",
      "skipLibCheck": true,
      "esModuleInterop": true,
      "allowSyntheticDefaultImports": true,
      "forceConsistentCasingInFileNames": true,
      "useDefineForClassFields": true,
      "sourceMap": true,
      "allowJs": true,
      "baseUrl": ".",
  ```

## log
### vue3 프로재트 생성
### package.json
  ``` json
    로컬호스트는 포트포워딩 안되므로 로컬에서 고정 아이피로 만들고 실행
    아이피 설정
    "serve" : "vite --host 172.30.1.10 --port 8088" 

    "scripts": {
      "dev": "vite",
      "serve" : "vite --host 172.30.1.10 --port 8088",
      "build": "run-p type-check build-only",
      "preview": "vite preview",
      "build-only": "vite build",
      "type-check": "vue-tsc --noEmit -p tsconfig.app.json --composite false",
      "lint": "eslint . --ext .vue,.js,.jsx,.cjs,.mjs,.ts,.tsx,.cts,.mts --fix --ignore-path .gitignore"
    },
  ```
  - 바이트로 프로젝트 생성
    - Customize with create-vue  를 선택해야 
    - Route, typescript, lint, side effects program could be select
```js
  ❯  yarn create vite
  yarn create v1.22.19
  [1/4] 🔍  Resolving packages...
  [2/4] 🚚  Fetching packages...
  [3/4] 🔗  Linking dependencies...
  [4/4] 🔨  Building fresh packages...
  success Installed "create-vite@4.4.0" with binaries:
        - create-vite
        - cva
  ✔ Project name: … hg-mobile
  ✔ Select a framework: › Vue
  ✔ Select a variant: › Customize with create-vue ↗
  yarn create v1.22.19
  [1/4] 🔍  Resolving packages...
  [2/4] 🚚  Fetching packages...
  [3/4] 🔗  Linking dependencies...
  [4/4] 🔨  Building fresh packages...

  success Installed "create-vue@3.7.1" with binaries:
        - create-vue
  [##############] 14/14
  Vue.js - The Progressive JavaScript Framework

  ✔ Add TypeScript? … No / Yes
  ✔ Add JSX Support? … No / Yes
  ✔ Add Vue Router for Single Page Application development? … No / Yes
  ✔ Add Pinia for state management? … No / Yes
  ✔ Add Vitest for Unit Testing? … No / Yes
  ✔ Add an End-to-End Testing Solution? › No
  ✔ Add ESLint for code quality? … No / Yes
  ✔ Add Prettier for code formatting? … No / Yes

  Scaffolding project in /Users/hg/DEV/Web/hg-mobile...

  Done. Now run:

    cd hg-mobile
    yarn
    yarn dev
```


## 트러블슈팅 설정

- import HomeView from '../views/HomeView.vue'
- 최초 프로젝트 생성후 경로문제 가 있을 경우 2개 파일을 생성해서 넣어 주면 됨
- Typescript, ES, module types 을 설정 해서 사용가능
- not found 가 뜰경우
  - Typescript 설정을 하고 Els lint 일때
  - Scr 폴더 아래에 
  >  env.d.ts
  ``` typescript
  /// <reference types="vite/client" />

  declare module '*.vue' {
    import type { DefineComponent } from 'vue'
    // eslint-disable-next-line @typescript-eslint/no-explicit-any, @typescript-eslint/ban-types
    const component: DefineComponent<{}, {}, any>
    export default component
  }

  ```
  >  shims-vue.ts
  ``` typescript
  declare module '*.vue';
  ```



  ## yarn build or npm build
  > 빌드 할때 오류가 날 수 있
  는데 아래처럼 각각 파일  
  comilerOptions 에 넣어 준다
  ```json
    "compilerOptions": {
      "composite": true,
      "module": "ESNext",
      "types": ["node"],
      "allowJs": true
    }
  ```
   -  src 관련 임포트 일 경우
   -  tsconfig.app.json 
   -  tsconfig.node.json 
      -  "allowJs": true



# CSS
## App.vue

 -  여기에 일단 다 때려넣고, 나중에 분리
 -  <style> </style> 은 모든 프로젝트내에서 적용가능
 -  `<div :class="classes" style="max-width: 1500px;">`
 -  `<div class="app-container main-container " style="max-width: 1500px;">`
 > 가장중요한건 마진 넓이 , 전체크기 넓이, 높이가 중요
 > 크롬에서 크기조절이 자동으로 되므로 확인 필요
  -  모든 파일에서 전역 적용이 가능 하므로 scope 를 꼭 사용
  
  ```css
    <style scoped>
    /* Add any custom styles here */
    .app-container {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
      background-color: #f5f5f5; /* Bootstrap default background color */
    }

    .main-container {
      display: flex;
      flex-grow: 1;
      max-width: 1300px;
      margin: 0 auto;
      padding: 20px; /* Add some padding to the main container */
    }

    .router-view-container {
      flex-grow: 1;
      overflow-y: auto;
      background-color: #ffffff; /* White background for the router view area */
      border: 1px solid #e0e0e0; /* Bootstrap default border color */
      border-radius: 10px; /* Add border radius to create rounded corners */
    }
    </style>
  ```

# 마크다운
## 사용법
- MarkdownView.vue 안에서 경로를 주고   
  ` <MarkdownNaviComp :message="mdPath"/>` 프로프로 주소를 넘김  


  - 프로프 넘기는 방법은 1가지
    -  ref 로 선언은 한다음, 보낼 곳에 ref 를 넘김
       1. `const isSidebarOpen = ref(false);`
       2. `<router-view :is-sidebar-open="isSidebarOpen" />`
    -  받을때는 2가지   
       1. 그냥 ref로 보내변 받는 쪽에서 받아짐
       ```typescript
        const isSidebarOpen = ref(true);
        const classes = computed(() => [
          isSidebarOpen.value ? 'xl:pl-4 flex mt-11' : 'md:ml-23 mt-3',
          'pt-12',
          'px-1',
          'pb-5',
          // 'bootstrap-class-name', // Bootstrap 클래스 이름을 추가해야 합니다.
        ]);
        ```
        2. 받는쪽에서 defineProps 를 하는데 잘 안쓰는듯
        ```typescript
        // 부모컴퍼넌트에서 데이터를 받을때 
        import { defineProps } from 'vue';

        const props = defineProps({
          message: String
        });
        const selectedMarkdownPath = ref(props.message);


        ```
              