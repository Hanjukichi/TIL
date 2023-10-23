# Dart private속성

## Ⅰ. private 속성
```dart
void main () {
  _Idol blackPink = _Idol(
    "블랙핑크",
    ["지수", "제니", "리사", "로제"]    
  );
}


class _Idol {
  String name;
  List<String> members;
  
  _Idol(this.name, this.members);
}
```
- 변수명 앞에 `_`을 붙히면 private 선언
- 같은 파일 내에서만 사용 가능
- 다른 파일에서 import 하여 사용 불가능