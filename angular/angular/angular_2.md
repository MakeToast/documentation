# Angular Component
- `Angular`는 **Front End Web Application Framework**
- Web Browser상에서 동작하는 Client가 사용하는 응용 프로그램 만들어 낼 수 있다.
- 이런 프로그램은 사용자가 직접 접근할 수 있는 `View`라는 것을 가지고 동작한다.

- 전체 웹 어플리케이션 화면이 하나의 View가 될 수도 있고 어플리케이션 화면의 기능이나 목적에 따라 세부 View들로 분할되어 웹 어플리케이션의 화면을 구성할 수도 있다.

![분할된 view 예시](https://moon9342.github.io/assets/built/images/view-layout.png)
[이미지출처](https://msdn.microsoft.com)

- 이렇게 화면을 여러 View들로 분할해서 구성할 수 있다.
- 분할된 View들은 결국 **Angular에서 `Component`의 단위**가 된다.

- 또한 하나의 View안에 여러 View들을 넣어 화면을 구성할 수도 있다. (부모 - 자식의 관계 성립)
- 부모 자식간의 관계를 크게 보면 tree모양으로 구성되는데 이를 `Component Tree`라고 한다.
- Component tree의 제일 위쪽에 위치한 Component를 우리는 `Root Component`라고 한다.

- Component는 View를 rendering하는 주체가 되기 때문에 **어떤 정보로 View를 rendering할 것인가에 대한 정보**를 가지고 있어야 한다.
- 이 정보를 `Template` 이라고 한다.

## Template
- `Template`은 View를 rendering하기 위해 필요한 **HTML Element와 Angular의 문법 요소** 그리고 클라이언트 **이벤트 처리 코드**를 담고 있다.
- __Application 실행 시 Angular는 Component와 Template의 정보를 이용하여 View를 그린다.__
![이미지 출처 : https://angular.io/guide/architecture](https://moon9342.github.io/assets/built/images/angular-template.png)

## Component - class
- MySearchProject의 src폴더에 가면 `index.html`파일이 존재한다.
- `index.html` : Web application의 시작 HTML파일이다.
- **http://localhost:4200**으로 접속하면 rendering되는 파일이 index.html이다.
```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>MySearchProject</title>
  <base href="/">

  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
</head>
<body>
  <app-root></app-root>
</body>
</html>
```
- `<app-root></app-root>` :  하나의 View -> 이에 대응하는 component 존재
- src/app 폴더에 `app.component.ts` :  TypeScript로 Component를 정의한 파일.
```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
}
```
- Component는 `class`이다.
- `@Component` : **Component decorator** 이 class가 Component로 사용된다는 것을 Angular에게 알려주어야 Angular가 Component로 동작을 시킬 수 있다.
- `@angular/core` : Component decorator를 제공하는 Angular Core Module Package

## Component - Metadata
- Component decorator를 이용해 설정 정보인 `Metadata` 를 Angular Framework에게 전달 할 수 있다.
```
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
```
- Metadata는 상당히 종류가 많지만 필수요소는 없다.
- 하지만 `selector`와 `template 정보`는 존재하지 않으면 화면에 rendering이 되지 않기 때문에 필수요소라 볼 수 있다.

### selector
- **template 코드**안에서 해당 Component를 사용하고자 할 때 이용할 HTML Element명을 정의
- 위와 같은 경우 해당 Component는 `<app-root></app-root>` HTTML Element로 사용될 수 있다.

### template 정보
- **template** 혹은 **templateUrl**을 이용할 수 있다.
- **template**은 View를 rendering할 때 필요한 HTML을 inline형태로 직접 기술할 때 사용된다.
- **templateUrl**은 template code를 따로 HTML파일로 분리해서 작성할 때 사용

### style 정보
- **styles** 혹은 **styleUrls**을 이용할 수 있다.
- **template 정보**에 명시된 HTML에 댜한 style을 정의한 CSS가 inline형태 혹은 파일 형태로 포함될 수 있다.
- 여러 CSS 정의와 파일을 이용할 수 있기 때문에 배열형태로 표현.

## Module & Bootstrapping
- `Bootstrapping` : 브라우저에서 Application이 최초로 실행될 때 진행되는 과정
- 우리가 작성한 Component는 Application이 bootstrapping될 때 Angular에 의해서 제어
- `Module` : Application을 구성하는 단위로 관련된 요소를 하나로 묶어 놓은 것.
- Angular는 Module단위로 Application 코드를 인식하기 때문에 Angular Application은 반드시 하나 이상의 Module을 가지게 되며 최상위 모듈을 `Root Module`이라고 한다.

__이러한 Module안에 Component와 같ㅇ느 것들을 선언해 놓아야 비로소 사용할 수 있다.__

- `Root Module`은 관례상 `AppModule`이라고 명하고 class로 표현하게 된다.
- `src/app`폴더 안에 `app.module.ts` 파일이 존재하는데 이 파일 안에 Root Module이 정의되어 있다.
```
// BrowserModule은 Web Application인 경우 Root Module에서 
// 반드시 import 처리를 해야 합니다.
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```
- `BrowserModule`은 Web Browser를 위한 Module이다. 브라우저에서 동작하는 Web Application인 경우 Root Module은 반드시 BorwserModule을 import해야 한다.
- 위의 코드에서처럼 `AppModule` class가 정의 되어 있고 상단에 `@NgModule` decorator를 이용하여 우리의 class가 Module임을 명시했다.
```
import { AppComponent } from './app.component';
```
- 이 코드는 `app.component.ts` 파일로부터 AppComponent class를 import하는 부분이다.
- AppComponent class를 `export`처리 한 것은 외부에서 **import**해서 사용할 수 있다.
- import 할 경우 확장자인 `.ts`는 명시하지 않는다.

__**declarations**안에는 Component, Directive, Pipe에 대한 리스트가 선언된다. 이렇게 선언된 요소만이 Module내에서 사용 가능하다.__
__**imports**안에는 의존 관계에 있는 Angular Library Module과 하위 Module, Routing Module, Ionic과 같은 Third Party Module이 포함된다.__

- `@NgModule` decorator의 Metadata 중 `bootstrap`은 오직 Root Module만 가지고 있는 property이다.
- `bootstrap`은 browser가 최초로 index.html을 읽어들여 application을 시작할 때 사용할 Component를 명시한다.
- `@NgModule` decorator의 Metadata에 사용되는 Component를 등록해야 Component의 TypeScript코드를 browser에서 실행가능한 JavaScript 코드로 컴파일해서 변환 시킬 수 있다.

- src/main.ts
```
platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.log(err));
```
- Angular는 저 위의 코드로 `AppModule`을 읽어들이고 Module안에 등록된 여러 Component들을 `JavaScript`코드로 컴파일하게 되는 것
- Root Module은 최상위 Module로 main.ts에 의해 bootstrap 된다. 이 때 위에서 언급한 Component Tree의 최상위 Component인 Root Component가 Root Module에 의해서 bootstrap 된다. 따라서 **모든 Angular 프로젝트는 Root Module과 Root Component를 반드시 가지고 있어야 한다.**

__지금까지 살펴본 것처럼 Angular CLI를 이용하지 않으면 우리가 .ts파일을 만들어서 등록해야 한다. 따라서 Angular CLI를 이용하면 기본 Skeleton코드의 생성과 등록절차까지 자동으로 처리된다.__

[reference](https://moon9342.github.io/angular-lecture-component)