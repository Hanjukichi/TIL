# `url_launcher `

[공식 문서](https://pub.dev/packages/url_launcher)

## 1. 기본 사용법
```dart
void onButtonTap() async {
  final url = Uri.parse('https://comic.naver.com/webtoon/detail?titleId=$webtoonId&no=${episode.id}');
  await launchUrl(url);
}
```
- url를 `parse` 해줌
- `launchUrl`함수를 이용하여 해당 url의 브라우저를 띄워줌