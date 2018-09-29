# PRACTICE #1.3

## 도서 검색 화면

- 3개의 메뉴 중 Home 메뉴는 단일 페이지이기 때문에 적절하게 수정해서 화면을 보여줘야 한다.
- 먼저 최종적으로 만들어진 도서 검색 화면은 아래와 같다.
![mySearchProject](https://moon9342.github.io/assets/built/images/exercise-result.jpg)
- 총 4개의 View로 구성
> 파란색으로 되어 있는 가장 큰 View안에 검색결과를 보여주는 영역과 도서 종류를 선택하는 Select Box가 들어 있다.<br>
부모 View안에 빨간색으로 되어 있는 3개의 자식 View가 포함된다.<br>
(검색어를 입력할 수 있는 View, 특정 책을 선택하면 그 책의 내용을 자세하게 출력해주는 View, 검색어에 해당하는 책에 대한 리스트 표현하는 View)
---------------------------
## AppComponent 수정
- 도서검색 화면을 만들고 그애 따른 Component들을 생성, 등록해보자.

- `src/app`폴더 안에 `app.component.ts`파일
```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css', './blog.css']
})
export class AppComponent {
  title = 'app';
}
``` 
- 이 Component가 우리의 Root Component이다.

- `selector: 'app-root'` 설정에 의해 이 Component는 template 코드내에서 `<app-root></app-root>` 로 되어 있는 부분을 rendering 한다.
- 또한 `templateUrl`에 의해 `app.component.html`을 이용해 rendering한다.

-`index.html` 파일
```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>MySearchProject</title>
  <base href="/">

  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <!-- Material Icon 설정. -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>
  <app-root></app-root>
</body>
</html>
```
- `index.html` 안의 `<app-root></app-root>`은 `app.component.html`으로 우리 Component에 의해서 rendering된다.

- Routing Module과 Bootstrap코드를 포함시킨`app.component.html` 파일
```
<div class="container">
  <header class="blog-header py-3">
    <div class="row flex-nowrap justify-content-between align-items-center">
      <div class="col-4 pt-1">

      </div>
      <div class="col-4 text-center">
        <a class="blog-header-logo text-dark" href="#">my Search Project</a>
      </div>
      <div class="col-4 d-flex justify-content-end align-items-center">

      </div>
    </div>
  </header>

  <div class="nav-scroller py-1 mb-2">
    <nav class="nav d-flex justify-content-between">
      <a class="p-2 text-muted" routerLink="/">Home</a>
      <a class="p-2 text-muted" routerLink="/book">도서 검색</a>
      <a class="p-2 text-muted" routerLink="/movie">영화 검색</a>
      <a class="p-2 text-muted" href="#"></a>
      <a class="p-2 text-muted" href="#"></a>
      <a class="p-2 text-muted" href="#"></a>
      <a class="p-2 text-muted" href="#"></a>
      <a class="p-2 text-muted" href="#"></a>
      <a class="p-2 text-muted" href="#"></a>
      <a class="p-2 text-muted" href="#"></a>
      <a class="p-2 text-muted" href="#"></a>
      <a class="p-2 text-muted" href="#"></a>
    </nav>
  </div>

  <div class="jumbotron p-3 p-md-5 text-dark rounded bg-warning">
    <div class="col-md-12 px-0">
      <router-outlet></router-outlet>
    </div>
  </div>

</div>
```
- Navigation Menu를 작성하고 각 Menu를 클릭하면 Router에게 `routerLink`에 명시된 경로로 전달한다. 그러면 Router는 해당 경로에 매핑되는 Component를 찾고 해당 Component는 `<router-outlet></router-outlet>`위치에 View를 Rendering한다.

- 결과적으로 도서 검색 메뉴를 클릭하면 `<router-outlet></router-outlet>`부분에 `book-search-main.component.html`의 내용이 rendering되게 되고 이제 그 내용을 수정해서 화면을 다시 구성한다. 
---------------------------
## Component 추가
- `book-search-main.component.html`은 내부에 3개의 View영역을 포함한다.
>- 첫번째 영역 : 검색 키워드를 입력하고 검색 버튼을 눌러 실행시키는 View
>- 두번쨰 영역 : 검색된 책을 선택하면 책의 세부정보가 출력되는 View
>- 세번째 영역 : 검색된 책들의 리스트를 출력하기 위한 View

- Angular CLI를 이용하여 새로운 Component를 추가한다.
> Angular CLI의 `generate`를 이용하여 Component 생성 시 Component를 구성하는 관련 파일들을 자동을 손쉽게 생성할 수 있다.
```
ng generate component bookSearch/search-box
```
- 생성된 `src/app/book-search/search-box` 폴더 안에 있는 `search-box.component.ts` 파일을 열어서 selector를 확인해보니 `app-search-box`로 지정되어 있다. template 코드에서 `<app-search-box></app-search-box>`을 이용하면 이 Component가 해당 영역을 rendering하게 된다.

- 이와 유사하게 2개의 Component를 더 생성한다.
```
ng generate component bookSearch/detail-box
```
```
ng generate component bookSearch/list-box
```
- `src/app/book-search/book-search-main` 안의 `book-search-main.component.html` 파일 수정
```
<div class="bookSearch-outer">
  <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded box-shadow">
    <img class="mr-3" src="assets/images/search-icon.png" alt="" width="48" height="48">
    <div class="lh-100">
      <h5 class="mb-0 text-white lh-100">Search Result</h5>
    </div>
  </div>

  <div class="form-group col-md-4">
    <label for="inputState">도서 종류</label>
    <select id="inputState" class="form-control">
      <option selected>선택하세요...</option>
      <option>국내외도서</option>
      <option>국내도서</option>
      <option>국외도서</option>
    </select>
  </div>

  <div>
    <app-search-box></app-search-box>
  </div>
  <div>
    <app-detail-box></app-detail-box>
  </div>
  <div>
    <app-list-box></app-list-box>
  </div>
</div>
``` 
- `src/app/book-search/book-search-main` 안의 `book-search-main.component.css` 파일 수정 
```
.bookSearch-outer {
  font-family: Georgia !important;
  width: 70%;
  text-align: center;
  margin: 0 auto;
}
```
# 각 Component의 View 작성
- 이제 각각의 Component의 `templateUrl`에 명시된 html을 Angular Material 을 이용해 화면을 만들어 낸다.
- `src/app/book-search/search-box` 안의 `search-box.component.html` 파일 수정
```
<div class="example-container">
  <mat-toolbar class="search-toolbar-style">Search Keyword : </mat-toolbar>
  <mat-form-field>
    <input matInput placeholder="Search Keyword">
  </mat-form-field>
  <button mat-raised-button color="warn">Search!</button>
</div>
```
- `search-box.component.css` 파일 내용 수정
```
.search-toolbar-style {
  font-family: Georgia;
  color: white;
  background-color: teal;
  margin-bottom: 20px;
}
```
- `book-search.module.ts` 파일 내용 수정 (Angular Material을 이용했기 때문에 해당 Element에 대한 Material Module을 import)
```
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BookSearchMainComponent } from './book-search-main/book-search-main.component';
import { SearchBoxComponent } from './search-box/search-box.component';
import { ListBoxComponent } from './list-box/list-box.component';
import { DetailBoxComponent } from './detail-box/detail-box.component';

import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';

@NgModule({
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatToolbarModule
  ],
  declarations: [BookSearchMainComponent, 
                 SearchBoxComponent, 
                 ListBoxComponent, 
                 DetailBoxComponent]
})
export class BookSearchModule { }
```
![결과화면](https://moon9342.github.io/assets/built/images/search-box-view.png)

- `detail-box.component.css` 파일 수정 (`src/assets/images` 폴더 안에 `book-icon.jpg` 파일 하나 넣어둬야 한다.)
```
.example-card {
  width: 500px;
  margin: 0 auto;
}

.example-header-image {
  background-image: url('/assets/images/book-icon.jpg');
  background-size: cover;
}

.book-image {
  width: 100px !important;
}

.detail-header-style {
  font-family: Georgia;
}
```
- `detail-box.component.html` 파일 수정
```
<mat-card class="example-card">
  <mat-card-header class="detail-header-style">
    <div mat-card-avatar class="example-header-image"></div>
    <mat-card-title>제목 : Angular 일주일 완성</mat-card-title>
    <mat-card-subtitle>저자 : 홍길동</mat-card-subtitle>
  </mat-card-header>
  <img mat-card-image class="book-image" src="">
  <mat-card-content>
    <p>
      ISBN : 123-456, 도서 가격 : 5000, 출판일 : 2017년 12월
    </p>
  </mat-card-content>
  <mat-card-actions>
    <button mat-button mat-raised-button color="primary">바로 구입</button>
  </mat-card-actions>
</mat-card>
```
- `book-search.module.ts`파일 수정 (Material Card Layout Component를 사용했기 때문에 해당 Module에 대한 처리)
```
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BookSearchMainComponent } from './book-search-main/book-search-main.component';
import { SearchBoxComponent } from './search-box/search-box.component';
import { ListBoxComponent } from './list-box/list-box.component';
import { DetailBoxComponent } from './detail-box/detail-box.component';

import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';

import { MatCardModule } from '@angular/material/card';

@NgModule({
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatToolbarModule,
    MatCardModule
  ],
  declarations: [BookSearchMainComponent, 
                 SearchBoxComponent, 
                 ListBoxComponent, 
                 DetailBoxComponent]
})
export class BookSearchModule { }
```
-----------------------
## 결과 화면
![최종 결과 화면](https://moon9342.github.io/assets/built/images/step-1-result.png)

[reference](https://moon9342.github.io/angular-lecture-exercise-1)