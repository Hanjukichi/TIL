# Dart Static

## Ⅰ. Static 변수
```dart
// main 함수
void main() {
  Employee person1 = Employee("A");
  Employee person2 = Employee("B");
  
  Employee.building = "멀티캠퍼스";
  
  person1.printInfos();
  person2.printInfos();
}

// Employee 클래스
class Employee {
  static String? building;
  final String name;
  
  Employee (
    this.name,
  );
    
  void printInfos() {
    print('제 이름은 $name입니다. $building 건물에서 근무하고 있습니다.');
  }
}
```
- `static` 키워드로 사용
- 변수가 인스턴스가 아닌 클래스에 귀속됨

## Ⅱ. Static 메서드
```dart
// main 함수
void main() {
  Employee person1 = Employee("A");
  Employee person2 = Employee("B");
  
  Employee.building = "멀티캠퍼스";
  
  Employee.printBuilding();
}

// Employee 클래스
class Employee {
  static String? building;
  final String name;
  
  Employee (
    this.name,
  );

  
  static void printBuilding() {
    print('저희는 $building에서 근무하고 있습니다.');
  }
}
```
- `static`으로 메서드 또한 선언 가능
- `클래스.메서드명` 으로 사용