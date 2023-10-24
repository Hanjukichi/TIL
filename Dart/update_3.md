# Dart 3 신규 문법

## Ⅰ. Record

### 1. 기본 사용법
```dart
// main 함수
void main() {
  final result = nameAndAge({
    'name' : '민지',
    'age' : 20
  });
  
  print(result.$1);
  print(result.$2);
}

// Record 활용 함수
(String, int) nameAndAge(Map<String, dynamic> json) {
  return (json['name'] as String, json['age'] as int);
}
```
- 타언어의 튜플과 비슷
- `$숫자`로 요소에 접근 가능
- 타입과 타입의 순서를 보장받을 수 있음
- 이후 자동 완성에 도움

### 2. 네이밍
```dart
// main 함수
void main() {
  final fruits = getFruitsType();
  print(fruits);
}

// Record 활용 함수
List<(String name, int price)> getFruitsType() {
  return [
    ('apple', 3000),
    ('banana', 2000)
  ];
}
```
- 가독성을 위해 네이밍을 달아줄 수 있음

### 3. Map처럼 활용
```dart
// main 함수
void main() {
  final fruits = getFruitsType();
  for (final fruit in fruits) {
    print(fruit.name);
  }
}

// Record 활용 함수
List<({String name, int price})> getFruitsType() {
  return [
    (name: 'apple', price: 3000),
    (name: 'banana', price: 2000)
  ];
}
```
- 자체에 key를 붙여줄 수 있음
- key값으로 value에 접근 가능
  
<br>

## Ⅱ. Distruction

### 1. 기본 사용법
```dart
// main 함수
void main() {
  final (name, price) = ('사과', 2000);
  
  print(name);
  print(price);
}
```
- 한 번에 변수 할당 가능
- Record 뿐만 아니라 거의 모든 데이터 타입에 적용 가능

### 2. rest match
```dart
// main 함수
void main() {
  final numbers = [1,2,3,4,5,6,7,8];
  final [x, y, ..., z] = numbers;
  final [x, y, ...rest, z] = numbers;
}
```
- 중간 요소들을 생략 가능
- 따로 변수에 넣어줄 수도 있음
- 딱 한 번 사용 가능

### 3. ignore
```dart
// main 함수
void main() {
  final numbers = [1,2,3,4,5,6,7,8];
  final [x, _, y, ..., z, _] = numbers;
}
```
- 요소를 무시할 수도 있음
- `_`를 사용

### 4. Map
```dart
// main 함수
void main() {
  final fruits = {'name': '사과', 'price': 20};
  final {'name': name1, 'price': price1} = fruits;
}
```
- value 위치에 변수를 선언해줘야함

### 5. Class
```dart
// main 함수
void main() {
  final fruit = Fruit(name: "사과", price: 2000);
  final Fruit(name: name1, price: price1) = fruit;
}

// Fruit 클래스
class Fruit {
  final String name;
  final int price;
  
  Fruit({
    required this.name,
    required this.price,
  });
}
```
- class에도 적용 가능

<br>

## Ⅲ. Pattern Match

### 1. Validation
```dart
// main 함수
void main() {
  final fruit = ("사과", 2000);
  
  final (name as String, price as int) = fruit;
}
```
- 타입을 미리 지정해줘서 사전에 오류 발견 가능
- 만약 타입이 잘못되었다면 런타임 오류 발생 

### 2. switch match
```dart
// main 함수
void main() {
  switcher([1, 2, 3]);
  switcher([1, 4]);
}

// 스위치 함수
void switcher(dynamic anything) {
  switch(anything) {
    case [_, _, _]:
      print('match : [_, _, _]');
    case [int a, int b]:
      print('match : [int $a, int $b]');
    default:
      print('not match');
  }
}
```
- `switch`문에도 패턴 매칭 가능
- 변수로 선언해줬다면 활용 가능

### 3. 화살표 `switch`
```dart
// main 함수
void main() {
  switcher(5, true);
  switcher(5, false);
}

// switcher 함수
void switcher(dynamic val, bool condition) => switch (val) {
  5 when condition => print('match: 5'),
  // default
  _ => print('no match')
};
```
- 화살표를 사용해서 swtich를 정의 가능
- `default`는 `_`로 대체
- `when`으로 추가 조건 정의 가능

### 3. for match
```dart
// main 함수
void main() {
  final List<Map<String, dynamic>> fruits = [
    {'name': "사과", "price": 3000},
    {'name': "바나나", "price": 2000},
  ];
  
  for (var {'name': name, 'price': price} in fruits) {
    print(name);
    print(price);
  }
}
```

### 4. if match
```dart
// main 함수
void main() {
  final Map<String, dynamic> fruit = {'name': "사과", "price": 3000};
  if (fruit case {'name': String name, 'price': int price}) {
    print(name);
    print(price);
  };
}
```
- `case`를 활용해 `if` 안에서도 패턴 매칭 가능

<br>

## Ⅳ. Class 추가 기능

### 1. `final`
```dart
final class Person{
  final String name;
  final int age;
  
  Person({
    required this.name,
    required this.age
  });
}
```
- class에 `final` 키워드 추가 가능
- 다른 파일이면 `extends`, `implements`, `mixin`으로 사용 불가능

### 2. `base`
```dart
base class Person{
  final String name;
  final int age;
  
  Person({
    required this.name,
    required this.age
  });
}
```
- class에 `base` 키워드 추가 가능
- 다른 파일이면 `extends`는 가능하지만 `implements` 불가능

### 3. `interface`
```dart
interface class Person{
  final String name;
  final int age;
  
  Person({
    required this.name,
    required this.age
  });
}
```
- class에 `interface` 키워드 추가 가능
- 다른 파일이면 `implements`만 가능

### 4. `seald`
```dart
sealed class Person {}

class Developer extends Person {}

class Police extends Person {}

void whoIsHe(Person person) => switch(person) {
    Developer d => print('d'),
    Police p => print('p'),
};
```
- class에 `sealed` 키워드 추가 가능
- `abstract`이면서 `final`이다
- 패턴매칭을 사용할 수 있게 해줌
- 모든 경우의 수를 `switch`문에 넣어줘야 에러발생 x