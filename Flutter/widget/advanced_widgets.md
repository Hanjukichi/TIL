# 추가 위젯들

## `SingleChildScrollView`
```dart
body: SingleChildScrollView(
  child: ...
)
```
- UI 길이가 길어 화면에 다 나타나지 않을 시 사용
- 스크롤을 가능하게 함

<br>

## `CircularProgressIndicator`
```dart
Center(
  child: CircularProgressIndicator(),
);
```
- 로딩 시 사용하기 좋은 위젯

<br>
  
## `Hero`
```dart
  Hero(
    tag: id,
    ...
  )
```
- `navigator`로 스크린을 이동할 때 위젯을 없애고 다시 만들지 않음
- `tag`를 공유하는 위젯을 재활용
