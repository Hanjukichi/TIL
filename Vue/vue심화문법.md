# Basic of stntax

## <b>Template Syntax</b> 
- 렌더링된 DOM을 기본 Vue instance의 data에 선언적으로 바인딩할 수 있는 HTML 기반 template syntax를 사용
  - 렝더링 된 DOM : 브라우저에 의해 보기좋게 그려질 HTML 코드
  - HTML 기반 template syntax : HTML 코드에 직접 작성할 수 있는 문법 제공
  - 선언적으로 바인딩 : Vue instance와 DOM을 연결

<br>

## <b>Text Interpolation</b>
- 가장 기본적인 바인딩 방법
- 중괄호 2개로 표기
- DTL과 동일한 형태로 작성
- Text interpolation 방법은 모두 일반 텍스트로 표현
```html
<div id="app">
  <p>메시지: {{ msg }}</p>   
  <p>HTML 메시지 : {{ rawHTML }}</p>
</div>
<script>
  const app = new Vue({
    el : '#app',
    data: {
      msg: 'Text interpolation',
      rawHTML: '<span style="cololr:red">빨간 글씨</span>'
    }
   })
</script>
```
<br>

## <b>Raw HTML</b>
- v-html directive을 사용하여 data와 바인딩
- directive -HTML 기반 template syntax
- HTML의 기본 속성이 아닌 Vue가 제공하는 특수 속성의 값으로 data 작성
```html
<div id="app">
  <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
</div>
<script>
  const app = new Vue({
    el : '#app',
    data: {
      msg: 'Text interpolation',
      rawHTML: '<span style="cololr:red">빨간 글씨</span>'
    }
   })
</script>
```
<br><br>

# Directives

## <b>Directives 기본 구성</b>
- v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음
  - 값에는 JS 표현식을 작성할 수 있음
- directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것

`v-on:submit.prevent="onSubmit`
- `:`을 통해 전달인자를 받을 수 있음
- `.`으로 표시되는 특시 접미사 -directvie를 특별한 방법으로 바인딩

```html
<div id="app2">
  <p v-text="message"></p>
  <!-- 같음 -->
  <p>{{ message }}</p>
</div>
<script>
  const app2 = new Vue({
    el: '#app2',
    data: {
      message: 'Hello!'
    }
  })
</script>
```
<br>

## <b>`v-html`</b> 
- Raw HTML을 표현할 수 있는 방법
- 단 사용자가 입력하거나 제공하는 컨텐츠에는 절대사용 금지
  - 보안상의 문제
  
```html
<div id="app2">
  <p v-html="html"></p>
</div>
<script>
  const app2 = new Vue({
    el: '#app2',
    data: {
      html: '<a href="https://www.google.com">Google</a>'
    }
  })
</script>
```
<br>

## <b>`v-show` vs `v-if`</b>

```html
<div id="app3">
  <!-- 존재하지만 안 보임 -->
  <p v-show="isActive">보이니? 안보이니?</p>
  <!-- 존재하지 않음 -->
  <p v-if="isActive">안보이니? 보이니?</p>
</div>
<script>
  const app3 = new Vue({
    el: '#app3',
    data: {
      inActive: false,
    }
  })
</script>
```

### `v-show`
- 표현식에 작성된 값에 따라 element를 보여줄 것인지 결정
  - boolean 값이 변경될 때마다 반응
- 대상 element의 display 속성을 기본 속성과 none으로 toggle
- 요소 자체는 항상 DOM에 렌더링됨
- 초기 렌더링에 필요한 비용은 v-if보다 높을 수 있음
- display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음

## `v-if`
- v-show와 사용 방법은 동일
- isActive의 값이 변경될 때 반응
- 단, 값이 false인 경우 DOM에서 사라짐
- v-if v-else-if v-else 형태로 사용
- 초기 렌더링 비용은 v-show 보다 낮을 수 있음
- 단, 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용 증가 가능

<br>

## <b>`v-for`</b>
- `for .. in ..`형식으로 작성
- 반복한 데이터타입에 모두 사용 가능
- index를 함께 출력하고자 한다면 (char, index) 형태로 사용 가능
- 배열 역시 문자열과 동일하게 사용 가능
- 각 요소가 객체라면 dot notation으로 접근할 수 있음

### [참고] 특수 속성 key
- `v-for` 사용 시 반드시 key 속성을 각 요소에 작성
- 주로 `v-for` directive 작성시 사용
- vue 화면 구성시 이전과 달라진 점을 확인하는 용도로 활용
  - 따라서 key가 중복되어서는 안 됨
- 각 요소가 고유한 값을 가지고 있다면 생략할 수 있음

```html
<!-- 3. v-for -->
<div id="app">
  <h2>1. String</h2>
  <div v-for="char in myStr">
    {{ char }}
  </div>
  <div v-for="(char, index) in myStr" :key="index">
    <p>{{ index }}번째 문자열 {{ char }}</p>
  </div>

  <h2>2. Array</h2>
  <div v-for="(item, index) in myArr" :key="`ssafy-${index}`">
    <p>{{ index }}번째 아이템 {{ item }}</p>
  </div>

  <div v-for="(item, index) in myArr2" :key="`arry-${index}`">
    <p>{{ index }}번째 아이템</p>
    <p>{{ item.name }}</p>
  </div>

  <h2>3. Object</h2>
  <div v-for="value in myObj">
    <p>{{ value }}</p>
  </div>

  <div v-for="(value, key) in myObj" :key="key">
    <p>{{ key }} : {{ value }}</p>
  </div>
</div>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      // 1. String
      myStr: 'Hello, World!',

      // 2-1. Array
      myArr: ['python', 'django', 'vue.js'],

      // 2-2. Array with Object
      myArr2: [
        { id: 1, name: 'python', completed: true},
        { id: 2, name: 'django', completed: true},
        { id: 3, name: 'vue.js', completed: false},
      ],
      
      // 3. Object
      myObj: {
        name: 'harry',
        age: 27
      },
    }
  })
</script>
```
<br>

## <b>`v-on`</b>
- `:`을 통해 전달받은 인자를 확인
- 값으로 JS 표현식 작성
- `addEventListener`의 첫 번째 인자와 동일한 값들로 구성
- 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행
- method를 통한 data 조작도 가능
- 일반 함수를 호출할 때와 동일하게 method에 인자를 넘김
- `:`를 통해 전달된 인자에 따라 특별한 modifiers가 있을 수 있음
  - ex) `v-on:keyup.enter` 등
- `@` shortcut 제공
  - ex) `@keyup.click`

```html
<div id="app">
  <button v-on:click="number++">increase Number</button>
  <p>{{ number }}</p>

  <button v-on:click="toggleActive">toggle isActive</button>
  <p>{{ isActive }}</p>

  <button @click="checkActive(isActive)">check isActive</button>
</div>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      number: 0,
      isActive: false,
    },
    methods: {
      toggleActive: function () {
        this.isActive = !this.isActive
      },

      checkActive: function (check) {
        console.log(check)
      }
    }
  })
</script>
```

<br>

## <b>`v-bind`</b>
- HTML 기본 속성에 Vue data를 연결
- class의 경우 다양한 형태로 연결 가능
- 조건부 바인딩
  - `{classname: '조건 표현식'}`
  - 삼항 연산자도 가능
- 다중 바인딩
  - `['js표현식','js표현식']`
- Vue data의 변화에 반응하여 DOM에 반영하므로 상황에 따라 유동적 할당 가능
- `:` shortcut 제공

```html
<div id="app2">
  <a v-bind:href="url">Go To Naver</a>
  <a :href="url">Go To Naver</a>
  <p :class="redText">Red</p>
  <p :class="{'red-text': true}">Red</p>
  <p :class="[redText, borderBlack]">Red</p>
</div>
<script>
  const app2 = new Vue({
    el: '#app2',
    data: {
      url: 'https://www.naver.com/',
      redText: 'red-text',
      borderBlack: 'border-black',
      darkMode: 'dark-mode',
      whiteMode: 'white-mode'
    }
  })
</script>
```

<br>

## <b>`v-model`</b>
- Vue instance와 DOM의 양방향 바인딩
- Vue data 변경 시 `v-model`로 연결된 사용자 입력 element에도 적용

```html
<div id="app">
  <h2>2. Input <-> Data</h2>
  <h3>{{ myMessage }}</h3>
  <input v-model="myMessage" type="text">
  <hr>
</div>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      myMessage: '',
    },
  })
</script>
```

<br><br>

# Vue advanced

## <b>`computed`</b>
- Vue instance가 가진 options 중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
  - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을 반환

### `methods`
- 호출될 때마다 함수를 실행
- 같은 결과여도 매번 새롭게 계산

### `computed`
- 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
- 종속 대상이 변하지 않으면 항상 저장된 값을 반환

```html
<div id="app">
  <h1>data_01 : {{ number1 }}</h1>
  <h1>data_02 : {{ number2 }}</h1>
  <!-- 함수를 호출할 때마다 계산 -->
  <h1>add_method : {{ add_method() }}</h1>
  <h1>add_method : {{ add_method() }}</h1>
  <!-- 변수가 변하지 않는 한 한 번만 계산 -->
  <h1>add_computed : {{ add_computed }}</h1>
  <h1>add_computed : {{ add_computed }}</h1>
  <button v-on:click="dataChange">Change Data</button>
</div>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      number1: 100,
      number2: 100
    },
    computed: {
      add_computed: function () {
        console.log('computed 실행됨!')
        return this.number1 + this.number2
      },
    },
    methods: {
      add_method: function () {
        console.log('method 실행됨!')
        return this.number1 + this.number2
      },
      dataChange: function () {
        this.number1 = 200
        this.number2 = 300
      },
    }
  })
</script>
```
<br>

## <b>`watch`</b>
- 특정 데이터의 변화를 감지하는 기능
  - watch 객체를 정의
  - 감시할 대상 data를 지정
  - data가 변할 시 실행할 함수를 정의
- 첫 번째 인자는 변동 후 data
- 두 번째 인자는 변동 전 data
- 실행 함수를 Vue method로 대체 가능
  - 감시 대상 data의 이름으로 객체 생성
  - 실행하고자 하는 method를 handler에 문자열 형태로 할당
- Array, Object의 내부 요소 변경을 감지를 위해서는 `deep` 속성 추가 필요

```html
<div id="app">
  <p>{{ number }}</p>
  <button @click="number++">+</button>  

  <p>{{ name }}</p>
  <input type="text" v-model="name">

  <p>{{ myObj }}</p>
  <button @click="itemChange">change Item</button>
</div>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      number: 0,
      name: '',
      myObj: {completed: true}
    },
    methods: {
      nameChange: function () {
        console.log('name is changed')
      },
      itemChange: function () {
        this.myObj.completed = !this.myObj.completed
      }
    },

    watch: {
      number: function (val, oldVal) {
        console.log(val, oldVal)
      },
      name: {
        handler: 'nameChange'
      },
      myObj: {
        handler: function (val) {
          console.log(val)
        },
        deep: true
      },
    }
  })
</script>
```
<br>

## <b>`filters`</b>
- 텍스트 형식화를 적용할 수 있는 필터
- interpolation 혹은 v-bind를 이용할 때 사용 가능
- 필터는 자바스크립트 표현식 마지막에 `|`와 함께 추가되어야 함
- 이어서 사용 가능

```html
<div id="app">
  <p>{{ numbers | getOddNums}}</p>
</div>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    },
    filters: {
      getOddNums: function (nums) {
        const oddNums = nums.filter((num) => {
          return num % 2
        })
        return oddNums
      },
    }
  })
</script>
```
