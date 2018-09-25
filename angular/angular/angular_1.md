# Angular 개발환경 - Angular CLI
- 일반적으로 Framework를 도입할 때 가장 힘든 점 중 하나 : 개발환경 구축
- Angular는 `Angular CLI`를 제공함으로 이런 복잡함 해결
- Angular Project를 쉽게 생성하고 프로젝트를 시작하기 위한 scaffolding을 포함해서 다양한 기능을 제공하는 것이 바로 Angular CLI

![ANGULAR CLI를 이용할 경우와 그렇지 않는 경우](https://qph.fs.quoracdn.net/main-qimg-f461e39bf3273763a1234972eb7d4fff)
[이미지출처](https://www.quora.com/What-is-Angular-CLI)

- Angular CLI 설치
```
npm install -g @angular/cli
```
- 성공적으로 설치가 끝난 후 Angular CLI 버전 확인
```
ng --version
```

## Angular 프로젝트 생성
- Angular CLI를 이용하여 프로젝트 생성. 프로젝트 명은 mySearchProject
```
ng new mySearchProject  // --skip-install 을 사용하면 프로젝트 기본 구조와 파일만 scaffolding
```

## 개발환경 서버를 이용한 Angular 프로젝트 실행
- 프로젝트 root로 working directory를 이동 후 다음 명령을 실행하면 `Webpack`을 이용하여 우리 소스를 bundling하고 로컬 웹서버를 이용하여 우리 프로젝트를 서비스하게 된다.
```
ng serve
```
- 명령 수행이 끝나면 **webpack: Compiled Successfully.** 메세지가 출력된다.
- 아래의 주소를 브라우저에서 접속해보자.
__http://localhost:4200__
- `--o` 를 이용하여 `ng serve`를 실행시키면 default browser를 실행시켜서 해당 URL에 접속해 결과를 쉽게 확인 가능

