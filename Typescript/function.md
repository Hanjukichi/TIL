# Typescript 함수

## Ⅰ. 함수의 타입

### 1. 함수의 타입 지정
- 함수에 들어가는 매개 변수, 결과값 모두 타입 지정 해줘야함
```ts
function add(num1:number, num2:number):number {
  return num1 + num2
}

// 리턴값이 없으면 void
function add(num1:number, num2:number):void {
  console.log(num1 + num2)
}
```

### 2. `this` 타입 지정
- 선언된 인터페이스를 활용한 함수를 사용할 때 `this`에 관한 타입을 따로 지정해줘야함
```ts
interface User {
  name : string;
}

const Sam: User = {name:'sam'}

function showName(this.User, age:number, gender:'m'|'f') {
  console.log(this.name)
}

const a = showName.bind(Sam);
a(30, 'm')
```
<br>

## Ⅱ. 선택적 매개변수

### 1. 선택적 매개변수 선언
- 매개변수 뒤에 `?`를 붙이면 선택적 매개변수가 됨
```ts
function hello(name?: string) {
  return `Hello, ${name || "world"}`
}

// default값 지정
function hello(name = "world") {
  return `Hello, ${name}`
}
```
- 선택적 매개변수는 함수 뒷부분에 선언해야함
```ts
function hello(name:string, age?:number):string {
  if (age === undefined) {
    return `Hello, ${name}`
  } else {
    return `Hello, ${name}. You are ${age}`
  }
}
```

### 2. 나머지 매개변수의 타입 지정
- 매개변수의 개수를 특정할 수 없을 때 배열 형태로 타입 지정
```ts
function add(...nums : number[]) {
  return nums.reduce((result, num) => result + num, 0)
}
```
<br>

##  Ⅲ. 함수 오버로드
- 매개변수의 개수나 타입에 따라 다른 동작을 하게 함

```ts
interface User {
  name: string;
  age: number;
}

function join(name:string, age:string): User
function join(name:string, age:number): User
function join(name:string, age:number|string): User|string {
  if (typeof age === "number") {
    return {
      name,
      age
    };
  } else {
    return "나이는 숫자로 입력해주세요.";
  }
}
```
<br>