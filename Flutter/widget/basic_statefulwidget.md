# 상태 저장 위젯

## `StatefulWidget`
상태를 저장하고 상태 변화를 UI에 반영할 때 사용  
```dart
class App extends StatefulWidget {
  const App({super.key});

  @override
  State<App> createState() => _AppState();
}

// 이 클래스에 코드 입력
class _AppState extends State<App> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      ...
    );
  }
}
```
- VSCode에서 `st`만 입력하면 자동완성 가능

<br>

## `setState`
```dart
...
int count = 0;

void onClicked() {
  count++;
  setState(() {});
}
...
```
- `setState()`를 사용해야 상태를 변화 시키는 코드를 통해 UI도 변경됨
- `setState()` 안에 반드시 코드가 들어가야하는 건 아님

<br>

## `widget.속성`
```dart
// 상위 위젯
class DetailScreen extends StatefulWidget {
  final String title, thumb, id;
  const DetailScreen({
    super.key,
    required this.title,
    required this.thumb,
    required this.id,
  });

  @override
  State<DetailScreen> createState() => _DetailScreenState();
}

// state 위젯
class _DetailScreenState extends State<DetailScreen> {
  ...

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        ...
        title: Text(
          // 상위 위젯에서 프로퍼티 들고 오는 방법
          widget.title,
          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w600),
        ),
      ),
      ...
    );
  }
}
```
- `StatefulWidget`로 선언된 위젯에서 인자로 넘겨받은 프로퍼티 사용 방법
- `widget`으로 프로퍼티에 접근 가능