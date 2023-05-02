# Vue CLI

## <b>Vue CLI란?</b> 
- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 플러그인, GUI, Babel등 다양한 Tool 제공


<br>

## <b>package.json</b> 
- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함

<br>

## <b>package-lock.json</b> 
- node_moudles에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
- 사용할 패키지의 버전을 고정
- 개발 과정 간의 의존성 패키지 충돌방지
- python의 requirements.txt 역할

<br>

## <b>Public/index.html</b>
- Vue 앱의 뼈대가 되는 html 파일
- Vue 앱과 연결될 요소가 있음

<br>

## <b>node_modules</b>
- node.js 환경의 여러 의존성 모듈
- python의 venv와 비슷한 역할을 함
  - 따라서 `.gitignore`에 넣어주어야 함
  - Vue 프로젝트를 생성하면 자동으로 추가됨

### Module이란?
- 애플리케이션의 크기가 커지고 복잡해지면서 파일 하나에 모든 기능을 담기 어려워짐
- 자연스럽게 파일을 여러 개로 분리하여 관리를 하게되고, 각각 파일을 모듈이라고 함
- 모듈은 대개 기능 단위로 분리
- 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성

### 모듈 의존성 문제
- 모듈의 수가 많아지고 라이러리 혹은 모듈 간의 의존성이 깊어지는 문제 발생
- 이러한 경우 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
  - Webpack은 이 모듈 간의 의존성 문제를 해결하기 위해 등장

### Bundler
- 모듈 의존성 문제를 해결해주는 작업이 Bundling
- 이러한 일을 해주는 도구가가 Bundler이고, Webpack은 다양한 Bundler 중 하나
- 모듈들을 하나로 묶어주고 묶인 파일은 하나로 만들어짐
- Bundling된 결과물을은 개별 모듈의 실행 순서에 영향을 받지 않고 동작
- Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음

### 1. node_modules - Babel
- "JavaScript complier"
- 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구
- 자바스크립트의 파편호, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양

### 2. node_modules - Webpack
- "static module bundler"
- 모듈간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함

<br>

## <b>src</b>

### 1. assets
- 정적 파일을 저장하는 디렉토리

### 2. components
- 하위 컴포넌트들이 위치

### 3. App.vue
- 최상위 컴포넌트
- public/index.html과 연결됨

### 4. main.js
- webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
- public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳
- Vue 전역에서 활용할 모듈을 등록할 수 있는 파일

<br><br>

# Vue Component

## <b>Component란?</b> 
- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임

<br>

## <b>Component based architecture 특징</b>
- 관리가 용이
  - 유지/보수 비용 감소
- 재사용성
- 확장 가능
- 캡슐화
- 독립적

<br>

## <b>SFC(Single File Component)</b>
- 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다.
- Vue instance에서는 HTML, CSS, JavaScript 코드를 한 번에 관리
- 컴포넌트 기반 개발의 핵심 기능

<br>

## <b>Vue component 구조</b>

### 템플릿(HTML)
- HTML의 body 부분
- 눈으로 보여지는 요소 작성
- 다른 컴포넌트를 HTML 요소처럼 추가 가능

### 스크립트(JavaScript)
- JavaScript 코드가 작성되는 곳
- vue 인스턴스를 구성하는 대부분이 작성됨

### 스타일(CSS)
- CSS가 작성되며 컴포넌트의 스타일을 담당

<br>

## <b>Vue component 구조 정리</b>
- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
- root에 해당하는 최상단의 component가 App.vue
- 이 App.vue를 index.html과 연결
- 결국 index.html 파일 하나만을 rendering

<br><br>

# 기본 커맨드

## <b>Vue CLI 시작하기</b> 
- 설치
> npm install -g @vue/cli
- 프로젝트 생성
> vue create vue-cli
- 프로젝트 실행
> npm run serve

<br>

## <b>컴포넌트 생성</b> 
- `src/components/`안에 생성
- `script`에 이름 등록
- `template`에 요소 추가
  - template 안에는 하나의 요소만 추가 가능
  - 비어 있어도 안 됨
```html
<!-- MyComponent.vue -->
<template>
  <div class="border">
    <h1>This is MyComponent</h1>
  </div>
</template>

<script>
export default {
  name: 'MyComponent',
}
</script>

<style>
  .border {
    border: solid
  }
</style>
```
<br>

## <b>component 등록</b> 
### 불러오기
- `import {instance name} from {위치}`
- `instance name`은 instance 생성 시 작성한 name
- `@`는 src의 shortcut
- `.vue`는 생략 가능

### 보여주기
- 닫는 태그만 있는 요소처럼 사용

```html
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComnent/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyComnent from './components/MyComponent'

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComnent
  }
}
</script>
```
