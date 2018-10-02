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