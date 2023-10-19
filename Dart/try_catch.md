# Dart 예외 처리

## Ⅰ. try...catch
```Dart
void main () {
  try {
    final String fruit = '사과';
    print(fruit);
  } catch(e) {
    print(e);
  }
}
```
- try문의 코드를 실행
- 에러 발생시 이후 로직 실행 X => 바로 catch 구문으로 넘어감

## Ⅱ. `throw`
```Dart
void main () {
  try {
    final String fruit = '사과';
    throw Exception('에러 발생');
    print(fruit);
  } catch(e) {
    print(e);
  }
}
```
- `throw`를 통해 에러 발생시킬 수 있음