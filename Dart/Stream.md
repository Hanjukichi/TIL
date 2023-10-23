# Dart - Stream을 활용한 비동기 처리

## Ⅰ. Stream 기본

### 1. Stream 이란?
  데이터나 이벤트가 들어오는 통로입니다.<br>
  데이터의 추가나 변경이 일어나면 이를 관찰하던데서 처리하는 방법입니다. <br>

### 2. 기본 사용법
```dart
import 'dart:async';

void main() {
  // stream 선언
  final controller = StreamController();
  final stream = controller.stream;
  
  // 이벤트 리스터
  final streamListener1 = stream.listen((val){
    print('listen1 : $val');
  });
  
  // 이벤트 전달
  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);
}
```
- `dart:async` 패키지 `import` 필요
- 이벤트를 전달할 때마다 리스너 실행

<br>

## Ⅱ. Stream 응용

### 1. Stream Broadcast 
```dart
import 'dart:async';

// main 함수
void main() {
  final controller = StreamController();
  final stream = controller.stream.asBroadcastStream();
  
  final streamListener1 = stream.listen((val){
    print('listen1 : $val');
  });
  
  final streamListener2 = stream.listen((val){
    print('listen2 : $val');
  });
  
  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);
}
```
- 기존 `stream`에 `asBroadcastStream()` 추가
- 다수의 리스너 정의 가능

### 2. Stream 메서드
```dart
import 'dart:async';

// main 함수
void main() {
  final controller = StreamController();
  final stream = controller.stream.asBroadcastStream();
  
  final streamListener1 = stream.where((val) => val % 2 == 1).listen((val){
    print('listen1 : $val');
  });
  
  final streamListener2 = stream.where((val) => val % 2 == 0).listen((val){
    print('listen2 : $val');
  });
  
  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);
}
``` 
- `stream`에 기존 배열을 수정할 때 사용하던 메서드들 사용 가능

<br>

## Ⅲ. Stream 함수

### 1. 기본 사용법
```dart
import 'dart:async';

// main 함수
void main() {
  calculate(1).listen((val){
    print('calculate(1) : $val');
  });
}

// Stream 함수
Stream<int> calculate(int number) async*{
  for (int i = 0; i < 5; i++){
    yield i * number;
  }
}
```
- `Stream<타입>` + `async*` 로 Stream 함수 선언 가능
- `return` 대신 `yield` 사용
- `yield`가 실행될 때마다 리스너 실행

### 2. `await`
```dart
import 'dart:async';

// main 함수
void main() {
  calculate(1).listen((val){
    print('calculate(1) : $val');
  });
}

// Stream 함수
Stream<int> calculate(int number) async*{
  for (int i = 0; i < 5; i++){
    yield i * number;
    await Future.delayed(Duration(seconds:1));
  }
}
```
- `async`로 선언되었기 때문에 내부에 `await` 사용 가능
- `await` 수행 후 다음 연산 실행

### 3. `yield*`
```dart
...

// Stream 함수1
Stream<int> playAllStream() async* {
  yield* calculate(1);
  yield* calculate(3);
}

...
```
- `calculate(1)`의 모든 `yield`가 실행된 후 `calculate(3)` 실행