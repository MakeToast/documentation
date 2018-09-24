# TypeScript Variable Declarations
- var과 let은 유사하지만 다르다.
- TypeScript에선 let과 const를 이용한다.

## var
- 변수 선언
```
var myVar = 100;
```
- 함수 선언
```
function myFunc(){
    var message = "Hello World";

    return message
}
```
- 내부 함수가 외부 함수가 가지고 있는 변수 참조 가능
```
function outerFunc(){
    var a = 100;

    return fuction(){ // 익명 함수
        var b = a + 100;
        return b;
    }
}

var myFunc = outerFunc();
console.log(myFunc()); // 200 출력
```
- var 변수의 scope는 좀 다르다.
- outerFunc() 함수의 호출이 끝났음에도 a 변수값 유지.

- 내부 함수에서 선언된 변수 외부 함수에서 사용 가능
```
function myFunc(init){
    if (init){
        var x = 10;
    }
    return x;
}
console.log(myFunc(true)); // 10 출력
```
- 중복 선언 가능
```
function f(){
    var x;
    var x;
    if(true){
        var x;
    }
}
```
- var로 선언된 변수는 block에 상관없이 function내에서 사용 가능 : `function-scoping`을 가진다.

## let
- var의 모호성을 해결
- `block-scoping` (lexcial-scoping)을 가진다.
- 중복선언 불가
```
let myVar: string = "Hello World!!";
```
```
function myFunc(input: boolean){
    let a = 100;
    if(input){
        let b = a + 1; // a에 접근 가능
        return b;
    }
    return b; // b에 접근 불가 (에러)
}
```

## const
- const로 선언된 변수에는 재 할당 불가능.
```
const myName: string = "홍길동";
myName = "강감찬"; // 코드 에러
```
- const 변수가 객체를 지칭하면 다른 객체로 reference를 바꾸지는 못한다.
- 하지만 현재 reference하고 있는 객체의 속성의 값은 변경 가능.
```
const count: number = 100;
const myProfile = {
    myName: "홍길동",
    myAddress: "서울",
    myCount: count
};

myProfile = {       // 코드 에러 (재할당 안됨)
    myName: "강감찬",
    myAddress: "인천",
};

myProfile.myName = "강감찬";    // 가능
myProfile.myAddress = "인천";
myProfile.myCount = 10;
```
[reference](https://moon9342.github.io/typescript-variable)