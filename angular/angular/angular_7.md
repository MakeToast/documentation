# Data Binding

## Data Binding
- `Data Binding` : Angular는 View와 Component에서 발생한 데이터의 변경 사항을 자동으로 일치시키는 기능 제공
>- `Two-Way Data Binding` : 양방향 바인딩이라고 한다. Component와 View의 상태 정보를 자동으로 일치시켜 주는 기능이다.
>- `One-Way Data Binding` : 단방향 바인딩이라고 한다. Component에서 View로 혹은 View에서 Component로 한 방향으로 데이터를 바인딩 해주는 기능이다.
- 양뱡향 바인딩은 내부적으로 두 개의 단방향 바인딩으로 구성된다.

### 단방향 바인딩
>- `Interpolation` : Component에서 선언한 속성을 View에서 사용하는 경우이다.
```
{{ value }}
```
>- `Property binding` : Veiw의 DOM이 소유한 HTML Element property를 `[]`를 이용하여 binding하는 경우이다.
```
[property] = "value"
```
>- `Event binding` : View의 DOM에 대한 Event handler로 Component의 method를 사용하는 경우이다.
```
(event) = "function"
```

## Interpolation
- `search-box.component.html` 수정
```
<div class="example-container">
  <mat-toolbar class="search-toolbar-style">Search Keyword : {{ keyword }}</mat-toolbar>
  <mat-form-field>
    <input matInput placeholder="Search Keyword">
  </mat-form-field>
  <button mat-raised-button color="warn">Search!</button>
</div>
```
> `{{ keyword }}` : interpolation이라고 부르는 단방향 바인딩<br>
>  `keyword` 라는 이름의 Component 속성을 찾아 그 값을 View에 표현하라는 것.<br>
> 따라서 우리의 Component에는 `keyword`라는 이름이 존재해야 한다.

- `search-box.component.ts` 수정
```
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css']
})
export class SearchBoxComponent implements OnInit {

  keyword = 'java';
  
  constructor() { }

  ngOnInit() {
  }

}
```
> `SearchBoxComponent` class안의 keyword 속성에 있는 `Java`란 값이 View에 그대로 출력된다.

## Event Binding
- `Event Binding` 역시 단방향 바인딩의 한 종류로 DOM의 Event Handler로 Component의 method를 활용할 수 있는 방법이다.
- search-box Component의 View에서 `Search` 버튼을 클릭하면 입력된 키워드가 위쪽 Toolbar영역에 출력되도록 코드를 작성해보자
- `search-box.component.html` 수정
```
<div class="example-container">
  <mat-toolbar class="search-toolbar-style">Search Keyword : {{keyword}}</mat-toolbar>
  <mat-form-field>
    <input matInput #inputKeyword placeholder="Search Keyword">
  </mat-form-field>
  <button mat-raised-button color="warn"
          (click)="setKeyword(inputKeyword.value)">Search!</button>
</div>
```
> `#inputKeyword` : Angular의 Template Reference Variable<br>
> `Template Reference Variable` : DOM의 HTML Element에 대한 참조 변수이다. 쉽게 말해 HTML Element에 변수를 하나 지정했다고 보면 된다. 이렇게 참조 변수를 선언해 놓으면 template 내의 JavaScript코드에서 `#`기호를 제외한 변수이름으로 참조가 가능하다.<br>
> `setKeyword(inputKeyword.value)` : Template Reference Variable inputKeyword를 `#` 기호없이 사용해서 변수를 참조하고 있다. 입력상자이기 때문에 `value`속성을 이용해서 입력된 값을 알아내고 있다.<br>
> * 주의할 사항 : Template Reference Variable은 HTML Template상에서만 사용할 수 있다.<br>
> Angular는 interpolation을 사용할 때 `Safe Navigation Operator`를 이용할 수 있다. `?` 기호로 표현되며 Component class의 속성값이 null이거나 undefined 일 경우 interplation을 이용하면 오류가 발생할 여지가 있다. 이때 `?`를 이용하면 그런 오류를 만났을 떄 처리를 종료하고 에러를 발생시키지 않는다. 예를 들어 `{{book?.btitle}}`이런식으로 사용

- `search-box.component.ts` 수정
```
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css']
})
export class SearchBoxComponent implements OnInit {

  keyword = 'Java';

  constructor() { }

  ngOnInit() {
  }

  setKeyword(keyword: string): void {
    this.keyword = keyword;
  }
}
```
> 버튼을 클릭했을 때 Template Reference Variable을 이용하여 키워드 입력상자에서 사용자가 입력한 검색 keyword 값을 가져와 Component의 method를 호출하여 Component 속성의 값을 변화시킨다. 이렇게 변경된 Component의 속성은 interpolation을 통해 다시 View에 출력되게 된다.

## Two-Way Data Binding
- 위에서 설명한 search 버튼은 입력된 키워드를 기반으로 실제 검색을 하기 위한 버틍니지 검색어를 위쪽 Toolbar 영역에 출력하기 위한 버튼은 아니다. 키워드 입력상자(`input`) 상자에 키워드를 입력할 때 사용자가 입력한 내용이 위쪽 Toolbar영역에 출력되도록 처리해보자.

- 양방향 바인딩을 사용하는 가장 쉬운 방법은 `FormsModule`이 제공하는 `NgModel` directive를 이용하는 것이다. 따라서 먼저 FormsModule을 import하는 부분부터 처리해야 한다.
- `book-search.module.ts` 수정
```
// 양방향 바인딩을 위한 FormsModule import
import { FormsModule } from '@angular/forms';
```
> 다음과 같이 바인딩할 요소의 속성에 `[(ngModel)]`과 함께 바인딩할 대상을 선언하면 된다.

- `search-box.component.html` 수정
```
<div class="example-container">
  <mat-toolbar class="search-toolbar-style">Search Keyword : {{keyword}}</mat-toolbar>
  <mat-form-field>
    <input matInput #inputKeyword placeholder="Search Keyword"
           [(ngModel)]="keyword">
  </mat-form-field>
  <button mat-raised-button color="warn"
          (click)="setKeyword(inputKeyword.value)">Search!</button>
</div>
``` 
> 이렇게 양방향 바인딩이 설정되어 있을 떄 사용자가 글자를 입력하면 `NgModel`로 바인딩한 값이 변경이 된다. 이 때 이벤트가 하나 발생하는데 이 이벤트를 처리하기 위해 `ngModelChange`를 이용하자.
```
<div class="example-container">
  <mat-toolbar class="search-toolbar-style">Search Keyword : {{keyword}}</mat-toolbar>
  <mat-form-field>
    <input matInput #inputKeyword placeholder="Search Keyword"
           [(ngModel)]="keyword" (ngModelChange)="inputChange()">
  </mat-form-field>
  <button mat-raised-button color="warn"
          (click)="setKeyword(inputKeyword.value)">Search!</button>
</div>
```
> `(ngModelChange)`에 바인딩 된 `inputChange()`는 `search-box.component.ts`안에 class의 method로 정의되어 있어야 한다. 데이터가 변경될 때 자동적으로 이벤트가 발생되고 바인딩된 method를 통해 특정 로직을 수행할 수 있다.<br>
> 영문일 경우는 문제없이 잘 수행되지만 한글 일 경우는 조합형 문자이기 때문에 약간의 문제가 있다. 양방향 바인딩은 기본적으로 문자 입력이 완료된 시점에 `compositionend`라는 브라우저 이벤트가 발생하고 이에 따라 바인딩을 처리한다. 하지만 한글은 글자가 다 만들어지기 전까지 해당 이벤트가 발생하지 않아 화면에 출력되지 않게 된다.<br>
> 이 문제를 해결하기 위해서는 Angular에서 제공하는 `COMPOSITION_BUFFER_MODE`를 설정하면 된다.

- `book-search.module.ts` 수정
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

// 양방향 바인딩을 위한 FormsModule import
import { FormsModule } from '@angular/forms';

// COMPOSITION_BUFFER_MODE import
import { COMPOSITION_BUFFER_MODE } from '@angular/forms';

@NgModule({
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatToolbarModule,
    MatCardModule,
    FormsModule
  ],
  providers: [
    {
      provide: COMPOSITION_BUFFER_MODE,
      useValue: false
    }
  ],
  declarations: [BookSearchMainComponent, 
                 SearchBoxComponent, 
                 ListBoxComponent, 
                 DetailBoxComponent]
})
export class BookSearchModule { }
```
![결과화면](https://moon9342.github.io/assets/built/images/angular-hangul-input.png)

## Property Binding
- `Property binding`을 이용하면 DOM 상의 HTML Element에 대한 property를 Component의 속성과 바인딩 할 수 있다. 주의할 점은 property binding은 HTML Element의 Attribute에 값을 binding하는 것이 아니라 HTML이 browser에 의해 parsing되면 메모리에 DOM이 생성되는데 이 DOM의 HTML Element에 대한 property에 값이 binding된다.

![결과화면](https://moon9342.github.io/assets/built/images/detail-box-view.png)
> 제목, 저자, ISBN, 가격, 출판일, 이미지정보는 interploation을 이용해 출력하고 property binding을 이용하여 만약 책의 가격이 20000을 초과하면 구입버튼을 `disabled` 시키게 처리했다.

- `detail-box-component.css` 수정
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
- `detail-box.component.html` 수정
```
<mat-card class="example-card">
  <mat-card-header class="detail-header-style">
    <div mat-card-avatar class="example-header-image"></div>
    <mat-card-title>제목 : {{book.btitle}}</mat-card-title>
    <mat-card-subtitle>저자 : {{book.bauthor}}</mat-card-subtitle>
  </mat-card-header>
  <img mat-card-image class="book-image" src="{{book.bimgurl}}">
  <mat-card-content>
    <p>
      ISBN : {{book.bisbn}}, 도서 가격 : {{book.bprice }}, 출판일 : {{book.bdate}}
    </p>
  </mat-card-content>
  <mat-card-actions>
    <button mat-button
            mat-raised-button color="primary"
            [disabled]="book.bprice > 20000">바로 구입</button>
  </mat-card-actions>
</mat-card>
```
> book 객체의 속성으로 바인딩 시켰다. 당연히 `detail-box.component.tx`안에 class속성으로 `book`객체가 정의되어 있다.
```
<button mat-button
        mat-raised-button color="primary"
        [disabled]="book.bprice > 20000">바로 구입</button>
```
> `disabled`라는 속성에 property binding을 이용해 조건을 걸었다. 사용하는 방법을 잘 알면 도움이 될 것이다.

- `detail-box.component.ts` 수정
```
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-detail-box',
  templateUrl: './detail-box.component.html',
  styleUrls: ['./detail-box.component.css']
})
export class DetailBoxComponent implements OnInit {

  book = {
    btitle: 'Head First Design Patterns: 스토리가 있는 패턴 학습법',
    bauthor: '에릭 프리먼외 3명',
    bprice: 28000,
    bdate: '2005년 08월',
    bisbn: '89-7914-340-0',
    bimgurl: 'http://image.hanbit.co.kr/cover/_m_1340m.gif'
  };

  constructor() { }

  ngOnInit() {
  }

}
```