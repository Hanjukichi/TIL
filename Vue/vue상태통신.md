# State Management

## <b>상태 관리의 필요성</b>
- Web Application에서의 상태 표현
  - 현재 App이 가지고 있는 Data로 표현 가능
- 하나의 App은 여러 개의 component를 조합해서 만들어짐
- 각 component는 독립적이기 때문에 각각 상태를 가짐
- 여러 개의 component가 같은 상태를 유지할 필요가 존재

<br>

## <b>Pass Props & Emit Event
- 같은 데이터를 공유하고 있으므로, 각 컴포넌트가 동일한 상태를 유지
- 데이터의 흐름을 직관적으로 파악 가능
- component의 중첩이 깊어지면 데이터 전달이 쉽지 않음

<br>

## <b>Centralized Store</b>
- 중앙 저장소에 데이터를 모아서 상태 관리
- 각 component는 중앙 저장소의 데이터를 사용
- component의 계층에 상관없이 중앙 저장소에 접근해 데이터를 얻거나 변경 가능
- 중앙 저장소의 데이터가 변경시 component들은 데이터의 변화에 반응헤 변경된 데이터반영
- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리

<br>

## <b>Vuex</b>
- 상태관리 패턴 + 라이브러리
- 중앙저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경될 수 있도록 하는 규칙 설정
- Vue의 반응성을 효율적으로 사용하는 상태 관리 기능 제공
- Vue의 공식 도구로써 다양한 기능 제공

<br><br>

# Vuex

## <b>프로젝트 with vuex</b>

### vuex plugin 적용
- `vue add vuex`
- src / store / index.js 가 생성

### index.js
```javascript
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
```

### Vue와 Vuex 인스턴스 비교
Vue|Vuex
---|---
|data|state|
|computed|getters|
|methods|mutations|
||actions|

<br>

## <b>State</b>
- vue 인스턴스의 data에 해당
- 중앙에서 관리하는 모든 상태 정보
- 개별 component는 state에서 데이터를 가져와서 사용
- state의 데이터가 변화하면 해당 데이터르 사용하는 component도 자동으로 다시 렌더링
- $store.state로 state 데이터에 접근

<br>

## <b>Mutations</b>
- 실제로 state를 변경하는 유일한 방법
- vue 인스턴스의 methods에 해당
- Mutations에서 호출되는 핸들러 함수는 반드시 동기적이어야 함
  - 비동기 로직 사용시 state의 변화 시기를 특정할 수 없음
- 첫 번째 인자로 `state`를 받음
  - component 혹은 Actions에서 `commit()`메서드로 호출

<br>

## <b>Actions</b>
- mutations와 비슷하지만 비동기 작업을 포함 가능
- state를 직접 변경하지 않고 `commit()`메서드로 mutations를 호출해서 state를 변경
- context 객체를 인자로 받음
  - 이 객체를 통해 store.js의 모든 요소와 메서드에 접근 가능
- component에서 `dispatch()`메서드에 의해 호출됨

<br>

## <b>Getters</b>
- vue 인스턴스의 computed에 해당
- state를 활용하여 계산된 값을 얻고자 할 때 사용
  - state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
- computed와 마찬가지로 getters의 결과는 캐시되며, 종속된 값이 변경된 경우에만 재계산
- getters에서 계산된 값은 state에 영향을 미치지 않음
- 첫번째 인자로 `state`, 두번째 인자로 `getter`를 받음

<br>

## <b>Vuex 데이터 관리</b>
- Vuex를 사용한다고 해서 모든 데이터를 state에 넣어야 하는 것은 아님
- Vuex에서도 여전히 pass props, emit event를 사용하여 상태 관리 가능
- 개발 환경에 따라 적절하게 사용하는 것이 필요

<br>

## <b>Vuex 언제 사용할까?</b>
- Vuex는 공유된 상태 관리 처리에 유용
  - 개념에 대한 이해와 시작하는 비용이 큼
- 애플리케이션이 단순하다면 Vuex가 없는 것이 더 효율적일 수 있음
- 그러나 중대형 규모의 SPA를 구축하는 경우 Vuex는 자연스럽게 선택할 수있는 단계가 옴
- 결과적으로 역할에 적절한 상황에서 활용시 Vuex 라이브러리 효용 극대화

<br><br>

# Vuex 예제

## <b>state</b>
- 중앙에서 관리하는 모든 상태 정보
- `computed`에 정의 후 접근하는 것을 권장

```javascript
// store/index.js
...
state: {
  message: "message in store"
},
...
```
```html
<!-- App.vue -->
<template>
  <div id="app">
    <h1>{{ message }} </h1>
  </div>
</template>

<script>
export default {
  ...
  computed: {
    message() {
      return this.$store.state.message
    }
  }
}
</script>
```
<br>

## <b>actions</b>
- `state`를 변경할 수 있는 `mutations` 호출
- `dispatch(A, B)`
  - A : 호출하고자 하는 `actions` 함수
  - B : 넘겨주는 데이터(payload)
- `actions`의 첫 번째 인자는 `context`
  - `context`는 store의 전반적인 속성을 모두 가지고 있음
  - `context.state`, `context.getters`를 통해 `mutations`를 호출하는 것이 가능
  - `dispatch()`를 사용해 다른 `actions`도 호출 가능
  - `actions`에서 `state`를 직접 조작하는 것은 삼가야 함
- `actions`의 두 번재 인자는 `payload`
  - 넘겨준 데이터를 받아서 사용

```javascript
// store/index.js
...
actions: {
  changeMessage(context, message) {
    context.commit('CHANGE_MESSAGE', message)
  }
},
...
```
```html
<!-- App.vue -->
<template>
  <div id="app">
    <h1>{{ message }} </h1>
    <input type="text" @keyup.enter="changeMessage" v-model='inputData'>
  </div>
</template>

<script>
export default {
  ...
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    }
  },
  computed: {
    message() {
      return this.$store.state.message
    }
  }
}
</script>
```

<br>

## <b>mutations</b>
- actions에서 `commit()`을 통해 mutations 호출
- `commit(A, B)`
  - A: 호출하고자 하는 mutations 함수
  - B: payload
- `mutations` 함수의 인자
  - 첫번째 : `state`
  - 두번째 : `payload`

```javascript
// store/index.js
...
actions: {
  changeMessage(context, message) {
    context.commit('CHANGE_MESSAGE', message)
  }
},
mutations: {
  CHANGE_MESSAGE(state, message) {
    state.message = message
  }
},
...
```
<br>

## <b>getters</b>
- `state`를 활용한 새로운 변수
- `getters`의 두 인자
  - 첫번째 : `state`
  - 두번재 : `getters`
- `state`와 마찬가지로 `computed`에 정의 후 사용을 권장

```javascript
  getters: {
    messageLength(state) {
      return state.message.length
    },
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }
  },
```