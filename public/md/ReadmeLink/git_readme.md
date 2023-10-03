
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
 -  `1<div :class="classes" style="max-width: 1500px;">3`
 -  `1<div class="app-container main-container " style="max-width: 1500px;">`
 > 가장중요한건 마진 넓이 , 전체크기 넓이, 높이가 중요
 > 크롬에서 크기조절이 자동으로 되므로 확인 필요
    -  모든 파일에서 전역 적용이 가능 하므로 scope 를 꼭 사용
    -  
    ```js
    <style scoped>

    </style>
    ```
    ```js
    <style>

   
    </style>
    ```