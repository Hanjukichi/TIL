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

### 2. cascading operation
```dart
void main() {
  List<int> evens = [2,4,6,8];
  List<int> odds = [1,3,5,7,9];
  
  print([...evens, ...odds]);
}
```
- `...`을 통해 리스트 원소를 풀어서 저장할 수 있음
- 풀어서 다른 배열에 저장하면 다른 인스턴스가 됨

### 3. `List` 관련 함수들

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
- 초기값을 설정해줘야함
- `reduce()`와 같은 실행 논리
- 리스트 구성요소와 함수 반환값의 타입이 달라도 됨
  
<br>

## Ⅱ. `Map`

### 1. `Map`이란?
```Dart
void main() {
  Map<String, int> price = {
    "사과" : 1000,
    "바나나" : 500,
    "오렌지" : 1500
  };
  
  print(price["사과"]);
}
```
- key와 value의 짝을 저장
- 보통 key로 값에 접근

### 2. `key`, `value` 추출
```Dart
void main() {
  Map<String, int> price = {
    "사과" : 1000,
    "바나나" : 500,
    "오렌지" : 1500
  };
  
  print(price.keys);
  print(price.values);
}
```
- key와 value들을 모두 따로 이터러블로 추출 가능 

### 3. `Map` 관련 함수

#### `map`
```dart
void main() {
  Map<String, int> prices = {
    "사과" : 1000,
    "바나나" : 500,
    "오렌지" : 1500
  };
  
  final result = prices.map((key, value) {
    return MapEntry(key, value + 500);
  });
}
```
- `List`처럼 `map` 활용 가능
- `key`와 `value` 모두 인자로 입력해줘야함
- `MapEntry` 클래스 활용

<br>

## Ⅲ. `Set`

### 1. `Set`이란?
```Dart
void main() {
  Set<String> fruits = {'사과', '오렌지', '사과'};  // 사과 중복
  print(fruits);
  
  final fruitsList = fruits.toList();
  print(fruitsList);
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

#### `map`
```dart
void main() {
  Set numberSet = {1,2,3,4,4};
  
  final newNumberSet = numberSet.map((x) => x * 2).toSet();
  
  print(newNumberSet);
}
```
- `map` 메서드 활용 가능
- `List`로 변환해주기 때문에 `Set`으로 변환해줘야함

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


## Ⅴ. 집합과 클래스의 응용
```dart
// main 함수
void main() {
  final List<Map<String, String>> people = [
    {"name": "A", "departure": "E"},
    {"name": "B", "departure": "F"},
    {"name": "C", "departure": "G"},
    {"name": "D", "departure": "H"},
  ];
  
  final parsedPeople = people.map(
    (x) => Person(
      name: x['name']!,
      departure: x['departure']!
    )
  );
}

// Person 클래스
class Person {
  final String name;
  final String departure;
  
  Person({
    required this.name,
    required this.departure,
  });
}
```
- 배열의 요소 또한 class로 선언해줄 수 있음
  
