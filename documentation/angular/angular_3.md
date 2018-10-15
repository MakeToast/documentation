# Angular Material
- `Material Design`은 모바일과 데스크탑 그리고 그 외 다양한 디바이스들의 application을 개발할 때 하나의 일관된 디자인을 적용하고자 Google이 공개한 `design guidline`
- `Material Design`이란 플랫 디자인의 장점을 살리면서도 빛에 따른 종이의 그림자 효과를 이용하여 입체감을 살리는 디자인 방식. 미니멀리즘 (최소한의 요소만을 사용하여 대상의 본질을 표현하는 디자인 기법)추구
- 'Angular Material' 이란 Material Design에 대한 컨셉을 Angular application에 적용하기 위해 만든 Component

## Angular Material & Angular Material CDK 설치
```
npm install --save @angular/material @angular/cdk
```
- `--save`옵션은 `package.jsaon`의 `dependencies`에 설치된 패키지와 버전 정보가 기록

## Angular Animation Module 설치
- 몇개의 Material Component는 Angular Animation Module에 의존성을 가지고 있다.
```
npm install --save @angular/animations
```
- `@angular/animations` module은 내부적으로 `WebAnimation API` 아용
- `src/app`폴더 안에 있는 Root Module인 `app.module.ts`파일 수정
```
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

// BrowserAnimationsModule import 구문 추가
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule // BrowserAnimationsModule 추가
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

## 사용할 Component import
- 이 부분은 나중에 View에 대한 HTML을 작성할 떄 해야 되는 작업이다.
- 어떤 Component를 이용하여 View를 구성할지 결정이 되어야 import할 수 있기 때문이다.

- Practice : Material Table Component 
- `src/app`폴더 안에 있는 Root Module인 `app.module.ts` 파일 수정
```
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations'

// Material Table Component 사용을 위한 MatTableModule import
import { MatTableModule } from '@angular/material/table'

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

## 사용할 Theme 설정
- application에 적용할 Theme를 설정.
- 기본적으로 제공되는 built-in theme는 현재 4가지 존재. 그 중 하나를 설정하면 된다.
- Angular CLI를 이용하고 있기 때문에 `src` 폴더 안에 있는 `style.css`파일 수정
```
@import '~@angular/material/prebuilt-themes/indigo-pink.css';
```

## Gestures 지원을 위한 HammerJS설치
- 사용자 Gestures를 지원하기 위해 몇개의 Material Component들은 HammerJS에 의존한다.
```
npm install --save hammerjs
```
- 설치 후 우리 application의 시작점(entry point)인 `main.ts`에 코드 추가
```
// hammerjs import 추가
import 'hammerjs';
```

## Material Icon사용을 위한 설정
- Material은 쉽게 사용할 수 있는 Icon 제공
- `index.html` 파일 수정
```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>MySearchProject</title>
  <base href="/">

  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <!-- Material Icon 설정 -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>
  <app-root></app-root>
</body>
</html>
```

[reference](https://moon9342.github.io/angular-lecture-material)