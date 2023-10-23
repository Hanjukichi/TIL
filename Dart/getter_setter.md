# Dart getter와 setter

## Ⅰ. Getter
```dart
// Idol 클래스
class Idol {
  String name;
  List<String> members;
  
  Idol(this.name, this.members);
  
  get firstMember {
    return this.members[0];
  }
}
```
- `get` 키워드 사용
- `this`를 사용하여 인스턴스의 속성값 반환 가능

## Ⅱ. Setter
```dart
// main 함수
void main () {
  Idol blackPink = Idol(
    "블랙핑크",
    ["지수", "제니", "리사", "로제"]    
  );
  
  blackPink.firstMember = "한주";
  
  print(blackPink.firstMember);
}

// Idol 클래스
class Idol {
  String name;
  List<String> members;
  
  Idol(this.name, this.members);
  
  String get firstMember {
    return this.members[0];
  }
  
  set firstMember(String name) {
    this.members[0] = name;
  }
}
```
- `set` 키워드 사용
- `get`과 같은 메서드명 사용 가능
- 잘 안 씀

## Ⅲ. 일반 함수와의 차이
```dart
// getter 메서드
String get firstMember {
  return this.members[0];
}

// 일반 메서드
String getFirstMember {
  return this.members[0];
}
```
- 기능적인 차이는 없음
- `getter`는 단순한 값 반환용
- 일반 메서드는 더욱 복잡한 로직 구현 때 사용