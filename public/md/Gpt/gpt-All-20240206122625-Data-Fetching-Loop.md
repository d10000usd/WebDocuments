#2

# **<span style="font-size: 18px; font-style: italic;">Data Fetching Loop</span>**
The line `await his.fetchData('historyhtml')` is likely executing multiple times because it is within the `onMounted` lifecycle hook. This hook is called when the component is mounted, and it appears that every time the component is mounted or re-rendered, it triggers the execution of this line.

If you want to fetch data only once when the component is initially mounted, you should move the `await his.fetchData('historyhtml')` outside of the `onMounted` hook. For example, you can place it directly inside the `<script setup>` block:

```javascript
<script setup>
import { onMounted, ref } from 'vue';
import { ApiUrl } from '../../ts/serverconn/DataFetcher';

const his = new ApiUrl();
const data = ref();

// Fetch data only once when the component is mounted
(async () => {
  data.value = await his.fetchData('historyhtml');
})();

// Other setup code...
</script>
```

This way, the data will be fetched once when the component is initially mounted, and subsequent renders won't trigger the data fetching again.

#4

# **<span style="font-size: 18px; font-style: italic;">Data Fetching Loop</span>**
`await his.fetchData('historyhtml')`이 계속 실행되는 이유는 아마도 이 코드가 `onMounted` 라이프사이클 훅 안에 있기 때문입니다. `onMounted` 훅은 컴포넌트가 마운트될 때마다 호출되므로 컴포넌트가 마운트되거나 다시 렌더링될 때마다 이 코드가 실행됩니다.

컴포넌트가 처음 마운트될 때만 데이터를 한 번만 가져오려면 `onMounted` 훅 바깥으로 `await his.fetchData('historyhtml')`을 이동해야 합니다. 예를 들어, 다음과 같이 `<script setup>` 블록 안에 직접 배치할 수 있습니다.

```javascript
<script setup>
import { onMounted, ref } from 'vue';
import { ApiUrl } from '../../ts/serverconn/DataFetcher';

const his = new ApiUrl();
const data = ref();

// 컴포넌트가 처음 마운트될 때만 데이터를 가져옴
(async () => {
  data.value = await his.fetchData('historyhtml');
})();

// 다른 설정 코드...
</script>
```

이렇게 하면 컴포넌트가 처음 마운트될 때 데이터가 한 번만 가져와지며, 후속 렌더링에서는 데이터를 다시 가져오지 않습니다.

#6

# **<span style="font-size: 18px; font-style: italic;">Data Fetching Loop</span>**
`await his.fetchData('historyhtml')`이 계속해서 실행되는 이유는 아마도 컴포넌트가 다시 렌더링될 때마다 `onMounted` 훅이 호출되기 때문입니다. `onMounted` 훅은 컴포넌트가 마운트될 때 실행되는데, 여러 이유로 인해 컴포넌트가 다시 렌더링되면 이 훅이 다시 실행됩니다.

이를 방지하려면 `onMounted` 훅 안에 있는 코드를 조절하거나 다른 방식으로 접근해야 합니다. 한 가지 방법은 `onMounted` 훅 내에서 해당 코드를 실행하지 않도록 하는 것입니다. 예를 들면:

```javascript
<script setup>
import { onMounted, ref } from 'vue';
import { ApiUrl } from '../../ts/serverconn/DataFetcher';

const his = new ApiUrl();
const data = ref();

const fetchData = async () => {
  data.value = await his.fetchData('historyhtml');
};

// 컴포넌트가 처음 마운트될 때만 데이터를 가져옴
onMounted(fetchData);

// 다른 설정 코드...
</script>
```

이렇게 하면 `fetchData` 함수가 처음 한 번만 실행되고, 이후에는 다시 실행되지 않습니다.

#8

# **<span style="font-size: 18px; font-style: italic;">Data Fetching Loop</span>**
`await his.fetchData('historyhtml')`이 여러 번 실행되는 이유를 확인하기 위해 몇 가지 가능한 원인을 살펴보겠습니다:

1. **컴포넌트 다시 렌더링**: 컴포넌트가 다시 렌더링될 때마다 `onMounted` 훅이 호출됩니다. 다시 렌더링되는 이유를 확인하고, 이를 방지하기 위해 상태나 조건을 확인해 보세요.

2. **비동기 이슈**: `onMounted` 훅 안에서 비동기 작업이 완료되기 전에 다시 렌더링이 일어나면 코드가 다시 실행될 수 있습니다. 이 경우 `await his.fetchData('historyhtml')`이 여러 번 실행됩니다.

3. **컴포넌트 재생성**: 컴포넌트가 재생성되는 경우에도 `onMounted` 훅이 호출됩니다. 컴포넌트의 상태가 변경되면서 재생성되는지 확인해 보세요.

해결책으로는:

- 컴포넌트 상태나 조건을 확인하여 불필요한 렌더링을 방지합니다.
- `onMounted` 훅 안에서 `await his.fetchData('historyhtml')` 호출 이후에 어떤 동작이 일어나는지 확인하여 이후 동작이 예상과 다른지 확인합니다.
- 컴포넌트 재생성을 막기 위해 상태를 적절히 관리합니다.

코드를 조금 더 상세히 살펴보고 문제의 원인을 찾아서 수정할 수 있습니다.

