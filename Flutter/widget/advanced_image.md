# `Image`

## 1. `Image.network`
```dart
Image.network(
  thumb,
  headers: const {
    "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
  },
),
```
- 첫번째 인자(`src`) : 온라인 이미지 주소
- `header` : 이미지 로드 시 토큰 등의 인증이 필요하다면 설정해줘야함 