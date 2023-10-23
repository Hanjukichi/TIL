# Typescript 타입

## Ⅰ. 타입 지정 방법
- `{변수명}:{타입명}` 방식으로 지정
- 타입에 맞지 않는 값을 넣으면 오류
```ts
let car:string = "hyundai"
```

<br>

## Ⅱ. 기본 타입 종류
```ts
// 숫자
let age:number = 27

// 문자열
let name:string = "한주"

// 불린형
let isAddult:boolean = true

// 배열
let nums1:number[] = [1,2,3,4,5]
let nums2:Array<number> = [1,2,3,4,5]

// 튜플
let tuple1:[number, string] = [1, 'a']
```

<br>

## Ⅲ. 특수 타입
```ts
// void - return 값이 없음
function sayHello():void {
  console.log('hello')
}


// never - 항상 에러를 반환 or 끝나지 않는 함수
function showError():never {
  throw new Error();
}

function inLoop():never {
  while (true) {}
}


// enum - 인덱스(숫자)와 양방향 맵핑
enum Os {
  first, // 0 or 지정값
  second, // first + 1 or 지정값
  third = 5 // second + 1 or 지정값
}

// 문자 입력시 단방향 맵핑
enum OS {
  first = 'a',
  second = 'b',
  third = 'c'
} 


// null, undefined
let a:null = null
let b:undefined = undefined
```
<br>