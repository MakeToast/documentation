# PRACTICE #1.2

## Navigation Menu 작성
- Routing Module을 이용해 Router의 구성과 등록이 완성되었으나 해당 Routing Path에 대한 View를 어디에 표시할지는 아직 지정하지 않았다.
- `app.component.html`을 수정해 `RouterOutlet` directive를 이용해 Viewdml Rendering 위치를 지정해야 한다.
- 이번 예제에서는 Bootstrap을 이용해서 화면을 구성했다.
- beta.3은 Angular CLI로 Production build했을 때 bundling 오류가 발생한다.
```
npm install bootstrap@4.0.0-beta.2
```
-`.angular.json` 파일 수정
```
"styles": [
        "../node_modules/bootstrap/dist/css/bootstrap.min.css",
        "styles.css"
   ],
```
- `app.component.html` 파일 수정
```
<nav>
  <a routerLink="/">Home</a>
  <a routerLink="/book">도서검색</a>
  <a routerLink="/movie">영화검색</a>
</nav>
<router-outlet></router-outlet>
```
>`<a>`의 href속성을 이용하면 서버에 request를 보내게되니 href를 이용하지 않는다. 각각의 메뉴를 클릭했을 때 해당 URL을 Router에 전달하고 Router에 의해서 Component가 선택되어 `<router-outlet></router-outlet>`안에 Component가 지정한 HTML이 출력되게 된다. Home 화면의 내용을 바꾸려면 `src/app/pages/home`안의 `home.component.html`을 수정해야 한다.<br>
>> 참고로 `routerLinkActive` directive를 이용하면 routerLink directive의 값과 현재 browser URL이 정확히 일치할 때 특정 style의 class를 지정할 수 있다.
```
<nav>
    <a routerLink="/">Home</a>
    <a routerLink="/book"
       [routerLinkActiveOptions]="{ exact: true }"
       routerLinkActive="menuActiveClass">>도서검색</a>
    <a routerLink="/movie">영화검색</a>
</nav>
<router-outlet></router-outlet>
``` 
> 위처럼 링크를 클릭해서 특정 경로로 Routing을 할 수도 있지만 버튼을 클릭했을 때처럼 프로그램적으로 Routing을 변경해야 하는 경우도 있을 수 있다. 이때 Angular Router의 `navigate` method를 이용하면 된다.
```
import { Router } from '@angular/router';
...
...
constructor(private route:Router) { }
...
...
gotoBook() {
    // Router객체에 대해 method호출
    this.route.navigate(['book']);
}
```
- 현재까지 작성한 Angular Project에 대해 production build를 진행하려면
```
ng build --prod --base-href=/my-base-url/
```
[reference](https://moon9342.github.io/angular-lecture-exercise-1)