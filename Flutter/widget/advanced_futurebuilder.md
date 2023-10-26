# `FutureBuilder`
```dart
FutureBuilder(
  future: webtoons,
  builder: (context, snapshot) {
    if (snapshot.hasData) {
      return const Text("Done!");
    } else {
      return const Text("Loading");
    }
  },
),
```
- `Future`를 통해 값을 나중에 받아오는 변수를 사용할 수 있게 해줌
- `StatelessWidget`위젯 안에서도 사용 가능

## 1. `future`
- 반드시 필요
- `Future`로 선언해준 변수

## 2. `builder`
- 반드시 필요
- 콜백함수를 넣어줌
- 빌더의 상태에 따라 상이한 위젯을 넣어줄 수 있음
- `snapshot` : `Future`의 상태