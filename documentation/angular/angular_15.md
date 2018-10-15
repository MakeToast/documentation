# Service Mediator Pattern
- Service의 개념을 이용해서 Component간 데이터를 공유하는 Service Mediator Pattern
- 도서 종류와 검색어를 입력하고 Search!버튼을 클릭하면 Service를 이용해서 JSON파일로부터 데이터를 읽는다.

- RESTful 서버를 이용하지 않으니 JSON 파일로부터 데이터를 읽어들이고 데이터를 filtering해서 사용하자.
- 부모 Component인 **book-search-main** Component에서 선택된 도서 종류를 **search-box** Component에서 사용해야 하므로 선택된 도서종류에 대한 값을 **search-box** Component에서 사용할 수 있도록 코드를 수정하자.
- **book-search-main.component.html** 중 일부
```
    <app-search-box [bookCategory]="displayCategoryName"
                    [selectedValue]="selectedValue"
                    (searchEvent)="changeTitleBar($event)">
    </app-search-box>
```
> `@Input decorator`로 데이터를 받기 위해 **search-box.component.ts**를 수정하자.

- **search-box.component.ts** 파일 수정
```
import {
  Component, OnInit,
  Input, Output, EventEmitter
} from '@angular/core';
import { HttpSupportService } from "../http-support.service";
import {JSON_DATA_CONFIG, JsonConfig} from "./json-config";


@Component({
  selector: 'app-search-box',
  templateUrl: './search-box.component.html',
  styleUrls: ['./search-box.component.css'],
  providers: [
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
  
  @Input('selectedValue') selectedValue:string;

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

    this.httpSupportService.getJsonData(
      this.jsonConfig.url,
      this.jsonConfig.name,
      this.selectedValue,
      this.keyword);
  }

  inputChange(): void {

  }
}
```
> 부모 Component로부터 받은 도서종류와 Client로부터 입력받은 keyword를 가지고 injection된 Service의 method를 호출한다.
- **http-support.service.ts** 파일
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

  getJsonData(url:string, name:string, category:string, keyword:string) {
    this.http.get<IBook[]>(`${url}${name}`)
        .subscribe(res => {
           let tmp = null;
           // 도서종류와 검색어를 이용한 도서 데이터 Filtering 시작
           if( category == 'all' ) {
             tmp = res.filter(function(item,idx,arr) {
               if(item.btitle.includes(keyword)) {
                 return true;
               } else {
                 return false;
               }
             });
           } else if( category == 'country') {
             tmp = res.filter(function(item,idx,arr) {
               if(item.btitle.includes(keyword)) {
                 return true;
               } else {
                 return false;
               }
             }).filter(function(item,idx,arr) {
               if(item.btranslator == '') {
                 return true;
               } else {
                 return false;
               }
             });
           } else if( category == 'foreign') {
             tmp = res.filter(function(item,idx,arr) {
               if(item.btitle.includes(keyword)) {
                 return true;
               } else {
                 return false;
               }
             }).filter(function(item,idx,arr) {
               if(item.btranslator != '') {
                 return true;
               } else {
                 return false;
               }
             });
           }
          // 도서종류와 검색어를 이용한 도서 데이터 Filtering 끝
           this.books = tmp;
           console.log(this.books);
        });
  }

  getBooks(): IBook[] {
    return this.books;
  }
}
```
> Filtering처리된 JSON데이터를 얻어와서 일단 `books`속성에 저장했다.<br>
> `list-box` Component에서 데이터를 가져가기 위해 `getBooks()` method를 하나 작성했다.<br>

- **list-box.component.html** 파일
```
<br>
<button mat-raised-button color="warn"
        (click)="getData()">Get DATA!</button>
<div class="example-container mat-elevation-z8">
  <mat-table class="list-table-style" #table [dataSource]="dataSource">

    <ng-container matColumnDef="bisbn">
      <mat-header-cell *matHeaderCellDef> ISBN </mat-header-cell>
      <mat-cell *matCellDef="let element">  </mat-cell>
    </ng-container>

    <ng-container matColumnDef="btitle">
      <mat-header-cell *matHeaderCellDef> Title </mat-header-cell>
      <mat-cell *matCellDef="let element">  </mat-cell>
    </ng-container>

    <ng-container matColumnDef="bauthor">
      <mat-header-cell *matHeaderCellDef> Author </mat-header-cell>
      <mat-cell *matCellDef="let element">  </mat-cell>
    </ng-container>

    <ng-container matColumnDef="bprice">
      <mat-header-cell *matHeaderCellDef> Price </mat-header-cell>
      <mat-cell *matCellDef="let element">  </mat-cell>
    </ng-container>

    <mat-header-row class="list-header-style"
                    *matHeaderRowDef="displayedColumns">
    </mat-header-row>
    <mat-row *matRowDef="let row; columns: displayedColumns;"></mat-row>
  </mat-table>

  <mat-paginator #paginator
                 [pageSize]="5"
                 [pageSizeOptions]="[5, 10, 20]"
                 showFirstLastButtons>
  </mat-paginator>
</div>
```
> Table 상단에 `Get DATA!`라는 버튼을 만들고 event binding을 시켰다.

- **list-box.component.ts** 파일
```
import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { MatTableDataSource } from '@angular/material';
import { MatPaginator } from '@angular/material';
import { ViewChild } from '@angular/core';
import {HttpSupportService} from "../http-support.service";

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
export class ListBoxComponent {

  displayedColumns = ['bisbn', 'btitle', 'bauthor', 'bprice'];
  dataSource;
  books: IBook[];

  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private httpSupportService:HttpSupportService) {
  }

  getData(): void {
    this.books = this.httpSupportService.getBooks();
    this.dataSource = new MatTableDataSource<IBook>(this.books);
    this.dataSource.paginator = this.paginator;
  }

}
```
> 주입된 Service객체를 이용해서 Service에 저장되있는 JSON데이터를 가져다가 Table의 DataSource에 설정한다.
![결과 화면](https://moon9342.github.io/assets/built/images/service-mediator-pattern.jpg)
> Service에 의해서 데이터가 공유되는 것은 확인했지만 새로 검색을 해서 데이터가 변경되면 list쪽에서는 데이터가 자동으로 변경되지 않는다.
[reference](https://moon9342.github.io/angular-lecture-data-share-service-mediator-pattern)