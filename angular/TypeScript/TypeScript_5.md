# TypeScript Destructuring
- 배열의 요소나 객체의 속성을 배열 literal 혹은 객체 literal과 유사한 형태의 문법을 이용하여 변수에 할당하는 기법

## Array Destructuring
```
let myArr: string[] = ["Hello", "World", "Moon"];

let first: string = myArr[0];
let second: string = myArr[1];
let third: string = myArr[2];

console.log(first);     // "Hello"
console.log(second);    // "World"
console.log(third);     // "Moon"
```
- 위 코드를 Destructuring Assignment(비구조할당) 이용하면
```
let myArr: string[] = ["Hello", "World", "Moon"];

let [first, second, third] = myArr; // 비구조배열

console.log(first);     // "Hello"
console.log(second);    // "World"
console.log(third);     // "Moon"
```
- 비구조배열(Destructuring Array)에 data type을 지정하고 싶은 경우
```
let myArr: string[] = ["Hello", "World", "Moon"];

let [first, second, third]: string[] = myArr;
```
- swap 처리
```
let myArr: string[] = ["Hello", "World"];

let [first, second] = myArr;

console.log(first);     // "Hello"
console.log(second);    // "World"

[second, first] = [first, second];

console.log(first);     // "World"
console.log(second);    // "Hello"
```
- parameter 전달
```
function myFunc([x, y]: [number, number]) : void {
    console.log(`x의 값은 ${x}`);
    console.log(`y의 값은 ${y}`);
}

myFunc([10, 20]);
```
- `...` 이용한 서브배열
```
let myArr: number[] = [1, 2, 3, 4];

let [first, ...others] = myArr;

console.log(first);     // 1
console.log(others);    // 2, 3, 4 (서브배열)
```
- 그 외
```
let myArr: number[] = [1, 2, 3, 4];

let [first] = myArr;

let [, second, , fourth] = myArr;

console.log(first);     // 1
console.log(second);    // 2
console.log(fourth);    // 4
```

## Object Destructuring
- 객체를 비구조할당을 통해 이용해보자.
```
let obj = {
    key1 : "Hello World",
    key2 : 100,
    key3 : "TypeScript"
};

let { key1:a, key2: b } = obj;

console.log(a);     // Hello World
console.log(b);     // 100
```
- 비구조 객체에 쓰이는 변수의 이름과 동일하게
```
let { key1, key2 } = obj;

console.log(key1);     // Hello World
console.log(key2);     // 100
```
```
let {a, b} = {a: "Hello World", b: 100};

console.log(a);     // Hello World
console.log(b);     // 100
```
- `...` 을 이용한 서브배열 생성
```
let obj = {
    myName: "홍길동",
    myAddress: "서울",
    myAge: 30
};

let {myName, ...otherInfo} = obj;

console.log(`이름은 : ${myName}`);          // 홍길동
console.log(`나이는 : ${otherInfo.myAge}`); // 30
```
- 객체의 property의 이름 바꾸기
(`:`의 의미는 data type을 지정하는 것으로 사용된 것이 아니다.)
```
let obj = {
    a: "홍길동",
    b: "서울",
    c: 30
};

let {a:myName, b:myAddress} = obj;

console.log(`이름은 : ${myName}`);      // 홍길동
console.log(`주소는 : ${myAddress}`);   // 서울
```
- 데이터 타입을 지정해서 사용하기.
```
let {a:myName, b:myAddress}: {a:string, b:string} = obj;
```
- default 값 지정
```
let obj: {myName:string, myAge?:number} = {
    myName : "홍길동",
};

let {myName:uNname, myAge:uAge = 30} = obj;

console.log(uName);     // 홍길동
console.log(uAge);      // 30
```
- `myAge?:number`의 `?` :  해당 property가 있을수도 있고 없을 수도 있다는 뜻.

## 응용
- Map사용에 응용할 수 있다.
```
let map = new Map();

map.set("myName", "홍길동");
map.set("myAddress","서울");
map.set("myAge", 30);

for(let [key, value] of map){
    console.log(`${key} 의 값은 ${value} 입니다.`);
}
for(let [key] of map){ // 모든 key 값만을 출력
    console.log(`${key}`);
}
for(let [value] of map){ // 모든 value 값만을 출력
    console.log(`${value}`);
}
```
- 함수의 리턴값에 응용
```
function myFunc(): string[] {
    let arr: string[] = [];
    // 로직처리 ...
    arr[0] = "첫번째 결과값";
    arr[1] = "두번째 결과값";

    return arr;
}

let [result1, result2] = myFunc();

console.log(result1);
console.log(result2);
```
- 객체를 리턴받는 경우
```
function myFunc(): {result1:string, result2?:number} {

    let obj = {
        result1 : "",
        result2 : 0
    };
    // 로직처리 ...
    obj.result1 = "첫번째 결과값";
    obj.result2 = 100;

    return obj;
}

let {result1:first, result2:second} = myFunc();

console.log(first);
console.log(second);
```
[reference](https://moon9342.github.io/typescript-destructuring) 