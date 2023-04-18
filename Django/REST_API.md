# REST API
<br>

## <b>Ⅰ. HTTP</b>

---
<br>

### <b>ⅰ. HTTP REQUEST Methods</b>

- 리소스에 대한 행위를 정의
- 리소스에 대해 수행할 원하는 작업을 나타내는 모음을 정의
- `GET`, `POST`, `PUT`, `DELETE` 등

#### `GET`
- 서버에 리소스의 표현을 요청
- GET을 사용하는 요청은 데이터만 검색해야 함

#### `POST`
- 데이터를 지정된 리소스에 제출
- 서버의 상태를 변경

#### `PUT`
- 요청한 주소의 리소스를 수정

#### `DELETE`
- 지정된 리소스를 삭제
  
<br>

### <b>ⅱ. HTTP response status codes</b>

특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나탬

- Informational responses(100-199)
- Successful responses(200-299)
- Redirection messages(300-399)
- Client error resposes(400-499)
- Server error responses(500-599)

<br><br>

## <b>Ⅱ. Identifying Resources on the Web</b>

---
<br>

### <b>ⅰ. 웹에서의 리소스 식별</b>

- HTTP 요청의 대상을 리소스라고 함
- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
- 각 리소스느 식별을 위해 URI로 식별됨

<br>

### <b>ⅱ. URI</b>

- Uniform Resuorce Identifier - 통합 자원 식별자
- 인터넷에서 리소스를 식별하는 문자열
- 가장 일반적인 URI는 웹주소로 알려진 URL
- 특정 이름공간에서 이름으로 리소스를 식별하는 URI는 URN

<br>

### <b>ⅲ. URL</b>

- Uniform Resuorce Locator - 통합 자원 위치
- 웹에서 주어진 리소스의 주소
- 네트워크 상에 리소스가 어디 있는지를 알려주기 위한 약속
  - 이러한 리소스는 HTML, CSS, 이미지 등이 될 수 있음
- URL은 다음과 같이 여러 부분으로 구성되며 일부는 필수이고 나머지는 선택사항

#### SCHEME (or protocol)
`https`
- 브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜
- URL의 첫부분은 브라우저가 어떤 규약을 사용하는지를 나타냄
- 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기 위한 `mailto:` 파일을 전송하기 위한 `ftp:`등 다른 프로토콜도 존재


### Authority
`www.example.com:80`
- Scheme 다음은 문자 패턴 `://`으로 구분된 Authority(권한)이 작성됨
- Authority는 domin과 port를 모두 포함하며 둘은 `:`으로 구분됨
- Domain Name
  - 요청 중인 웹서버를 나타냄
  - 어떤 웹 서버가 요구되는지를 가리키며 직접 IP 주소를 사용하는 것도 가능
  - `www.example.com`
- Port
  - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문
  - HTTP 프로토콜의 표준 포트는 다음과 같고 생략 가능(HTTP-80, HTTPS-443)
  - 장고의 경우 8000이 기본 포트로 설정
  - `80`

#### PATH
`path/to/myfile.html`
- 웹 서버의 리소스 경로
- 초기에는 실제 파일이 위치한 물리적 위치를 나타냈음
- 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현

#### PARAMETERS
`?key=value`
- 웹 서버에 제공하는 추가적인 데이터
- 파라미터는 `&` 기호로 구분되는 키-값 쌍 목록
- 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음

#### ANCHOR
`#quick-start`
- 리소스의 다른 부분에 대한 앵커
- 리소스 내부 일종의 북마크를 나타내며 브라우저에 해당 북마크 지점에 있는 콘텐츠를 표시
- fragment identifier라고 부르는 `#` 이후 부분은 서버에 전송되지 않음

<br>

### <b>ⅳ. URN</b>

- Uniform Resuorce Name (통합 자원 이름)
- URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함(독립적 이름)
- URL의 단점을 극복하기 위해 등장했으며 자원이 어디에 위치한지 여부와 관계없이 이름만으로 자원을 식별
- 하지만 이름만으로 실제 리소스를 찾는 방법은 보현화되어있지 않음
- ISBN(국제표준 도서번호), ISAN(국제표준 시청각 자료번호)

<br><br>

## <b>Ⅲ. REST API</b>

---
<br>

### <b>ⅰ. API</b>

- Application Programming Interface
- 애플리케이션과 프로그래밍으로 소통하는 방법
  - 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성
- API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약
- API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공

<br>

### <b>ⅱ. Web API</b>

- 웹서버 또는 웹 브라우저를 위한 API
- 현재 웹 개발은 모든 것을 하나부터 열까지 직접 개발하기보다 여러 Open API를 활용하는 추세
- API는 다양한 타입의 데이터를 응답

<br>

### <b>ⅲ. REST</b>

- Representational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- 소프트웨어 아키텍쳐 디자인 제약 모음
- REST 원리를 따르는 시스템음 RESTful 하다고 부름
- REST의 기본 아이디어는 리소스 즉 자원
  - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술

<br>

### <b>ⅳ. REST에서 자원을 정의하고 주소를 지정하는 방법</b>

1. 자원의 식별
   - URI
2. 자원의 행위
   - HTTP Method
3. 자원의 표현
   - 자원과 행위를 통해 궁극적으로 표현되는 결과물
   - JSON으로 표현된 데이터를 제공

<br>

### <b>ⅴ. JSON</b>
- JavaScript의 표기법을 따른 단순 문자열
- 파이썬의 dictionary, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 key-value 형태의 구조를 갖고 있음
- 사람이 읽고 쓰기 쉽고 기계가 파싱하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터 타입

<br><br>

## <b>Ⅳ. Response API</b>

---
<br>

### <b>ⅰ. JsonResponse()</b>
- 장고가 기본적으로 제공하는 JsonResponse 객체를 활용
- Python 데이터 타입을 손쉽게 Json으로 변환하여 응답가능
- Json-encoded response를 만드는 클래스
- `safe` parameter
  - 기본 값 True
  - False로 설정 시 모든 타입의 객체를 serializtion 할 수 있음
  - True면 dict 인스턴스만 허용
>```python
>return JsonResponse(articles_json, safe=False)
>```

<br>

### <b>ⅱ. serializers.serialize()</b>
- 장고의 내장 HttoResponse()를 활용한 JSON 응답
- 이전에는 JSON의 모든 필드를 하나부터 열까지 장성해야 했지만 이제는 그렇지 않음
- 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 줌
>```python
>data = serializers.serialize('json', articles)
>return HttpResponse(data, content_type='application/json')
>```

#### Serialization
- "직렬화"
- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 대표적 변환 포맷 : json, xml, yaml

<br>

### <b>ⅲ. Django REST framework (DRF)</b>
- 장고에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- Web API 구축을 위한 강력한 toolkit을 제공
- REST framework를 작성하기 위한 여러 기능을 제공
- DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동

>```python
># articles/serializers.py
>from rest_framework import serializers
>from .models import Article
>
>class ArticleSerializer(serializers.ModelSerializer):
>    class Meta:
>        model = Article
>        fields = '__all__'
>
>
># articles/views.py
>from rest_framework.decorators import api_view
>from rest_framework.response import Response
>from .serializers import ArticleSerializer
>
>@api_view(['GET'])
>def article_json_3(request):
>    articles = Article.objects.all()
>    aritcles = ArticleSerializer(articles, many=True)
>    return Response(serializers.data)

<br>

### <b>ⅳ. ModelSerializer</b>
- ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
  - Model 정보에 맞춰 자동으로 필드를 생성
  - serializer에 대한 유효성 검사기를 자동으로 생성
  - `.create()` 및 `.update()`의 간단한 기본 구현이 포함됨
- `many` option : 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize 하려면 `many=True`를 작성해야함

<br>

### <b>ⅴ. `api_view` decorator</b>
- DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음
- 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답