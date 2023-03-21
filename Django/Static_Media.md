# Static / Media
<br>

## <b>Ⅰ. Django Form</b>

---
<br>

### <b>ⅰ. 개요</b>
<br>

입력 데이터에 대한 유효성 검증이 필요
- 부가적인 것들을 고려해서 구현
- 개발 생산성을 늦추고 쉽지 않음

Django Form
- 이 과정에서 과중한 작업과 반복 코드를 줄여줌
- 훨씬 쉽게 유효성 검증을 지행할 수 있도록 만들어줌

<br>

### <b>ⅱ. 역할</b>
<br>

유효성 검사 도구 중 하나
- 외부의 악의적 굥격 및 데이터 손상에 대한 중요한 방어 수단

Form과 관련한 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공
- 직접 작성한 코드보다 더 안전하고 빠르게 수행하는 코드를 작성 가능

처리하는 영역
- 렌더링을 위한 데이터 준비 및 재구성
- 데이터에 대한 HTML forms 생성
- 클라이언트로부터 받은 데이터 수신 및 처리

<br><br>

## <b>Ⅱ. Django Form Class</b>

---
<br>

### <b>ⅰ. Form Class 선언</b>
<br>

#### Model Class를 선언하는 것과 비슷  
- 비슷한 이름의 필드 타입을 많이 가지고 있음
- Modle과 마찬가지로 상속을 통해 선언

#### 앱 폴더에 forms.py를 생성 후 ArticleForm Class 선언
- form에는 TextField가 존재하지 않음
>```python
>from django import forms
>
>class ArticleForm(forms.Form):
>   title = forms.CharField(max_length=10)
>   content = forms.CharField()   
>```

<br>

### <b>ⅱ. Form Class 활용</b>
<br>

#### view 업데이터
>```python
>form = ArticleForms()
>context = {'form': form}
>return render(request, 'articles/create.html', context)
>```

#### creat 템플릿 업데이터
>```html
><form action="{% url 'articles:create' %}" >method="POST">
>  {% csrf_token %}
>  {{form.as_p}}
>  <input type="submit">
></form>
>```

<br>

### <b>ⅲ. Form rendering options</b>
<br>

#### 1. `as_p()`
- 각 필드가 단락(`<p>`태그)로 감싸져서 렌더링

#### 2. `as_ul()`
- 각 필드가 목록 항목(`<li>`태그)로 감싸져서 렌더링
- `<ul>` 태그는 직접 작성해야 한다.

#### 3. `as_table()`
- 각필드가 테이블(`<tr>` 태그) 행으로 감싸져서 렌더링

<br>

### <b>ⅳ. 2가지 HTML input 요소 표현</b>
<br>

#### Form fields
- 입력에 대한 유효성 검사 로직을 처리
- 템플릿에서 직접 사용됨

#### Widgets
- 웹페이지의 HTML input 요소 렌더링을 담당
- 단순히 input 요소의 보여지는 부분을 변경
- Widgets은 반드시 form fields에 할당 됨

<br><br>

## <b>Ⅲ. Django ModelForm</b>

---
<br>

### <b>ⅰ. ModelForm Class</b>
<br>

Model을 통해 Form Class를 만들 수 있는 helper class

ModelForm은 Form과 똑같은 방식으로 View 함수에서 사용

<br>

### <b>ⅱ. ModelForm 선언</b>
<br>

forms 라이브러리에서 파생된 ModelForm 클래스르 상속받음

정의한 ModelForm 클래스 안에 Meta 클래스를 선언

어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta클래스에 지정

>```python
>from django import forms
>from .models import Article
>
>class ArticleForms(forms.ModelForm):
>
>    class Meta:
>        model = Article
>        fields = '__all__'
>```

<br>

### <b>ⅲ. Meta Class</b>
<br>

ModelForm의 정보를 작성하는 곳

Meta class의 model 속성이 ModelForm이 참조할 모델을 구성
- 참조하는 모델에 정의된 field 정보를 Form에 적용

>```python
>class Meta:
>    model = Article
>    fields = '__all__'
>   #exclude = ('title',)
>```

<br>

### <b>ⅳ. ModelForm 구현</b>
<br>

#### CREATE

- 유효성 검사를 통과하면
  - 데이터 저장 후
  - 상세 페이지로 리다이렉트

- 통과하지 못하면
  - 작성 페이지로 리다이렉트

>```python
>def create(request):
>    if request.method == 'POST':
>        form = ArticleForm(request.POST)
>        if form.is_valid():
>            form.save()
>            return redirect('articles:index')
>        return redirect('articles:create')
>```

#### ※ `is_valid()`
- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 여부를 boolean으로 반환
- 데이터 유효성 검사를 돕기 위해 Django는 `is_valid()`를 제공

#### ※ `save()`
- `form` 인스턴스에 바인딩된 데이터를 통해 데이터베이스 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 `instance` 여부를 통해 생성할 지, 수정할지를 결정함
  - 제공되지 않은 경우 새 인스턴스 생성
  - 제공되면 해당 인스턴스 수정
  
>```python
>form = ArticleForm(request.POST, instance=article)
>```

#### UPDATE
- `ModelForm`의 인자 `instance`는 수정 대상이 되는 객체(기존 객체)를 지정
- 
>```python
>def update(request, pk):
>    article = Article.objects.get(pk=pk)
>    if request.method == 'POST':
>        form = ArticleForm(request.POST, instance=article)
>        if form.is_valid():
>            form.save()
>            return redirect('articles:detail', article.pk)
>    else:
>        form = ArticleForm(instance=article)
>
>    context = {'form': form, 'article': article}
>    return render(request, 'articles/update.html', context)
>```

<br>

### <b>ⅴ. Form과 ModelForm</b>
<br>

#### Form
- 사용자의 입력을 필요로 함
- 직접 입력 데이터가 DB 저장에 사용되지 않거나 일부데이터만 사용될 때

#### ModelForm
- 사용자의 입력을 필요로 하며 입력을 받은 것을 그대로 DB필드에 맞춰 저장할 때
- 데이터 유효성 검사가 끝나면 데이터를 어떤 레코드에 맵핑할지 정해져있음
- 곧바로 `save()`호출 가능

<br><br>

## <b>Ⅳ. Static File</b>

---
<br>

### <b>ⅰ. Static File이란?</b>
<br>

응답할 때 별도의 처리없이 파일 내용 그대로 보여주면 되는 파일
- 사용자의 요청에 따라 요청한 것을 그대로 보여줌

파일 자체가 고정되어있음
- 서비스 중에도 추가되거나 변경 X

Django에서는 이러한 파일들을 static file이라 함
- `staticfiles` 앱을 통해 정적 파일과 관련된 기능을 제공

<br>

### <b>ⅱ. Media File</b>
<br>

미디어 파일

사용자가 웹에서 업로드하는 정적 파일

유저가 업로드한 모든 정적 파일

<br>

### <b>ⅲ. 웹 서버와 정적 파일</b>
<br>

1. 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서
2. 응답(HTTP response)을 처리하고 제공(serving)하는 것
3. 이는 자원과 자원에 접근 가능한 주소가 있다라는 의미
4. 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공

<br><br>

## <b>Ⅴ. Static File 구성</b>

---
<br>

### <b>ⅰ. 준비 단계</b>
<br>

1. `INSTALLED_APPS`에 `django.contrib.staticfiles`가 포함되어 있는지 확인
2. setting.py에서 `STATIC_URL` 정의
3. 앱의 static 폴더에 정적 파일을 위치

<br>

### <b>ⅱ. 장고 템플릿 태그</b>
<br>

#### `{% load %}`
- load tag
- 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드

#### `{% static '' %}`
- static tag
- STATIC_ROOT에 저장된 정적 파일 연결
  
<br>

### <b>ⅲ. Core Setting</b>
<br>

#### `STATICFILES_DIRS`
- Default : []
- `app/static/` 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성

#### `STATIC_URL`
- Default : None
- `STATIC_ROOT`에 있는 정적 파일을 참조할 때 사용할 URL
- 실제 파일이나 디렉토리 X
- 비어있지 않은 값이면 반드시 `/`로 끝나야 함
- 개발 단계에서는 `app/static/` 경로와 `STATICFILES_DIRS`에 정의된 추가 경로들을 탐색

<br><br>

## <b>Ⅵ. Media File</b>

---
<br>

### <b>ⅰ. `ImageField()`</b>
<br>

이미지 업로드에 사용하는 모델 필드

`FileField`를 상속 받는 서브 클래스
- `FileField`의 모든 속성 및 메서드를 사용 가능

더해서 사용자에 의해 업로드된 객체가 유효한 이미지인지 검사

`ImageField` 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성
- max_length 인자를 사용하여 최대 길이 변경 가능

<br>

### <b>ⅱ. `FileField()`</b>
<br>

`FileField(upload_to='', storage=None, max_length=100, **options)`

파일 업로드에 사용하는 모델 필드

2개의 선택 인자를 가지고 있음
- `upload_to`
- `storage`


<br>

### <b>ⅲ. field 옵션</b>
<br>

#### 1. `blank`
- default : False
- True인 경우 필드를 비워둘 수 있음
  - 이 경우 DB에는 빈 문자열이 저장됨
- 유효성 검사에서 사용돔(`is_valid`)

#### 2. `null`
- Default: False
- True인 경우 Django는 빈 값을 DB에 NULL로 저장
- 문자열 기반 필드에는 사용 피해야함
  - 설정시 데이터 없음에 대한 표현이 `''`과 `NULL` 모두 가능
  
<br>

### <b>ⅳ. 준비 단계</b>
<br>

1. settings.py에 `MEDIA_ROOT`, `MEDIA_URL` 설정
2. `upload_to` 속성을 정의하여 업로드 된 파일에 사용할 `MEDIA_ROOT`의 하위 경로를 지정
<br>

#### 1. `MEDIA_ROOT`
- Default : ''
- 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로
- Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
- `STATIC_ROOT`와 반드시 다른 경로로 지정해야 함

#### 2. `MEDIA_URL`
- Default : ''
- `MEDIA_ROOT`에서 제공되는 미디어 파일을 처리하는 URL
- 업로드된 파일의 주소를 만들어 주는 역할
  - 웹 서버 사용자가 사용하는 public URL
- 비어 있지 않은 값으로 설정한다면 반드시 `/`로 끝나야 함
- `STATIC_URL`와 반드시 다른 경로로 지정해야 함

<br><br>

## <b>Ⅶ. Media File 사용하기</b>

---
<br>

### <b>ⅰ. CREATE</b>
<br>

#### ImageField 작성
`image = models.ImageField(blank=True)`

#### Migrations
- `ImageField`를 사용하려면 반드시 `Pillow` 라이브러리가 필요
`pip install pillow`

#### form 태그 수정
- form 태그에 `enctype`속성을 변경
`enctype="multipart/form-data"`

#### `request.FILES`
- 파일 및 이미지는 POST 속성값으로 넘어가지 않음
`form = ArticleForm(request.POST, request.FILES)`

<br>

### <b>ⅱ. READ</b>
<br>

#### 업로드 이미지 출력
- 업로드된 파일의 상대 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음
`<img src = {{ article.image.url }}">`

#### 이미지가 없는 게시물
- 이미지 데이터가 있는 경우만 이미지 출력할 수 있도록 처리
>```html
>{% if article.image %}
>  <img src="{{ article.image.url }}" alt="{{ article.image }}">
>{% endif %}
>```