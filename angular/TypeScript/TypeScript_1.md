# TypeScript Introduction

## TypeScript란

Microsoft에서 개발하여 2012년에 발표한 오픈소스 프로그래밍 언어 

`TypeScript` 의 특징

- TypeScript는 JavaScript의 Superset.
JavaScript의 모든 기능 포함 + 그 외 추가적인 기능
- TypeScript는 컴파일 언어. 
- 컴파일 결과는 JavaScript코드(메타프로그래밍, compile대신 transpile이라고 함)
- 정적 타입 언어  
compile시점에 type checking 

## TypeScript 개발환경

`iTerm` & `vscode`

```
npm install -g typescript
```
(global mode로 설치해야 tsc명령어가 실행이 됐다.)

```
tsc --init  
```
(프로젝트에 tsconfig.json 생성)

- hello.ts파일 생성
```
class Greeting{
    greeting: string;
    constructor(message: string){
        this.greeting = message;
    }
    sayHello(){
        return "Hello "+this.greeting;
    }
}

let tmp = new Greeting("World!!");

console.log(tmp.sayHello());
```

- Compile hello.ts
```
tsc hello.ts
```
(hello.js 생성됨)
- hello.js
```
var Greeting = /** @class */ (function () {
    function Greeting(message) {
        this.greeting = message;
    }
    Greeting.prototype.sayHello = function () {
        return "Hello " + this.greeting;
    };
    return Greeting;
}());
var tmp = new Greeting("World!!");
console.log(tmp.sayHello());
```

- Run TypeScript code
```
node hello.js
``` 