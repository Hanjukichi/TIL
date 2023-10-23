# Dart 형변환

## Ⅰ. `toSet()`
```dart
void main() {
  List<int> numbers = [1,2,3,4,5];

  print(numbers.toSet());
}

```
- `Set` 으로 타입 변경

## Ⅱ.`asMap()`
```dart
void main() {
  List<int> numbers = [1,2,3,4,5];

  Map numbersMap = numbers.asMap();
}
```
- `Map`으로 타입 변경
- 인덱스가 key가 됨

## Ⅲ. `toList()`
```dart
void main() {
  List<int> numbers = [1,2,3,4,5];

  Map numbersMap = numbers.asMap();

  print(numbersMap.values.toList())
}
```
- `List`로 타입 변경