# 네비게이션 가드

## <b>네비게이션 가드란?</b>
- Vue router로 URL에 접근할 때 다른 url로 redirect를 하거나 해당 URL로의 접근을 막는 방법

<br>

## <b>네비게이션 가드의 종류</b>
- 전역 가드
  - 애플리케이션 전역에서 동작
- 라우터 가드
  - 특정 URL에서만 동작
- 컴포넌트 가드
  - 라우터 컴포넌트 안에 정의

<br><br>

# 전역 가드

## <b>Global Before Guard</b>
- 다른 url 주소로 이동할 때 항상 실행
- router/index.js에 router.beforeEach()를 사용하여 설정
- URL이 변경되어 화면이 전환되기 전 `router.beforeEach()`가 호출됨
  - 화면이 전환되지 않고 대기 상태가 됨
- 변경된 URL로 라우팅하기 위해서는 `next()`를 호출해줘야함
  - `next()`가 호출되기 전까지 화면이 전환되지 않음

<br>

## <b>전역가드의 인자</b>
- `to` : 이동할 URL 정보가 담긴 Route 객체
- `from` : 현재 URL 정보가 담긴 Route 객체
- `next` : 지정한 URL로 이동하기 위해 호출하는 함수
  - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
  - 기본적으로 `to`에 해당하는 URL로 이동

## <b>예시코드</b>
```javascript
// router/index.js
router.beforeEach((to, from, next) => {
  // 로그인 여부
  const isLoggedIN = false
  // 로그인이 필요한 페이지
  const authPages = ['hello']
  // 앞으로 이동할 페이지가 로그인이 필요한 사이트인지 확인
  const isAuthRequired = authPages.includes(to.name)
  
  // 로그인 여부 판단에 따른 페이지 이동
  if (! isAuthRequired || isLoggedIN) {
    console.log('to로 이동')
    next()
  } else {
    console.log('login으로 이동')
    next({name:'login'})
  }
})
```

<br><br>

# 라우터 가드

## <b>라우터 가드란?</b>
- 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용

<br>

## <b>`beforEnter()`</b>
- route에 진입했을 때 실행
- 라우터를 등록한 위치가 추가
- 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
- 콜백 함수는 `to`, `from`, `next`를 인자로 받음

<br>

## <b>예시 코드</b>
```js
// router/index.js
const isLoggedIn = true

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 함')
        next({name: 'home'})
      } else {
        next()
      }
    }
  }
]
```

<br><br>

# 컴포넌트 가드

## <b>컴포넌트 가드란?</b>
- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
  
<br>

## <b>`beforeRouteUpdate()`</b>
- 해당 컴포넌트를 렌더링하는 경로가 변경될 때 싱행

<br>

## <b>예시 코드</b>
```js
// view/HelloView.vue
<script>
export default {
    name: 'HelloView',
    data() {
        return {
            userName: this.$route.params.userName
        }
    },
    beforeRouteUpdate(to, from, next) {
        this.userName = to.params.userName
        next()
    }
}
</script>
```
<br><br>

# 404 Not Found

## <b>요쳥한 리소스가 존재하지 않는 경우</b>
- 모든 경로에 대해서 404 page로 redirect 시키기
- 기존에 명시한 경로가 아닌 모든 경로가 404 page로 redirect됨
- 이 때, `routes`에 최하단부에 작성해야 함
```js
const routes = [
  ...
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  }
]
```