# Front-end Development

## <b>개요</b>

### Front-end Development란?
- Front-end 개발은 Web App 또는 Web site의 UI/UX를 제작하고 관리하는 과정
- Front-end 프레임워크와 라이브러리를 사용하여 개발효율성을 높이고, Web App의 복잡성을 관리
- Front-end 개발에 사용되는 주요 기술은 HTML, CSS, JavaScript

### Web App이란?
- 웹브라우저에서 실행되는 어플리케이션 소프트웨어
- 개발자 도구 > 디바이스 모드
- 웹페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보이는 것
- 웹페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태

### SPA(Single Page Application)
- Web App가 함께 자주 등장할 용어 SPA
- 이전까지는 사용자의 요청에 대해 적절한 페이지 별 template을 반환
- SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
  - 어떻게 한 페이지로 모든 요청에 대응할 수 있을까?
  - CSR(Client Side Rendering) 방식으로 요청을 처리하기 때문
  
<br>

## <b>CSR</b>

### CSR이란?
```javascript
axios.get(
  HOST_URL,
  {
    header:{
      Authorization: `Token ${key}`
    }
  }
)
  .then(res => {
    this.todos = res.data
  })
  .catch(err => console.log(err))
```

- 최초 한 장의 HTML을 받아오는 것은 동일
  - 단, Server로부터 최초로 받아오는 건 빈 html문서
- 각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링
  - 필요한 페이지를 서버에 AJAX로 요청
  - 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
  - JSON 데이터를 JavaScript로 처리, DOM 트리에 반영(렌더링)

### Why CSR?
- 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨
  - 트래픽 감소로 인해 응답 속도가 빨라짐
- 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행
  - 요청이 자연스럽게 진행 되면서 UX 향상
- BE와 FE의 작업 영역을 명확히 분리할 수 있음
  - 협업이 용이해짐 

### CSR의 단점
- 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요
- 모바일에 설치된 Web-App을 실행하게 되면 잠깐의 로딩 시간이 필요
- 검색 엔진 최적화가 어려움
  - 서버가 제공하는 것은 텅 빈 HTML
  - 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트가 진행
- 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움
  
<br>

## <b>SSR</b>

### SSR이란?
```javascript
{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="수정">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```
- 기존 요청 처리 방식은 SSR
- Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
- 전달받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

### SSR vs CSR
- CSR가과 SSR은 흑과 백이 아님
  - 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
- SPA 서비스에서도 SSR을 지원하는 Framework이 발전하고 있음
  - Vue의 Nuxt.js
  - React의 Next.js
  - Angular Universal 등

<br><br>

# Vue란?

## <b>Why Vue?</b>
- 쉬움
- 타 Framework에 비해 입문자가 시작하기에 좋은 Framework
- 구조가 매우 직관적

### Vue의 기본구조
```html
<template>
  <!-- HTML -->
  <div>
    <p>Hello :)</p>
  </div>
</template>

<script>
  // JavaScript
</script>

<style>
  /* CSS */
  p {
    color: black;
  }
</style>
```

<br>

## <b>Vue로 코드 작성하기</b>
```html
  <div id="app">
    <p id="name">name : {{message}}</p>
    <input id="inputName" type="text" v-model="message">
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    // CODE HERE
    const app = new Vue({
      el: '#app',
      data: {
        message: '',
      }
    })
```
- Vue CDN 가져오기
- Vue instance 생성
  - Vue instance - 1개의 Object
  - 미리 정해진 속성명을 가진 Object
- `el`, `data` 설정
  - data에 관리할 속성 정의
- 선언적 렌더링 `{{}}`
  - Vue data를 화면에 렌더링
- input tag에 `v-model` 작성
  - input에 값 입력 > Vue data 반영
  - Vue data > DOM 반영

<br>

## <b>Vue3 vs Vue2</b>

### Vue3
- 2022년 02월부터 Vue 프레임워크의 기본 버전이 3버전으로 전환
- 대체적인 설정들이 Vue3을 기본으로 적용되어 있음

### Vue2
- 여전히 Vue2가 많이 사용됨
- 사용된 기간이 긴 만큼 상대적으로 많은 문서의 양, 참고자료, 질문/답변

<br></br>

# Vue instance

## <b>MVVM Pattern</b>
- MVE 패턴에서 Controller를 제외하고 View Model을 넣은 패턴
- 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발을 Back-end(model)로부터 분리시킴
- view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함

### View
- 우리 눈에 보이는 부분
- DOM

### Model
- 실제 데이터
- JSON

### View Model(Vue)
- View를 위한 Model
- View와 연결되어 Action을 주고 받음
- Model이 변경되면 View Model도 변경되고 연결된 View도 변경됨
- View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 연결된 다른 View도 변경

<br>

## <b>Vue Instance</b>
```html
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const vm = new Vue()
  console.log(vm)
</script>
```
- Vue CDN 가져오기
- `new` 연산자를 사용한 생성자 함수 호출
  - vue instance 생성
- vue instance === 1개의 객체
- 아주 많은 속성과 메서드를 이미 가지고 있고, 이러한 기능들을 사용하는 것

<br>

## <b>El (element)</b>
```html
<div id="app">
  {{message}}
</div>
<div>
  {{message}}
</div>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app'
  })
  console.log(app)
</script>
```
- Vue instance와 DOM을 mount(연결)하는 옵션
  - View와 Model을 연결하는 역할
  - HTML id 혹은 class와 마운트 가능
- Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음
  - Vue 속성 및 메서드 사용 불가
- 두 div의 차이점
  - `message` 속성이 정의되지 않았다는 경고
  - `{{message}}`가 그대로 출력

<br>

## <b>Data</b>
```html
<div id="app">
  {{message}}
</div>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      message: 'Hello, Vue!'
    }
  })
  console.log(app)
</script>
```
- Vue instance의 데이터 객체 혹은 인스턴스 속성
- 데이터 객체는 반드시 기본 객체 `{}`여야 함
- 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
- 정의된 속성은 `interplation {{}}`을 통해 view에 렌더링 가능
- 추가된 객체의 각 값들은 `this.message`형태로 접근 가능

<br>

## <b>Methods</b>
```html
<div id="app">
  {{message}}
</div>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
const app = new Vue({
  el: '#app',
  data: {
    message: 'Hello, Vue!'
  },
  methods : {
    print: function () {
      console.log(this.message)
    },
    bye: function () {
      this.message = 'Bye, Vue!'
    }
  }
})
console.log(app)
```
- Vue instance의 method들을 정의하는 곳
- method를 호출하여 data 변경 가능
- 메서드를 정의할 때 Arrow Function 사용 X
  - this가 함수가 선언될 때 상위 스코프를 가리킴
  - 호출은 문제없이 가능하나 this로 Vue data 변경 불가