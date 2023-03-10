# 반응형웹과 부트스트랩
<br>

## <b>Ⅰ. 부트스트랩</b>

---
<br>

### <b>ⅰ. CDN(Content Delivery(Distribution) Network)</b>
<br>

컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해  
여러 노드를 가진 네트워크에서 데이터를 제공하는 시스템
- 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
- 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

<br>

### <b>ⅱ. Spacing</b>
<br>

#### `.mt-1`
rem
- 현재 <html> 폰트 사이즈의 1/4  
- 폰트 사이즈를 변경하지 않았다면 `1 rem = 4px` 
```css
`0.25rem !important`
```

#### `.mx-0`
```css
margin-right: 0 !important;
margin-left: 0 !important;
```

#### `.mx-auto`
수평 중앙 정렬
```css
margin-right: auto !important;
margin-left: auto !important;
```

#### `.py-0`
```css
padding-top: 0 !important;
padding-bottom: 0 !important;
```

#### 종합
||뜻||뜻||뜻|
|---|---|---|---|---|---|
|m|margin|t|top|0|0 rem||
|p|padding|b|bottom|1|0.25 rem||
|||s|left|2|0.5 rem|
|||e|right|3|1 rem|
|||y|top, bottom|4|1.5 rem|
|||x|left, right|5|3 rem|


<br>

### <b>ⅲ. color</b>
<br>

#### `bg-문구`  

|문구|color|
|---|---|
|primary|007bff|
|secondary|6c757d|
|success|28a745|
|info|17a2b8|
|warning|ffc10|
|danger|dc3545|
|light|f8f9fa|
|dark|343a40|

이외에도 더 많은 기능이 있으니 찾아볼 것


<br><br>

## <b>Ⅱ. 반응형 웹 (Responsive Web)</b>

---
<br>

### <b>ⅰ. Responsive Web Design</b>
<br>

다양한 화면 크기를 가진 디바이스의 등장과 함께 나타난 개념

웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이되는 사례들의 모음등을 기술

<br>

### <b>ⅱ. Grid System</b>
<br>

구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함

기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인

정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

<br><br>

## <b>Ⅲ. Bootstrap Grid System</b>

---
<br>

### <b>ⅰ. 기본 요소</b>
<br>

column
- 실제 컨텐츠를 포함하는 부분

Gutter
- 칼럼과 칼럼 사이의 공간(사이 간격)

Container
- Column들을 담고 있는 공간

<br>

### <b>ⅱ. Bootstrap Grid System</b>
<br>

기본적으로 flexbox로 제작됨

Container, rows, columns으로 컨텐츠를 배치하고 정렬

반드시 기억할 2가지
- 12개의 column
- 6개의 gird breakpoints

<br>

### <b>ⅲ. Grid System breakpoints</b>
<br>

명칭|class|크기
---|---|---
extra small|None|<576px
small|sm|>=576px
Medium|md|>=768px
Large|lg|>=992px
Extra large|xl|>=1200px
Extra extra large|xxl|>=1400px

