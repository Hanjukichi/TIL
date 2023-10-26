# Flutter 시작하기

## Ⅰ. `main` 함수
```dart
void main() {
  runApp(App());
}
```
- 시작점이 되는 함수
- `App`은 최상위 루트 앱

<br>

## Ⅱ. Root App
```dart
class App extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        ...
      )
    );
  }

}
```
- 최상위 앱
- `build` 메서드 필수
- 최상위 위젯은 `CupertinoApp`(애플 스타일) 또는 `MaterialApp`(구글 스타일)을 `return` 해야함
- 구글에서 만든 프레임워크라 `MaterialApp`을 추천

### 1. `StatelessWidget`
- 코어 위젯
- 가장 기초적인 위젯
- 상태가 없는 위젯
- 

### 2. `MaterialApp`
- 여러 관련 위젯을 지원해주는 구글 스타일 최상위 위젯

### 3. `Scaffold`
- 레이아웃을 상단바, 몸통, 하단 등으로 구분 할 수 있게 여러 위젯들을 지원
- appBar, body 등으로 레이아웃 구분

<br>

<br>

## Ⅲ. VSCode 관련 팁

### 1. `const` 자동 입력 및 부모 위젯 표시
1. 설정 json으로 이동
  - Ctrl + Shift + P
  - `Open User Setting(json)` 입력
2. 아래 문구 입력
```json
"editor.formatOnSave": true,
"editor.codeActionsOnSave": {
    "source.fixAll": true
},

"dart.previewFlutterUiGuides": true,
```

### 2. 부모 위젯으로 감싸기
1. 전구 클릭 후 `wrap ~~~` 선택
2. `ctrl + .` 입력 후 `wrap ~~~` 선택
3. 부모 위젯 삭제도 가능
4. 위젯 위치 이동도 가능

<br>

## Ⅳ. 패키지 설치
```
dart pub add 패키지명
```
```
flutter pub add 패키지명
```
```yaml
# pubspec.yaml
dependencies:
  package version
```