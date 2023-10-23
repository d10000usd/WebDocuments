# **<span style="font-size: 35px; font-style: italic;">Vue Component Integration</span>**


<style>
.body-full {
    overflow-x: hidden;
    margin: .21rem;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Apple SD Gothic Neo", Arial, sans-serif;
    font-weight: 500;
    position: relative;
    word-break: break-all;
    -webkit-text-size-adjust: none;
    background-color: #eaeef3;
    color: #474787;
    font-size: 16px;
    line-height: 19px;
    border-color: white;
    }
</style>
<div class="body-full">

```markdown
# {제목}: Vue.js 템플릿에서 변수를 전달하는 방법

## {메타 설명}: Vue.js 템플릿에서 변수를 전달하는 방법과 그에 따른 코드 조정 방법을 설명합니다.

1. 아래 코드에서 `giturl` 변수를 전달하는 부분에서 문제가 발생하고 있습니다.
   
```vue
<script setup>
const giturl = ref({
    receivedRouteName: "받는 데이터 유형 정의"
})
</script>
```

2. 코드 조정을 위해 다음과 같이 수정할 수 있습니다.

```vue
<script setup>
import { ref } from 'vue'
import { defineProps } from 'vue'
import GitGetOnlineUseUrl from "../components/body/GitGetOnlineUseUrl.vue"

const props = defineProps({
  message: Object,
});

const selectNo = ref(38)
const st = 'https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/md/Gpt/gpt-All-Divide-HTML-into-Columns-2023.md'
const giturl = ref({ receivedRouteName: "데이터 수신 유형 정의" })

</script>
```

3. 또한, 아래 부분에서 데이터를 받는 방식을 수정할 수 있습니다.

```vue
<template>
    <p>받은 라우트 이름: - {{ props }}</p>
    <GitGetOnlineUseUrl :message="'랜덤 선택에 따른 넘버'" :gitnum="Number(selectNo)" :burl='st' />
</template>
```

위의 수정 사항들을 참고하여 코드를 조정해보시기 바랍니다.
```


</div>

<div class="body-full">

이해했습니다. 코드에서 `giturl` 변수는 전달하고 받는 변수로 사용되는 것으로 이해했습니다. 이 경우, `giturl` 변수는 Vue 컴포넌트에서 정상적으로 변수를 전달하고 받는 목적을 수행하고 있습니다. 코드가 `RouterLink` 컴포넌트를 사용하여 `giturl` 변수를 전달하고 받는 부분은 올바르게 작동할 것입니다.

따라서, 변수를 전달하고 받는 목적을 수행하는데 문제가 없는 것으로 보입니다. 단, 코드의 다른 부분에서 `giturl` 변수를 사용하는 방법과 목적이 명확하게 정의되어야 하며, 코드의 전체 목적과 흐름을 이해하기 쉽도록 주석이나 설명을 추가하는 것이 도움이 될 수 있습니다.


</div>

<div class="body-full">

당신이 제공한 코드에서 `giturl` 변수를 받는 부분은 코드의 다른 부분에 위치할 것입니다. 보통 Vue 컴포넌트에서 다른 컴포넌트로 데이터를 전달하는 방법은 프로퍼티를 사용하는 것입니다. 따라서 다음과 같이 `giturl` 변수를 받는 부분이 일반적으로 있을 것입니다.

```javascript
// Body_view 컴포넌트 내부에서 giturl 변수를 받는 부분
props: {
  message: {
    type: Object, // giturl이 객체 타입인지 확인
    required: true // 필수 프로퍼티인지 확인
  }
}
```

위의 코드는 `Body_view` 컴포넌트 내부에서 `giturl` 변수를 받는 방법을 보여줍니다. `message`라는 프로퍼티를 정의하고, 해당 프로퍼티는 객체 형태의 데이터를 기대하고 필수 프로퍼티로 설정되어 있습니다. 이 부분은 `giturl` 변수가 `Body_view` 컴포넌트로 전달되는 방식을 보여주고 있습니다. 이 코드를 적절한 위치에 추가하여 `giturl` 변수를 올바르게 받을 수 있습니다.


</div>

<div class="body-full">

당신이 요청한 코드는 두 개의 Vue 컴포넌트 간의 데이터 전달을 보여주는 것입니다. 이를 위해서 Vue Router와 프로퍼티를 사용합니다. 여기에 전체 코드를 제공합니다.

```vue
<template>
  <div class="card custom-card">
    <div class="card-body">
      <blockquote class="blockquote mb-0">
        <!-- RouterLink 컴포넌트를 사용하여 giturl 변수를 Body_view 컴포넌트로 전달 -->
        <RouterLink class="navbar-brand" to="/Body_view" :message="giturl" :key="giturl">Body_view</RouterLink>
        <p>A well-known quote, contained in a blockquote element.</p>
        <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite>
        </footer>
      </blockquote>
    </div>
    <img
      src="https://i.ebayimg.com/images/g/SJcAAOSwtkBgucpI/s-l1600.jpg"
      class="card-img-top" alt="Image">
  </div>
</template>
<script setup>
import { RouterLink } from 'vue-router'

// giturl 변수를 생성하고 초기화
const giturl = ref({
    receivedRouteName: "Define the type of data being received"
})
</script>
<style scoped>
</style>

<!-- Body_view 컴포넌트 -->
<script setup>
// Body_view 컴포넌트 내에서 giturl 변수를 받음
props: {
  message: {
    type: Object,
    required: true
  }
}
</script>
```

이 코드에서, `<RouterLink>` 컴포넌트를 사용하여 `giturl` 변수를 `Body_view` 컴포넌트로 전달하고 있습니다. 그리고 `Body_view` 컴포넌트는 `message` 프로퍼티를 통해 이 데이터를 받아옵니다.

이 코드는 Vue 컴포넌트 간의 데이터 전달을 보여주며, `giturl` 변수는 Vue Router를 통해 다른 컴포넌트로 전달되고 `Body_view` 컴포넌트에서 받아집니다.


</div>

<div class="body-full">

당신이 제공한 코드를 확인하였습니다. 여기서 `receivedRouteName`이 제대로 전달되어야 하는데, 현재 `props` 선언에서는 `message`만 정의되어 있습니다. 따라서 `receivedRouteName`을 사용하려면 `props`에 해당 프로퍼티를 추가해야 합니다.

다음은 수정된 코드입니다.

```vue
<script setup>
import { ref } from 'vue'

import { defineProps } from 'vue'
import GitGetOnlineUseUrl from "../components/body/GitGetOnlineUseUrl.vue"
  
// Define props to receive data from RouterLink
const props = {
  message: {
    type: Object, // giturl이 객체 타입인지 확인
    required: true // 필수 프로퍼티인지 확인
  },
  receivedRouteName: {
    type: String, // receivedRouteName이 문자열 타입인지 확인
    required: true // 필수 프로퍼티인지 확인
  }
}

const selectNo = ref(38)
const st = 'https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/md/Gpt/gpt-All-Divide-HTML-into-Columns-2023.md'

</script>

<template>
    <p>Received route name: {{ receivedRouteName }}</p> <!-- receivedRouteName 출력 -->
    <GitGetOnlineUseUrl :message="'넘버로 랜덤 선택'" :gitnum="Number(selectNo)" :burl='st' />
</template>
<style scoped>

</style>
```

위의 코드에서 `props`에 `receivedRouteName`이 추가되었습니다. 이제 `receivedRouteName`을 템플릿에서 사용하여 받아올 수 있어야 합니다. 이를 통해 `receivedRouteName`을 정상적으로 출력할 수 있을 것입니다.


</div>

<div class="body-full">

주어진 오류를 살펴본 결과, 코드의 문제는 `Body_view.vue`의 17번째 줄에서 발생하는 것으로 보입니다. 해당 줄의 코드에서 `string`이 정의되지 않았다는 오류가 발생했습니다.

해당 줄을 살펴보니 `receivedRouteName`을 출력하는 부분에서 문제가 발생했습니다. 수정된 코드에서는 `receivedRouteName`이 `props`에 정의되었으나, 템플릿에서는 이를 직접 사용하려고 했을 때 `receivedRouteName`이 정의되지 않았다는 오류가 발생했습니다.

이러한 오류를 해결하기 위해서는 `props`로 받은 데이터를 사용할 때는 `props` 객체를 통해 사용해야 합니다. 따라서 코드를 다음과 같이 수정하여 문제를 해결할 수 있습니다.

```vue
<script setup>
import { ref } from 'vue'

import { defineProps } from 'vue'
import GitGetOnlineUseUrl from "../components/body/GitGetOnlineUseUrl.vue"
  
// Define props to receive data from RouterLink
const props = defineProps({
  message: {
    type: Object, // giturl이 객체 타입인지 확인
    required: true // 필수 프로퍼티인지 확인
  },
  receivedRouteName: {
    type: String, // receivedRouteName이 문자열 타입인지 확인
    required: true // 필수 프로퍼티인지 확인
  }
})

const selectNo = ref(38)
const st = 'https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/md/Gpt/gpt-All-Divide-HTML-into-Columns-2023.md'

</script>

<template>
    <p>Received route name: {{ props.receivedRouteName }}</p> <!-- receivedRouteName을 props 객체를 통해 사용 -->
    <GitGetOnlineUseUrl :message="'넘버로 랜덤 선택'" :gitnum="Number(selectNo)" :burl='st' />
</template>
<style scoped>

</style>
```

위의 수정된 코드에서는 `props` 객체를 통해 `receivedRouteName`을 사용하도록 변경하였습니다. 이제 오류가 해결되었을 것입니다.


</div>

<div class="body-full">

만약 `receivedRouteName`이 라우터를 통해 전달되는 값이라면, 라우터 설정도 적절히 수정되어야 합니다. 일반적으로 Vue Router를 사용할 때, 라우터 설정에서 해당 값을 전달하고 받는 방법을 명시해야 합니다. 따라서 라우터 설정을 살펴보고 필요한 경우 해당 값을 적절히 전달해야 합니다.

라우터 설정을 확인하고 `receivedRouteName`을 적절히 전달하는 방법은 다음과 같습니다.

```javascript
// 라우터 설정 예시
import { createRouter, createWebHistory } from 'vue-router';
import BodyView from './path/to/Body_view.vue';

const routes = [
  {
    path: '/Body_view',
    name: 'BodyView',
    component: BodyView,
    props: (route) => ({ receivedRouteName: route.query.receivedRouteName }), // 라우터를 통해 receivedRouteName 전달
  },
  // 다른 라우터 설정
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
```

위의 코드에서 `createRouter` 함수를 사용하여 라우터를 생성하고, `routes` 배열에 각 경로와 컴포넌트를 설정합니다. 여기서 `props` 속성을 사용하여 `receivedRouteName`을 전달하고 있습니다. 이렇게 하면 `Body_view.vue` 컴포넌트로 `receivedRouteName`이 전달될 것입니다.

따라서, 만약 라우터 설정에서 해당 값을 전달하고 있다면, 위와 같이 수정된 코드를 확인하여 `receivedRouteName`이 적절히 전달되고 있는지 확인할 수 있습니다.


</div>

<div class="body-full">

주어진 코드에서 라우터 설정을 수정하여 `receivedRouteName`을 적절히 전달하는 방법은 다음과 같습니다.

```javascript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/PluginWebsocket_tabView.vue')
    },
    // MainView
    {
      path: '/MainView',
      name: 'MainView',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/MainView.vue')
    },
    {
      path: '/Body_view',
      name: 'Body_view',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Body_view.vue'),
      props: (route) => ({ receivedRouteName: route.query.receivedRouteName }), // 라우터를 통해 receivedRouteName 전달
    }
  ]
})

export default router
```

위의 코드에서 `/Body_view` 경로에 대한 설정 부분에 `props`를 추가하여 `receivedRouteName`을 전달하도록 설정했습니다. 이제 `Body_view` 컴포넌트로 `receivedRouteName`이 전달되어야 합니다. 이를 통해 `Body_view.vue` 컴포넌트에서 `receivedRouteName`을 정상적으로 사용할 수 있을 것입니다.


</div>

<div class="body-full">

주어진 코드를 보면 `props`를 올바르게 정의하고, `receivedRouteName`을 템플릿에서 사용하도록 수정하였습니다. 하지만 라우터 설정 부분이 아직 수정되지 않았습니다. 따라서 라우터 설정에 대한 수정이 필요합니다.

아래는 라우터 설정을 수정한 코드입니다.

```javascript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/PluginWebsocket_tabView.vue')
    },
    // MainView
    {
      path: '/MainView',
      name: 'MainView',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/MainView.vue')
    },
    {
      path: '/Body_view',
      name: 'Body_view',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Body_view.vue'),
      props: route => ({
        receivedRouteName: route.query.receivedRouteName
      })
    }
  ]
})

export default router
```

위의 코드는 `Body_view` 경로에 대한 라우터 설정을 수정하여 `receivedRouteName`을 전달하도록 설정한 것입니다. 이제 `receivedRouteName`은 `Body_view` 컴포넌트로 정상적으로 전달될 것입니다.


</div>

<div class="body-full">

주어진 코드를 확인하였고, 이미 코드는 `props`를 올바르게 정의하고 `receivedRouteName`을 템플릿에서 사용하도록 되어 있습니다. 따라서 코드에는 추가적인 수정이 필요하지 않습니다. 다만, 라우터 설정 부분을 수정해야 `receivedRouteName`이 적절히 전달될 수 있습니다.

라우터 설정에서 `receivedRouteName`을 전달하는 부분을 수정하기 위해서 다음과 같이 코드를 업데이트할 수 있습니다.

```javascript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/PluginWebsocket_tabView.vue')
    },
    // MainView
    {
      path: '/MainView',
      name: 'MainView',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/MainView.vue')
    },
    {
      path: '/Body_view',
      name: 'Body_view',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Body_view.vue'),
      props: route => ({
        receivedRouteName: route.query.receivedRouteName
      })
    }
  ]
})

export default router
```

이제 `receivedRouteName`은 `Body_view` 컴포넌트로 적절히 전달될 것입니다.


</div>

<div class="body-full">

주어진 코드를 살펴보았습니다. 코드에서는 `RouterLink` 컴포넌트를 사용하여 `giturl` 변수를 `Body_view` 컴포넌트로 전달하려고 하고 있습니다. 코드에서 `giturl` 변수는 `receivedRouteName`이라는 값을 가지고 있습니다.

다음은 수정된 코드입니다.

```vue
<template>
  <div class="card custom-card">
    <div class="card-body">
      <blockquote class="blockquote mb-0">
        <!-- RouterLink 컴포넌트를 사용하여 giturl 변수를 Body_view 컴포넌트로 전달 -->
        <RouterLink class="navbar-brand" :to="{ path: '/Body_view', query: { receivedRouteName: giturl.receivedRouteName }}" :key="giturl.receivedRouteName">Body_view</RouterLink>
        <p>A well-known quote, contained in a blockquote element.</p>
        <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite>
        </footer>
      </blockquote>
    </div>
    <img
      src="https://i.ebayimg.com/images/g/SJcAAOSwtkBgucpI/s-l1600.jpg"
      class="card-img-top" alt="Image">
  </div>
</template>
<script setup>
import { ref } from 'vue'

// giturl 변수를 생성하고 초기화
const giturl = ref({
    receivedRouteName: "Define the type of data being received"
})
import { RouterLink } from 'vue-router'
</script>
<style scoped>
</style>
```

이제 수정된 코드에서 `RouterLink` 컴포넌트는 `giturl.receivedRouteName`을 `Body_view` 컴포넌트로 전달할 수 있게 되었습니다. 이를 통해 원활한 데이터 전달이 이루어질 것입니다.


</div>

<div style="background-color: grey; height: 15px;"></div>

