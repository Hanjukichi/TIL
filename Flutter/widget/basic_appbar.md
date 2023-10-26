# `AppBar`
상단바 UI

## 1. 기본 사용법
```dart
...
AppBar(
  elevation: 2,
  centerTitle: true,
  backgroundColor: Colors.white,
  foregroundColor: Colors.green,
  title: const Text(
    "오늘의 웹툰",
    style: TextStyle(fontSize: 24, fontWeight: FontWeight.w600),
  ),
),
...
```
- 다양한 속성 및 위젯 존재

## 2. 유용한 속성들

### 1. `centerTitle`
-  타이틀 중앙 정렬

### 2. `elevation`
-  그림자 음영 조정

### 3. `elevation`
- 기본 텍스트 색깔 설정 