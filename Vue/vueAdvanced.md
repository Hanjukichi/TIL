# Local Storage

## <b>상태 유지하기</b>    
- 현재 앱을 재실행하거나, 새로 고침을 하면 초기값으로 돌아감
- 상태를 유지하기위해선 특별한 방법이 필요

<br>

## <b>Window.localStorage</b>
- 브라우저의 내장 객체 중 하나
- Key-Value 형태로 데이터를 저장할 수 있는 저장소
- localSotrage에 저장된 데이터는 브라우저를 종료해도 계속해서 유지됨
  - 다른 탭에서도 동일한 데이터를 공유할 수 있음
  - 다른 도메인에서는 접근 X
  - 보안과 관련된 중요한 정보를 저장하기에는 적합하지 않음

### `setItem(key, value)`
  - key, value 형태로 데이터 저장
  - 데이터 저장시 문자열 형태로 저장됨
### `getItem(key)`
  - key 값으로 저장된 데이터 불러오기

```javascript
// setItem
const numbers = [1, 2, 3]
localStorage.setItem('name','SSAFY')
localStorage.setItem('age',30)
localStorage.setItem('numbers', numbers)

// getItem
const name = localStorage.getItem('name')
const age = localStorage.getItem('age')
const nums = localStorage.getItem('numbers')
```

<br>

##  <b>JSON Method</b> 

### `JSON.stringify`
- JSON 객체의 메서드
- 자바스크립트 객체를 JSON 형식의 문자열로 변환하여 반환

### `JSON.parse`
- JSON 형식의 문자열을 자바스크립트 객체로 변환하여 반환

```javascript
// stringify
const numbers = [1,2,3]
const stringifyNumbers = JSON.stringify(numbers)
localStorage.setItem('numbers', stringifyNumbers)

// parse
const parsedAge = JSON.parse(age)
const parsedNumbers = JSON.parse(numbers)
```

<br><br>

# Plugins

## <b>plugins이란?</b>
- Vuex store에 추가적인 기능을 제공하는 확장 기능
- 일반적으로 state의 변화를 감지해, 어플리케이션의 성능을 최적화하는 목적을 가짐

<br>

## <b>vuex-persistedstate</b>
- Vuex store의 상태를 브라우저 local storage에 저장해주는 plugin
- 페이지를 새로 고침 or 브라우저를 종료 후 다시 열었을 때, 이전 상태를 유지할 수 있도록 해줌
- 설치
```
npm i vuex-persistedstate
```
- 적용
```javascript
import createdPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createdPersistedState
  ],
})
```

<br><br>

# Vuex Binding Helper

## <b>Vuex Binding Helper</b>
- Vuex store의 `state`, `mutations`, `actions` 등을 간단하게 사용할 수 있도록 만들어진 헬퍼 함수
- `mapState`, `mapActions`와 같은 형식으로 사용
- 사용하기 위해서는 import 받아와야 함
```javascript
import {mapState, mapActions, mapGetters} from 'vuex'
```
<br>

## <b>`mapState`</b>
- Vuexs store의 상태를 컴포넌트의 데이터에 매핑할 때 사용
- 객체 혹은 배열 형태로 상태를 매핑하여 사용할 수 있음

### 1 .객체 형태로 매핑
- mapState 내부에 불러오고자 하는 값을 정의
- 화살표 함수를 사용하여 key에 state의 value를 할당
- key값은 컴포넌트에서 사용하고자 하는 다른 이름으로 변경하여 사용할 수 있음
```html
<script>
import { mapState } from 'vuex'

export default {
  ...
  computed: {
    ...mapState({
      msg: state => state.message
    }),
  }
}
</script>
```

### 2. 배열형태로 매핑
- vuex store의 상태 중, 불러오고자 하는 대상을 배열의 원소로 정의
```html
<script>
import { mapState } from 'vuex'

export default {
  ...
  computed: {
    ...mapState(['message']),
  }
}
</script>
```
<br>

## <b>`mapActions`</b>
- 컴포넌트에서 `this.$store.dispathc()`를 호출하는 대신, 액션 메서드를 직접 호출하여 사용할 수 있음
- `mapState`와 같이 객체 혹은 배열 형태로 매핑 가능

### 배열 형태로 매핑
- mapState와 동일한 형식으로 사용
- inputData를 인자로 직접 값을 넘겨주어야함
```html
<template>
  <div id="app">
    ...
    <input type="text" @keyup.enter="changeMessage(inputData)" v-model="inputData">
  </div>
</template>

<script>
export default {
  ...
  methods: {
    ...mapActions(['changeMessage'])
  }
}
</script>
```

### 객체 형태로 매핑
- payload를 넘겨주거나 추가적인 로직 작성 가능
```html
<template>
  <div id="app">
    ...
    <input type="text" @keyup.enter="onSubmit" v-model="inputData">
  </div>
</template>

<script>
export default {
  ...
  methods: {
    ...mapActions({
      actionsChangeMessage: 'changeMessage'
    }),
    onSubmit() {
      const newMessage = this.inputData
      this.actionsChangeMessage(newMessage)
      this.inputData = ''
  }
  },
}
</script>
```
<br>

## <b>`mapGetters`</b>
- mapState, mapActions와 동일한 방식으로 사용 가능
- 상황에 따라서는 배열과 객체 형태로 각각 매핑하여 사용할 수 있음
```html
<script>
export default {
  ...
  computed: {
    ...mapGetters(['messageLength'])
    ...mapstate({
      age: state => state.age
    })
  },
}
</script>
```

<br><br>

# Modules

## <b>Moudles란?</b>
- Vuex store를 여러 파일로 나눠서 관리할 수 있게 해주는 기능
- Vuex store와 동일한 구성을 가진 별도의 객체를 정의하여 modules 옵션에 작성한 객체를 추가하여 사용
- 별개의 .js 파일에 정의하고 import 하는 방식으로도 사용 가능
- Store의 가독성을 향상시킬 수 있음

```js
// store/modules.myModules.js
const myModule = {
  state:{
    level:20,
  },
  mutations: {
    INCREMENT_LEVEL(state) {
      state.level += 1
    }
  },
  actions: {
    incrementLevel(context) {
      context.commit(INCREMENT_LEVEL)
    }
  }
}
export default myModule


// index.js
import myModule from './modules/MyModules'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    myModule
  },
  ...
})
```
