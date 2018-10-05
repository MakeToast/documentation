# Component Data Sharing

## @Output Decorator
- 자식 Component에서 부모 Component로 데이터를 전달하기 위한 `@Output Decorator`에 대해 알아보자.
- 자식 Component에서 부모 Component로 데이터를 전달하기 위해서는 `EventEmitter`를 이용한 이벤트 처리를 해야 한다. 즉 자식 Component에서 발생한 event를 부모 Component가 `event binding`을 이용해 데이터를 받는 방식이다.

- `search-box.component.ts` 코드
```
import { Component, OnInit,
         Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css']
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

  constructor() { }

  ngOnInit() {
  }

  setKeyword(keyword: string): void {
    this.keyword = keyword;
    this.searchEvent.emit({
      keyword : `${this.keyword}`,
      category: `${this._bookCategory.replace('category: ','')}`
    });
  }

  inputChange(): void {

  }
}
```
> 부모 Component에게 이벤트를 전달하기 위해 EventEmitter객체를 생성하고 @Output decorator를 이용했다. 부모 Component는 `searchEvent` 이름으로 event binding 해야 한다.<br>
> @Output() searchEvent = new EventEmitter(); : 자식 Component에서 Search! 버튼을 눌렀을 때 `setKeyword()` method가 호출되는데 이 안에서 searchEvent에 대한 이벤트를 발생시킨다. 그러면서 부모 Component에게 전달할 데이터를 인자로 넣어준다.<br>
> this.searchEvent.emit({
    keyword : `${this.keyword}`,
    category: `${this._bookCategory.replace('category: ','')}`
});<br>

- `book-serach-main.component.html` 코드에서 부모 Component에서 어떻게 event binding을 이용해서 데이터를 받는지 살펴보자
```
<div class="bookSearch-outer">
  <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded box-shadow">
    <img class="mr-3" src="assets/images/search-icon.png" alt="" width="48" height="48">
    <div class="lh-100">
      <h5 class="mb-0 text-white lh-100">Search Result : {{searchTitle}}</h5>
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
    <app-search-box [bookCategory]="displayCategoryName"
                    (searchEvent)="changeTitleBar($event)">
    </app-search-box>
  </div>
  <div>
    <app-detail-box></app-detail-box>
  </div>
  <div>
    <app-list-box></app-list-box>
  </div>
</div>
```
```
<app-search-box [bookCategory]="displayCategoryName"
                (searchEvent)="changeTitleBar($event)">
</app-search-box>
```
> event binding을 이용해서 `searchEvent` 이벤트가 발생하면 `ChangeTitleBar()` method를 호출하고 인자를 받아서 처리하는 부분
```
<h5 class="mb-0 text-white lh-100">Search Result : {{searchTitle}}</h5>
```
> interpolation을 이용해 searchTitle 속성의 값을 View에 출력하고 있다. `changeTitleBar()` method안에서 내용이 결정될 것이다.

- `book-search-main.component.ts` 코드
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
}
```

[reference](https://moon9342.github.io/angular-lecture-data-share-2)