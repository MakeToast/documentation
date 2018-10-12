# Component Data Sharing

## 부모 Component의 직접적인 자식 요소 제어
- `@Input decorator`를 이용해 부모 Component에서 자식 Component로 데이터를 전달하는 방법
* 부모 Component는 자식 Component 객체 뿐만 아니라 자식으로 포함된 `Directive`에 직접 접근할 수 있다.
* Component가 Rendering하는 View 자체에 직접 접근할 수 있다.

- 단점
* Component의 재사용성과 유지보수성에 문제가 생길 여지가 있다. 

## @ViewChild, @ViewChildren Decorator
- 부모 Component template안에 위치한 모든 자식 요소들을 `ViewChild`라고 한다.
- `ViewChild` 안에는 자식 Component, Component가 Rendering하는 View의 DOM, Directive가 포함된다.

### 자식 Component객체에 직접 접근하는 방법
- `@ViewChild` decorator를 이용한다.
> 조건에 부합되는 객체 1개를 찾게 되고 그에 대한 property를 지정해서 사용할 수 있다.<br>
> `@ViewChildren`을 이용하면 조건에 부합되는 객체를 모두 찾고 `QueryList`형태로 객체들의 집합을 얻을 수 있다.<br>

- 부모 Component에 초기화버튼을 만들어서 해당 버튼을 누르면 Client가 선택한 도서 종류와 입력된 키워드를 초기화시키는 작업
- book-search-main.component.html
> 검색 초기화 버튼을 생성하고 해당 버튼에 `clearCondition()` method가 호출되도록 처리했다.
```
<div class="bookSearch-outer">
  <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded box-shadow">
    <img class="mr-3" src="assets/images/search-icon.png" alt="" width="48" height="48">
    <div class="lh-100">
      <h5 class="mb-0 text-white lh-100">Search Result : </h5>
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
          
        </mat-option>
      </mat-select>
    </mat-form-field>
    <button mat-raised-button color="primary"
            (click)="clearCondition()">검색 초기화</button>
  </div>

  <div>
    <app-search-box [bookCategory]="displayCategoryName"
                    (searchEvent)="changeTitleBar($event)"></app-search-box>
  </div>
  <div>
    <app-detail-box></app-detail-box>
  </div>
  <div>
    <app-list-box></app-list-box>
  </div>
</div>
```
- 부모 Component : book-search-main.component.ts
> `clearCondition()` method를 작성하고 해당 method안에서 자신의 검색에 관련된 사항을 초기화하고 자식 Component를 찾아 자식 Component의 property를 초기화시키는 작업을 진행한다.
```
import {Component, OnInit,
        ViewChild, ViewChildren, QueryList } from '@angular/core';
import { SearchBoxComponent } from "../search-box/search-box.component";

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

  searchTitle = null;

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

  changeTitleBar(searchInfo) : void {
    this.searchTitle = `${searchInfo.keyword} ( ${searchInfo.category} )`;
  }

  @ViewChild(SearchBoxComponent) searchComp: SearchBoxComponent;
  @ViewChildren(SearchBoxComponent) searchCompArr: QueryList<SearchBoxComponent>;

  clearCondition(): void {
    this.selectedValue = null;
    this.searchTitle = null;
/*
    @ViewChild를 사용할 경우
    this.searchComp._bookCategory = null;
    this.searchComp.keyword = null;
*/
    // @ViewChildren을 사용할 경우
    this.searchCompArr.toArray()[0]._bookCategory = null;
    this.searchCompArr.toArray()[0].keyword = null;
  }
}
```
- 부모 Component와 자식 Component가 데이터를 공유하는 것이 아니라 `부모 Component가 직접 자식 Component 객체를 제어`하는 방식이다.

## Component가 Rendering하는 View의 DOM에 직접 접근
- `@ViewChild`와 `@ViewChildren`을 이용하면 View의 DOM에 직접 접근이 가능하다.
- Template Reference Variable을 이용해서 Component가 DOM에 접근한다.

- book-search-main.component.html 수정 버튼 추가
> 결과를 표시하는 영역에 Template Reference Variable `#resultStatus`을 지정했다.<br>
> 해당 버튼을 클릭하면 `changeDOM()` 호출된다.
```
...
...
<h5 #resultStatus class="mb-0 text-white lh-100">Search Result : </h5>
...
...
...
    <button mat-raised-button color="primary"
            (click)="changeDOM()">DOM 직접 변경</button>
...
...     
```
- book-search-main.component.ts
> `resultStatus` Tempate Reference Variable을 이용해서 해당 Element의 Reference를 획득하는 부분을 보면 `ElementRef` type의 객체를 획득하면 `nativeElement` 속성으로 직접 제어할 수 있다.
```
import {Component, OnInit,
        ViewChild, ViewChildren, QueryList,
        ElementRef } from '@angular/core';
import { SearchBoxComponent } from "../search-box/search-box.component";


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

  searchTitle = null;

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

  changeTitleBar(searchInfo) : void {
    this.searchTitle = `${searchInfo.keyword} ( ${searchInfo.category} )`;
  }

  @ViewChild(SearchBoxComponent) searchComp: SearchBoxComponent;
  @ViewChildren(SearchBoxComponent) searchCompArr: QueryList<SearchBoxComponent>;

  clearCondition(): void {
    this.selectedValue = null;
    this.searchTitle = null;
/*
    @ViewChild를 사용할 경우
    this.searchComp._bookCategory = null;
    this.searchComp.keyword = null;
*/
    // @ViewChildren을 사용할 경우
    this.searchCompArr.toArray()[0]._bookCategory = null;
    this.searchCompArr.toArray()[0].keyword = null;
  }

  @ViewChild('resultStatus') resultToolbar: ElementRef;

  changeDOM(): void {
    this.resultToolbar.nativeElement.onclick = function() {
      alert('DOM을 직접 제어할 수 있어요!!');
    };
    this.resultToolbar.nativeElement.innerHTML = "클릭해보세요!!";
  }

}
```