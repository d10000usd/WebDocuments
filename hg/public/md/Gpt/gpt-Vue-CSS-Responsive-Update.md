PROMPT:

<template> <div class="app-container"> <Headerbar :isSidebarOpen="isSidebarVisible" /> <div class="main-container"> <Sidebar v-if="isSidebarVisible" /> <div class="router-view-container"> <router-view /> </div> </div> </div> </template> <script setup> import { ref, watchEffect } from 'vue'; import Sidebar from "./layouts/Sidebar.vue"; import Headerbar from "./layouts/Headerbar.vue"; const isSidebarVisible = ref(true); watchEffect(() => { const handleResize = () => { isSidebarVisible.value = window.innerWidth >= 780; }; window.addEventListener('resize', handleResize); handleResize(); return () => { window.removeEventListener('resize', handleResize); }; }); </script> <style > /\* Add any custom styles here \*/ .app-container { display: flex; flex-direction: column; height: 100vh; } .main-container { display: flex; flex-grow: 1; } .router-view-container { flex-grow: 1; padding-top: 20px; /\* Adjust this value to create space below the Headerbar \*/ overflow-y: auto; } .sidebar { width: 200px; /\* Set the desired width for the sidebar \*/ height: 100%; background-color: #c51515; /\* Set the desired background color \*/ /\* Add other styles as needed \*/ } </style> App.vue <template> <div class="sidebar"> <!-- Sidebar content --> Sidebar </div> </template> <script setup> // Empty script setup as no reactive logic is needed in this component </script> <style> .sidebar { width: 60px; /\* Set the desired width for the sidebar \*/ height: 100vh; /\* Set the height to 100% of the viewport height \*/ background-color: #c51515; /\* Set the desired background color \*/ /\* Add other styles as needed \*/ } </style> Side.vue <template> <header class="header navbar navbar-expand-lg navbar-light bg-light"> <div class="container-fluid"> <router-link class="navbar-brand" to="/">Your Logo</router-link> <button class="navbar-toggler" type="button" @click="isSidebarOpen = !isSidebarOpen" > <span class="navbar-toggler-icon"></span> </button> <div :class="sidebarClasses" id="navbarSupportedContent"> <ul class="navbar-nav me-auto mb-2 mb-lg-0"> <li class="nav-item"> <router-link class="nav-link" to="/Markdown">Markdown</router-link> </li> <li class="nav-item"> <router-link class="nav-link" to="/GitReadme">GitReadme</router-link> </li> <li class="nav-item"> <router-link class="nav-link" to="/FastApi">서버루틴뷰</router-link> </li> </ul> </div> </div> </header> </template> <script setup> import { ref, computed } from 'vue'; const isSidebarOpen = ref(true); const sidebarClasses = computed(() => isSidebarOpen.value ? 'collapse navbar-collapse show' : 'collapse navbar-collapse' ); </script> <style lang="scss" scoped> /\* Add any custom styles here \*/ .header { width: 100%; } </style> Header.vue App.vue Side.vue , Header.vue 를 서로 참고 해서 반응형으로 css 를 boostrap 으로 보기 좋게 수정해줘 헤더바는 크기가 작아 졌을때 메뉴 왼쪽에서 보이게해주고 헤더를 기준으로 전체 크기가 1200보다 더크게 늘어나지 않게 해줘,

RESPONSE:

Sure, I'll modify the CSS code in the components (App.vue, Sidebar.vue, Header.vue) to make them responsive and use Bootstrap to improve the layout. Here's the updated code:

**App.vue**:

```html
<template>
  <div class="app-container">
    <Headerbar :isSidebarOpen="isSidebarVisible" />
    <div class="main-container">
      <Sidebar v-if="isSidebarVisible" />
      <div class="router-view-container">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue';
import Sidebar from "./layouts/Sidebar.vue";
import Headerbar from "./layouts/Headerbar.vue";

const isSidebarVisible = ref(true);

watchEffect(() => {
  const handleResize = () => {
    isSidebarVisible.value = window.innerWidth >= 780;
  };

  window.addEventListener('resize', handleResize);
  handleResize();

  return () => {
    window.removeEventListener('resize', handleResize);
  };
});
</script>

<style>
/* Add any custom styles here */
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Instead of height: 100vh, use min-height to ensure it expands when content exceeds viewport height */
}

.main-container {
  display: flex;
  flex-grow: 1;
  max-width: 1200px; /* Set a maximum width for the main container */
  margin: 0 auto; /* Center the main container horizontally */
}

.router-view-container {
  flex-grow: 1;
  padding-top: 20px; /* Adjust this value to create space below the Headerbar */
  overflow-y: auto;
}

/* ... other styles remain the same ... */

</style>
```

**Sidebar.vue**:

```html
<template>
  <div class="sidebar">
    <!-- Sidebar content -->
    Sidebar
  </div>
</template>

<script setup>
// Empty script setup as no reactive logic is needed in this component
</script>

<style>
.sidebar {
  width: 250px; /* Increased the width to make it more usable on larger screens */
  height: 100%; /* Set the height to 100% of the parent container */
  background-color: #c51515;
  /* Add other styles as needed */
}
</style>
```

**Header.vue**:

```html
<template>
  <header class="header navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">Your Logo</router-link>
      <button
        class="navbar-toggler"
        type="button"
        @click="isSidebarOpen = !isSidebarOpen"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div :class="sidebarClasses" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <!-- Add 'navbar-nav' class to the parent UL element -->
          <li class="nav-item">
            <router-link class="nav-link" to="/Markdown">Markdown</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/GitReadme">GitReadme</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/FastApi">서버루틴뷰</router-link>
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue';

const isSidebarOpen = ref(true);
const sidebarClasses = computed(() =>
  isSidebarOpen.value ? 'collapse navbar-collapse show' : 'collapse navbar-collapse'
);
</script>

<style lang="scss" scoped>
/* Add any custom styles here */
.header {
  width: 100%;
}

/* Media query to show/hide the sidebar button on smaller screens */
@media (max-width: 768px) {
  .navbar-toggler {
    display: block;
  }

  .navbar-collapse {
    display: none;
  }

  .show.navbar-collapse {
    display: block;
  }
}
</style>
```

With these changes, the header will display a responsive sidebar button when the screen size is smaller, and the main container will have a maximum width of 1200 pixels, ensuring it doesn't expand beyond that on larger screens. Additionally, the sidebar width has been increased to 250 pixels for a better user experience.

PROMPT:

전체적으로 블로그처럼 보이도록 색상이랑 외곽선을 boostrap 으로 넣어줘, Side 는 내용이 수직으로 나오도록 해주고 모서리는 크게 굴곡을 만들어줘 배경색은 253,253,253

RESPONSE:

Sure, let's modify the CSS to give the components a blog-like appearance with Bootstrap colors and styles.

**App.vue**:

```html
<template>
  <div class="app-container">
    <Headerbar :isSidebarOpen="isSidebarVisible" />
    <div class="main-container">
      <Sidebar v-if="isSidebarVisible" />
      <div class="router-view-container">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue';
import Sidebar from "./layouts/Sidebar.vue";
import Headerbar from "./layouts/Headerbar.vue";

const isSidebarVisible = ref(true);

watchEffect(() => {
  const handleResize = () => {
    isSidebarVisible.value = window.innerWidth >= 780;
  };

  window.addEventListener('resize', handleResize);
  handleResize();

  return () => {
    window.removeEventListener('resize', handleResize);
  };
});
</script>

<style>
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
  max-width: 1200px;
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

/* ... other styles remain the same ... */

</style>
```

**Sidebar.vue**:

```html
<template>
  <div class="sidebar">
    <!-- Sidebar content -->
    Sidebar
  </div>
</template>

<script setup>
// Empty script setup as no reactive logic is needed in this component
</script>

<style>
.sidebar {
  width: 250px;
  height: 100%;
  background-color: rgb(253, 253, 253);
  padding: 20px; /* Add some padding to the sidebar */
  border-radius: 10px; /* Add border radius to create rounded corners */
  display: flex;
  flex-direction: column;
}

/* Style for sidebar content (optional, you can customize this) */
.sidebar-content {
  flex-grow: 1;
}

/* Style for the sidebar footer (optional, you can customize this) */
.sidebar-footer {
  margin-top: 20px;
}

</style>
```

**Header.vue**:

```html
<template>
  <header class="header navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">Your Logo</router-link>
      <button
        class="navbar-toggler"
        type="button"
        @click="isSidebarOpen = !isSidebarOpen"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div :class="sidebarClasses" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/Markdown">Markdown</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/GitReadme">GitReadme</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/FastApi">서버루틴뷰</router-link>
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue';

const isSidebarOpen = ref(true);
const sidebarClasses = computed(() =>
  isSidebarOpen.value ? 'collapse navbar-collapse show' : 'collapse navbar-collapse'
);
</script>

<style lang="scss" scoped>
/* Add any custom styles here */
.header {
  width: 100%;
}

/* Media query to show/hide the sidebar button on smaller screens */
@media (max-width: 768px) {
  .navbar-toggler {
    display: block;
  }

  .navbar-collapse {
    display: none;
  }

  .show.navbar-collapse {
    display: block;
  }
}
</style>
```

With these changes, the layout should resemble a blog-like appearance with Bootstrap colors, rounded corners, and a white background for the main content area. The sidebar will have a light gray background and a more blog-like appearance with the specified modifications.

PROMPT:

header.vue를 가운데 정렬해줘

RESPONSE:

To center the Header.vue component, we can use Bootstrap's utility classes to align the content horizontally. We'll modify the Header.vue component to achieve this:

```html
<template>
  <header class="header navbar navbar-expand-lg navbar-light bg-light justify-content-center">
    <div class="container">
      <router-link class="navbar-brand" to="/">Your Logo</router-link>
      <button
        class="navbar-toggler"
        type="button"
        @click="isSidebarOpen = !isSidebarOpen"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div :class="sidebarClasses" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/Markdown">Markdown</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/GitReadme">GitReadme</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/FastApi">서버루틴뷰</router-link>
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue';

const isSidebarOpen = ref(true);
const sidebarClasses = computed(() =>
  isSidebarOpen.value ? 'collapse navbar-collapse show' : 'collapse navbar-collapse'
);
</script>

<style lang="scss" scoped>
/* Add any custom styles here */
.header {
  width: 100%;
}

/* Media query to show/hide the sidebar button on smaller screens */
@media (max-width: 768px) {
  .navbar-toggler {
    display: block;
  }

  .navbar-collapse {
    display: none;
  }

  .show.navbar-collapse {
    display: block;
  }
}
</style>
```

In this modification, we added the `justify-content-center` class to the header element, which is a Bootstrap utility class to horizontally center its children. The container class is used inside the header to provide padding and limit the content width. The result will be a centered header component on the page.

PROMPT:

안되는데

RESPONSE:

Apologies for the confusion. Let's use a different approach to center the Header.vue component. We can use flexbox to achieve the centering. Here's the updated code for Header.vue:

```html
<template>
  <header class="header navbar navbar-expand-lg navbar-light bg-light">
    <div class="container d-flex justify-content-center">
      <router-link class="navbar-brand" to="/">Your Logo</router-link>
      <button
        class="navbar-toggler"
        type="button"
        @click="isSidebarOpen = !isSidebarOpen"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div :class="sidebarClasses" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/Markdown">Markdown</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/GitReadme">GitReadme</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/FastApi">서버루틴뷰</router-link>
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue';

const isSidebarOpen = ref(true);
const sidebarClasses = computed(() =>
  isSidebarOpen.value ? 'collapse navbar-collapse show' : 'collapse navbar-collapse'
);
</script>

<style lang="scss" scoped>
/* Add any custom styles here */
.header {
  width: 100%;
}

/* Media query to show/hide the sidebar button on smaller screens */
@media (max-width: 768px) {
  .navbar-toggler {
    display: block;
  }

  .navbar-collapse {
    display: none;
  }

  .show.navbar-collapse {
    display: block;
  }
}
</style>
```

With this change, the Header.vue component should be centered on the page using the `justify-content-center` class. The `d-flex` class applies the `display: flex` property to the container, and `justify-content-center` centers its children horizontally.

PROMPT:

<template> <div class="app-container"> <Headerbar :isSidebarOpen="isSidebarVisible" /> <div class="main-container"> <Sidebar\_left v-if="isSidebarVisible" /> <Sidebar\_right v-if="isSidebarVisible" /> <div class="router-view-container"> <router-view /> </div> </div> </div> </template> </template> 사이드바 left, right 를 왼쪽1개, 오른쪽 1개 나오도록 수정해줘 app.vue

RESPONSE:

Sure, let's modify the App.vue to have two sidebars, one on the left and one on the right.

```html
<template>
  <div class="app-container">
    <Headerbar :isSidebarOpen="isSidebarVisible" />
    <div class="main-container">
      <Sidebar_left v-if="isSidebarVisible" />
      <div class="router-view-container">
        <router-view />
      </div>
      <Sidebar_right v-if="isSidebarVisible" />
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue';
import Sidebar_left from "./layouts/Sidebar_left.vue";
import Sidebar_right from "./layouts/Sidebar_right.vue";
import Headerbar from "./layouts/Headerbar.vue";

const isSidebarVisible = ref(true);

watchEffect(() => {
  const handleResize = () => {
    isSidebarVisible.value = window.innerWidth >= 780;
  };

  window.addEventListener('resize', handleResize);
  handleResize();

  return () => {
    window.removeEventListener('resize', handleResize);
  };
});
</script>

<style>
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
  max-width: 1200px;
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

/* Style for both left and right sidebars */
.sidebar {
  width: 250px;
  height: 100%;
  background-color: rgb(253, 253, 253);
  padding: 20px; /* Add some padding to the sidebar */
  border-radius: 10px; /* Add border radius to create rounded corners */
  display: flex;
  flex-direction: column;
}

/* Style for left sidebar */
.sidebar-left {
  margin-right: 20px; /* Add margin between the left and main content */
}

/* Style for right sidebar */
.sidebar-right {
  margin-left: 20px; /* Add margin between the right and main content */
}

/* Style for sidebar content (optional, you can customize this) */
.sidebar-content {
  flex-grow: 1;
}

/* Style for the sidebar footer (optional, you can customize this) */
.sidebar-footer {
  margin-top: 20px;
}
</style>
```

Now, the App.vue has two sidebars, one on the left and one on the right. The main content is placed between them with some margin to create separation. Each sidebar has its own styling, and the main container has a maximum width with a white background and rounded corners, giving it a clean and organized appearance.

PROMPT:

sidebar 사이에 간격을 넣어줘 3

RESPONSE:

Sure, to add space between the two sidebars, we can add a margin between them in the App.vue component. Let's modify the code to include the gap:

```html
<template>
  <div class="app-container">
    <Headerbar :isSidebarOpen="isSidebarVisible" />
    <div class="main-container">
      <Sidebar_left v-if="isSidebarVisible" />
      <div class="sidebar-gap"></div> <!-- Add a div for the gap -->
      <div class="router-view-container">
        <router-view />
      </div>
      <Sidebar_right v-if="isSidebarVisible" />
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue';
import Sidebar_left from "./layouts/Sidebar_left.vue";
import Sidebar_right from "./layouts/Sidebar_right.vue";
import Headerbar from "./layouts/Headerbar.vue";

const isSidebarVisible = ref(true);

watchEffect(() => {
  const handleResize = () => {
    isSidebarVisible.value = window.innerWidth >= 780;
  };

  window.addEventListener('resize', handleResize);
  handleResize();

  return () => {
    window.removeEventListener('resize', handleResize);
  };
});
</script>

<style>
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
  max-width: 1200px;
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

/* Style for both left and right sidebars */
.sidebar {
  width: 250px;
  height: 100%;
  background-color: rgb(253, 253, 253);
  padding: 20px; /* Add some padding to the sidebar */
  border-radius: 10px; /* Add border radius to create rounded corners */
  display: flex;
  flex-direction: column;
}

/* Style for left sidebar */
.sidebar-left {
  margin-right: 10px; /* Add margin to create space between the sidebars */
}

/* Style for right sidebar */
.sidebar-right {
  margin-left: 10px; /* Add margin to create space between the sidebars */
}

/* Add a gap between the sidebars */
.sidebar-gap {
  width: 20px; /* Adjust the width to your desired gap size */
}

/* Style for sidebar content (optional, you can customize this) */
.sidebar-content {
  flex-grow: 1;
}

/* Style for the sidebar footer (optional, you can customize this) */
.sidebar-footer {
  margin-top: 20px;
}
</style>
```

I've added a `sidebar-gap` div with a width of 20 pixels between the `Sidebar_left` and `Sidebar_right` components. You can adjust the width value to your desired gap size. This will create a space of 20 pixels between the two sidebars.

PROMPT:

<script setup lang="ts"> // import FastApiComp from '../components/comp/FastApiComp.vue' import FastApiComp\_get from "../components/comp/FastApiComp\_get.vue" import FastApiComp\_put from "../components/comp/FastApiComp\_put.vue" import FastApiComp\_post from "../components/comp/FastApiComp\_post.vue" import FastApiComp\_ServerDocs from "../components/comp/FastApiComp\_ServerDocs.vue" import { ref, onMounted, computed } from 'vue'; const isSidebarOpen = ref(true); const classes = computed(() => \[ isSidebarOpen.value ? 'xl:pl-64 flex mt-3 ' : 'md:ml-23 mt-3 ', 'pt-32', 'px-1', 'pb-5', \]); </script> <template> <main :class="classes" style="max-width: 100vw;"> <FastApiComp\_get /> <hr> <FastApiComp\_put /> <hr> <FastApiComp\_post /> <hr> <FastApiComp\_ServerDocs /> </main> </template> <style > .center-container { display: flex; justify-content: center; align-items: center; height: 100vh; /\* Adjust this as needed to control the vertical centering \*/ max-width: 1200px; } </style> Fast.vue 인데 router-view 크기를 다른것들이랑 같게 해줘

RESPONSE:

To make the `router-view` element have the same size as other components, we can modify the Fast.vue component as follows:

```html
<template>
  <main :class="classes">
    <router-view />
  </main>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
const isSidebarOpen = ref(true);
  
const classes = computed(() => [
  isSidebarOpen.value ? 'xl:pl-64 flex mt-3' : 'md:ml-23 mt-3',
  'pt-32',
  'px-1',
  'pb-5',
]);
</script>

<style>
.center-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Adjust this as needed to control the vertical centering */
  max-width: 1200px;
}

/* Adjust the router-view styles to match the other components */
main {
  flex-grow: 1;
  max-width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center; /* Center the content horizontally */
  padding-top: 32px;
  padding-bottom: 5px;
}

hr {
  width: 100%;
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
```

In this modification, we set the `flex-grow` property of the `main` element to 1, which makes it take up the available vertical space. The `max-width` is set to `100vw`, which allows the `main` element to take up the full width of the viewport. The content inside the `main` element will be centered both horizontally and vertically, and the `hr` elements will span the full width of the container. Now, the `router-view` element will have the same size as other components in the Fast.vue file.

PROMPT:

<template> <main :class="classes" style="max-width: 100vw;"> <FastApiComp\_get /> <hr> <FastApiComp\_put /> <hr> <FastApiComp\_post /> <hr> <FastApiComp\_ServerDocs /> </main> </template> 크기를 1200으로 고정해줘

RESPONSE:

Sure, let's modify the Fast.vue component to fix the size of the `main` element to a width of 1200 pixels:

```html
<template>
  <main :class="classes" style="max-width: 1200px;">
```

PROMPT:

<template> <main :class="classes" style="max-width: 100vw;"> <FastApiComp\_get /> <hr> <FastApiComp\_put /> <hr> <FastApiComp\_post /> <hr> <FastApiComp\_ServerDocs /> </main> </template> 크기를 1200으로 고정해줘 사이즈가 줄면 줄어 들고

RESPONSE:

Apologies for the confusion. Let's make sure the size of the `main` element is fixed at 1200 pixels even when the viewport is smaller.

To achieve this, we'll update the Fast.vue component as follows:

```html
<template>
  <main :class="classes">
    <div class="main-content" style="max-width: 1200px;">
      <FastApiComp_get />
      <hr>
      <FastApiComp_put />
      <hr>
      <FastApiComp_post />
      <hr>
      <FastApiComp_ServerDocs />
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
const isSidebarOpen = ref(true);

const classes = computed(() => [
  isSidebarOpen.value ? 'xl:pl-64 flex mt-3' : 'md:ml-23 mt-3',
  'pt-32',
  'px-1',
  'pb-5',
]);
</script>

<style>
.center-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Adjust this as needed to control the vertical centering */
  max-width: 1200px;
}

/* Adjust the router-view styles to match the other components */
main {
  flex-grow: 1;
  display: flex;
  justify-content: center; /* Center the content horizontally */
  padding-top: 32px;
  padding-bottom: 5px;
}

.main-content {
  width: 100%;
}
</style>
```

In this modification, we wrap the content of the `main` element with a `div` having the class `main-content`. This div will have a `max-width` of 1200 pixels, which will keep the content fixed at that width even when the viewport is smaller. The `main` element itself will take up the full width of the viewport (`100vw`) and center its child content horizontally using `justify-content: center`.