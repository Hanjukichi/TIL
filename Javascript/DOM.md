# DOM 개요

## <b>Javascript의 다양한 기능</b>
<br>

### 1. 브라우저에서의 JavaScript
- Javascript는 웹 페이지에서 다양한 기능을 구현하는 스크립트 언어
- 정적인 정보만 부여주던 웹페이지를 데이터가 주기적으로 갱신
- 사용자와 상호작용
- 애니메이션 등이 동작

#### 스크립트 언어
- 기존 존재하는 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어

<br>

### 2. 웹페이지에서의 Javascript
- 클라이언트 사이드 Javascript 언어 위에 올라가있는 기능들이 다양함
- API라고 부르는 이 기능들은 Javascript의 기능들을 더 무궁무진하게 만들어줌
- API의 두 가지 범주
  - Browser APIs
  - Third party APIs

<br><br>

## <b>Browser APIs
<br>

### 1. Browser APIs란?
- 웹 브라우저에 내장된 API
- 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터 제공, 오디오 재생 등 많은 일을 수행하게 함
- Javascript로 Browser API들을 사용해서 여러가지 기능 사용
- 종류
  - DOM
  - Geolocation API
  - WebGL

<br>

### 2. 브라우저가 웹페이지를 불러오는 과정
- 웹페이지를 브라우저로 불러오면, 브라우저는 코드를 실행 환경에서 실행
- Javascript는 DOM API를 통해 HTML과 CSS를 동적으로 수정
- 사용자 인터페이스를 업데이트하는 일에 가장 많이 쓰임

<br><br>

## <b>DOM이란?</b>
<br>

### 문서 객체 모델
- Document Object Model
- 문서의 구조화된 표현을 제공, 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
  - 문서 구조, 스타일, 내용등을 쉽게 변경할 수 있게 도움
  - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일 추가
- HTML 문서를 구조화하여 각 요소를 객체로 취급
- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작이 가능

<br>

### 논리 트리
- DOM은 문서를 논리 트리로 표현
- DOM 메서드를 사용하면 프로그래밍적 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음

<br>

### DOM 특성
- 웹페이지는 일종의 문서
- 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
- DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
- Dom은 웹페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정 가능

<br><br>

---
# DOM 기본 구조

## <b>DOM의 기본 구성</b>
<br>

### 1. DOM Tree
- DOM은 문서를 논리 트리로 표현
- DOM에서 모든 것은 Node
- 각 노드는 부모, 자식 관계를 형성하고 이에 따라 상속 개념도 동일하게 적용

<br>

### 2. Node
- DOM의 구성 요소 중 하나
- HTML 문서의 모든 요소를 나타냄
  - 각각의 HTML 요소는 DOM Node로서 특정한 노드 타입을 가짐
  - Document Node : HTML 문서 전체를 나타내는 노드
  - Element Node : HTML 요소를 나타내는 노드
  - Text Node :  HTML 텍스트, Element Node 내의 텍스트 컨텐츠를 나타냄
  - Attribute Node : HTML 요소의 속성을 나타내는 노드
  
<br>

### 3. DOM에 접근하기
- DOM을 사용하기 위해 특별히 해야할 일은 없음
- 모든 웹 브라우저는 스크립트 언어가 손쉽게 웹페이지의 요소에 접근할 수 있도록 만들기 위해 DOM 구조를 항상 사용
- 우리는 DOM의 주요 객체들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음

<br><br>

## <b>DOM의 주요 객체</b>
<br>

### 1. `window`
- DOM을 표현하는 창
- 가장 최상위 객체(작성 시 생략 가능)
- 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄

```javascript
// 새 탭 열기
window.open()

// 경고 대화 상자 표시
window.alert()

// 인쇄 대화 상자 표시
window.print()
```
<br>

### 2. `document`
- 브라우저가 불러온 웹페이지
- 페이지 컨텐츠의 진입점 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함하고 있음
- document는 window의 속성이다.
```javascript
// 문서 제목 바꾸기
document.title = 'Javascript'
```
<br>

### 3. Node vs Element
- HTML 문서의 모든 것은 Node
- `<head>`, `<body>`는 HTML요소로 element
- `<title>`, `<p>`는 Text Node이면서 element
- `id="unique"`는 DOM에서는 Attr Node이고, HTML 요소인 `<p>`의 속성이므로 element는 아님

<br><br>

---
# DOM 조작

## <b>선택 관련 메서드</b>
<br>

### 1. `document.querySelector(selector)`
- 제공한 선택자와 일치하는 element 한 개 선택
- 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)
```javascript
document.querySelector('#title')
```
<br>

### 2. `document.querySelectorAll(selector)`
- 제공한 선택자와 일치하는 여러 element를 선택
- 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자로 받음
- 제공한 CSS selector를 만족하는 NodeList를 반환
```javascript
document.querySelectorAll('.text')
```
<br>

### 3. Nodelist
- DOM 메서드를 사용해 선택한 노드의 목록
- 배열과 유사한 구조를 가짐
- Index로만 각 항목에 접근 가능
- 배열의 `forEach` 메서드 및 다양한 메서드 사용 가능
- `querySelectorAll()`에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간을 반영하지 않음
  
<br><br>

## <b>조작 관련 메서드</b>
<br>

### 1. `documnet.createElement(tagName)`
- 작성한 tagName의 HTML 요소를 생성하여 반환
```javascript
const title = document.createElement('h1')
```
<br>

### 2. `HTMLElement.innerText`
- Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현
- 사람이 읽을 수 있는 요소만 남김
- 줄바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨
```javascript
title.innerText = 'DOM 조작'
```
<br>

### 3. `Node.appendChild()`
- 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
- 한 번에 오직 하나의 Node만 추가 가능
- 추가된 Node 객체를 반환
- 새롭게 생성한 Node가 아닌 이미 문서에 존재하는 Node를 다른 Node의 자식으로 삽입하는 경우 위치를 이동
```javascript
div.appendChild(title)
```
<br>

### 4. `Node.removeChild()`
- DOM에서 자식 Node를 제거
- 제거된 Node를 반환
```javascript
div.removeChild(title)
```
<br><br>

## <b>속성 조회 및 설정</b>
<br>

### 1. `Element.getAttribute(attributeName)`
- 해당 요소의 지정된 값을 반환
- 인자는 값을 얻고자 하는 속성의 이름

<br>

### 2. `Element.setAttribute(name, value)`
- 지정된 요소의 값을 설정
- 속성이 이미 존재하면 값을 갱신
- 존재하지 않으며 지정된 이름과 값으로 새 속성을 추가
```javascript
aTag.setAttribute('href', 'https://google.com')
```

### 3. 해당 요소 속성들의 집접적 제어
- `Element.classList`
- `Element.style`
```javascript
// 클래스 삭제
h1.classList.remove('red')

// 클래스 추가
h1.classList.add('blue')

// 클래스 on/off
h1.classList.toggle('red')
```