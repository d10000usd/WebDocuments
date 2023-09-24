````javascript
<template>
  <div id="app">
    <vue-mermaid-string :value="diagram" />
  </div>
</template>

<script setup>
import VueMermaidString from "vue-mermaid-string";
import { ref, computed } from "vue";
import endent from "endent";

const diagram = computed(() => endent`
  graph TD
    DateTime[Date and time]

    JavaScript --> Frameworks
    JavaScript --> DateTime
    JavaScript --> 3D
    Frameworks --> Vue.js
    Frameworks --> React
    DateTime --> Moment.js
    DateTime --> date-fns
    3D --> Three.js
    3D --> Babylon.js
`);

</script>
```