# Data in Component

## <b>컴포넌트간 데이터 통신</b>
- 필요한 컴포넌트들끼리 데이터를 주고 받게될 경우
  - 데이터의 흐름을 파악하기 힘듦
  - 개발 속도 저하
  - 유지 보수 난이도 증가
- 부모-자식 관계만 데이터를 주고받음
  - 데이터의 흐름을 파악하기 용이
  - 유지 보수하기 쉬워짐

<br>

## <b>pass props & emit event</b>
- 부모 -> 자식으로의 데이터의 흐름
  - pass props의 방식
- 자식 -> 부모로의 데이터의 흐름
  - emit event의 방식

<br><br>

# Pass Props

## <b>Pass Props란?</b> 

```html
<!-- HelloWorld.vue -->
<div class="hello">
    <h1>{{ msg }}</h1>
</div>
<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- App.vue -->
<div id="app">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</div>
```
- 요소의 속성을 사용하여 데이터 전달
- props는 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 요소에 속성을 작성하듯이 사용 가능, `prop-data-name="value"`형태로 데이터 전달
  - 이 때 속성의 키 값은 kebab-case를 사용
- 하위 컴포넌트에서도 props에 대해 명시적으로 작성해주어야 함
- 전달받은 props를 type과 함께 명시
- 잘못된 타입이 전달되는 경우 브라우저의 자바스크립트콘솔에서 사용자에게 경고

<br>

## <b>Pass Props convention</b>
- 부모에서 넘겨주는 props
  - kebab-case : HTML 속성명은 대소문자를 구분하지 않음
- 자식에서 받는 props
  - camelCase
- 자식의 스크립트에서 자동으로 camelCae로 변환하여 인식

<br>

## <b>Dynamic props</b>
```html
<!-- MyComponent.vue -->
<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild
    static-props="component에서 child로"
    :dynamic-props="dynamicProps"
    />
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  data: function() {
    return {
      dynamicProps: "It's in data"
    }
  },
  components: {
    MyChild,
  }
</script>


<!-- MyChild.vue -->
<template>
  <div>
    <h3>This is child component</h3>
    <p>{{staticProps}}</p>
    <p>{{dynamicProps}}</p>
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  props: {
    staticProps: String,
    dynamicProps: String,
  }
}
```
- 변수를 props로 전달할 수 있음
- v-bind directive를 사용해 데이터를 동적을 바인딩
- 부모 컴포넌트의 데이터가 업데이트되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트

<br>

## <b>컴포넌트의 data 함수</b>
```javascript
data: function() {
  return {
    dynamicProps: "It's in data"
  }
},
```
- 각 vue 인스턴스는 같은 data 객체를 공유
- 새로운 data 객체를 반환(`return`)하여 사용해야함

<br>
 
## <b>단방향 데이터 흐름</b> 
- 모든 props는 부모에서 자식으로 즉 아래로 단방향 바인딩을 형성
- 부모 속성이 업데이트되면 자식으로 흐르지만 반대 방향은 아님
  - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신값으로 새로고침

### 목적
- 하위 컴포넌트가 상위 컴포넌트 상태를 변경, 데이터 흐름이 복잡해지는 걸 방지
- 하위 컴포넌트에서 prop를 변경하려고 시도해서는 안 됨
- 위의 경우 Vue는 콘소에서 경고를 출력

<br><br>

# Emit Event

## <b>Emit Event란?</b>
```html
<!-- MyChild.vue -->
<template>
  <div>
    <button @click="ChildToParent">클릭!</button>
  </div>
</template>

<script>
export default {
  ...
  methods: {
    ChildToParent() {
      this.$emit('child-to-parent')
    }
  }
}
</script>


<!-- MyComponent.html -->
<template>
  <div class="border">
    <MyChild
    ...
    @child-to-parent="parentGetEvent"
    />
  </div>
</template>

<script>
  ...
  methods: {
    parentGetEvent() {
      console.log("자식 컴포넌트에서 발생한 이벤트!")
    }
  }
}
</script>
```
- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트를 발생
- 이벤트 발생으로 데이터를 전달하는 방법
  - 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
  - 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음
- `$emit` 메서드를 통해 부모 컴포넌트에 이벤트 발생
  - `$emit('event-name')`형식으로 사용
  - 부모 컴포넌트에 event-name이라는 이벤트가 발생했다는 것을 알림

### ※ `$`
- javascript는 변수에 `_`, `$` 두 개의 특수문자를 사용 가능
- vue는 `$emit`을 이벤트 전달을 위한 방식으로 채택
- 기존에 사용하던 벼누, 메서드들과 겹치지 않게 하기 위함

<br>

## <b>Emit with Data</b>
```html
<!-- MyChild.vue -->
<template>
  <div>
    ...
    <button @click="ChildToParent">클릭!</button>
  </div>
</template>

<script>
export default {
  ...
  methods: {
    ChildToParent() {
      this.$emit('child-to-parent', 'child data')
    },
  }
}
</script>

<!-- MyComponent.vue -->
<template>
    ...
    @child-to-parent="parentGetEvent"
    />
  </div>
</template>

<script>
export default {
  ...
  methods: {
    parentGetEvent(inputData) {
      console.log("자식 컴포넌트에서 발생한 이벤트!")
      console.log(`하위 컴포넌트에서 ${inputData}를 받음`)
    }
  }
}
</script>
```
- 이벤트를 발생시킬 때 인자로 데이터를 전달 가능
- 이렇게 전달한 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러 함수의 인자로 사용 가능
- pass props와 마찬가지로 동적인 데이터도 전달 가능

<br>

## <b>Emit with dynamic Data</b>
```html
<!-- MyChild.vue -->
<template>
  <div>
    ...
    <input type="text" v-model="childinputData" @keyup.enter="ChildInput">
  </div>
</template>

<script>
export default {
  ...
  data: function() {
    return {
      childinputData: null
    }
  },
  methods: {
    ChildInput() {
      this.$emit('child-input', this.childinputData)
      this.childinputData = ""
    }
  }
}
</script>


<!-- MyComponent.html -->
<template>
  <div class="border">
    <MyChild
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
export default {
  ...
  methods: {
    getDynamicData(inputData){
      console.log(`하위 컴포넌트에서 ${inputData}를 받음`)
    }
  }
}
</script>
```
- pass props와 마찬가지로 동적인 데이터도 전달 가능

<br>

## <b>pass props / emit event 컨밴션</b>
- kebab-case와 camelCase
  - HTML 요소 : kebab-cae
  - JavaScript : camelCase
- props
  - 상위 => 하위에서 HTML요소로 내려줌 : kebab-case
  - 하위에서 받을 때 JavaScript에서 받음 : camelCase
- emit
  - emit 이벤트를 발생, HTML 요소가 이벤트를 청취 : kebab-case
  - 메서드, 변수명 등은 JavaScript에서 사용 : camelCase

<br><br>

# Lifecycle Hooks

## <b>Lifecycle Hooks란?</b>
- 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
- 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
- 이를 Lifecycle Hooks라고 함

<br>

## <b>created</b>
```javascript
export default {
  ...
  created() {
    this.getDogImage()
    console.log('Dog created!')
  },
}
```
- Vue instance가 생성된 후 호출됨
- data, computed 등의 설정이 완료된 상태
- 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합
- 단, mount되지 않아 요소에 접근할 수 없음

<br>

## <b>mounted</b>
```javascript
export default {
  ...
  mounted() {
    console.log('Dog mounted!')
    const button = document.querySelector('button')
    button.innerText = '멍멍!'
  },
}
```
- Vue instance가 요소에 mount된 후 호출됨
- mount된 요소를 조작할 수 있음

<br>

## <b>updated</b>
```javascript
export default {
  ...
  updated() {
    console.log('새로운 멍멍이!')
    console.log('Dog updated!')
  }
}
```
- 데이터가 변경되어 DOM에 변화를 줄 때 호출됨

<br>

## <b>Lifecycle Hooks 특징</b>
- instance마다 각각의 Lifecycle을 가지고 있음
- 컴포넌트별로 정의 가능
- 부모 컴포넌트 mount != 자식 컴포넌트 mount
- 부모 컴포넌트 update != 자식 컴포넌트 update
