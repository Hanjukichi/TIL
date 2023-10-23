# Dart - await를 통한 비동기 제어

## Ⅰ. `await`란?
```dart
// main 함수
void main() {
  addNumbers(3, 5);
}

// 더하기 함수
void addNumbers(int num1, int num2) async {
  print('계산 시작: $num1 + $num2');
  
  // 서버 시뮬레이션
  await Future.delayed(Duration(seconds:2), (){
    print('계산 완료: ${num1 + num2}');
  });
  
  print('함수 완료');
}
```
- `async`를 활용한 함수에서만 `await` 사용 가능
- `Future`를 반환해주는 함수에만 `await` 사용 가능
- `await`처리가 된 연산이 종료될 때까지 해당 연산 단위의 연산은 대기 상태
- 출력 결과
  1. `계산 시작 : 3 + 5`
  2. `계산 완료 : 8`
  3. `함수 완료`

<br>

## Ⅱ. `await` 연산 특징
```dart
// main 함수
void main() {
  addNumbers(3, 5);
  addNumbers(2, 6);
}

// 더하기 함수
void addNumbers(int num1, int num2) async {
  print('계산 시작: $num1 + $num2');
  
  // 서버 시뮬레이션
  await Future.delayed(Duration(seconds:2), (){
    print('계산 완료: ${num1 + num2}');
  });
  
  print('함수 완료');
}
``` 
- 다른 연산 단위는 기다리지 않고 연산 진행
- 출력 결과
  1. 계산 시작: 3 + 5
  2. 계산 시작: 2 + 6
  3. 계산 완료: 8
  4. 함수 완료
  5. 계산 완료: 8
  6. 함수 완료

<br>

## Ⅲ. 함수의 `Future`화
```dart
// main 함수
void main() async {
  await addNumbers(3, 5);
  await addNumbers(2, 6);
}

// 더하기 함수
Future<void> addNumbers(int num1, int num2) async {
  print('계산 시작: $num1 + $num2');
  
  // 서버 시뮬레이션
  await Future.delayed(Duration(seconds:2), (){
    print('계산 완료: ${num1 + num2}');
  });
  
  print('함수 완료');
}
```
- 함수 자체를 `Future`화 가능
- `Future`화된 함수는 `await` 사용 가능
- `main()`함수에 `async`처리 가능

<br>

## Ⅳ. `Future` 함수의 반환값
```dart
// main 함수
void main() async {
  final num1 = await addNumbers(3, 5);
  final num2 = await addNumbers(2, 6);
  print(num1 + num2);
}

// 더하기 함수
Future<int> addNumbers(int num1, int num2) async {
  print('계산 시작: $num1 + $num2');
  
  // 서버 시뮬레이션
  await Future.delayed(Duration(seconds:2), (){
    print('계산 완료: ${num1 + num2}');
  });
  
  print('함수 완료');
  
  return num1 + num2;
}
```
- `Future`함수의 반환값을 받기 위해선 `await`를 반드시 붙여야함.