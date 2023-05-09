# Routing

## <b>Routing이란?</b>
- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
  - 유저가 방문한 URL에 대해 적절한 결과를 응답

<br>

## <b>Routing in SSR</b>
- Server가 모든 라우팅을 통제
- URL로 요청이 들어오면 응답으로 완성된 HTML 제공
  - Django로 보낸 요청의 응답 HTML은 완성본인 상태였음
- 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

<br>

## <b>Routing in SPA / CSR</b>
- 서버는 하나의 HTML(index.html)만을 제공
- 이후에 모든 동작은 하나의 HTML 문서 위에서 JavaScript 코드를 활용
  - axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
- 즉, 하나의 URL만 가질 수 있음

<br>

## <b>Routing이 없다면?</b>
- 유저가 URL을 통한 페이지의 변화 감지 불가능
- 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
  - 새로고침 시 처음 페이지로 돌아감
  - 링크 공유 시 처음 페이지만 공유 가능
- 브라우저의 뒤로 가기 기능 사용 불가능

<br><br>

# Vue Router

## <b>Vue Router란?</b>
- Vue의 공식 라우터
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트에서 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링할 지 알려주
  - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
  - URL이 변경되지 않는다는 SPA 단점을 해결
- MPA(Multiple Page Application)
  - 여러 개의 페이지로 구성된 애플리케이션
  - SSR 방식으로 렌더링

<br>

## <b>Vue Start Setting</b>
- Vue CLI를 통해 router plugin 적용
```
vue add router
```
- history mode 사용 여부 -> Yes
- App.vue에 `router-link` 요소 및 `router-view`가 추가
```html
<!-- App.vue -->
<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
  </div>
</template>
```
- router/index.js 생성
- views 폴더 생성

<br>

## <b>History mode</b> 
- 브라우저의 History API를 활용한 방식
  - 새로고침 없이 URL 이동 기록을 남길 수 있음
- 우리에게 익숙한 URL 구조로 사용 가능
- Default값은 Hash mode(`#`을 통해 URL을 구분하는 방식)

<br>

## <b>`router-link`</b>
- a 태그와 비슷한 기능 -> URL을 이동시킴
  - routes에 등록된 컴포넌트와 매핑됨
  - 히스토리 모드에서 router-link는 클릭 이벤트를 차단
- 목표 경로는 `to` 속성으로 지정됨
- 기능에 맞게 HTML에서 a 태그로 렌더링되고, 다른 태그로 변경 가능

<br>

## <b>`router-view`</b>
- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
- 장고의 block tag와 비슷

<br>

## <b>src / router / index.js</b>
- 라우터에 관련된 정보 및 설정이 작성된 곳
- Django에서의 urls.py에 해당
- routes에 URL와 컴포넌트를 매핑
```javascript
// index.js
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
```
<br>

## <b>src / views</b>
- `router-view`에 들어갈 컴포넌트 작성
- 기존에 컴포넌트를 작성하던 곳은 컴포넌트 폴더 뿐이었지만 이제 두 폴더로 나눠짐
- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님

### views/
- routes에 매핑되는 컴포넌트
- 다른 컴포넌트와 구분하기 위해 View로 끝나도록 이름을 만듦

### components/
- routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더

<br><br>

# Vue Router 활용

## <b>선언적 방식 네비게이션</b>
- `router-link`의 `to`속성으로 주소 전달
- `routes`에 등록된 주소와 매핑된 컴포넌트로 이동
- 동적인 값을 사용ㅎ게되면 v-bind를 사용해야 정상적으로 작동
```html
<router-link to="/">Home</router-link>
<router-link :to="{name: 'home'}">Home</router-link>
```

<br>

## <b>프로그래밍 방식 네비게이션</b>
- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 가능
- 다른 URL로 이동하려면 `this.$router.push`를 사용
  - history stack에 이동할 URL을 넣는 방식
  - history stack에 기록이 남아 브라우저의 뒤로 가기 버튼 사용 가능
```html
<!-- AboutView.vue -->
<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click='toHome'>홈으로</button>
  </div>
</template>
<script>
export default {
  name: 'AboutView',
  methods: {
    toHome() {
      this.$router.push({name:'home'})
    }
  }
}
</script>
```

<br>

## <b>Dynamic Route Matching</b>
- 동적 인자 전달
  - URL의 특정 값을 변수처럼 사용 가능
- route를 추가할 때 동적 인자를 명시
- `$route.params`로 변수에 접근 가능
- data에 넣어서 사용하는 것을 권장
``` javascript
// router/index.js
import HelloView from '../views/HelloView.vue'

...
const routes = [
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  }
]
...
```
```html
<!-- HelloView.vue -->
<template>
  <div>
    <h1>hello, {{ $route.params.userName }}</h1>
    <h1>hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HellowView',
  data() {
    return {
      userName: this.$route.params.userName
    }
  }
}
</script>
```

### 1. 선언적 방식 네비게이션
- params를 이용하여 동적 인자 전달 가능
```html
<!-- App.vue -->
<router-link :to="{name: 'hello', params: { userName: 'harry'}}">Hello</router-link>
```

### 2. 프로그래밍 방식 네비게이션
- 직접 데이터를 입력받아 router를 통해 전달
```html
<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click='toHome'>홈으로</button>
    <input type="text" v-model="inputData" @keyup.enter="goToHello">
  </div>
</template>
<script>
export default {
  name: 'AboutView',
  data() {
    return{
      inputData: null
    }
  },
  methods: {
    toHome() {
      this.$router.push({name:'home'})
    },
    goToHello() {
      this.$router.push({name:'hello', params: {userName: this.inputData}})
    }
  }
}
</script>
```
<br>

## <b>lazy - loading</b>
- 모든 파일을 한 번에 로드하면 시간이 매우 오래 걸림
- 특정 라우트에 방문할 때만 매핑 컴포넌트 로드
  - 최초 로드하는 시간이 빨라짐
```javascript
// router/index.js
  {
    path: '/about',
    name: 'about',
    component: () => import( '../views/AboutView.vue')
  },
```
