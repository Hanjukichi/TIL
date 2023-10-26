# `Row`와 `Column`

## 1. `Row`
- 행 방향으로 UI 요소 배치
```dart
Row(
  children: []
)
```
- `children` 안에 배치할 위젯들 추가

## 2. `Column`
- 행 방향으로 UI 요소 배치
```dart
Column(
  children: []
)
```
- `children` 안에 배치할 위젯들 추가

## 3. 정렬
```dart
...
// 주방향 정렬 옵션
mainAxisAlignment: MainAxisAlignment.end,
// 직각방향 정렬 옵션
crossAxisAlignment: CrossAxisAlignment.end,
...
```