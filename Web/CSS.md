# CSS
<br>

## <b>Ⅰ. Box model</b>

---
<br>

### <b>ⅰ. css 원칙1</b>
<br>

모든 요소는 네모(박스모델)이다.  

위에서 아래로, 왼쪽에서 오른쪽으로 쌓임  

Normal Flow:
- 인라인 요소는 좌우로 쌓임
- 블록 요소는 상하로 쌓임

<br>

### <b>ⅱ. box model</b>
<br>

![](boxmodel.png)

모든 HTML 요소는 box 형태로 되어있음  

하나의 박스는 네 부분으로 이루어짐  
1. content : 요소의 실제 내용
2. padding : 테두리 안쪽의 내부 여백  
  배경색과 이미지는 padding까지 적용
3. border : 테두리 영역
4. margin : 테두리 바깥의 외부 여백  
배경색 지정 불가

#### <b>margin</b>
```
.margin{
  margin-top : 10px;
  margin-right : 20px;
  margin-bottom : 30px;
  margin-left : 40px;
}
```

#### <b>padding</b>
```
.margin-padding{
  margin : 10px;
  padding: 30px;
}
```

#### <b>border</b>
```
.border{
  border-width: 2px;
  border-style: dashed;
  border-color: black;
}
```

#### <b>shorthand</b>
전부
```
.margin-1{
  margin: 10px;
}
```
상하(10px), 좌우(20px)
```
.margin-2{
  margin: 10px 20px;
}
```
상(10px), 하(30px), 좌우(20px)
```
.margin-3{
  margin: 10px 20px 30px;
}
```

상(10px), 하(30px), 우(20px), 좌(40px)
```
.margin-4{
  margin: 10px 20px 30px 40px;
}
```

<br>

### <b>ⅲ. box sizing</b>
<br>

기본적으로 모든 요소의 box-sizing은 content-box
- padding을 제외한 순수 contents 영역만을 box로 지정

다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 원함
- box-sizing을 border-box로 설정

<br><br>

## <b>Ⅱ. 개발자 도구</b>

---
<br>

### <b>ⅰ. 크롬 개발자 도구</b>
<br>

웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공

#### <b>주요기능</b>
- Elements : DOM 탐색 및 CSS 확인 및 변경
  - Styles : 요소에 적용된 CSS 확인
  - Computed : 스타일이 계산된 최종 결과
  - Event Listeners : 해당 요소에 적용된 이벤트(JS)
- Sources, Network, Performance, Applicaition, Seurity, Audits 등


<br><br>

## <b>Ⅲ. CSS Display</b>

---
<br>

### <b>ⅰ. Block</b>
<br>

줄 바꿈이 일어나는 요소(다른 요소를 밀어냄)  

화면 크기 전체의 가로 폭을 차지  

블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.  

block의 기본 너비는 가질 수 있는 너비의 100%  

너비를 가질 수 없다면 margin이 자동으로 부여됨  

`div` / `ul`, `ol`, `li` / `p` / `hr` / `form`

<br>

### <b>ⅱ. Inline</b>
<br>

줄바꿈이 일어나지 않는 행의 일부 요소  

content를 마크업 하고 있는 만큼만 가로폭을 차지  

`width`, `height`, `margin-top`, `margin-bottom`을 지정할 수 없음  

상하 여백은 `line-height`로 지정
inline의 기본 너비는 컨텐츠 영역 만큼  

내가(inline) 정렬 하는 게 아닌 부모가(block) 정렬해 주는 것  

`span` / `a` / `input`, `label` / `b`, `em`, `i`, `strong`

<br>

### <b>ⅲ. Inline-block</b>
<br>

block과 inline 레벨 요쇼의 특징을 모두 가짐  

inline처럼 한 줄에 표시 가능  

block처럼 width, height, margin 속성을 모두 지정할 수 있음  

<br>

### <b>ⅳ. None</b>
<br>

해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

`visibilty: hidden` : 공간은 차지하나 화면에 표시 X

<br><br>

## <b>Ⅳ. CSS Position</b>

문서 상에서 요소의 위치를 지정

---
<br>

### <b>ⅰ. static</b>
<br>

모든 태그의 기본 값(기준 위치)

일반적인 요소의 배치 순서에 따름(좌측 상단)

부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준을 배치됨

<br>

### <b>ⅱ. relative</b>
<br>

상대 위치

자기 자신의 static 위치를 기준으로 이동(normal flow 유지)

레이아웃에서 요소가 차지하는 공간은 static 일 때와 같음

normal poistion 대비 offset

<br>

### <b>ⅲ. absolute</b>
<br>

절대 위치

요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음

static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동

<br>

### <b>ⅳ. fixed</b>
<br>

고정 위치

요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음

부모 요소와 관계없이 viewport를 기준으로 이동

스크롤 시에도 항상 같은 곳에 위치함

<br>

### <b>ⅴ. sticky</b>
<br>

스크롤에 따라 static > fixed로 변경

속성을 적용한 박스는 평소에 문서 안에서 static 상태

스크롤 위치가 임계점에 이르면 fixed