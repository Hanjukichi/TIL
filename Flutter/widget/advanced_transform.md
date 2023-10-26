# `Trasfrom`

## 1. `Trasfrom.scale`
```dart
Transform.scale(
  scale: 2,
  child: ...
),
```
- `child`의 크기를 `scale`배 만큼 늘려줌
- `scale` 프로퍼티를 필수적으로 설정해줘야함
- 감싸는 부모 위젯의 크기에는 영향을 주지 않음

## 2. `Trasfrom.translate`
```dart
Transform.translate(
  offset: const Offset(5, 10),
  child: const Icon(
    Icons.euro_rounded,
    color: Colors.white,
    size: 90,
  ),
),
```
- `child`의 위치를 옮겨줌
- `offset` 필수 설정, `Offset` 클래스 이용
- 감싸는 부모 위젯애는 영향을 주지 않음
