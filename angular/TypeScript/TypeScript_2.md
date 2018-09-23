# TypeScript Data Type

- TypeScript는 JavaScript의 superset이기 때문에 JavaScript의 data type을 그대로 이용하면서 추가적인 데이터 타입이 더 존재한다.
- TypeScript는 변수 선언시 `var`을 사용하지 않고 `const`와 `let`을 사용한다.

## boolean
- `true` or `false`
```
let myVar: boolean = false; // primitive type
let myBooleanVar: Boolean = new Boolean(true); // 생성자 함수를 이용한 객체의 생성

console.log(myVar.valueOf()); // autoboxing -> method 호출 가능
console.log(myBooleanVar.valueOf());
```

- boolean type의 변수에 Boolean wrapper object를 assign할 수 없다.
```
let myVar: boolean = new Boolean(true); // code error

console.log(myVar.valueOf());
```

## number
- TypeScript는 정수와 실수 구분하지 않는다.
- 모두 다 `실수`(floating poing valuse)이다.

```
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;

console.log(octal.valueOf());
```

## string
- 문자열. `' '` 또는 `" "` 둘 다 이용
- `template string` : ` 를 이용하여 여러 줄에 걸쳐 문자열 입력 가능 / ${ expr } 형태로  embedded expression 사용 가능

```
let myStr: string = "Hello";
let myNumber: number = 100;

let myTemplateString = `this is
a
sample
Text => ${myNumber + 100} // Text => 200
myStr : ${myStr} // myStr : Hello
`;

console.log(myTemplateString);
```

## Array
- 배열.
- primitive data type이 아닌 객체
```
let myArr: string[] = ["Hello", "Hi", "안녕하세요"];
console.log(myArr);
```

- Array Interface와 generic을 이용할 수 있다.
```
let myNumArr: Array<number> = [1,2,3,4];
console.log(myNumArr);
```

## Tuple
- 특수한 형태의 배열 : 배열의 각 원소마다 다른 data type 허용
- tuple선언에 사용한 data type의 union type을 이용
```
let myTuple: [string, number];

myTuple = ["Hello", 100]; // 가능
myTuple = ["Hello", "world"]; // 위에 선언한 tuple type과 맞지 않기 때문에 에러

console.log(myTuple[0]); // "Hello"
console.log(myTuple[1]); // 100
console.log(myTuple[2]); // undefined 

myTuple[2] = "World" // string 가능
myTuple[2] = 200 // number 가능
myTuple[2] = true; // boolean 불가능
```

## enum
- 숫자 대신 친숙한 이름으로 설정
- 값은 1씩 증가
```
enum Color {Red, Green, Blue}
let myColor: Color = Color.Red;
console.log(myColor); // 0
```
```
enum Color {Red = 1, Green, Blue = 4}
let myColor: Color = Color.Green;
console.log(myColor); // 2

myColor = Color.Blue;
console.log(myColor); // 4
```
[reference](https://moon9342.github.io/typescript-datatype-1)
