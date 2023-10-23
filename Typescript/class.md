# Typescript 클래스

## Ⅰ. 타입스크립트 클래스 선언
- 생성자에서 사용할 변수는 미리 클래스 내부에서 선언되어있어야함
- 그렇지 않을 경우 접근 제한자를 선언해주어야함
```ts
class Car {
  color: string;
  constructor(color: string) {
    this.color = color;
  }
  start() {
    console.log("start")
  }
}
```
<br>

## Ⅱ. 접근 제한자

### `public`
- 아무것도 선언하지 않으면 자동으로 `public`으로 선언
- 자식 클래스, 자식 인스턴스에서도 부모 변수에 접근 가능
```ts
class Car {
  name:string = "car";
  color: string;
  constructor(color: string) {
    this.color = color;
  }
  start() {
    console.log("start")
  }
}

class BMW extends Car {
  constructor(color:string) {
    super(color);
  }
  showName() {
    console.log(super.name);
  }
}
```

### `private`
- 해당 클래스 내부에서만 접근 가능
- `#`으로도 선언 가능
```ts
class Car {
  #name:string = "car";
  color: string;
  constructor(color: string) {
    this.color = color;
  }
  start() {
    console.log("start")
  }
}

class BMW extends Car {
  constructor(color:string) {
    super(color);
  }
  showName() {
    // 오류 발생
    console.log(super.name);
  }
}
```

### `protected`
- 자식 클래스 내부에서는 접근 가능하나 자식 인스턴스에서는 접근 불가능
```ts
class Car {
  protected name:string = "car";
  color: string;
  constructor(color: string) {
    this.color = color;
  }
  start() {
    console.log("start")
  }
}

class BMW extends Car {
  constructor(color:string) {
    super(color);
  }
  showName() {
    console.log(super.name);
  }
}

const z4 = new BMW("black");
console.log(z4.name);  // 오류 발생
```
<br>

## Ⅲ. 속성 변경 제한
- `readonly`로 선언된 속성은 따로 변경 불가능
- 변경하려면 생성자를 통해 변경해야함
```ts
class Car {
  readonly name:string = "car";
  color: string;
  constructor(color: string, name:string) {
    this.color = color;
    this.name = name;
  }
  start() {
    console.log("start")
  }
}

class BMW extends Car {
  constructor(color:string, name:string) {
    super(color, name);
  }
  showName() {
    console.log(super.name);
  }
}

const z4 = new BMW("black", "zzzzzz");
```
<br>


## Ⅳ. static 속성
- `static`으로 선언한 속성은 `{class명}.{속성명}`으로 접근 가능
```ts 
class Car {
  readonly name:string = "car";
  color: string;
  static wheels = 4;
  constructor(color: string, name:string) {
    this.color = color;
    this.name = name;
  }
  start() {
    console.log("start")
  }
}

console.log(Car.wheels);
```
<br>

## Ⅴ. 추상 클래스
- `abstract`로 선언된 클래스는 변수에 할당할 수 없음
- 반드시 자식 클래스가 상속받아 사용해야함
- `abstact`로 선언된 메서드는 상속받는 자식 클래스에서 반드시 구체적으로 구현해야함
```ts
abstract class Car {
  readonly name:string = "car";
  color: string;
  constructor(color: string, name:string) {
    this.color = color;
    this.name = name;
  }
  abstract doSomething():void;
}

// 오류 발생 - doSomething()를 정의해줘야함
class BMW extends Car {
  constructor(color:string, name:string) {
    super(color, name);
  }
}

// 오류 발생 - 추상 클래스라 이런 식으로 사용 불가
const car = new Car();
```