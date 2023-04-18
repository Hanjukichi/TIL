# Backend Framework
<br>

## <b>Ⅰ. Django REST framework(Single Model)</b>

---
<br>

### <b>ⅰ. POST</b>

#### Raising an exception on invalid data
- 유효하지 앟은 데이터에 대해 예외발생시키기
- `is_valid()`는 유효성 검사 오류가 있는 경우 Validation Error 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음
- DRF에서 제공하는 기본 예외처리기에 의해 자동으로 처리
- 기본적으로 HTTP 400응답을 바환
  
#### CODE
>```python
>from rest_framework import status
>
>@api_view(['GET', 'POST'])
>def article_list(request):
>    if request.method == 'GET':
>        articles = Article.objects.all()
>        serializer = ArticleListSerializer(articles, many=True)
>        return Response(serializer.data)
>    elif request.method == 'POST':
>        serializer = ArticleListSerializer(data=request.data)
>        if serializer.is_valid(raise_exception=True):
>            serializer.save()
>            return Response(serializer.data, status=status.HTTP_201_CREATED)
>```

<br>

### <b>ⅱ. DELETE</b>

#### CODE
>```python
>@api_view(['GET', 'DELETE'])
>def article_detail(request, article_pk):
>    article = Article.objects.get(pk=article_pk)
>    if request.method == 'GET':
>        serializer = ArticleListSerializer(article)
>        return Response(serializer.data)
>    elif request.method == 'DELETE':
>        article.delete()
>        return Response(status=status.HTTP_204_NO_CONTENT)
>```

<br>

### <b>ⅲ. PUT</b>

#### CODE
>```python
>def article_detail(request, article_pk):
>    ......
>    elif request.method == 'PUT':
>        serializer = ArticleListSerializer(article, data=request.data)
>        if serializer.is_valid(raise_exception=True):
>            serializer.save()
>            return Response(serializer.data)
>```

<br><br>

## <b>Ⅱ. Django REST framework(N:1)</b>

---
<br>

### <b>ⅰ. GET - List</b>

#### CODE
>```python
>@api_view(['GET'])
>def comment_list(request):
>    comments = Comment.objects.all()
>    serializer = CommentSerializer(comments, many=True)
>    return Response(serializer.data)
>```

<br>

### <b>ⅱ. GET - Detail</b>

#### CODE
>```python
>@api_view(['GET'])
>def comment_detail(request, comment_pk):
>    comments = Comment.objects.get(pk=comment_pk)
>    serializer = CommentSerializer(comments)
>    return Response(serializer.data)
>```

<br>

### <b>ⅲ. POST</b>

#### Passing Additional attributes to `.save()`
- `save()`메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
  
#### 읽기 전용 필드 설정
- `read_only_fields`를 사용해 외래 키 필드를 읽기 전용 필드로 설정
- 읽기 전용 필드는 데이터를 전송하는 시점에 해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력하도록 함

#### CODE
>```python
>@api_view(['POST'])
>def comment_create(request, article_pk):
>    article = Article.objects.get(pk=article_pk)
>    serializer = CommentSerializer(data=request.data)
>    if serializer.is_valid(raise_exception=True):
>        serializer.save(article=article)
>        return Response(serializer.data, status=status.HTTP_201_CREATED)
>```

<br>

### <b>ⅳ. DELETE & PUT</b>
>```python
>@api_view(['GET', 'POST', 'PUT'])
>def comment_detail(request, comment_pk):
>    comment = Comment.objects.get(pk=comment_pk)
>    if request.method == 'GET':
>        serializer = CommentSerializer(comment)
>        return Response(serializer.data)
>    elif request.method == 'DELETE':
>        comment.delete()
>        return Response(status=status.HTTP_204_NO_CONTENT)
>    elif request.method == 'PUT':
>        serializer = CommentSerializer(comment, data=request.data)
>        if serializer.is_valid(raise_exception=True):
>            serializer.save()
>            return Response(serializer.data)
>```

<br><br>

## <b>Ⅲ. N:1 역참조 데이터 조회</b>

---
<br>

### <b>ⅰ. `PrimaryKeyRelatedField`</b>
- Serializer는 기존 필드를 override 하거나 추가적인 피드 구성 가능
>```python
>    comments_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
>```

<br>

### <b>ⅱ. Nested relationships</b>
- 모델 관계상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩 가능
- 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현할 수 있음
- 두 클래스의 상/하 위치를 변경해야함
>```python
>class ARticleSerializer(serializers.ModelSerializer):
>    comments = CommentSerializer(many=True, read_only=True)
>```

<br>

### <b>ⅲ. `source`</b>
- serializers field's argument
- 필드를 채우는 데 사용할 속성의 이름
- 점 표기법을 사용하여 속성을 탐색할 수 있음
>```python
>comment_count = serializers.IntegerField(source='comments.count', read_only=True)
>```

<br><br>

## <b>Ⅳ. Django shortcuts functions</b>

---
<br>

### <b>ⅰ. `get_object_or_404()`</b>
- 모델 manager objects에서 get()을 호출
- 해당 객체가 없을 땐 기존 DoesNotExist 대신 Http404를 raise

<br>

### <b>ⅱ. `get_list_or_404()`</b>
- 모델 manager objects에서 filter()을 호출
- 해당 객체 목록이 없을 땐 Http404를 raise

<br>

### <b>ⅲ. 사용하는 이유</b>
- Http500 같은 원인이 정확하지 않은 에러는 혼란 야기
- 서버가 적절한 예외 처리 수행 후, 클라이언트에게 올바른 에러 전달 또한 중요