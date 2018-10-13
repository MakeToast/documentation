# Angular Service

## Service
- Component는 View를 표현하고 관리하는 것이 주된 역할이다.
- 즉, 데이터를 받아와서 View에 출력한다던지 View의 값이 변경되면 그것을 또 처리하는 View와 밀접한 로직을 Component class가 가지고 있다.
- `SoC`(Seperation of Concern) : 별도의 로직들을 작성하고 다른 Component에서 이 `Service`를 가져다 사용하는 식으로 관리
- 문제점 `Dependency`
- 예제
> Component class안에서 직접 Service객체를 생성해서 이용하는 pseudocode
```
MyService service = new MyService();
service.getUserAuth('moon9342');
```
> `Dependency Relationship` :  Component는 Service에 의존하는 경우. 이 때 Component class의 입장에서 Service 객체를 `Dependency`라고 표현한다.<br>
> 이렇게 의존관계가 성립되면 Service가 변경되었을 때 Component는 영향을 받는다. 연관관계가 강하게 성립되어 재사용이나 유지보수에 문제가 생긴다.<br>

- `DI`(Dependency Injection) 는 이문제를 해결하는 Design Pattern : Service객체(Dependency)를 사용하는 객체인 Component에게 주입해서 사용
- 주입하는 방법은 constructor를 이용하는 방법과 setter를 이용하는 방법이 있는데 Angular는 `constructor injection`을 지원한다.
- Angular Framework이 Service를 Component가 사용할 수 있도록 Service 객체를 생성해서 Component에게 넣어주는 방식, `IoC`(Inversion of Control)이라고 한다.

## Service 생성
- bookSearch Module에 서비스 추가하자.
```
ng generate service HttpSupport
``` 
- **http-support.service.ts** 파일 내용
```
import { Injectable } from '@angular/core';

@Injectable()
export class HttpSupportService {

  constructor() { }

}
```
> `@Injectable decorator` : 해당 class가 다른 class에 주입될 수 있다는 의미. 주입은 생성자를 이용하게 되고 주입과정은 Angular Framework가 담당한다.<br>

- JSON 파일로부터 데이터 받자. **http-support.service.ts** 파일
```
import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

interface IBook {
  bauthor: string;
  bdate: string;
  btranslator: string;
  bpublisher: string;
  btitle: string;
  bprice: number;
  bisbn: string;
  bimgurl: string;
}

@Injectable()
export class HttpSupportService {

  books: IBook[];
  constructor(private http: HttpClient) { }

  getJsonData() {
    this.http.get<IBook[]>('assets/data/book.json')
        .subscribe(res => {
           this.books = res;
           console.log(this.books);
        });
  }
}
```
> constructor(private http: HttpClient) { } <br>
> 생성자로 인자가 하나 들어온다. 이것도 HttpClient차입의 객체가 서비스 안으로 주입되는 것이다. 생성자에서 인자를 받으면서 Access Modifier를 이용하면 class안에 속성으로 자동 지정된다. 여기에서는 private으로 주입된 HttpClient 객체를 받았다.<br>
> `getJsonData()` method 호출되면 주입받은 HttpClient 객체를 이용해서 파일로부터 JSON 데이터를 읽어들인 후 console에 출력

## Service Injection
- 생성한 Service 객체를 search-box Component에 Injection 하는 코드 : **search-box.component.ts** 파일
```
import {
  Component, OnInit,
  Input, Output, EventEmitter
} from '@angular/core';

import { HttpSupportService } from "../http-support.service";

@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css'],
  providers: [
    HttpSupportService
  ]
})
export class SearchBoxComponent implements OnInit {

  _bookCategory: string;
  //@Input() bookCategory:string;
  //@Input('bookCategory') mySelected:string;

  @Input()
  set bookCategory(value: string) {
    if( value != null ) {
      // 추가적인 작업이 들어올 수 있습니다.
      this._bookCategory = 'category: ' +value;
    } else {
      this._bookCategory = value;
    }

  }

  @Output() searchEvent = new EventEmitter();

  keyword = null;

  constructor(private httpSupportService:HttpSupportService) { }

  ngOnInit() {
  }

  setKeyword(keyword: string): void {
    this.keyword = keyword;
    this.searchEvent.emit({
      keyword : `${this.keyword}`,
      category: `${this._bookCategory.replace('category: ','')}`
    });

    this.httpSupportService.getJsonData();

  }

  inputChange(): void {

  }
}
```
> `import { HttpSupportService } from "../http-support.service";` : import 시켜줘야 사용가능하다.<br>
> `constructor(private httpSupportService:HttpSupportService) { }` : constructor를 이용해 Service가 Injection 된다. <br>
> `this.httpSupportService.getJsonData();` : Injection 받은 Service의 method를 호출하는 부분<br>
```
@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css'],
  providers: [
    HttpSupportService
  ]
})
```
> Angular Framework에 어떤 class가 Injection이 되는지 알려줘야 한다. Component의 Metadata부분에 `providers`를 이용해 처리헤야 한다.

## Injector
- Angular Framework는 dependency객체를 어떻게 생성해야 하는지 모르기 때문에 Component의 Metadata를 이용해서 `providers`에 그 정보를 명시했다.
- 이 정보를 근간으로 `Injector`가 의존객체를 생성하고 주입한다.
![injection](https://moon9342.github.io/assets/built/images/angular-injector.png)
> Component가 생성될 때 Angular는 Injection에 필요한 객체를 Injector에 요청한다. 이 Injector는 이미 생성한 객체들을 담고 있는 Container를 유지하는데 이 안에 객체가 있으면 바로 주입하고 그렇지 않으면 의존객체를 생성한 후 주입하게 된다.

- 주의할 점 : **각각의 Component 각자 하나씩의 Injector를 가지고 있다.**
> Component는 tree형식으로 구성되니 Injector도 tree형태로 구성이 된다.<br>
> 만약 Injection요청에 대한 내용이 현재 Component의 providers부분에 명시되어 있지 않으면 부모 Component의 providers에서 검색한다. 이렇게 부모로 타고 올라가면서 의존객체를 찾게 된다.<br> 
> 만약 상위 Component에서 의존객체를 생성해 놓있으면 하위 Component에서 따로 선언하지 않아도 사용 가능하다.<br>
> 또한 Module의 providers에도 등록할 수 있다. 이런 경우 해당 Module안에 있는 모든 Component들이 해당 의존모듈을 사용할 수 있다.<br>
> 최상위 Component인 Root Cmponent가 가지고 있는 Root Injector는 Application 전역에서 사용가능한 의존모듈을 가지고 있다.

## Provider
- Module안에 providers로 등록한 의존객체는 Module안에서 사용이 가능하다. Component에서 등록한 의존객체는 자신과 자식 Component에서 사용이 가능하다.
- Module에 등록하는 경우 의존객체는 하나의 객체가 생성되어서 사용되어 `Singleton`형태로 사용된다. (반면 Component에 등록된 의존객체는 해당 Component가 생성될 때마다 의존객체가 따로 생성된다.)
- Component안에서 의존객체를 등록하려면
```
@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css'],
  providers: [
    HttpSupportService
  ]
})
```
> 실제 객체뿐만아니라 `Value`도 주입가능하다.
- 위의 코드는 밑의 코드의 축약형이다.
```
@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css'],
  providers: [
    {
      provide: HttpSupportService,    // 데이터 타입
      useClass: HttpSupportService    // 실제 객체를 생성하기 위해 필요한 class명
    }
  ]
})
```
> `provide`의 값과 `useClass`의 값이 같을 경우 축약형으로 표현할 수 있다. provide는 만들어지는 객체의 데이터 타입이다.<br>
> useClass는 실제 객체를 생성하기 위해 사용되는 class명이다.<br>
> `interface`를 이용하거나 `duck typing`을 이용하면 서로 다른 데이터 타입과 class를 사용할 수 있다.

- 의존객체가 아닌 고정값을 주입하는 방법 : configuration값을 주입받는 경우
```
ng generate class jsonConfig
```
- **json-config.ts** 파일
```
export class JsonConfig {
  url: string;
  name: string;
}

export const JSON_DATA_CONFIG: JsonConfig = {
  url: 'assets/data/',
  name: 'book.json'
};
```
- **search-box.component.ts** 파일 
```
import {
  Component, OnInit,
  Input, Output, EventEmitter
} from '@angular/core';
import { HttpSupportService } from "../http-support.service";
import { JSON_DATA_CONFIG, JsonConfig } from "./json-config";


@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css'],
  providers: [
    {
      provide: HttpSupportService,
      useClass: HttpSupportService
    },
    {
      provide: JsonConfig,
      useValue: JSON_DATA_CONFIG
    }
  ]
})
export class SearchBoxComponent implements OnInit {

  _bookCategory: string;
  //@Input() bookCategory:string;
  //@Input('bookCategory') mySelected:string;

  @Input()
  set bookCategory(value: string) {
    if( value != null ) {
      // 추가적인 작업이 들어올 수 있습니다.
      this._bookCategory = 'category: ' +value;
    } else {
      this._bookCategory = value;
    }

  }

  @Output() searchEvent = new EventEmitter();

  keyword = null;

  constructor(private httpSupportService:HttpSupportService,
              private jsonConfig:JsonConfig) { }

  ngOnInit() {
  }

  setKeyword(keyword: string): void {
    this.keyword = keyword;
    this.searchEvent.emit({
      keyword : `${this.keyword}`,
      category: `${this._bookCategory.replace('category: ','')}`
    });

    this.httpSupportService.getJsonData(this.jsonConfig.url, this.jsonConfig.name);

  }

  inputChange(): void {

  }
}
```
> `Value`를 Injection받을 때 어떻게 처리하는지 잘 보자

- **http-support.service.ts** 파일 : service의 method를 호출할 때 주입값을 가지고 method를 호출하기 떄문에 service의 코드도 변경해야 한다.
```
import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

interface IBook {
  bauthor: string;
  bdate: string;
  btranslator: string;
  bpublisher: string;
  btitle: string;
  bprice: number;
  bisbn: string;
  bimgurl: string;
}

@Injectable()
export class HttpSupportService {

  books: IBook[];
  constructor(private http: HttpClient) { }

  getJsonData(url:string, name:string) {
    this.http.get<IBook[]>(`${url}${name}`)
        .subscribe(res => {
           this.books = res;
           console.log(this.books);
        });
  }
}
```

## Optional Dependency
- `Optional Dependency`는 의존객체의 주입이 필수가 아니라는 것을 의미한다.
- `@Optional decorator`를 이용하면 의존객체가 존재하지 않더라도 프로그램 오류가 나지 않는다.
```
constructor(private httpSupportService:HttpSupportService,
            @optional private jsonConfig:JsonConfig) { }
```
[reference](https://moon9342.github.io/angular-lecture-data-share-service)