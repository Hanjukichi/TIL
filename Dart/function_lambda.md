# Dart 함수와 람다

## Ⅰ. 함수의 일반적 특징

### 1. 함수의 기본 활용
```Dart
int addNumbers(int num1, int num2) {
  return num1 + num2;
}

void main () {
  print(addNumbers(3,4));
}
```
- 함수를 한 번만 작성하면 다른 곳에서 여러 번 재활용 가능
- 반환값이 없으면 `void` 사용

### 2. 매개변수 설정
```Dart
int addNumbers1(int num1, int num2) {
  return num1 + num2;
}

int addNumbers2({
  required int num1, 
  required int num2
 }) {
  return num1 + num2;
}

void main () {
  print(addNumbers1(3,4));
  print(addNumbers2(num1: 2, num2: 5));
}
```
- positional parameter : 순서대로 매개변수 입력됨
- named parameter : 키와 값 형태로 매개변수 입력
  - `{}`와 `required` 사용해야함
  - `required` : null이 불가능한 타입

### 3. 매개변수의 기본값
```Dart
int addNumbers1(int num1, [int num2 = 3]) {
  return num1 + num2;
}

int addNumbers2({
  required int num1, 
  int num2 = 10
 }) {
  return num1 + num2;
}

void main () {
  print(addNumbers1(3));
  print(addNumbers2(num1: 2));
}
```
- positional parameter : `[]` 사용하여 기본값 할당
- named parameter : `required`를 생략하고 기본값 할당

### 4. 매개변수 혼용 사용
```Dart
int addNumbers1(
  int num1, {
  required int num2,
  int num3 = 3
}) {
  return num1 + num2;
}

void main () {
  print(addNumbers1(3, num2: 2));
}
```
- 두 종류의 매개변수를 혼용하여 사용 가능
- positional parameter가 먼저 위치해야함

<br>

# Ⅱ. 익명 함수와 람다 함수

### 1. 익명 함수
```Dart
void main () {
  List<int> numbers = [1, 2, 3, 4, 5];
  
  final biggerNumbers = numbers.map((number) {
    return number + 5;
  });
    
  print(biggerNumbers);
}
```
- 함수 이름이 없고, 일회성으로 사용

### 2. 람다 함수
```Dart
void main () {
  List<int> numbers = [1, 2, 3, 4, 5];
  
  final biggerNumbers = numbers.map((number) => number + 5);
    
  print(biggerNumbers);
}
```
- 익명함수에서 `{}`를 빼고 `=>`를 추가
- 대신 단 하나의 명령 단위만 사용 가능

<br>

## Ⅲ. `typedof`와 함수

### 1. `typedof`
```Dart
typedef Operation = void Function(int x, int y);

void add(int x, int y) {
  print("정답 : ${x + y}");
}

void main () {
  Operation oper = add;
  oper(3,4);
}
```
- `typedof`로 시그니처 정의
- 시그니처에 맞춘 함수를 만들어서 사용

### 2. First-class citizen
```Dart
typedef Operation = void Function(int x, int y);

void add(int x, int y) {
  print("정답 : ${x + y}");
}

void cal(int x, int y, Operation oper) {
  oper(x, y);
}

void main () {
  cal(5, 6, add);
}
```
- First-class citizen : 함수를 값처럼 사용 가능
- flutter에서 typedef로 선언한 함수를 매개변수로 넣어 사용