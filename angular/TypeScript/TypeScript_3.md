# TypeScript Data Type

- TypeScript의 색다른 data type에 대해 알아보자.

## any
- 어떤 변수의 data type을 결정할 수 없는 경우 : `어떠한 data type도 될 수 있다`
- 특정 목적을 제외하고는 당연히 사용하지 않는 것이 좋다.
```
let myVar: any = 100;

myVar = "Hello World!!" // 가능
myVar = true; // 가능
```
```
let myArr: any[] = [100, "Hello", true]; // 가능
```

## void
- 함수의 리턴 type : 함수가 리턴값이 없을 떄 사용
```
function myFunc(name: string) : void {
    console.log(`Hello, ${name}!!`);
}

myFunc("Moon");
```
- 변수 type : `null` 또는 `undefined`만 할당 가능
- `tsconfig.json` 안에 `compilerOptions` 부분에 `"strictNullChecks" : false`
```
let myVar: void;
myVar = 100;        // 불가능(에러)
myVar = "Hello";    // 불가능(에러)
myVar = null;       // 가능
myVar = undefined; // 가능
```

## null & undefined
- 값이자 하나의 data type
- 다른 모든 type의 subtype : 다른 모든 type에 null과 undefined 할당 가능
```
let myNull: null = null;
let myUndefined: undefined = undefined;
```
- .ts파일을 컴파일 할 경우 `strictNullChecks` flag를 이용할 때 : void 혹은 자신의 data type에만 null과 undefined 할당 가능 
- `tsconfig.json` 안에 `compilerOptions` 부분에 `"strictNullChecks" : false` 한 경우
```
let myName: string = "홍길동";
let myVoid: void;
let myNull: null;
let myUndefined: undefined;

myName = null;      // 가능
myName = undefined; // 가능

myVoid = null;      // 가능
myvoid = undefined; // 가능

myNull = null;      // 가능
myNull = undefined; // 가능

myUndefined = null;      // 가능
myUndefined = undefined; // 가능
```
- `tsconfig.json` 안에 `compilerOptions` 부분에 `"strictNullChecks" : true` 한 경우
```
let myName: string = "홍길동";
let myVoid: void;
let myNull: null;
let myUndefined: undefined;

myName = null;      // 불가능
myName = undefined; // 불가능

myVoid = null;      // 불가능
myvoid = undefined; // 불가능

myNull = null;      // 불가능
myNull = undefined; // 불가능

myUndefined = null;      // 불가능
myUndefined = undefined; // 불가능
```

## never
- 함수의 리턴 type : 항상 exception 발생 혹은 절대 return 되지 않음(무한 루프)
```
function error(message: string): never{
    throw new Error(message);
}
error("Somthing Wrong!!");

function infiniteLoop(): never{
    while(true){

    }
}
```

## type assertions
- type casting과 같은 의미로 사용
- 실제 특별한 체크작업이나 데이터 재구조화 작업 발생하지 않는다.(TypeScript가 따로 검증하지 않는다.)
- `<>` 과 `as` syntax를 이용하여 나타냄
- data type `any`와 함께 사용되는 경우가 많으며 데이터 타입을 한정지어서 사용할 수 있도록 도와준다. 
```
let myVar: any = "Hello World";
let myVarCount: number = (<string>myVar).length;
myVarCount = (myVar as string).length;
console.log((<number>myVar).toFixed()); // runtime error
```
[reference](https://moon9342.github.io/typescript-datatype-2)