# Build Context
하위 위젯에서 상위 위젯에 접근하게 하는 역할

## 상위 위젯
```dart
class _AppState extends State<App> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        theme: ThemeData(
          textTheme: const TextTheme(
            titleLarge: TextStyle(
              color: Colors.red,
            ),
          ),
        ),
    ...
  );
  }
}
```
- 루트 위젯에 `theme`을 정의해줌
- 앱 전체의 테마를 지정해주는 역할

## 하위 위젯
```dart
class MyLargeTitle extends StatelessWidget {
  const MyLargeTitle({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Text(
      "My Large Title",
      style: TextStyle(
        color: Theme.of(context).textTheme.titleLarge!.color,
        fontSize: 36,
        fontWeight: FontWeight.w600,
      ),
    );
  }
}
```
- `Theme.of(context).textTheme.titleLarge!.color`로 상위 위젯에 접근
- `!`을 넣어주는 게 좋음 => 상위 위젯에 찾고자 하는 값 무조건 있다고 판단해줌