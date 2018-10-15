# TypeScript Class
- TypeScript에서 class를 정의할 때 적절한 data type의 정보를 포함하고 있어야 한다.
```
class Book{
    btitle: string;
    bauthor: string;

    constructor(btitle:string, bauthor:string){
        this.btitle = btitle;
        this.bauthor = bautor;
    }

    printInfo(): void{
        console.log(`제목: ${this.btitle}, 저자: ${this.bauthor}`);
    }
}

let book:Book = new Book('젊은 베르테르의 슬픔', '괴테');
book.printInfo();
```

## Inheritance
- 기존 class를 확장하여 새로운 class를 정의하는 방법
- `IS-A Relationship` 역시 성립 : 상위 타입으로 객체 사용 가능
- `method overriding`, `dynamic binding` 개념 존재
```
class Book{
    btitle: string;
    bauthor: string;

    //  상위 클래스의 생성자
    constructor(btitle:string, bauthor:string){
        this.btitle = btitle;
        this.bauthor = bautor;
    }

    // 상위 클래스의 method
    // 입력 인자가 있으면 사용하고 없으면 default 사용

    printInfo(input:string = 'Initial'): void{
        console.log(input);
        console.log(`제목: ${this.btitle}, 저자: ${this.bauthor}`);
    }
}

// class의 상속
class EBook extends Book{
    btype: string;
    constructor(btitle:string, bauthor:string, btype:string){
        // 상위 class 생성자 호출
        super(btitle, bauthor);
        this.btype = btype;
    }

    // method overriding
    printInfo(): void{
        // 상위 class의 method 호출
        super.printInfo();
        console.log(`제목: ${this.btitle},
                     저자: ${this.bauthor},
                     타입: ${this.btype}`);
    }
}

// IS-A relationship에 의한 상위 class type 사용
let book:Book = new EBook('젊은 베르테르의 슬픔', '괴테', 'PDF');

// dynamic binding에 의한 overriding method 호출
book.printInfo();
```

## Access Modifier
- TypeScript는 3가지 종류의 접근제어 연산자 제공.
- 생성자에 인자 명시할 때 access modifier를 같이 명시하면 명시적으로 해당 property가 선언되어 사용할 수 있다.

- `public` : default값, 접근제한 없다. class 외부에서 자유롭게 접근 가능.
- `protected` : class 외부에서 접근 불가. 단, 상속받은 하위 class에서는 접근 가능.
- `private` : class 외부에서 접근 불가. 상속받은 하위 class에서도 접근 불가.
```
class Book{
    protected btitle: string;

    public constructor(btitle:string, private _bauthor:string){
        this.btitle = btitle;
    }

    public printInfo(): void{
        console.log(`제목: ${this,btitle}, 저자: ${this._bauthor}`);
    }

    // private property인 _bauthor의 getter
    get bauthor(): string{
        return this._bauthor;
    }

    // private property인 _bauthor의 setter
    set bauthor(value: string){
        this._bauthor = value;
    }
}

class EBook extends Book {

    private btype: string;

    public constructor(btitle:string, bauthor:string, btype:string) {
        super(btitle, bauthor);
        this.btype = btype;
    }

    public printInfo(): void {
        console.log(`제목: ${this.btitle}, 
                     저자: ${this.bauthor},
                     타입: ${this.btype}`);
    }
}

let book:Book = new EBook('젊은 베르테르의 슬픔','괴테',
    'PDF');

book.printInfo();
```
- private property의 이름 앞에 `_`를 관용적으로 써준다.

## Readonly Property
- readonly로 지정되면 property가 선언될 때 혹은 생성자안에서 반드시 초기화 진행.
```
class Book{
    public readonly btitle: string;

    constructor(btitle: string){
        this.btitle = btitle;
    }
}

let book: Book = new Book('젊은 베르테르의 슬픔');

book.btitle = '파우스트'; // 코드 에러
```
- 생성자의 parameter를 readonly로 선언하면 따로 class의 property로 선언할 필요가 없다.
```
class Book{

    constructor(readonly btitle: string){
        this.btitle = btitle;
    }
}

let book: Book = new Book('젊은 베르테르의 슬픔');

console.log(book.btitle);
```

## Static Property
- static property는 class의 이름으로 직접 access 가능
```
class Book{
    public btitle: string;
    static count: number;

    constructor(btitle: string){
        this.btitle = btitle;
        Book.count++;
    }
}

let book1:Book = new Book('젊은 베르테르의 슬픔');
let book2:Book = new Book('파우스트');

console.log(Book.count);
```

## Abstract Class
- 하나이상의 abstract method를 가지고 있는 class 의미
- method의 선언만을 가지고 있기 때문에 직접적인 객체생성 할 수 없고 상속을 이용해 하위 클래스에서 abstract method를 overriding해서 사용
```
abstract class Book{
    public btitle:string;

    constructor(btitle: string){
        this.btitle = btitle;
    }

    abstract printInfo(): void;
}

class EBook extends Book{
    printInfo(): void{
        console.log(this.btitle);
    }
}

let book:Book = new EBook('젊은 베르테르의 슬픔');
book.printInfo();
```

## interface의 의미로 class 사용
- class를 확장해서 interface를 정의 가능
```
class Book{
    btitle: string;
}

interface EBook extends Book{
    bautor: string;
}

let book:EBook = {
    btitle: '파우스트',
    bauthor: '괴테'
} 
```
[reference](https://moon9342.github.io/typescript-class) 