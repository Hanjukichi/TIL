# `Container`
html의 `div` 역할

## 1. `decoration`
```dart
...
Container(
  decoration: BoxDecoration(
    color: Colors.amber,
    borderRadius: BorderRadius.circular(45),
  ),
  child: const Padding(
    ...
  )
),
...
```
- `decoration`과 `BoxDecoration`으로 스타일 수정 가능

## 2. `clipBehavior`
```dart
Container(
  clipBehavior: Clip.hardEdge,
)
```
- 자식 위젯이 `Container`의 범위를 벗어났을 때의 옵션
- `Clip` 클래스를 활용
- `Clip.hardEdge` : 외부로 벗어난 요소를 자름