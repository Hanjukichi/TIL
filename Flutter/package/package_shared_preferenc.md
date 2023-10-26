# `shared_preferences `

[공식 문서](https://pub.dev/packages/shared_preferences)

## 1. 초기 설정
```dart
final SharedPreferences prefs = await SharedPreferences.getInstance();
```
- 앱 내부 저장소를 이용할 수 있는 패키지
- `SharedPreferences` 클래스를 이용하여 저장소 인스턴스 생성

## 2. `set`
```dart
await prefs.setInt('counter', 10);
await prefs.setBool('repeat', true);
await prefs.setDouble('decimal', 1.5);
await prefs.setString('action', 'Start');
await prefs.setStringList('items', <String>['Earth', 'Moon', 'Sun']);
```
- 저장소에 데이터를 저장하는 방법
- 데이터 타입마다 다른 메서드를 사용

## 3. `get`
```dart
final int? counter = prefs.getInt('counter');
final bool? repeat = prefs.getBool('repeat');
final double? decimal = prefs.getDouble('decimal');
final String? action = prefs.getString('action');
final List<String>? items = prefs.getStringList('items');
```
- 저장소에서 데이터를 들고 오는 방법
- 데이터 타입마다 다른 메서드를 사용

## 4. `remove`
```dart
await prefs.remove('counter');
```
- 저장소의 해당하는 키의 데이터를 삭제
