# Dart 생성자

## Ⅰ. Class 기본 사용법

### 1. class 선언
```dart
// Idol 클래스
class Idol {
  String name = "블랙핑크";
  List<String> members = ["지수", "제니", "리사", "로제"];
  
  void sayHello() {
    print("안녕하세요 블랙핑크입니다.");
  }
  
   void introduce() {
    print("저희 맴버는 지수, 제니 리사, 로제");
  }
}
```
- `class`로 객체 선언
- 안에 메서드 정의 가능

### 2. class 활용
```dart
// main 함수
void main () {
  Idol blackPink = Idol();
  
  print(blackPink.name);
  print(blackPink.members);
  blackPink.sayHello();
  blackPink.introduce();
}
```
- 타입을 선언 후 객체 선언

<br>

## Ⅱ. 생성자(Constructor) 기본

### 1. 생성자 기본
```dart
// Idol 클래스
class Idol {
  String name;
  List<String> members;
  
  Idol(String name, List<String> members)
    : this.name = name,
      this.members = members;
  
  void sayHello() {
    print('안녕하세요 ${this.name}입니다.');
  }
  
   void introduce() {
    print("저희 맴버는 ${this.members}입니다.");
  }
}
```
- 인자를 받아서 속성에 할당 가능

### 2. 더욱 간편한 사용법
```dart
// Idol 클래스
class Idol {
  String name;
  List<String> members;
  
  Idol(this.name, this.members)
  ...
}
```
- 타입에 맞게 인자를 넣어줘야함

### 3. 커스텀 사용법
```dart
// Idol 클래스
class Idol {
  String name;
  List<String> members;
  
  Idol.fromList(List values)
    : this.members = values[0],
      this.name = values[1];

  ...
}
```
- 메서드처럼 원하는 대로 정의해서 사용 가능

### 4. 생성자를 사용한 선언
```dart
// main 함수
void main () {
  Idol blackPink = Idol(
    "블랙핑크",
    ["지수, 제니, 리사, 로제"]    
  );
  print(blackPink.name);
  print(blackPink.members);
  blackPink.sayHello();
  blackPink.introduce();
  
  Idol bts = Idol.fromList([
    ["RM","진", "슈가"], 
    "BTS"
  ]);
  print(bts.name);
  print(bts.members);
  bts.sayHello();
  bts.introduce();
}
```

## Ⅲ. 속성 변경 방지

### 1. `final` 키워드
```dart
// main 함수
void main () {
  Idol blackPink = Idol(
    "블랙핑크",
    ["지수, 제니, 리사, 로제"]    
  );
  
  Idol.name = "한주";  // 에러 발생
}

// Idol 클래스
class Idol {
  final String name;
  final List<String> members;
  
  Idol(this.name, this.members);
}
```
- `final` 키워드로 속성 변경 방지 가능
- 자주 바뀌는 속성이 아니면 웬만하면 `final`로 선언해줘야함

### 2. `const` 생성자
```dart
// main 함수
void main () {
  Idol blackPink = const Idol(
    "블랙핑크",
    ["지수, 제니, 리사, 로제"]    
  );

  Idol blackPink2 = const Idol(
    "블랙핑크",
    ["지수, 제니, 리사, 로제"]    
  );
}

// Idol 클래스
class Idol {
  final String name;
  final List<String> members;
  
  const Idol(this.name, this.members);
}
```
- `final`과 마찬가지로 속성 변경 불가능
- 빌드타임 속성을 알 수 있음
- `const`로 선언한 변수가 그 값까지 똑같다면 같은 인스턴스로 판단