# Dart 컬렉션

## Ⅰ. `List`

### 1. `List`란?
```Dart
void main() {
  List<String> fruits = ["사과", "오렌지", "배", "포도"];
  print(fruits);
  print(fruits[0]);
  
  fruits[3] = "귤";  // 리스트의 원소 변경
  print(fruits);
}
```
- 여러값을 순서대로 한 변수에 저장
- 리스트의 구성 단위를 원소라고 함
- `리스트명[인덱스]` 형식으로 특정 원소에 접근

### 2. `List` 관련 함수들

#### `toList()`
- 리스트가 아닌 배열을 `List`타입으로 변경

#### `length`
```Dart
void main() {
  List<String> fruits = ["사과", "오렌지", "배", "포도"];
  print(fruits.length);
}
```
- 리스트의 길이 반환

#### `add()`
```Dart
void main() {
  List<String> fruits = ["사과", "오렌지", "배", "포도"];
  fruits.add("귤");
  print(fruits);
}
```
- 리스트에 원소 추가

#### `where()`
```Dart
void main() {
  List<String> fruits = ["사과", "오렌지", "배", "포도"];
  
  final newList = fruits.where( 
    (fruit) => fruit == "오렌지",
  );
  
  print(newList);
}
```
- 조건에 맞는 원소들만 이터러블로 반환

#### `map()`
```Dart
void main() {
  List<String> fruits = ["사과", "오렌지", "배", "포도"];
  
  final newList = fruits.map( 
    (fruit) => '과일 $fruit',
  );
  
  print(newList);
}
```
- 리스트에 있는 값들을 변경
- 기존 원소를 하나씩 매개변수로 받는 함수 입력
- 그 함수의 반환값이 현잿값을 대체

#### `reduce()`
```Dart
void main() {
  List<String> fruits = ["사과", "오렌지", "배", "포도"];
  
  final allFruits = fruits.reduce((value, element) => 
    value + ", " + element
  );
  
  print(allFruits);
}
```
- 순회할 때마다 값을 쌓아감
- 리스트 구성요소와 함수 반환값의 타입이 같아야함
  
#### `fold()`
```Dart
void main() {
  List<String> fruits = ["사과", "오렌지", "배", "포도"];
  
  final numFruits = fruits.fold(0, (value, element) => 
    value + element.length
  );
  
  print(numFruits);
}
```
- `reduce()`와 같은 실행 논리
- 리스트 구성요소와 함수 반환값의 타입이 달라도 됨
  
<br>

## Ⅱ. `Map`

```Dart
void main() {
  Map<String, int> price = {
    "사과" : 1000,
    "바나나" : 500,
    "오렌지" : 1500
  };
  
  print(price["사과"]);
  print(price.keys);
  print(price.values);
}
```
- key와 value의 짝을 저장
- key와 value들을 모두 이터러블로 반환 가능 

<br>

## Ⅲ. `Set`

### 1. `Set`이란?
```Dart
void main() {
  Set<String> fruits = {'사과', '오렌지', '사과'};  // 사과 중복
  print(fruits);
  
  final fruitsList = fruits.toList();
  print(fruitsList);
  
   final fruitsSet = Set.from(fruitsList);
  print(fruitsSet);
}
```
- 중복없는 값들의 집합

### 2. `Set` 관련 함수

#### `contains()`
```Dart
void main() {
  Set<String> fruits = {'사과', '오렌지', '사과'};  // 사과 중복
  print(fruits.contains("사과"));
  print(fruits.contains("포도"));
}
```
- 값이 있는지 없는지 확인

#### `Set.from()`
```Dart
void main() {
  List<String> fruits = ['사과', '오렌지', '사과'];  
  final fruitsSet = Set.from(fruits);
  print(fruitsSet);
}
```
- 리스트를 `Set`타입으로 변경
- 중복값 제거

<br>

## Ⅳ. `enum`
```Dart
enum Status {
  approved,
  pending,
  rejected
}

void main() {
  Status status = Status.approved;
  print(status);
}
```
- 한 변수의 값을 몇 가지 옵션으로 제한하는 기능
- 자동 완성 지원
- 정확히 어떤 선택지가 존재하는지 정의
  
