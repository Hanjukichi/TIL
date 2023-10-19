# Dart 연산자

## Ⅰ. 기본 수치 연산자
```Dart
void main() {
  double number = 2;
  
  print(number + 2);
  print(number - 2);
  print(number * 2);
  print(number / 2);  // 몫
  print(number % 2);  // 나머지
  
  // 삼항 연산자도 가능
  number++;  // 3
  number--;  // 2
  number += 2;  // 4
  number -= 2;  // 2
  number *= 2;  // 4
  number /= 2;  // 2
}
```
- 기본적인 산수 기능 제공

<br>

## Ⅱ. null 관련 연산자
```Dart
void main() {
  double? number1 = null;
  double number2 = null;  // 에러 발생
}
```
- `null` : 아무 값도 없음을 뜻 함. 0과 다름
- 타입 뒤 `?`를 추가해야 `null`값 저장 가능

```Dart
void main() {
  double? number;
  print(number);
  
  number ??= 3;
  print(number);
  
  number ??= 4;
  print(number);
}
```
- `??` : 기존 `null`일 때만 값이 저장되도록 함

<br>

## Ⅲ. 값 비교 연산자
```Dart
void main() {
  int num1 = 1;
  int num2 = 2;
  
  print(num1 > num2);
  print(num1 < num2);
  print(num1 >= num2);
  print(num1 <= num2);
  print(num1 == num2);
  print(num1 != num2);
}
```
- 기본적인 정수 크기 비교 가능

<br>

## Ⅳ. 타입 비교 연산자
```Dart
void main() {
  int num = 1;
  
  print(num is int);
  print(num is String);
  print(num is! int);
  print(num is! String);
}
```
- `is` 키워드를 통해 타입 비교 가능
  
<br>

## Ⅴ. 논리 연산자
```Dart
void main() {
  print(2 > 1 && 1 > 0);  // true
  print(2 > 1 && 1 < 0);  // false
  print(2 < 1 && 1 > 0);  // false
  print(2 < 1 && 1 < 0);  // false
  
  print(2 > 1 || 1 > 0);  // true
  print(2 > 1 || 1 < 0);  // true
  print(2 < 1 || 1 > 0);  // true
  print(2 < 1 || 1 < 0);  // false
}
```
- `&&` : and
- `||` : or