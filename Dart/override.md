# Dart Override

## Ⅰ. Override 기본 사용법
```dart
// 부모 클래스
class TimesTwo{
  final int number;
  
  TimesTwo(
    this.number,
  );
    
  // method
  int calculate() {
    return number * 2;
  }
}


// 자식 클래스
class TimesFour extends TimesTwo{
  TimesFour(
    int number,
  ): super(number);
   
  @override
  int calculate() {
    return super.calculate * 2;
  }
}
```
- `@override`를 메서드 위에 표시
- 부모 클래스의 메서드를 덮어쓰기 가능
- 덮어쓴 메서드의 `return`에 정석은 `super`이나 `this`나 생략도 가능

## Ⅱ. 부모 메서드 활용
```dart
// 자식 클래스
class TimesFour extends TimesTwo{
  TimesFour(
    int number,
  ): super(number);
   
  @override
  int calculate() {
    return super.calculate() * 2;
  }
}
```
- 부모 메서드를 불러와서 자식 메서드에서 값으로 활용 가능
- `super.메서드명` 으로 불러옴

## Ⅲ. 공통 메서드 활용
```dart
// Person 클래스
class Person {
  final String name;
  final String departure;
  
  Person({
    required this.name,
    required this.departure,
  });
  
  // 출력 형태를 변환해줌   
  @override
  String toString() {
    return '{name: $name, group: $departure}';
  }
}
```
- 출력의 형태 또한 오버라이드로 변환해줄 수 있음