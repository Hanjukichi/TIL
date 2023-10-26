# `http`

[공식문서](https://pub.dev/packages/http)

## 1. 사용법
```dart
import 'package:http/http.dart' as http;

final url = Uri.parse('$baseurl/$today');
final response = await http.get(url);
```
- 외부 패키지로 별도로 다운받아야함
- `get` 말고도 `post` 등 다양한 http method 사용 가능

## 2. `Uri`
```dart
final url = Uri.parse('$baseurl/$today');
```
- 입력한 url은 `Uri` 클래스르 통해 변형해야함

<br>