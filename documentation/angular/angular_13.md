# Component Data Sharing

## Comtent Projection
- AngularJS에서 `transclusion`이락 불리던 `Content Projection`에 대해 알아보자
> 부모 Component가 자식 Component에게 template을 전달해 줄 수 있는 기능<br>

- book-search-main.component.html
```
<div class="bookSearch-outer">
  <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded box-shadow">
    <img class="mr-3" src="assets/images/search-icon.png" alt="" width="48" height="48">
    <div class="lh-100">
      <h5 #resultStatus class="mb-0 text-white lh-100">Search Result : {{searchTitle}}</h5>
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
    <button mat-raised-button color="primary"
            (click)="clearCondition()">검색 초기화</button>
    <button mat-raised-button color="primary"
            (click)="changeDOM()">DOM 직접 변경</button>
  </div>

  <div>
    <app-search-box [bookCategory]="displayCategoryName"
                    (searchEvent)="changeTitleBar($event)">
      <p>Content Projection!</p>
      <p>First Paragraph</p>
      <p>Second Paragraph</p>
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
- 변경된 부분
```
<app-search-box [bookCategory]="displayCategoryName"
                (searchEvent)="changeTitleBar($event)">
  <p>Content Projection!</p>
  <p>First Paragraph</p>
  <p>Second Paragraph</p>
</app-search-box>
```
> 하위 Component를 포함시키면서 3개의 `<p>` Element를 전달한다. 이렇게 부모 Component가 자식 Component에게 특정 template을 전달해 줄 수 있는 기능이다. <br>

- 자식 Component : search-box.component.html
```
<div class="example-container">
  <mat-toolbar #toolbar class="search-toolbar-style">
    Search Keyword : {{keyword}}
    <ng-container *ngIf="_bookCategory != null">
      ( {{_bookCategory}} )
    </ng-container>
  </mat-toolbar>
  <mat-form-field>
    <input matInput #inputKeyword placeholder="Search Keyword"
           [(ngModel)]="keyword" (ngModelChange)="inputChange()">
  </mat-form-field>
  <button mat-raised-button color="warn"
          (click)="setKeyword(inputKeyword.value)">Search!</button>
  <ng-content></ng-content>
</div>
```
> 맨 마지막에 `<ng-content></ng-content>` directive가 보인다. 이 directive가 부모 Component가 전달해 준 template으로 치환된다.

[reference](https://moon9342.github.io/angular-lecture-data-share-4)