# 인증과 권한 활용하기
<br>

## <b>Ⅰ. 회원 가입</b>

---
<br>

### <b>ⅰ. 개요</b>
<br>

User를 Create 하는 것
- `UserCreationForm` built-in form을 사용

<br>

### <b>ⅱ. UserCreationForm</b>
<br>

주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

3개의 필드를 가짐
- username(from the user model)
- password1
- password2(확인용)

<br>

### <b>ⅲ. 로직 작성</b>
<br>

>```python
># view.py
>from django.contrib.auth.forms import UserCreationForm
>
>def signup(request):
>    if request.method == 'POST':
>        form = UserCreationForm(request.POST)
>        if form.is_valid():
>            form.save()
>            return redirect('articles:index')
>    else:
>        form = UserCreationForm()
>        context = {'form': form}
>        return render(request, 'accounts/signup.html', context)
>```

<br>

### <b>ⅳ. 회원가입 진행 후 에러 페이지를 확인</b>
<br>

`UserCreationForm`
- 우리가 대체한 커스텀 유저 모델 기반 X
- 기존 유저 모델로 인해 작성된 클래스
  
<br><br>

## <b>Ⅱ. Custom user & Built-in auth forms</b>

---
<br>

### <b>ⅰ. `AbstractBaseUser`의 모든 subclass와 호환되는 forms</b>
<br>

`User`모델을 대체하더라도 커스텀 하지 않아도 사용 가능
- `AuthenticationForm`
- `SetPasswordForm`
- `PasswordChangeForm`
- `AdminPasswordChangeForm`

기존 `User`모델을 참조하는 Form이 아니기 때문

<br>

### <b>ⅱ. 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야하는 forms</b>
<br>

두 form 모두 `class Meta: model = User`가 등록된 form이기 때문에 반드시 커스텀 필요

1. `UserCreationform`
2. `UserCahngeForm`

<br>

### <b>ⅲ. `get_user_model()`</b>
<br>

현재 프로젝트에서 활성화된 사용자 모델을 반환

직접 참조하지 않는 이유
- 자동으로 커스텀 User 모델을 반환

Django는 User 클래스를 직접 참조하는 대신 `get_user_model()`을 사용해 참조해야 한다고 강조하고 있음

<br>

### <b>ⅳ. 로직 작성</b>
<br>

#### 1. 커스텀 유저 생성 폼 생성

>```python
># forms.py
>from django.contrib.auth import get_user_model
>from django.contrib.auth.forms import UserCreationForm
>
>class CustomUserCreationForm(UserCreationForm):
>    
>    class Meta(UserCreationForm.Meta):
>        model = get_user_model()
>```


#### 2. 회원가입 로직 작성

>```python
># views.py
>from .forms import CustomUserCreationForm
>
>def signup(request):
>    if request.method == 'POST':
>        form = CustomUserCreationForm(request.POST)
>        if form.is_valid():
>           # 회원가입 후 로그인 진행
>            user = form.save()
>            auth_login(request, form)
>            return redirect('articles:index')
>    else:
>        form = CustomUserCreationForm()
>    context = {'form': form}
>    return render(request, 'accounts/signup.html', context)
>```

<br><br>

## <b>Ⅲ. 회원 탈퇴</b>

---
<br>

### <b>ⅰ. 로직 작성</b>
<br>

>```python
>def delete(request):
>    request.user.delete()
>    # 유저 세션도 함게 제거
>    auth_logout(request)
>    return redirect('articles:index')
>```

<br><br>

## <b>Ⅳ. 회원정보 수정</b>

---
<br>

### <b>ⅰ. 'UserCHangeForm'</b>
<br>

사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

`UserchangeForm` 또한 ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일

<br>

### <b>ⅱ. 주의할 점</b>
<br>

일반 사용자가 접근해서는 안 될 정보들까지 모두 수정이 가능해짐
- admin 인터페이스에서 사용되는 ModelForm이기 때문

`CustomUserChangForm`을 수정해야함

<br>

### <b>ⅲ. 로직 작성</b>
<br>

#### 1. 필드 재정의

>```python
># forms.py
>class CustomUserChangeForm(UserChangeForm):
>    
>    class Meta(UserChangeForm.Meta):
>        model = get_user_model()
>        fields = ('username', 'email', 'first_name', 'last_name',)
>```

#### 2. 회원정보 수정

>```python
># views.py
>def update(request):
>    if request.method == 'POST':
>        form = CustomUserChangeForm(request.POST, instance=request.user)
>        if form.is_valid():
>            form.save()
>            return redirect('articles:index')
>    else:
>        form = CustomUserChangeForm(instance=request.user)
>    context = {'form': form}
>    return render(request, 'accounts/update.html', context)
>```

<br><br>

## <b>Ⅴ. 비밀변호 변경</b>

---
<br>

### <b>ⅰ. `PasswordChangeForm`</b>
<br>

사용자가 비밀번호를 변경할 수 있도록 하는 Form

이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함

<br>

### <b>ⅱ. 암호 변경시 세션 무효화 방지하기</b>
<br>

비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 됨
- 로그인 상태 유지 X
- 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보 일치 X

<br>

### <b>ⅲ. `update_session_auth_hash()`</b>
<br>

`update_session_auth_hash(request, user)`

현재 요청과 새 세션 데이터가 파생될 업데이트된 사용자 객체를 가져오고, 세션 데이터를 업데이트해줌

암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 세션 데이터로 세션 업데이트

<br>

### <b>ⅳ. 로직 작성</b>
<br>

>```python
># views.py
>def change_password(request):
>    if request.method == 'POST':
>        form = PasswordChangeForm(request.user, request.POST)
>        if form.is_valid():
>            form.save()
>            update_session_auth_hash(request, form.user)
>            return redirect('articles:index')
>    else:
>        form = PasswordChangeForm(request.user)
>    context = {'form': form}
>    return render(request, 'accounts/change_password.html', context)
>```

<br><br>

## <b>Ⅵ. View decorators</b>

---
<br>

### <b>ⅰ. Django의 데코레이터</b>
<br>

해당 함수를 수정하지 않고 기능을 추가해주는 함수

Django는 view 함수에 적용할 수 있는 여러 데코레이터를 제공

<br>

### <b>ⅱ. Allowed HTTP methods</b>
<br>

`django.views.decorators.http`의 데코레이터 사용
- 요청 메서드를 기반으로 접근을 제한

일치하지 않는 메서드 요청이라면 405 Method Not Allowed를 반환
- 405 : 요청방법은 전달됐지만 사용 불가능

#### 1. `require_http_methods()`

- 특정한 요청 method만 허용하도록 하는 데코레이터
- `require_http_methods(['GET', 'POST'])`

#### 2. `require_POST`

- POST요청 method만 허용하도록 하는 데코레이터

#### 3. `require_safe`

- `require_GET`이 존재
- 장고에선 `require_safe`를 사용하는 걸 권장

<br><br>

## <b>Ⅶ. Limiting access to logged-in users</b>

---
<br>

### <b>ⅰ. `is_authenticated`</b>
<br>

User model의 속성 중 하나

사용자가 인증되었는지 여부를 알 수 있는 방법

모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
- AnonymousUser에 대해서는 항상 False

일반적으로 `request.user`에서 이 속성을 사용
- `request.user.is_authenticated`

※ 권한과는 관련이 없음
※ 사용자 활성화 상태 or 유효한 세션 확인도 X

<br>

### <b>ⅱ. 로직 작성하기</b>
<br>

#### 1. 로그인과 비로그인 상태 링크 구분
>```html
><!-- base.html -->
>{% if user.is_authenticated %}
> <a href="{% url 'accounts:logout' %}">로그아웃</a>
> <a href="{% url 'accounts:update' %}">회원정보수정</a>
> <form action="{% url 'accounts:delete' %}" method='GET'>
>   <input type="submit" value="회원탈퇴">
> </form>
> <h3 id="user-hello"><i>안녕하세요, {{user}} 님 !</i></h3>
>{% else %}
> <a href="{% url 'accounts:signup' %}">회원가입</a>
> <a href="{% url 'accounts:login' %}">로그인</a>
>{% endif %}
>```

#### 2. 인증된 사용자만 게시글 작성하게 하기

>```html
><!-- base.html -->
>{% if request.user.is_authenticated %}
>  <a href="{% url 'articles:create' %}">작성하기</a>
>{% else %}
>  <a href="{% url 'accounts:login' %}">새 글을 작성하려면 로그인하세요</a>
>{% endif %}
>

#### 3. 인증된 사용자라면 로그인 로직 수행할 수 없도록 처리

>```python
># views.py
>def login(request):
>    if request.user.is_authenticated:
>        return redirect('articles:index')
>```