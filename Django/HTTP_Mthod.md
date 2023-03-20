# HTTP Method
<br>

## <b>Ⅰ. Admin site</b>

---
<br>

### <b>ⅰ. 개요</b>
<br>

Django의 가장 강력한 기능 중 하나
- automatic admin interface

관리자 페이지
- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- 모델 class를 admin.py에 등록하고 관리
- 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수 도 있음
  
<br>

### <b>ⅱ. admin 조작
<br>

`python manage.py createsuperuser`
- username과 password를 입력해 관리자 계정을 생성
- emmail은 선택사항
- 비밀번호 생성시 보안상 터미널에 입력되지 않음

`http://127.0.0.1:8000/admin`로 접속 후 로그인
- 계정만 만든 경우 Django 관리자 화면에서 모델 클래스는 보이지 않음
  
`관리자명.site.register(모델명)`
- 모델의 record를 보기 위해서는 admin.py에 등록 필요

<br><br>

## <b>Ⅰ. HTTP Method</b>

---
<br>

### <b>ⅰ. 우리의 약속 HTTP</b>
<br>

HTTP란?
- 네트워크 상에서 데이터를 주고 받기 위한 약속

HTTP Method
- 데이터에 어떤 요청을 원하는지를 나타낸 것

<br>

### <b>ⅱ. GET & POST</b>
<br>

#### <b>1. GET</b>
- 어떠한 데이터를 조회하는 요청
- GET 방식으로 데이터를 전달하면 Query String 형식으로 보내짐
- 특정 리소스를 가져오도록 요청할 때 사용
- 반드시 데이터를 가져올 때만 사용
- DB에 변화를 주지 않음
- CRUD에서 R 역할을 담당

#### <b>2. POST</b>
- 어떠한 데이터를 생성(변경)하는 요청
- POST 방식으로 전달하면 Body에 담겨서 보내짐
- 서버로 데이터를 전송할 때 사용
- 서버에 변경사항을 만듦
- 리소스를 생성/변경하기 위해 데이터를 HTTP Body에 담아 전송
- GET의 쿼리 스트링 파라미터와 다르게 URL로 데이터를 보내지 않음
- CRUD에서 C/U/D 역할을 담당

<br>

### <b>ⅲ. 403 Forbidden</b>
<br>

서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미

서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환됨

즉, 게시글을 작성할 권한이 없음

모델(DB)을 조작하는 것은 단순 조회와 달리 최소한의 신원 확인이 필요하기 때문

<br>

### <b>ⅳ. CSRF</b>
<br>

#### <b>1. Cross-Site-Request-Forgery</b>
- 사이트 간 요청 위조
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취햑하게 하는 공격 방법

#### <b>2. CSRF 공격 방어</b>
- Security Token 사용 방식
- 사용자의 데이터에 임의의 난수 값을 부여해 매 요청마다 해당 난수 값을 포맷시켜 전송시키도록 함
- 이후 서버에서 요청을 받을 때마다 전달된 token값이 유효한지 검증
- 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용
- Django는 DTL에서 csrf_token 템플릿 태그를 제공

#### <b>3. 템플릿 태그 : `csrf_token` </b>

해당 태그가 없다면 403 forbidden으로 응답

내부 URL로 향하는 Post form을 사용하는 경우에 사용
- 외부 URL의 경우 토근 유출 가능