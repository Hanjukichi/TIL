# Dart 상속

## Ⅰ. `extends`
```dart
// 부모 클래스
class Idol {
  String name;
  int membersCount;
  
  Idol({
    required this.name,
    required this.membersCount
  });
  
  void sayName() {
    print("저희는 ${this.name}입니다.");
  }
  
  void sayMembersCount() {
    print("저희는 ${this.name}은 ${this.membersCount}명입니다.");
  }
}

// 자식 클래스
class BoyGroup extends Idol{
  BoyGroup(
    String name,
    int membersCount
  ): super(
    name: name,
    membersCount: membersCount
  );
  
  void sayMale() {
    print("저희는 남자아이돌입니다.");
  }
}
```
- `extends`로 선언
- 부모 클래스를 상속받을 때 생성자 또한 준수해줘야함
- 부모 클래스를 지칭할 때는 `super`를 사용

## Ⅱ. 메서드 상속
```dart
// main 함수
void main() {
  BoyGroup bts = BoyGroup("BTS", 7);

  bts.sayName();
  bts.sayMembersCount();

  bts.sayMale();
}
```
- 부모 클래스에 선언된 메서드들은 자식 클래스에서 사용가능
- 그 반대는 불가능

## Ⅲ. 타입 상속
```dart
// main 함수
void main() {
  Idol apink = Idol(name:"Apink", membersCount: 5);
  BoyGroup bts = BoyGroup("BTS", 7);
  
  print(apink is Idol);  // true
  print(apink is BoyGroup);  // false
   
  print(bts is Idol);  // true
  print(bts is BoyGroup);  // true
}
```
- 자식 클래스는 부모 클래스의 타입도 상속받음
- 그 역은 성립 X
- 자식들끼리는 상관관계가 없음