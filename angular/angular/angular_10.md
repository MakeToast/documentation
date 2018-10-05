# Component Data Sharing
Component 간의 데이터 공유
- 도서 검색 시 도서 종류(국내 도서, 국외 도서, 국내외도서) 에 대한 Filtering이 가능하다.
- 키워드 입력 후 Search버튼을 클릭하면 해당 키워드에 대한 책만 list-box에 출력된다.
- list-box에 출력된 책 중 하나를 선택하면 해당 책에 대한 세부 내역을 detail-box에 출력한다.
## @Input Decorator
- `Component Tree` : Component간의 부모-자식 관계가 성립되면 서로 간의 데이터 연결통로가 생성되어 데이터 공유가 이루어 진다.

### 부모 Component -> 자식 Component
> 부모 Component가 사용자 입력 양식을 가지고 있다면 Client에 의해서 사용자 입력양식의 상태값이 변경될 수 있고 그 상태값을 자식 COmponent와 공유할 필요가 있다. <br>
이런 경우 부모 Component는 `property binding`을 이용해 자식 Component에게 데이터를 전달해 줄 수 있다. 이렇게 전달된 데이터는 `@Input decorator`에 의해서 자식 Component에서 사용될 수 있다.<br>

- Client가 Select Box에서 선택한 도서 종류 정보가 하위 Component인 `search-box` Component와 공유되는 코드로 수정해보자

- `book-search-main.component.html`
```
<div class="bookSearch-outer">
  <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded box-shadow">
    <img class="mr-3" src="assets/images/search-icon.png" alt="" width="48" height="48">
    <div class="lh-100">
      <h5 class="mb-0 text-white lh-100">Search Result</h5>
    </div>
  </div>

  <div class="example-container">
    <mat-form-field>
      <mat-select placeholder="도서종류"
                  #bookCategorySelect
                  [(ngModel)]="selectedValue"
                  (ngModelChange)="changeValue(bookCategorySelect.value)">
        <mat-option *ngFor="let category of bookCaterory"
                    [value]="category.value">
          {{ category.viewValue }}
        </mat-option>
      </mat-select>
    </mat-form-field>
  </div>

  <div>
    <app-search-box [bookCategory]="displayCategoryName"></app-search-box>
  </div>
  <div>
    <app-detail-box></app-detail-box>
  </div>
  <div>
    <app-list-box></app-list-box>
  </div>
</div>
```
> Template Reference Variable 과 양방향 바인딩을 이용해 Client가 도서 종류를 변경하면 `changeValue()` method가 호출된다.

- `book-search-main.component.ts` 에  `changeValue()` method 정의
```
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-book-search-main',
  templateUrl: './book-search-main.component.html',
  styleUrls: ['./book-search-main.component.css',
  './offcanvas.css']
})
export class BookSearchMainComponent implements OnInit {

  selectedValue = null;
  displayCategoryName = null;
  bookCaterory = [
    {value: 'all', viewValue: '국내외도서'},
    {value: 'country', viewValue: '국내도서'},
    {value: 'foreign', viewValue: '국외도서'}
  ];

  constructor() { }

  ngOnInit() {
  }

  changeValue(category: string): void {
      for(let element of this.bookCaterory ) {
        if(element.value == category) {
          this.displayCategoryName = element.viewValue;
        }
      }
  }
}
```
> changeValue() : Client가 선택한 도서 종류를 가지고 `displayCategoryName`이라는 속성의 값을 변경한다. displayCategoryName 이 속성이 바로 자식 Component인 search-box Component에게 전달되는 데이터이다.

- `book-search-main.component.html`
```
<div>
    <app-search-box [bookCategory]="displayCategoryName"></app-search-box>
</div>
```
> search-box Component에 property binding을 이용해 `bookCategory`라는 이름으로 `displayCategoryName` 속성을 바인딩해 놓은 것을 확인 할 수 있다.

- `search-box.component.ts` 코드
```
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css']
})
export class SearchBoxComponent implements OnInit {

  @Input() bookCategory:string;

  keyword = null;

  constructor() { }

  ngOnInit() {
  }

  setKeyword(keyword: string): void {
    this.keyword = keyword;
  }

  inputChange(): void {

  }
}
```
> @Input() bookCategory:string; : `bookCategory`라는 이름으로 부모 Component가 propterty binding으로 전달해준 데이터를 받을 수 있다. 이 속성을 View에 interploation을 이용해서 출력한다.

- View에 rendering되는 `search-box.component.html` 코드
```
<div class="example-container">
  <mat-toolbar class="search-toolbar-style">
    Search Keyword : {{keyword}}
    <ng-container *ngIf="bookCategory != null">
      ( {{bookCategory}} )
    </ng-container>
  </mat-toolbar>
  <mat-form-field>
    <input matInput #inputKeyword placeholder="Search Keyword"
           [(ngModel)]="keyword" (ngModelChange)="inputChange()">
  </mat-form-field>
  <button mat-raised-button color="warn"
          (click)="setKeyword(inputKeyword.value)">Search!</button>
</div>
```
> Toolbar 부분에 `{{keyword}}`와 함께 `{{bookCategory}}`를 이용해서 속성과 binding시킨 것을 확인 할 수 있다. 만약 bookCategory값이 null이면 출력되지 않게끔 built-in directive를 이용해서 처리했다. <br>

* 자식 Component인 `select-box` Component는 자신에게 데이터를 주는 부모 Component가 어떤 Component인지는 알 필요가 없다. 단지 전달된 데이터를 사용할 수 있도록 해주는 **property 이름**과 **data type**만이 필요하다.

### 자식 Component -> 부모 Component
- `setter`를 이용하자
- `search-box.component.ts` 코드
```
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css']
})
export class SearchBoxComponent implements OnInit {

  //@Input() bookCategory:string;
  //@Input('bookCategory') mySelected:string;
  _bookCategory: string;  

  @Input()
  set bookCategory(value: string) {
    if( value != null ) {
      // 추가적인 작업이 들어올 수 있습니다.
      this._bookCategory = 'category: ' +value;
    } else {
      this._bookCategory = value;
    }

  }

  keyword = null;

  constructor() { }

  ngOnInit() {
  }

  setKeyword(keyword: string): void {
    this.keyword = keyword;
  }

  inputChange(): void {

  }
}
```
> setter의 이름과 부모 Compoenent가 property binding하는 property의 이름이 같아야 한다. interpolation은 `_bookCategory`로 변경되어야 한다.<br>
> 부모 Component가 자식 Component에게 데이터를 전달해 줄 때 이 방식이 `call-by-reference` 방식이다.<br>
> 부모 Component와 자식 Component가 둘 다 `bookCategory`를 reference하고 있다.<br>
> 부모 Component가 해당 property의 값을 변경시키면 그 값을 자식 Component가 공유하고 있으므로 변경된 값을 그 즉시 사용할 수 있다. 하지만 데이터 변경을 tracking하기 힘들어지기 때문에 실제 코드 작업에서는 영향을 미치지 않는다.

- Angular는 `Stateful Component`와 `Stateless Component`의 개념이 있다. 
    * Stateful Component : Smart Component라고 부르며 이 Component는 데이터의 정보를 변경하거나 저장할 수 있다. 
    * Stateless Component : Dumb Component라고 불리며 단지 상태 정보를 참조만 해서 이용할 수 있다.

- `@Input decorator`를 이용하면 부모 Component에서 자식 Component에게 데이터를 전달 할 수 있지만 그 반대는 허용되지 않는다. 이 문제를 위해 `@Output decorator`를 사용할 수 있다.

[reference](https://moon9342.github.io/angular-lecture-data-share-1)