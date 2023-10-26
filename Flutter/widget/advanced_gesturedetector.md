# `GestureDetector`

## 1. 기본 사용법
```dart
GestureDetector(
  onTap: () {
    Navigator.push(
        context,
        MaterialPageRoute(
            builder: (context) =>
                DetailScreen(title: title, thumb: thumb, id: id)));
  },
)
```
- 동작을 감지할 수 있는 위젯
- `onTap` : 터치 혹은 클릭을 감지
- 이외에도 수많은 동작을 감지할 수 있음