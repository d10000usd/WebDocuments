# Vue 3 Tab Data

## 1
3에서 script setup을 사용하여 HTML 파일의 JSON 데이터를 각 탭에서 표시하기설명HTML 파일에서 JSON 데이터를 읽어오고Vue 3와 script setup을 사용하여 각 탭에서 데이터를 표시하는 방법을 설명합니다.키워드HTML 파일JSON 데이터Vue 3script setup각 탭데이터 표시저장 2

## 2
HTML 파일에서 JSON 데이터를 읽어오기 위해 JavaScript를 사용할 것입니다. 그런 다음 Vue 3와 script setup을 사용하여 각 탭에서 데이터를 표시합니다.HTML 파일에서 JSON 데이터 읽기:htmlCopy code<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue 3 Tab Example</title>
</head>
<body>
    <div id="app">
        <div>
            <button @click="switchTab(1)">Tab 1</button>
            <button @click="switchTab(2)">Tab 2</button>
        </div>
        <div v-if="currentTab === 1">
            <!-- Tab 1 Content -->
            <h2>Tab 1</h2>
            <p>{{ tab1Data }}</p>
        </div>
        <div v-if="currentTab === 2">
            <!-- Tab 2 Content -->
            <h2>Tab 2</h2>
            <p>{{ tab2Data }}</p>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue@3
저장 4