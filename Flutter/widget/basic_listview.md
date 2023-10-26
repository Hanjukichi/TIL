# `ListView`

## 1. 기본 사용법
```dart
ListView(
  children: [
    for (var webtoon in snapshot.data!) Text(webtoon.title)
  ],
);
```
- 기본적인 `ListView` 사용
- 한 번에 모든 리스트를 모두 렌더링함
- 메모리 소비가 클 수도 있음

## 2. `ListView.builder`
```dart
ListView.builder(
  scrollDirection: Axis.horizontal,
  itemCount: snapshot.data!.length,
  itemBuilder: (context, index) {
    var webtoon = snapshot.data![index];
    return Text(webtoon.title);
  },
)
```
- 현재 사용자가 보고 있는 아이템만 빌드
- `ScrollDirection` : 스크롤 방향을 정할 수 있음
- `ItmeCount` : 총 요소의 개수를 정할 수 있음
- `ItemBuilder`
  - 반드시 필요
  - 나머지는 메모리에서 삭제
  - `index` : 사용자가 보고 있는 아이템의 인덱스

## 3. `ListView.separated`
```dart
ListView.separated(
  ...
  separatorBuilder: (context, index) => const SizedBox(
    width: 20,
  ),
);
```
- 기능은 `ListView.builder`와 동일
- `separatorBuilder`가 반드시 필요
  - 아이템 사이에 빌드될 위젯을 정의