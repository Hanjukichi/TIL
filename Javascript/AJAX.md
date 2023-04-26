# AJAX 개요

## AJAX란?
- Asynchronous javascript And XML(비동기식 JavaScript와 XML)
- 비동기 통신을 이용하면 화면 전체를 새로고침 하지 않아도 됨
- 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능
- 이러한 '비동기 통신 웹 개발 기술'을 AJAX라고 함
- 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios

<br>

## AJAX 특징
- 페이지 전체를 reload(새로 고침)을 하지 않고서도 수행되는 "비동기성"
- 서버의 응답에 따라 전체 페이지가 아닌 일부분만을 업데이트 할 수 있음
  - 페이지 새로고침 없이 서버에 요청
  - 서버로부터 응답을 받아 작업을 수행

<br><br>

# 비동기 적용하기

## `data-*` attributes
- 사용자 지정 데이터특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환할 수 있는 방법
- 모든 사용자 지정 데이터는 dataset 속성을 통해 사용할 수 있음
- 만약 `data-test-value`라는 이름의 특성을 지정했다면 `element.dataset.testValue`로 접근할 수 있음
- 속성명 작성시 주의 사항
  - 대소문자 여부에 상관없이 xml로 시작하면 안 됨
  - 세미콜론을 포함해서는 안 됨
  - 대문자를 포함해서는 안됨
```javascript
<div data-my-id="my-data"></div>
<script>
  const myId = event.target.dataset.myId
</script>
```

<br>

## XHR
- "XMLHttpRequest"
- AJAX 요청을 생성하는 JavaScript API
- XHR의 메서드로 브라우저와 서버간 네트워크 요청을 전송할 수 있음
- Axios는 손쉽게 XHR을 보내고 응답결과를 Promise 객체로 반환해주는 라이브러리