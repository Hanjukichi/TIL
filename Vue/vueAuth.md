# Authentication & Authoriazation

## <b>Authentication - 인증, 입증</b>
- 자신이라고 주장하는 사용자가 누구인지 확인하는 행위
- 모든 보안 프로세스의 첫 번째 단계(가장 기본 요소)
- 즉, 내가 누구인지를 확인하는 과정
- 401 Unauthorized
  - HTTP 표준에서는 "미승인(unauthorized)"을 명확히 하고 있음
  - 의미상 이 응답은 "비인증(unauthenticated)"을 의미

<br>

## <b>Authorization - 권한 부여, 허가</b>
- 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정
- 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
  - 사용자는 액세스 권한을 부여받기 전에 자신의 ID를 먼저 확인해야함
- 서류 등급, 웹페이지에서 글을 조회,삭제,수정 할 수 있는 방법, 제한 구역
  - 인증이 되었어도 모든 권한을 부여받는 것은 아님
- 403 Forbidden
  - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음

<br>

## <b>Authenticaiton and authorization work together</b>
- 화원가입 후, 로그인 시 서비스를 이용할 수 있는 권한 생성
  - 인증 이후 권한이 따라오는 경우가 많음
- 단, 모든 인증을 거쳐도 권한이 동일하게 부여되는 것은 아님
- 세션, 토큰, 제 3자를 활용하는 등 다양한 방식 존재

<br><br>

# How to authentication determined in Django

## <b>인증 여부 확인 방법</b>
- `settings.py`에 작성하여야 할 설정
  - 기본적인 인증 절차를 어떠한 방식으로 둘 것이냐를 설정하는 것
- 우리가 사용할 방법은 DRF가 기본으로 제공해주는 인증 방식 중 하나
  - `TokenAuthentication`
- 모든 상황에 대한 인증 방식을 정의하는 것
  - 각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식 필요
  - `view` 함수 마다 다른 인증 방식을 설정하고자 한다면 decorator 사용
- `permission_classes`
  - 권한 관련 설정
  - 권한 역시 특정 view 함수마다 다른 접근 권한을 요구 할 수 있음

<br>

## <b>인증 방식의 종류</b>
- `settings.py`에서 `DEFAULT_AUTHENTICATION_CLASSES`를 정의
  - 어떤 인증 방식을 사용할 것임을 명시
  
### 1. `BasicAuthentication`
- 가장 기본적인 수준의 인증 방식
- 테스트에 적합

### 2. `SessionAuthentication`
- Django에서 사용하였던 session 기반의 인증 시스템
- DRF와 Djnago의 session 인증 방식은 보안적 측면을 구성하는 차이가 존재

### 3. `RemoteUserAuthentication`
- Django의 Remote user방식을 사용할 때 활용하는 인증 방식

### 4. `TokenAuthentication`
- 매우 간단하게 구현할 수 있음
- 기본적인 보안 기능 제공
- 다양한 외부 패키지가 있음

<br>

## <b>`TokenAuthentication` 사용 방법</b>
1. `INSTALLED_APPS`에 `rest_framework.authtoken` 등록

2. 각 `User`마다 고유 `Token` 생성

3. 생성한 `Token`을 각 `User`에게 발급
   - User는 발급받은 `Token`을 요청과 함께 전송
   - Token을 통해 `User` 인증 및 권한 확인

4. `User`는 발급받은 `Token`을 `headers`에 담아 요청과 함께 전송
    - 단, 반드시 `Token` 문자열 함께 삽입
    - 삽입해야할 문자열은 인증 방식마다 다름
    - `Token` 문자열과 발급받은 실제 `token` 사이를 공백으로 구분

<br><br>

# dj-Rest-Auth

## <b>`dj-rest-auth`란?</b>
- 회원가입, 인증, 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등을 위한 REST API end point 제공

<br>

## <b>`dj-rest-auth`사용 방법</b>
- 패키지 설치
```
pip install dj-rest-auth
```
- APP 등록
```python
INSTALLED_APPS = [
    'rest_framework',
    # Auth
    'rest_framework.authtoken',
    'dj_rest_auth',
]
```
- url 등록
```python
urlpatterns = [
    path('accounts/', include('dj_rest_auth.urls')),
]
```
- `auth.User`를 커스텀 유저 모델로 변경
```python
AUTH_USER_MODEL = 'accounts.User'
```

<br>

## <b>Registrations</b>
- Registrations 기능을 사용하기 위해 추가 기능 등록 및 설치 필요
  - dj-rest-auth는 소셜 회원가입을 지원
  - dj-rest-auth의 회원가입 기능을 사용하기 위해선 `django-allauth` 필요
1. `django-allauth` 설치
```
pip install 'dj-rest-auth[with_social]'
```
2. App 등록 및 Site_Id 설정
```python
INSTALLED_APPS = [
    # registration
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]

# 회원가입시 토큰 발급
REST_AUTH = {
    'SESSION_LOGIN': False
}

# 하나의 컨텐츠로 여러 개의 도메인에 등록하고 싶을 때 사용
SITE_ID = 1
```
3. URL 설정
```python
urlpatterns=[
path('accounts/signup/', include('dj_rest_auth.registration.urls'))]
```
4. migrate

<br>

## <b>Sign up & Login</b>
- 회원 가입 요청 후 결고 확인
  - 요청에 대한 응답으로 Token 발급
- 로그인 시에도 동일한 토큰 발급
  - 정상적인 로그인 가능

<br>

## <b>Password change</b>
- 로그인이 되어있거나, 인증이 필요한 기능
- DRF 자체 제공 HTML form에서는 토큰을 입력할 수 있는 공간이 없음
- Postman에서 진행
1. body/form-data에 값 입력
2. headers에 Token 입력
  - `Authorization: Token {your token}`
3. `settings.py`
```python
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
  }
```

<br>

## <b>Permission setting</b>
- 권한 세부 설정
  - 모든 요청에 대해 인증을 요구하는 설정
  - 모든 요청에 대해 인증이 없어도 허용하는 설정
- 설정 위치 === 인증 방법을 설정한 곳과 동일
  - 우선 모두 허용만 주석 해제
```python
REST_FRAMEWORK = {
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
```