# Material Table Component
- list-box Component가 표현하는 부분을 Material Table을 이용해서 작성해보자.
-  기본적인 테이블 구성과 함께 `Pagination`까지 추가해서 간단하게 `Paging`까지 구현해보자.
- `DataSource`만 Table에 잘 연결하면 알아서 보여주는 것이 Component 기반 개발의 장점

- `list-box.component.css`
```
.example-container {
  display: flex;
  flex-direction: column;
  min-width: 300px;
  margin-top: 30px;
}

.mat-table {
  overflow: auto;
  max-height: 500px;
}

.mat-header-cell.mat-sort-header-sorted {
  color: black;
}

.list-table-style {
  font-family: Georgia;
}

.list-header-style {
  background-color: beige;
}
```
- `list-box.component.html`파일
```
<div class="example-container mat-elevation-z8">
  <mat-table class="list-table-style" #table [dataSource]="dataSource">

    <ng-container matColumnDef="bisbn">
      <mat-header-cell *matHeaderCellDef> ISBN </mat-header-cell>
      <mat-cell *matCellDef="let element"> {{element.bisbn}} </mat-cell>
    </ng-container>

    <ng-container matColumnDef="btitle">
      <mat-header-cell *matHeaderCellDef> Title </mat-header-cell>
      <mat-cell *matCellDef="let element"> {{element.btitle}} </mat-cell>
    </ng-container>

    <ng-container matColumnDef="bauthor">
      <mat-header-cell *matHeaderCellDef> Author </mat-header-cell>
      <mat-cell *matCellDef="let element"> {{element.bauthor}} </mat-cell>
    </ng-container>

    <ng-container matColumnDef="bprice">
      <mat-header-cell *matHeaderCellDef> Price </mat-header-cell>
      <mat-cell *matCellDef="let element"> {{element.bprice}} </mat-cell>
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
> DataSource 바인딩 : "`<mat-table class="list-table-style" #table [dataSource]="dataSource">`"<br>
> Property binding을 이용하여 Component에 있는 `dataSource`라는 속성과 연결시켰다. 이 `dataSource`라는 속성은 도서정보에 대한 객체배열을 이용해서 만든 `MatTableDataSource` class의 객체이다. `JSON`데이터를 가져와서 만든 객체이다.

- `book-search.module.ts` 파일 import 구문 작성 (Table Component, MatPaginatorModule)
```
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
```
- `list-box.component.ts` 파일
```
import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { MatTableDataSource } from '@angular/material';
import { MatPaginator } from '@angular/material';
import { ViewChild } from '@angular/core';

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

  constructor(private http: HttpClient) {
    this.http.get<IBook[]>('assets/data/book.json')
      .subscribe(res => {
        this.books = res;
        this.dataSource = new MatTableDataSource<IBook>(this.books);
        this.dataSource.paginator = this.paginator;
      });
  }
}
```

## Code Review
> 원래 Code Review란 표현은 Code Inspection에서 기인한 용어로 **코드를 실제로 실행하지 않고 사람이 검토하는 과정을 통해 논리적인 잠재 오류를 찾아내고 이를 개선하는 작업**이다.

- Table 생성하는 구문
```
<mat-table [dataSource]="dataArray">
  ...
</mat-table>
```
> `dataArray`라고 되어있는 부분이 실제 Table에 rendering되는 데이터이다. 배열형태로 되어 있고 배열안의 각각의 객체를 `row`로 가져와서 화면에 출력

- Table의 컬럼을 표현하는 template
```
<ng-container matColumnDef="bisbn">
    <mat-header-cell *matHeaderCellDef> ISBN </mat-header-cell>
    <mat-cell *matCellDef="let element"> {{element.bisbn}} </mat-cell>
</ng-container>
```
> `matColumnDef` 속성은 사용할 컬럼의 이름이다. 이 부분은 `list-box.component.ts` 파일 안에 컬럼명에 대한 배열이 정의되는데 이 부분과 매칭되어야 한다.

- `list-box.component.ts`안에 정의된 컬럼명에 대한 배열
```
displayedColumns = ['bisbn', 'btitle', 'bauthor', 'bprice'];
```
- 아래의 구문에 의해 ISBN 컬럼의 제목과 내용이 출력된다.
```
<mat-header-cell *matHeaderCellDef> ISBN </mat-header-cell>
<mat-cell *matCellDef="let element"> {{element.bisbn}} </mat-cell>
```
> `dataSource`에 연결된 모든 `row`를 가져와서 `element`라는 변수에 반복적으로 할당하면서 `element.bisbn`값을 테이블에 출력하라는 말이다.
```
this.dataSource = new MatTableDataSource<IBook>(this.books);
```
> `list-box.component.ts`에서는 사용할 데이터를 `HttpClient`의 get() method로 가져온 후 객체화 시킨다.

**dataSource와 연결시키기 위해 위에 있는 코드처럼 객체를 생성해서 연결해야 한다.**
- `Paginator`의 사용은 코드에 나온것처럼 사용하면 된다. 내부적으로 처리되기 떄문에 사용하는 방법만 알자.
- `TypeScript`를 사용하기 때문에 interface를 이용하여 data type을 명확히 지정했다. 이 부분 역시 이전 HTML Table Element로 작업했을 때와는 다르게 처리해야 한다.

[reference](https://moon9342.github.io/angular-lecture-material-table)