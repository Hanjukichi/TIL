# Typescript 유니온/교차 타입

## Ⅰ. Literal Types
- 정해진  값을 가지고 있는 변수 or Type
```ts
const userName1 = "Bob";
// 문자형
type Job = "police" | "developer" | "teacher";
// 숫자형
type Num = 1 | 2 | 3
```
<br>

## Ⅱ. Union Types

### 1. 유니온 타입이란?
- 변수 값이 여러 타입을 가지는 경우에 사용
```ts
let age:number|string = 10;
```

## 식별 가능한 유니온 타입
- 여러 타입을 사용하여 오류가 발생할 경우 타입을 식별할 수 있는 처리를 해줘야함
```ts
interface Car {
  name: 'car';
  color: string;
  start(): void;
}

interface Mobile {
  name : "mobile";
  color : string;
  call(): void;
}

function getGift(gift: Car|Mobile) {
  console.log(gift.color);
  // name이 식별자가 됨
  if (gift.name === "car") {
    gift.start();
  } else {
    gift.call();
  }
}
```
<br>

## Ⅲ. intersection Types(교차 타입)
- and의 기능
- 교차된 모든 타입의 속성을 할당해줘야함
```ts
interface Car {
  name: string;
  start(): void;
}

interface Toy {
  name : string;
  color : string;
  price: number;
}

const toyCar: Toy & Car = {
  name: "타요",
  start() {},
  color: "red",
  price: 500
}
```