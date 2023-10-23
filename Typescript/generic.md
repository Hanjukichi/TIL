# Typescript Generic

## Ⅰ. 기본 사용법
- 함수에서 매개변수로 여러 타입을 사용해야할 경우 사용
- 보통 `T`를 사용
- 'type parameter'라고 함
```ts
function getSize<T>(arr:T[]):number {
  return arr.length;
}

const arr1 = [1,2,3];
getSize<number>(arr1);

const arr2 = ["a","b","c"];
getSize<string>(arr2);
```
<br>

## Ⅱ. 인터페이스에서의 사용
- generic으로 선언해준 속성은 인스턴스 생성 때 자유롭게 정의 가능
```ts
interface Mobile<T> {
  name : string;
  price : number;
  option : T;
}

const m1:Mobile<{color:string; coupon:boolean}> = {
  name : 'a',
  price:1000,
  option: {
    color: 'red',
    coupon:false,
  }
}
const m2:Mobile<string> = {
  name : 'b',
  price: 2000,
  option: 'good'
}
```
- 인스턴스를 변수로 사용하는 함수에서도 사용 가능
- 인스턴스의 속성이 존재하는지 선언한 타입이 맞는지 확인하고 오류 반환
```ts
interface User {
  name: string;
  age: number;
}

interface Car {
  name: string;
  color :string;
}

interface Book {
  price: number;
}

const user:User = {name:"a", age:10};
const car:Car = {name:"b", color:"red"};
const book:Book = {price:3000};

function showName<T extends {name:string}>(data:T):string {
  return data.name;
}

showName(user);
showName(car);
showName(book);  // 오류 발생
```