# Dart Generic

## Ⅰ. generic 기본
```dart
// main 함수
void main() {
  Lecture<String> lecture1 = Lecture('123', 'lecture1');
}

// Lecture 클래스
class Lecture<T> {
  final T id;
  final String name;
  
  Lecture(this.id, this.name);
}
```
- 타입을 외부에서 받을 때 사용
- 클래스를 정의할 때 `<타입 인자>`로 설정 가능

## Ⅱ. generic 응용
```dart
// main 함수
void main() {
  Lecture<String, String> lecture1 = Lecture('123', 'lecture1');
}

// Lecture 클래스
class Lecture<T, X> {
  final T id;
  final X name;
  
  Lecture(this.id, this.name);
}
```
- 여러 타입 또한 지정 가능