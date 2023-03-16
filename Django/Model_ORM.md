# 웹 프레임워크 이해하기
<br>

## <b>Ⅰ. Form & Data</b>

---
<br>

### <b>ⅰ. Client & Server Architecture</b>
<br>

웹은 기본적으로 클라이언트-서버 아키텍처를 사용

클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법

이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공 가능

<br><br>

## <b>Ⅱ. Sending form data</b>

---
<br>

### <b>ⅰ. HTML `<form>` element</b>
<br>

데이터가 전송되는 방법을 정의

웹에서 사용자 정보를 입력하는 여러 방식을 제공

사용자로부터 할당된 데이터를 서버로 전송

데이터를 어디(action)로 어떤 방식(method)로 보낼지

핵심 속성
- action
- method

<br>

### <b>ⅱ. HTML form's attribute</b>
<br>

#### <b>1. action</b>
- 입력 데이터가 전송될 URL을 지정
- 데이터를 어디로 보낼 것인지 지정하는 것, 반드시 유효한 URL이어야 함
- 속성을 지정하지 않으면 현재 form이 있는 페이지의 URL로 보내짐

#### <b>2. method</b>
- 데이터를 어떻게 보낼 것인지 
- 입력 데이터의 HTTP request methods를 지정
- HTML form 데이터는 오직 2가지 방법으로만 전송 가능
  - GET
  - POST
  
<br>

### <b>ⅲ. HTML `<input>` element</b>
<br>

사용자로부터 데이터를 입력받기 위해 사용

`type` 속성에 따라 동작 방식이 달라짐
- 기본값은 `text`

핵심 속성
- `name`

<br>

### <b>ⅳ. HTML input's attribute</b>
<br>

#### <b>1. name</b>
- form을 통해 데이터를 제출했을 때 name 속성에 설정된 값을 서버로 전송
- 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터값에 접근 가능
- 서버에 전달하는 파라미터(key: name, value: value)로 매핑

<br>

### <b>ⅴ. HTTP request methods</b>
<br>

#### <b>HTTP란?</b>
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
- 웹에서 이루어지는 모든 데이터 교환의 기초
- 주어진 리소스가 수행할 원하는 작업을 나타내는 request 

methods를 정의
자원에 대한 행위(수행하고자 하는 동작)를 정의

주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
- GET, POST, PUT, DELETE

<br>

### <b>ⅵ. GET</b>
<br>

서버로부터 정보를 조회하는데 사용
- 즉, 서버에게 리소스를 요청하기 위해 사용

데이터를 가져올 때만 사용

데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
- 데이터는 URL에 포함되어 서버로 보내짐

- 명시적 표현을 위해 대문자 사용을 권장

<br>

### <b>ⅶ. Quert String Parameters</b>
<br>

사용자가 입력 데이터를 전달하는 방법
- url 주소에 데이터를 파라미터를 통해 넘김

이러한 문자열은 `&`로 연결된 key=value쌍으로 구성
- 기본 URL과 물음표로 구분
- ex : `http://host:port/path?key=value&key=value`

Qurey String이라고도 함

<br><br>

## <b>Ⅲ. Retrieving the data</b>

---
<br>

### <b>ⅰ. 데이터 가져오기</b>
<br>

서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받음

이러한 목록에 접근하는 방법은 프레임워크에 따라 다름

모든 요청 데이터는 view 함수의 첫번째 인자 `request`에 들어있다.

<br>

### <b>ⅱ. Request and Response objects</b>
<br>

#### <b>요청과 응답 객체 흐름</b>
- 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
- 그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
- 마지막으로 view 함수는 HttpResponse object를 반환

<br><br>

## <b>Ⅳ. Database</b>

---
<br>

### <b>ⅰ.database란?</b>
<br>

체계화된 데이터의 모임

검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템

<br>

### <b>ⅱ. database 기본 구조</b>
<br>

#### <b>1. 스키마(Schema)</b>
- 뼈대(Structure)
- 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
 
column|datatype
---|---
id|INT
name|TEXT
age|INT
email|TEXT

#### <b>2. 테이블(Table)</b>
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
  - 필드: 속성, 컬럼
  - 레코드 : 튜플, 행
- 관계라고도 부름

<br>

### <b>ⅲ. PK(Primary Key)</b>
<br>

각 레코드의 고유한 값(식별자로 사용)

기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(uniaue)

데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용

<br>

### <b>ⅳ. 쿼리(Query)</b>
<br>

데이터를 조회하기 위한 명령어

조건에 맞는 데이터를 추출하거나 조작하는 명령어
- 주로 테이블형 자료구조에서 사용

<br><br>

## <b>Ⅴ. Model</b>

---
<br>

### <b>ⅰ. 개요</b>
<br>

Django는 Model을 통해 데이터에 접근하고 조작

사용하는 데이터들의 필수적인 필드들과 동작들을 포함

저장된 데이터베이스의 구조(layout)

일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
- 모델 클래스 == 데이터베이스 스키마

<br>

### <b>ⅱ. model의 이해</b>
<br>

각 모델은 `django.models.Model` 클래스의 서브 클래스
- 클래스 상속 기반 형태의 Django 프레임워크 개발

`models` 모듈을 통해 어떠한 타입의 DB필드를 정의할것인지 결정

클래스 변수명
- DB 필드의 이름

클래스 변수 값
- DB 필드의 데이터 타입

<br>

### <b>ⅲ. Django Model Field</b>
<br>

Django는 모델 필드를 통해 테이블의 필드에 저장할 데이터 유형의 정의

데이터 유형에 따라 다양한 모델 필드를 제공

<br><br>

## <b>Ⅵ. Migrations</b>

---
<br>

### <b>ⅰ. Migrations 관련 주요 명령어</b>
<br>

#### <b>1. makemigrations</b>
- `python manage.py makemigrations`
- 모델의 변경 사항에 대한 새로운 migration을 만들 때 사용

#### <b>2. migrate</b>
- `python manage.py migrate`
- makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정
- 결과적으로 모델의 변경사항과 데이터베이스를 동기화
- 설계도를 실제 `db.sqlite3` DB파일에 반영

#### <b>3. showmigrations</b>
- `python manage.py showmigrations`
- migrations 파일들이 migrate 됐는지 안 됐는지 여부를 확인하는 용도
- `[X]` 표시가 있으면 migrate가 완료되었음을 읨

#### <b>4. sqlmigrate</b>
- `python manage.py sqlmigrate articles 0001`
- 해당 migrations 파일이 SQL문으로 어떻게 해석될 지 미리 확인할 수 있음

<br>

### <b>ⅱ. Migrations 3 단계</b>
<br>

- model.py 에서 변경사항이 발생
- migration 생성 
  - `makemigrations`
- DB 반영(모델과 DB의 동기화)
  - `migrate`

<br><br>

## <b>Ⅶ. ORM</b>

---
<br>

### <b>ⅰ. ORM 개요</b>
<br>

Object - Relational - Mapping

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

Django는 내장 Django ORM을 사용

SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체

<br>

### <b>ⅱ. 장단점</b>
<br>

#### <b>1. 장점</b>
- SQL을 잘 알지 못 해도 객체지향 언어로 DB 조작이 가능
- 객체 지향적 접근으로 인한 높은 생산성
  
#### <b>2. 단점</b>
- ORM만으로 세밀한 데이터베이스 조작을 구현하기 어려운 경우가 존재

<br><br>

## <b>Ⅷ. QuerySet API</b>

---
<br>

### <b>ⅰ. Database API</b>
<br>

Django가 제공하는 ORM을 사용해 데이터베이스를 조작하는 방법

Model을 정의하면 데이터를 만들고 읽고 수정하고 지울 수 있는 API 제공

<br>

### <b>ⅱ. Database API 구문</b>
<br>

`Article.objects.alls()`

Model class|Manager|Queryset API
---|---|---
`Articles`|`objects`|`all()`

<br>

### <b>ⅲ. objects manager</b>
<br>

Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스

Django는 기본적으로 모든 Django 모델 클래스에 대해 objects라는 Manager 객체를 자동으로 추가

이 Manager를 통해 특정 데이터를 조작 가능

DB를 Python class로 조작할 수 있도록 여러 메서드를 제공

<br>

### <b>ⅳ. Query</b>
<br>

데이터 베이스에 특정한 데이터를 보여 달라는 요청
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달
- 데이터베이스의 응답 데이터를 ORM이 `QuerySet` 이라는 자료 형태로 변환하여 전달
  
<br>

### <b>ⅴ. QuerySet</b>
<br>

데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
- 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용 가능

Django ORM을 통해 만들어진 자료형, 필터를 걸거나 정렬등을 수행 가능

objects manager를 사용하면 반환되는 객체
- 복수의 데이터일때만
- 단일 객체는 모델의 인스턴스로 반환
  
<br><br>

## <b>Ⅸ. CRUD</b>

---
<br>

### <b>ⅰ. CRUD 개요</b>
<br>

Create/Read/Update/Delete
- 생성/조회/수정/삭제
- 보통 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말

<br>

### <b>ⅱ. CREATE</b>
<br>

데이터 객체를만드는 3가지 방법

#### <b>1. 첫 번째 방법</b>
- `article = Article()`
  - 클래스를 통한 인스턴스 생성
- `article.title`
  - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
- `article.save()`
  - 인스턴스로 save 메서드 호출
  
#### <b>2. 두 번째 방법</b>
- `article = Article(title = 'second', content = 'django!')`
  - 인스턴스 생성 시 초기 값을 함께 작성하여 생성

#### <b>3. 세 번째 방법</b>
- `Article.objects.create(title = 'second', content = 'django!')`
  - QuerySet API 중 `create()` 메서드 활용 

#### <b>`.save()`</b>
- 객체를 데이터 베이스에 저장함
- 데이터 생성 시 save를 호출하기 전에 객체의 id값은 None
  - id값은 Django가 아니라 데이터 베이스에서 계산되기 때문
- 모델 클래스로 인스턴스 생성하는 건 DB에 영향을 미치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨
  
<br>

### <b>ⅲ. READ</b>
<br>

#### <b>1. `all()`</b>
- 전체 데이터 조회
- QuerySet return

#### <b>2. `get()`</b>
- 단일 데이터 조회
- 고유성을 보장하는 조회에서 사용해야 함
- 예외 발생 상황
  - 객체를 찾을 수 없음 : `DoesNotExist`
  - 둘 이상의 객체가 존재 : `MultipleObjectReturned`

#### <b>3. `filter()`</b>
- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

#### <b>Field lookups</b>
- 특정 레코드에 대한 조건을 설정하는 방법
- filter(), exclude(), get()에 대한 키워드 인자로 지정

<br>

### <b>ⅳ. UPDATE</b>
<br>

1. 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2. article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
3. `save()` 인스턴스 메서드 호출

>```python
>article = Article.objects.get(pk=1)
># 인스턴스 변수를 변경
>article.title = 'byebye'
># 저장
>article.save()
>```

<br>

### <b>ⅴ. DELETE</b>
<br>

1. 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2. delete() 인스턴스 메서드 호출
   
>```python
>article = Article.objects.get(pk=1)
># delete 메서드 호출
>article.delete()
>```