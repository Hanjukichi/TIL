# 기초 위젯들

## `Padding`
상하좌우 여백을 설정을 위해 사용
```dart
...
Padding(
  padding: EdgeInsets.all(40),
  child: ...
)
...
```
- `padding` 프로퍼티를 통해 여백 설정
- `padding`에는 `EdgeInsets` 클래스 사용
- `child` 프로퍼티에 내부 위젯 설정

## `Text`
```dart
...
Text('Hey, Selena',
  style: TextStyle(
    color: Colors.white,
    fontSize: 24,
    fontWeight: FontWeight.w800,
  ),
),
...
```
- `style` 프로퍼티 안에 텍스트 스타일을 정의 가능

## `SizedBox`
여백을 주기위해 사용하는 박스 위젯
```dart
SizedBox(
  height: 40,
),
```
- `width`, `height` 설정 가능
- `child`를 통해 자식 위젯 설정 가능

## `Center`
컨텐츠를 중앙 정렬
```dart
body: Center(
  child: Text("Hello world"),
),
```
- `child` 위젯으로 정렬할 위젯 정의

## `Flexible`
```dart
Flexible(
    flex: 1,
    child: Container(
      decoration: const BoxDecoration(
        color: Colors.red,
      ),
    )),
```
- `flex` 프로퍼티로 현 화면에서 차지할 비율을 설정해줄 수 있음

## `Expanded`
```dart
Row(
  children: [
    Expanded(
      child: Container(
        decoration: BoxDecoration(
          color: Theme.of(context).cardColor,
        ),
        child: const Column(children: [
          Text('Pomodoros'),
          Text('0'),
        ]),
      ),
    ),
  ],
)
```
- 남는 공간을 꽉 채우는 위젯