# 네비게이터

## `push`
```dart
Navigator.push(
            context,
            MaterialPageRoute(
                builder: (context) =>
                    DetailScreen(title: title, thumb: thumb, id: id)));
```
- 첫번째 인자 : `context`
- 두번째 인자 : `MaterialPageRoute` 클래스로 위젯을 감싼 후 넘어줘야함

### 1. `fullscreenDialog`
```dart
Navigator.push(
    context,
    MaterialPageRoute(
        ...
        fullscreenDialog: true,
    ));
```
- 이동할 페이지가 어떻게 나타날지 설정

