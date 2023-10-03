PROMPT:

<template> <div id="app"> <vue-mermaid-string :value="diagram" /> </div> </template> <script> import VueMermaidString from "vue-mermaid-string"; import endent from "endent"; export default { computed: { diagram: () => endent\` graph TD DateTime\[Date and time\] JavaScript --> Frameworks JavaScript --> DateTime JavaScript --> 3D Frameworks --> Vue.js Frameworks --> React DateTime --> Moment.js DateTime --> date-fns 3D --> Three.js 3D --> Babylon.js \`, }, components: { VueMermaidString, }, }; </script> script setup 으로 수정

RESPONSE:

Sure! I can help you modify the code to use the `<script setup>` syntax. Here's the updated code with the `<script setup>` syntax:

```vue
<template>
  <div id="app">
    <VueMermaidString :value="diagram" />
  </div>
</template>

<script setup>
import VueMermaidString from "vue-mermaid-string";
import endent from "endent";

const diagram = endent`
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
`;

</script>

<script>
export default {
  components: {
    VueMermaidString,
  },
};
</script>
```

In the `<script setup>` section, you can directly declare variables and import statements without explicitly defining them as computed properties. The `diagram` variable holds the diagram string.

The rest of the code remains the same, where the `VueMermaidString` component is used to display the mermaid diagram based on the `diagram` value.

Please make sure you have the necessary dependencies installed (`vue-mermaid-string` and `endent`) for this code to work properly.