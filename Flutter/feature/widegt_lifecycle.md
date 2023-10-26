# 위젯 라이프사이클

## `initState()`
```dart
@override
  void initState() {
    super.initState();
    print("시작");
  }
```
- 위젯이 나타날 때 `build` 메서드 이전에 실행되는 메서드
- 위젯의 상태를 초기화하는 역할

## `dispose()`
```dart
@override
  void dispose() {
    super.dispose();
    print("끝");
  }
```
- 위젯이 사라지거나 삭제될 때 실행되는 메서드
- 위젯이 사라질 때 상태를 초기화하거나 삭제할 때 사용