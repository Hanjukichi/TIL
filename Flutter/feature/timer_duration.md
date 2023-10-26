# `Timer`와 `Duration`

## `Timer`
타이머 기능을 제공하는 플러터 내부 클래스

### 1. import
```dart
import 'dart:async';
```
- `Timer`을 자동완성하면 자동으로 `import`해줌

### 2. `periodic`
```dart
late Timer timer;

void onTick(Timer timer) {
  ...
  setState(() {
    totalSeconds--;
  });
}

void onStartPressed() {
  timer = Timer.periodic(const Duration(seconds: 1), onTick);
  setState(() {
    isRunning = true;
  });
}
```
- 첫번째 인자 : 시간 간격
- 두번째 인자 : 콜백 함수
- 설정한 시간마다 콜백함수 실행
- 콜백 함수의 인자로 `Timer`의 인스턴스를 넣어줘야함

### 3.`cancel`
```dart
void onPausePressed() {
  timer.cancel();
  ...
}
```
- `periodic`를 정지시켜줄 수 있음

<br>

## `Duration`
```dart
String timeFormat(int seconds) {
  var duration = Duration(seconds: seconds);
  return duration.toString().split('.').first.substring(2, 7);
}
```
- 시간에 관한 여러 기능을 제공