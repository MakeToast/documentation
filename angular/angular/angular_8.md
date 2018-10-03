# PRACTICE #2.1

## list-box Component View
- 도서 정보를 리스트 형태로 출력하는 list-box Component 구현
* Angular Material Table Component를 이용할 것이기 때문에 HTML Table Element에 대한 CSS처리는 하지 않았다.

![mySearchProject](https://moon9342.github.io/assets/built/images/listbox-html-table-view.png)

- `book-search.module.ts` 에 import 작업 추가
```
import { MatSelectModule } from '@angular/material/select';
```

- `book-search-main.component.html` 수정 (HTML Select Element -> Material Select)
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
      <mat-select placeholder="도서종류"  [(ngModel)]="selectedValue">
        <mat-option *ngFor="let category of bookCaterory"
                    [value]="category.value">
          {{ category.viewValue }}
        </mat-option>
      </mat-select>
    </mat-form-field>
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
> `mat-select`가 Select box에 대한 Angular Material Component이다. 양방향 바인딩으로 `selectedValue`란 이름의 Component의 속성에 바인딩 시켜놓은 상태이다.<br>
> `mat-option`은 Select box안의 각각의 Option Component이다. 여러개가 존재할 수있기 때문에 `ngFor` directive를 이용하여 반복처리했다.<br>
> Angular는 구조적 지시자(Structural Directive)를 제공. 여기서는 ngIF와 ngFor를 사용해서 DOM을 제어한다.<br>
> `bookCaterory`는 배열형태의 데이터고 배열의 각 원소는 객체이다.

- `book-search-main.component.ts` 내용 수정
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
  bookCaterory = [
    {value: 'all', viewValue: '국내외도서'},
    {value: 'country', viewValue: '국내도서'},
    {value: 'foreign', viewValue: '국외도서'}
  ];
  
  constructor() { }

  ngOnInit() {
  }

}
```
- `list-box.component.css`파일 수정. (위쪽 margin을 주기 위한 style 정의)
```
.example-container {
  margin-top: 20px;
}
```
- `list-box.component.html` 파일 
```
<table class="example-container">
  <thead>
  <th>ISBN</th>
  <th>Title</th>
  <th>Author</th>
  <th>Price</th>
  </thead>
  <tbody>
    <tr *ngFor="let book of books">
      <td>{{book.bisbn}}</td>
      <td>{{book.btitle}}</td>
      <td>{{book.bauthor}}</td>
      <td>{{book.bprice}}</td>
    </tr>
  </tbody>
</table>
```
- 코드 수행을 위한 `src/assets/data`폴더에 `book.json` 파일 생성
* `btranslator`는 번역자를 의미(외국서적만 해당)
```
[  
   {  
      "bauthor": "카일 루든(Kyle Loudon)",
      "bdate":"2000년 04월",
      "btranslator":"허 욱",
      "bpublisher":"한빛미디어(주)",
      "btitle":"C로 구현한 알고리즘",
      "bprice":25000,
      "bisbn":"89-7914-063-0",
      "bimgurl":"http://image.hanbit.co.kr/cover/_m_1063m.gif"
   },
   {  
      "bauthor":"권기경, 박용우",
      "bdate":"2002년 09월",
      "btranslator":"",
      "bpublisher":"한빛미디어(주)",
      "btitle":"IT EXPERT, 모바일 자바 프로그래밍",
      "bprice":23000,
      "bisbn":"89-7914-206-4",
      "bimgurl":"http://image.hanbit.co.kr/cover/_m_1206m.gif"
   },
   ...
   ...
   ...
]   
```
> JSON data를 불러오기 위해 `HttpClientModule` 이용
- `book-search.module.ts`파일 안에 import 구문 작성
```
import { HttpClientModule } from "@angular/common/http";
```
- `list-box.component.ts` 파일 
```
import { Component, OnInit } from '@angular/core';
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

@Component({
  selector: 'app-list-box',
  templateUrl: './list-box.component.html',
  styleUrls: ['./list-box.component.css']
})
export class ListBoxComponent implements OnInit {

  books: IBook[];

  constructor(private http: HttpClient) {
    this.http.get<IBook[]>('assets/data/book.json')
      .subscribe(res => this.books = res);
  }

  ngOnInit() {
  }

}
```
> 책의 정보를 가져오기 위해 HttpClient의 get() method를 호출하면서 `Arrow Function`을 이용해 코드를 작성했다. 

## 문제점
- 책이 100권 있으면 밑으로 쭉 나열된다. `Paging`처리 필요하다.
- `Event` 처리가 쉽지 않다.
- `book-search-main.component.html`에서 에서 만들어 놓은 선택 정보를 알ㅇ와서 필터링 해야하는데 현재로서는 어떤 도서를 선택했는지 알 수 없다.
- 그 외

[reference](https://moon9342.github.io/angular-lecture-exercise-2)