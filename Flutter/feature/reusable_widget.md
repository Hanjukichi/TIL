# 재사용가능한 위젯 만들기

## Ⅰ. 위젯 정의
```dart
// button.dart
import 'package:flutter/material.dart';

class Button extends StatelessWidget {
  // 사용자가 정의해줄 속성들
  final String text;
  final Color bgColor;
  final Color textColor;

  // 생성자
  const Button({
    super.key,
    required this.text,
    required this.bgColor,
    required this.textColor,
  });

  // 빌드
  @override
  Widget build(BuildContext context) {
    return Container(
        decoration: BoxDecoration(
          color: bgColor,
          borderRadius: BorderRadius.circular(45),
        ),
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 50),
          child: Text(
            text,
            style: TextStyle(
              color: textColor,
              fontSize: 20,
            ),
          ),
        ));
  }
}

```
- 위젯마다 달라지는 값들은 따로 정의 가능
- 변수로 빌드 부분에 값을 넣어줄 시 `const`는 빼줘야함

## Ⅱ. 정의한 위젯 사용
```dart
...
children: [
  Button(
      text: "Transfer",
      bgColor: Color(0xFFF1B33B),
      textColor: Colors.black),
  Button(
      text: "Request",
      bgColor: Color(0xFF1F2123),
      textColor: Colors.white)
],
...
```
- 필요하다 정의해준 프로퍼티는 입력해줘야함
- 자동완성 지원
- 자동 완성 시 알아서 `import` 해줌