# TypeScript Interface

- 새로운 데이터 타입을 만드는 추상 데이터 타입(abstract data type)으로 사용
- 일반 변수, 함수, 클래스의 type check를 위해 사용
- 프로그래밍의 일관성 확보 : interface 안에 명시된 property의 선언과 method의 구현 강제

## Basic Example
```
interface IBook{
    bookName: string;
    bookAuthor: string;
}

let myBook: IBook;

myBook = {
    bookName: "젊은 베르테르의 슬픔",
    bookAuthor: "괴테"
};

console.log(myBook);
```
- .ts 파일을 컴파일 한 결과 interface에 대한 내용은 포함되어 있지 않는다.
- type check를 위한 용도로 사용
```
"use strict";
var myBook;
myBook = {
    bookName: "젊은 베르테르의 슬픔",
    bookAuthor: "괴테"
};
console.log(myBook);
```

## Parameter Type Check
- 함수의 인자를 넘길 때
```
interface IBook{
    bookName: string;
    bookAuthor: string;
}

function printBookInfo(paramBook: IBook) : void{
    console.log(paramBook.bookName);
}

myBook = {
    bookName: "젊은 베르테르의 슬픔",
    bookAuthor: "괴테"
};

printBookInfo(myBook);
```

## Duck Typing
- class의 상속이나 interface의 구현으로 타입을 구분하는 것이 아니라 객체가 특정 타입에 걸맞는 property와 method를 가지고 있으면 해당 type으로 간주한다.
```
interface IBook{
    bookName: string;
    bookAuthor: string;
}

function printBookInfo(paramBook: IBook) : void{
    console.log(paramBook.bookName);
}

myBook = {
    bookName: "젊은 베르테르의 슬픔",
    bookAuthor: "괴테",
    bookPrice: 3000 // 정상적으로 코드 실행됨
};

printBookInfo(myBook);
```
- myBook 객체는 비록 IBook interface type은 아니지만 IBook interface type을 모두 커버할 수 있는 값들의 형태를 가지고 있다.
- 따라서 myBook 객체는 IBook interface 타입으로 간주한다.

## Optional Properties
- property 중 `?`가 붙어있는 property 의미.
- 선택적으로 구현여부 결정 : 해당 property는 재정의하지 않아도 상관없다.
```
interface IBook{
    bookName: string;
    bookAuthor: string;
    bookISBN?: string;      // optional property

    getName(): string;
}

function printBookInfo(paramBook: IBook) : void{
    console.log(paramBook.bookName);
    console.log(paramBook.getName());
}

let myBook: IBook = {
    bookName: "젊은 베르테르의 슬픔",
    bookAuthor: "괴테",
    
    getName: function(){
        return this.bookName;
    }
};

printBookInfo(myBook);
```

## Readonly Properties
- 객체가 처음 생성되는 시점에만 property들을 수정가능하도록 설정
- 한 번 값이 세팅되면 그 후에는 수정할 수 없다.
```
interface Point{
    readonly x: number;
    y: number;
}

let p1: Point = {x:10, y:20};
p1.x = 100;     // 오류 발생
```
- `ReadonlyArray<T>` 형태의 Array 지원
```
let arr: number[] = [1,2,3,4];

let roArray: ReadonlyArray<number> = arr;

roArray[0] = 100;       // 코드 에러
roArray.push(100);      // 코드 에러

arr = roArray;          // 코드 에러
arr = roArray as number[];  // 강제 형변환 가능
```
- readonly property 는 const와 비슷한 역할 
- 하지만 const는 변수의 선언에 사용 / readonly 는 property 지정에 사용

## Function Types
- 함수의 타입을 지정하는데 사용 가능
```
interface myInterface{
    (myName: string, myAge: number) : void;
}

let myFunc: myInterface = function(myName:string, myAge:number): void {
    console.log(`이름 : ${myName}, 나이 : ${myAge}`);
};

myFunc("홍길동", 30);
```

## Indexable Types
- interface로 index signature를 설정하여 사용

- JavaScript에서 객체 사용 : `.` operator / `[]` 이용하여 key값에 접근하여 value값 출력
```
let obj = {
    myName: '홍길동',
    myAddress: '서울'
};

console.log(obj.myName); // '.'operator 이용

let keys = Object.keys(obj); // 객체의 key값들에 대한 배열 획득

for(let i = 0 ; i < keys.lengthl i++){
    console.log(obj[keys[i]]);  // 배열 형식 이용
}
```
- .js에서 .ts로 변경시 -> `obj[keys[i]]` error!
- index signature를 이용하지 않았기 때문에 property에 접근할 때 어떤 타입인지 확인할 수 없어서 묵시적으로 any 타입 이용
- TypeScript compiler 옵션 중 `noImplicitAny`속성을 `false`로 바꿔야 한다.
- 더 좋은 해결책은 Indexable Type을 사용.
```
interface IObj {
    [idx: string]: string;
}
let obj: IObj = {
    myName: '홍길동',
    myAddress: '서울'
};

console.log(obj.myName); // '.'operator 이용

let keys = Object.keys(obj); // 객체의 key값들에 대한 배열 획득

for(let i = 0 ; i < keys.lengthl i++){
    console.log(obj[keys[i]]);  // 배열 형식 이용
}
```
- union type 이용
```
interface IObj{
    [idx: stirng]: string | number;
    [index: number]: string | number;
    myName: string;
    myAddress: string;
    myAge: number
}
let obj: IObj = {
    myName: '홍길동',
    myAddress: '서울',
    myAge: 30
};

console.log(obj.myName); // '.'operator 이용

let keys = Object.keys(obj); // 객체의 key값들에 대한 배열 획득

for(let i = 0 ; i < keys.lengthl i++){
    console.log(obj[keys[i]]);  // 배열 형식 이용
}
```
- readonly property 이용 -> ReadonlyArray처럼 사용 가능
```
interface ReadonlyStringArray{
    readonly [index: number]: string;
}
let myArr: ReadonlyStringArray = ["홍길동","강감찬"];
myArr[2] = "이순신";    // 코드 에러
```

## Class Types
- class의 구현을 명시적으로 강제함
JavaScript 코드
```
const PersonFactory = {
    getInstance: function(construct, name, age){
        return new construct(name, age);
    }
};

class Person{
    constructor(name, age){
        this.myName = name;
        this.myAge = age;
    }
    printInfo(){
        console.log("이름:" + this.myName + ", 나이:" + this.myAge);
    }
}

let obj = PersonFactory.getInstance(Person, "홍길동", 30);
obj.printInfo();
```
TypeScript 코드
```
const PersonFactory = {
    getInstance: function(construct:any, name:string, age:number){
        return new construct(name, age);
    }
};

class Person{
    myName: string;
    myAge: number;

    constructor(name:string, age:number){
        this.myName = name;
        this.myAge = age;
    }

    printInfo(){
         console.log("이름:" + this.myName + ", 나이:" + this.myAge);
    }
}

let obj = PersonFactory.getInstance(Person, "홍길동", 30);
obj.printInfo();
```
`any` 없이 정확한 타입 명시
```
interface IPersonConstructor{
    new (n:string, a:number): Person;
}
const PersonFactory = {
    getInstance: function(construct:IPersonConstructor,
                        name: string,
                        age: number){
        return new construct(name, age);
    }
};

class Person{
    myName: string;
    myAge: number;

    constructor(name:string, age:number){
        this.myName = name;
        this.myAge = age;
    }

    printInfo(){
         console.log("이름:" + this.myName + ", 나이:" + this.myAge);
    }
}

let obj = PersonFactory.getInstance(Person, "홍길동", 30);
obj.printInfo();
```
## interface의 확장
- 하나의 interface는 다른 interface로부터 상속받아서 확장 가능
```
interface Shape {
    color: string;
}

interface Square extends Shape{
    sideLength: number;
}

let square = <Square>{};       // type assertions
square.color = "blue";
square.sideLength = 10;
```
- 여러 interface 상속 가능
```
interface Shape{
    color: string;
}
interface PenStroke{
    penWidth: number;
}
interface Square extends Shape, PenStroke{
    sideLength: number;
}

let square = <Square>{};
square.color = "blue";
square.sideLength = 10;
square.penWidth = 5.0;
```
- interface는 type check를 위해 사용되기 때문에 객체를 생성할 수 없다!!
[reference](https://moon9342.github.io/typescript-interface) 