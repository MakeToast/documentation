# PRACTICE #1.1

## SPA(Single Page Application)
- 요즘 대부분의 Front End Web Application은 `SPA`형태이다.
> `SPA`는 Web Application이 하나의 Web Page로 구성되는 것을 말한다.
- 이에 대비되는 개념은 **JSP, ASP, PHP**같은 것들이다.
> 이 기술들은 모두 SSR(Server Side Rendering)기반의 Round Trip방식의 Web Application을 개발하는데 사용된다.

- 기존의 Web Application : Client가 새로운 Web Page를 요청할 때 마다 **서버**쪽에서 **Web Page**를 **동적**으로 만들어서 Client Browser에게 전송하는 방식
> 장점<br> 
>- 서버쪽에서 모든 작업이 이루어지기 떄문에 개발 용이. <br>
>- 개발방식 정형화.<br> 
>- **jQuery** 정도만 익혀서 결과 Web Page에 적용하는 식으로 Client쪽 처리도 쉽게 할 수 있다.

> 단점<br>
기존 Desktop환경에서 Mobile환경으로 넘어가면서 문제 발생<br>
>- 클라이언트가 새로운 페이지를 요청하고 받을 떄마다 web broswer화면 전체가 결과 Page로 **refresh** -> 필요한 부분만 갱신하면 되는데 전체 페이지를 새로 고침하는 것은 비효율적인 네트워크 사용량<br>
>- Mobile환경에서 Client는 이미 Native App을 사용하는 방식으로 **UX**가 확고하다. 따라서 우리의 Web Application도 마치 Native App처럼 동작하도록 만들어 제공해야 한다.

- **이와 같은 문제를 해결하기 위해 나온 모던 웹 패러다임 : SPA**
> Network traffic의 감소 및 사용성 관점에서 상당히 가치있는 Front End 개발 방식

- SPA 단점
1. 초기 로딩 속도 문제
2. 검색엔진최적화(`SEO`, Search Engine Optimization) 문제

- SEO 문제를 해결하기 위해 Angular Router를 이용하여 `PathLocationStrategy`라는 Location 정책을 이용해 Angular Application을 작성하자.

------------------------
## Module 생성

- Angular의 Module
> 연관성이 있는 Angular의 구성요소들을 하나의 단위로 묶은 것
(Angular Application : Module의 집합)
- Root Module : `AppModule`
- `Feature Module`
>- 특정화면을 구성하는 구성요소를 묶어서 Module로 관리할 수 있다.<br>
Home에 대한 Component는 Root Module에서 관리.<br>
도서검색이나 영화 검색같은 여러 요소들이 필요한 경우 Module로 따로 관리하는 것이 좋다.<br>
Application 전역에서 사용하는 구성요소들을 따로 묶어서 Module로 만들 수 있다.(Authentification Module, Routhing Module 등)
- `Shared Module`
>- Feature Module에 의해서 공통적으로 사용되는 구성요소들을 묶어서 Module로 관리할 수 있다.<br>
주로 Feature Module에서 공통적으로 사용되는 Driective나 Pipe같은 것들이 포함된다.
- Routhing Module을 생성하여 Routher를 구성하고 등록해보자.
```
ng generate module app-routing
```
- 정상적으로 실행되면 `src/app/app-routing` 폴더가 생성되고 그 폴더에 `app-routing.module.ts`파일이 생성.

## 각 Routing이 사용할 Component 생성
- 각 Routing 경로가 사용할 Component를 생성한다.
(도서 검색에 대한 Module과 영화 검색에 대한 Module 생성)
- Home화면을 담당할 Component는 `src/app/pages`하단에 생성하고 Root Module에서 직접 import해서 사용하도록 생성.
```
ng generate component pages/home
```
- 도서 검색을 위한 Module 생성. 그 안에 Component 생성
```
ng generate module bookSearch 
ng generate component bookSearch/bookSearchMain
```
- 영화 검색을 위한 Module 생성. 그 안에 Component 생성
```
ng generate module movieSearch 
ng generate component movieSearch/movieSearchMain
```
--------------------------
## Routing Module 수정
- `app-routing.module.ts`
```
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

// Angular Router Module import
import { Routes, RouterModule } from "@angular/router"

// Routing 처리를 할 각각의 Component import
import { HomeComponent } from "../pages/home/home.component"
import { BookSearchMainComponent } from "../bookSearch/book-search-main/book-search-main.component";
import { MovieSearchMainComponent } from "../movieSearch/movie-search-main/movie-search-main.component";

// Router 생성( path 표시할 때 Root path에 대한 '/'는 제외 )
const routers: Routes = [
  { path : '', component : HomeComponent },
  { path : 'book', component : BookSearchMainComponent },
  { path : 'movie', component : MovieSearchMainComponent }
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(routers)
  ],
  declarations: [],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```
## Root Module 수정
- `app.module.ts`
```
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations'

import { MatTableModule } from '@angular/material/table'

import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';

// Feature Module import
import { BookSearchModule } from "./book-search/book-search.module";
import { MovieSearchModule } from "./movie-search/movie-search.module";

// Routing Module import
import { AppRoutingModule } from "./app-routing/app-routing.module";
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatTableModule,
    AppRoutingModule,
    BookSearchModule,
    MovieSearchModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```
[reference](https://moon9342.github.io/angular-lecture-exercise-1)