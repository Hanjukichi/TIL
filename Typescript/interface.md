# Typescript 인터페이스


## Ⅰ. 인터페이스 구조

### 1. 기본 사용법
- `Object` 사용에 의한 오류를 해결하기 위해 사용
- `interface`를 사용해 타입을 정의하여 사용
- 정의하지 않은 속성을 사용하면 오류 발생
- 정의한 속성을 사용하지 않아도 오류 발생

```ts
type score = 'A'|'B'|'C'|'F'  // 커스텀 타입(지정된 값 이외에 존재 불가능)

interface User {
    name:string;  // 반드시 사용해야함
    age:number;   // 반드시 사용해야함
    gender?:string;  // 사용 여부가 자유
    readonly birthdayYear:number;  // 최초 할당 후 수정 불가능
    [grade:number]:score;  // 이름은 자유, '숫자 : Score'이 다수 존재 가능
};

let user:User = {
    name : 'hanju',
    age: 27,
    birthdayYear: 1997,
    1: 'A'
}
```

### 2. 함수형 `interface`
- `interface`를 통해 인풋값과 리턴값 타입 지정 가능
```ts
interface Add {
    (num1:number, num2:number): number;
}

const add:Add = function(x,y) {
    return x + y;
}
```

<br>


## Ⅱ. 인터페이스 상속

### 1. `implements`
- 상위 인터페이스의 하위 인터페이스 생성
- 값을 미리 지정해줄 수도 있음, 입력값으로 받을 수도 있음
- `constructor` : 생성자 함수
```ts
interface Car {
  color:string;
  wheels: number;
}

class BMW implements Car {
  color;
  wheels = 4;
  constructor(c:string) {
    this.color = c
  }
}

const a = new BMW('white')
```

### 2. `extends`
- 상위 인터페이스에 추가적인 속성값 부여 가능
- 상위 인터페이스의 필수 입력값들 또한 모두 입력해야함
- 여러 인터페이스 추가 가능
```ts
interface Car {
  color:string;
  wheels: number;
}

interface Machine {
  price:number;
}

interface Benz extends Car, Machine {
  doors: number;
}
```