# Dart Interface

## Ⅰ. 인터페이스 선언
```dart
// 인터페이스
class IdolInterface {
  String name;
  
  IdolInterface(this.name);
  
  void sayName() {}
}

// 상속 클래스
class BoyGroup implements IdolInterface {
  String name;
  
    
  BoyGroup(this.name);
  
  void sayName() {
    print("제 이름은 $name입니다.")
  }
}
```
- `interface` 키워드가 따로 없고 `class`를 그대로 사용.
- 특수한 구조를 강제
- `implements`를 통해 interface 상속

## Ⅱ. 인터페이스 인스턴스화 방지
```dart
// 인터페이스
abstract class IdolInterface {
  String name;
  
  IdolInterface(this.name);
  
  void sayName() {}
}
```
- `abstract` 로 선언된 클래스는 인스턴스 생성 금지됨