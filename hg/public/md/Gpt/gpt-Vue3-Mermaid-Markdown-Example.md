PROMPT:

import VueMermaidString from "vue-mermaid-string"; import endent from "endent"; 사용해서 마크다운 문서를 보게 vue3 , script setup 으로 해줘

RESPONSE:

Sure! Here's an example of how you can use VueMermaidString and endent to display a markdown document in Vue 3 with the script setup syntax:

```html
<template>
  <div>
    <div v-html="markdown"></div>
  </div>
</template>

<script setup>
import VueMermaidString from "vue-mermaid-string";
import endent from "endent";

const markdown = endent`
# Markdown Document

This is a **markdown** document rendered using Vue 3 and the vue-mermaid-string library.

Here's an example of a mermaid diagram using the \`vue-mermaid-string\` component:

\`\`\`mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
\`\`\`
`;

VueMermaidString.register();

</script>
```

In this example, we import the VueMermaidString component from the "vue-mermaid-string" library and the endent function from the "endent" library.

We define a `markdown` variable that contains the markdown content using the endent function to preserve the indentation and line breaks.

Within the `<template>` section, we use the `v-html` directive to render the markdown content as HTML.

In the `<script setup>` section, we register the VueMermaidString component using `VueMermaidString.register()`.

Make sure to install the required dependencies (`vue-mermaid-string` and `endent`) before using them in your project.

Note: This example assumes that you have already set up Vue 3 and have the necessary build tools configured.