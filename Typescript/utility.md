# Typescript 유틸리티 타입

## `keyof`
- 인터페이스의 키값들을 유니온 형태로 받을 수 있음
```ts
interface User {
  id: number;
  name: string;
  age: number;
  gender: 'm'|'f';
}

type UserKey = keyof User; // 'id' | 'name' | 'age' | 'gender
const uk:UserKey = "id"
```

## `Partial<T>`
- 속성을 모두 Optional로 바꿔줌
```ts
interface User {
  id: number;
  name: string;
  age: number;
  gender: 'm'|'f';
}

// 모든 속성을 정의하지 않아도 됨
let admin:Partial<User> = {
  id:1,
  name: "hanju"
}
```

## `Required<T>`
- 모든 속성값을 필수값으로 바꿔줌
```ts
interface User {
  id: number;
  name: string;
  age?: number;
}

let admin:Required<User> = {
  id:1,
  name: "hanju"
}
```

## `Readonly<T>`
- 처음에 할당만 가능하고, 값 교체 불가능
```ts
interface User {
  id: number;
  name: string;
  age?: number;
}

let admin:Readonly<User> = {
  id:1,
  name: "hanju"
}

admin.id = 4  // 오류 발생
```

## `Record<K,T>`
- 키와 타입을 따로 정의해서 사용 가능 

```ts
type Grade = 1 | 2 | 3 | 4
type Score = "A" | "B" | "C" | "D"

const score: Record<Grade, Score> = {
  1: "A",
  2: "B",
  3: "C",
  4: "D"
}
```

## `Pick<T, K>`
- 입력한 속성들만 정의 가능
```ts
interface User {
  id: number;
  name: string;
  age: number;
  gender: "M" | "W";
}

const admin: Pick<User, "id" | "name"> = {
  id: 0,
  name: "Bob"
}
```

## `Omit<T, K>`
- 특정 속성 제외 가능
```ts
interface User {
  id: number;
  name: string;
  age: number;
  gender: "M" | "W";
}

const admin: Omit<User, "age" | "gender"> = {
  id: 0,
  name: "Bob"
}
```

## `Exclude<T1, T2>`
- T1 타입에서 T2에 해당하는 타입 제외
```ts
type T1 = string | number | boolean;
type T2 = Exclude<T1, number | string>
```

## `NonNullable<T>`
- null, undefined를 타입에서 제외

```ts
type T1 = string | null | undefined | void;
type T2 = NonNullable<T1>;
```