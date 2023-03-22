# 인증과 권한 이해하기
<br>

## <b>Ⅰ. 인증과 권한</b>

---
<br>

### <b>ⅰ. 개요</b>
<br>

Django authentication system(인증 시스템)의 구성
- 인증(Authentication)
- 권한(Authorization)

세팅에서의 필수 구성
- `INSTALLED_APPS`의 `django.contrib.auth`
  
Authentication(인증)
- 신원확인
- 사용자가 자신이 누구인지 확인하는 것

Authorization(권한, 허가)
- 권한 부여
- 인증된 사용자가 수행할 수 있는 작업을 결정

<br><br>

## <b>Ⅱ. Custom User Model</b>

---
<br>

### <b>ⅰ. 개요</b>
<br>

Djnago는 기본적인 인증 시스템과 User Model을 제공
- 대부분 개발 환경에선 Custom User Model로 대체
- 일부 프로젝트에선 빌트 인 User Model의 기본 인증 요구 사항 적절 X

`AUTH_USER_MODEL`
- 현재 프로젝트에서 사용할 User Model
- Default User Model을 재정의 가능

<br>

### <b>ⅱ. `AUTH_USER_MODEL`</b>
<br>

프로젝트에서 User를 나타낼 때 사용하는 모델

프로젝트가 진행되는 동안 변경할 수 없음

프로젝트 시작 시 설정하기 위한 것
- 첫번째 마이그레이션 전에 확정 지어야 함

기본값
- `AUTH_USER_MODEL = 'auth.User'`

<br>

### <b>ⅲ. User Model의 대체 </b>
<br>

#### <b> 1. 대체하기</b>


`AbstractUser`를 상속받는 커스텀 User 클래스 작성
- 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습
  
>```python
>from django.db import models
>from django.contrib.auth.models import AbstractUser
>
>class User(AbstractUser):
>    pass
>

Django 프로젝트에서 User 나타내는데 사용하는 모델을 방금 생성한 커스텀 User 모델로 지정
  
>```python
>AUTH_USER_MODEL = 'accounts.User'
>```

admin.py에 커스텀 User 모델을 등록
- 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

>```python
>from django.contrib import admin
>from django.contrib.auth.admin import UserAdmin
>from .models import User
>
>admin.site.register(User, UserAdmin)
>```
<br>

#### <b> 2. 데이터베이스 초기화</b>

1. migrations 파일 삭제
   - migrations 폴더 및 __init__.py는 삭제 X
   - 번호가 붙은 파일만 삭제
2. db.sqlite3 삭제
3. migrations 진행
    - makemigrations
    - migrate

<br><br>

## <b>Ⅲ. HTTP</b>

---
<br>

### <b>ⅰ. HTTP 특징</b>
<br>

#### 1. 비 연결 지향
- 서버는 요청에 대한 응답을 보낸 후 연결을 끊음

#### 2. 무상태
- 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
- 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

<br>

### <b>ⅱ. 로그인 상태 유지하는 방법</b>
<br>

우리가 로그인을 하고 웹 사이트를 사용할 때 페이지를 이동해도 로그인 "상태"가 유지

서버와 클라이언트 간 지속적인 상태 유지를 위해 "쿠키와 세션"이 존재

<br><br>

## <b>Ⅳ. 쿠키와 세션</b>

---
<br>

### <b>ⅰ. 쿠키란?</b>
<br>

서버가 사용자의 웹 브라이저에 전송하는 작은 데이터 조각

사용자가 웹사이트 방문시 서버를 통해 사용자 컴퓨터에 설치되는 작은 기록 정보 파일
- 클라이언트는 쿠키를 로컬에 Key-Value 형식으로 저장
- 동일한 서버에 재요청시 저장된 쿠키를 함께 전송

쿠키는 두 요청이 동일한 브라우저에 들어왔는지 아닌지를 판단할 때 주로 사용
- 이를 이용해 사용자의 로그인 상태를 유지
- 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억시켜줌
  
<br>

### <b>ⅱ. 쿠키 사용 목적</b>
<br>

세션 관리
- 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

개인화
- 사용자, 선호, 테마 등의 설정

트래킹
- 사용자 행동을 기록 및 분석

<br>

### <b>ⅲ. 세션이란?</b>
<br>

사이트와 특정 브라우저 사이의 상태를 유지시키는 것

클라이언트가 서버에 접속
- 서버가 특정 session id를 발급
- 클라이언트는 session id를 쿠키에 저장
- 클라이언트가 동일한 서버에 재접속하면 요청과 쿠키를 서버에 전달
- 서버에서 쿠키에 들어있는 session id를 확인해 알맞은 로직 처리
  
session id는 세션을 구별하기 위해 필요, 쿠키에는 session id만 저장

<br>

### <b>ⅳ. 쿠키의 수명</b>
<br>

#### 1. session cookie
- 현재 세션이 종료되면 삭제됨
- 브라우저 종료와 함께 세션이 삭제됨

#### 2. Persistent cookies
- Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

<br>

### <b>ⅴ. session in Django</b>
<br>

Django는 database-backed sessions 저장 방식을 기본 값으로 사용
- session 정보는 Django DB의 djnago_session 테이블에 저장

Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄

Django는 우리가 session 메커니즘에 대부분을 생각하지 않게끔 많은 도움을 줌

<br><br>

## <b>Ⅴ. Login</b>

---
<br>

### <b>ⅰ. Autenticattion Form</b>
<br>

로그인을 위한 built-in form
  - 로그인 하고자 하는 사용자 정보를 입력받음
  - 기본적으로 username과 password를 받아 데이터가 유효한지 검증

request를 첫번째 인자로 취함

<br>

### <b>ⅱ. `login()`</b>
<br>

`login(request, user, backend=None)`

인증된 사용자를 로그인 시키는 로직으로 view 함수에서 사용됨

현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용

HttpRequest 객체와 User 객체가 필요

<br>

### <b>ⅲ. `get_user()`</b>
<br>

AuthenticationForm의 인스턴스 메서드

유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

<br>

### <b>ⅳ. 로그인 로직 작성</b>
<br>

>```python
>def login(request):
>    if request.method == 'POST':
>        form = AuthenticationForm(request, request.POST)
>        if form.is_valid():
>            auth_login(request, form.get_user())
>            return redirect('articles:index')
>    else:
>        form = AuthenticationForm()
>        context = {
>            'form': form
>        }
>        return render(request, 'accounts/login.html', context)
>```

<br><br>

## <b>Ⅵ. 로그인 정보 확인</b>

---
<br>

### <b>ⅰ. 현재 로그인 되어있는 유저 정보 출력하기</b>
<br>

base 템플릿에서 context 데이터 없이 user 변수 사용 가능
- settings.py의 context processors 설정값 때문
`<h3>안녕하세요, {{user}} 님!</h3>`

<br>

### <b>ⅱ. context processors</b>
<br>

템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록

작성된 컨텍스트 데이터는 기본적을 템플릿에서 사용 가능한 변수로 포함됨

즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해둔 것

<br>

### <b>ⅲ. `django.contrib.auth.context_processors.auth`</b>
<br>

현재 로그인한 사용자를 나타내느 User 클래스의 인스턴스가 템플릿 변수 {{ user }}에 저장됨
- 클라이언트가 로그인하지 않은 경우 `AnonymousUser` 클래스의 인스턴스로 생성

<br><br>

## <b>Ⅶ. 로그아웃</b>

---
<br>

### <b>ⅰ. `logout()`</b>
<br>

`logout(request)`

`HttpRequest` 객체를 인자로 받고 반환값이 없음

사용자가 로그인하지 않은 경우 오류를 발생시키지 않음

처리하는 로직
1. 현재 요청에 대한 session data를 DB에서 삭제
2. 클라이언트의 쿠키에서도 sessionid를 삭제
- 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함

<br>

### <b>ⅱ. 로그아웃 로직 작성하기</b>
<br>

>```python
>def logout(request):
>    auth_logout(request)
>    return redirect('articles:index')
>```