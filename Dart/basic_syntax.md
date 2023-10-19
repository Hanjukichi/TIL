# Dart 기초 문법

## Ⅰ. 메인 함수
```Dart
void main() {
  // 여기에 실행 코드 추가
}
```
- 프로그램 시작점인 엔트리 함수 기호
- 중괄호 사이에 원하는 코드 입력
- void는 반환값이 없다는 것을 의미
- () 안에 입력받을 매개 변수를 지정 가능

<br>

## Ⅱ. 주석
- `//` : 한줄 주석
- `/* */` : 여러 줄 주석
- `///` : 문서 주석

<br>

## Ⅲ. 출력 함수
```Dart
void main(){
  print("Hello World");
}
```
- `print()`로 콘솔 출력

<br>

## Ⅳ. 변수 선언

### 1. `var`
```Dart
void main() {
  var name = '사과';
  print(name);

  name = '바나나';
  print(name);
}
```
- `var 변수명 = 값` 형식
- 자동으로 타입 추론
- 컴파일 시 추론된 타입으로 `var`이 치환
- 변숫값 변경 가능
- 타입을 한 번 유추한 후 고정

### 2. `dynamic`
```Dart
void main() {
  dynamic name = '사과';
  name = 1  // 에러 발생하지 않음
}
```
- 변수의 타입이 고정되지 않음

### 3. `final`
```Dart
void main() {
  final String name = "사과";
  name = "바나나";  // 에러 발생

  final DateTime now = DateTime.now();
  print(now);  // 에러 발생 X
}
```
- 런타임 상수
- 값 선언 이후 고정
- 코드가 실행될 때 값이 확정될 때 사용

### 4. `const`
```Dart
void main() {
  const String name = "사과";
  name = "바나나";  // 에러 발생

  const DateTime now = DateTime.now();
  print(now);  // 에러 발생
}
```
- 빌드타임 상수
- 값 선언 이후 고정
- 코드를 실행하지 않은 상태에서 값이 확정될 때 사용

<br>

## Ⅴ. 변수 타입

### 1. 문자열
```Dart
void main() {
  String isStr = "사과";
}
```

### 2. 정수
```Dart
void main() {
  int isInt = 10;
}
```

### 3. 실수
```Dart
void main() {
  double isDouble = 2.5;
}
```

### 4. 불리언
```Dart
void main() {
  bool isTrue = true;
}
```