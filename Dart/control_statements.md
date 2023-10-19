# Dart 제어문

## Ⅰ. if문
```Dart
void main() {
  int number = 2;
  
  if (number % 2 == 0) {
    print('짝수입니다.');
  } else if (number % 2 == 1) {
    print('홀수입니다.');
  } else {
    print('잘못된 값입니다.');
  }
}
```
- `if`, `else if`, `else` 사용 가능

<br>

## Ⅱ. switch문
```Dart
enum Status {
  approved,
  pending,
  rejected
}

void main() {
  Status status = Status.approved;
  
  switch (status) {
    case Status.approved:
      print('승인 상태입니다.');
      break;
    case Status.pending:
      print('대기 상태입니다.');
      break;
    case Status.rejected:
      print('거부 상태입니다.');
      break;
    default:
      print("알 수 없는 상태입니다.");
  }
}
```
- 입력된 상수값에 따라 알맞은 `case` 블록을 수행
- `case` 끝에 `break`를 빼먹으면 컴파일 중 에러 발생
- `enum`과 함께 사용하면 유용

<br>

## Ⅲ. for문
```Dart
void main () {
  for (int i = 0; i < 3; i ++) {
    print(i);
  }
}
```
- 작업을 여러 번 반복해서 실행

```Dart
void main () {
  List<int> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  for (int number in numbers) {
    print(number);
  }
}
```
- List의 모든 값도 순회 가능

<br>

## Ⅳ. while 문

### 1. `while`
```Dart
void main () {
  int total = 0;

  while (total < 10) {
    total += 1;
  }

  print(total);
}
```
- 반복 작업시 사용
- 조건문이 `true`일동안 반복문 실행

### 2. `do...while`
```Dart
void main () {
  int total = 0;
  
  do {
    total += 1;
  } while (total < 10);
  
  print(total);
}
```
- 반복문 실행 후 조건 확인