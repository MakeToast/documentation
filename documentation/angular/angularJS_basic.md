# AngularJS의 개념
- Directives
확장된 HTML, 커스텀 속성과 요소들로 이루어짐
웹 개발 시 HTML 태그를 많이 사용하는데 angular에서는 태그를 직접 정의해서 사용이 가능하다. 그리고 태그에 있는 속성도 직접 정의해서 사용이 가능하다.
- Expressions
자바스크립트에서는 변수와 함수를 만들 수 있다. 만약 HTML에서 자바스크립트에 있는 변수를 출력해야 하는 경우 Angular에서는 이 Expressions 기법을 이용해서 출력 가능하다.

```
<p>hello {{ name }}!!</p>
```
자바스크립트에 있는 네임 변수에 있는 값이 HTML에서 출력이 가능하다. 만약 네임변수에 크리스라는 문자열 값이 저장되어 있다면 HTML에서 hello 크리스!! 라고 출력된다.

- Module
Angular에서는 drective, controller, service 등을 하나로 모아놓은 컨테이너를 모듈이라고 한다.
기능적으로 비슷한 것들을 모아서 하나의 모듈을 만든다.
모듈끼리 서로 의존관계가 있는 경우 다른 모듈을 주입해서 사용이 가능하다.

- Controller
HTML 뒷단에 위치하고 HTML View를 조절한다.
비지니스 로직을 구현하는데 사용한다. 

- Service
비지니스 로직인데 컨트롤러와 다르게 재사용 할 수 있는 비니지스 로직을 서비스라고 한다. angular에서는 싱글톤?으로 구현되어 있기 때문에 데이터를 관리용도로 사용하는 것이 좋다.

--------------------------------
# To-Do 리스트 앱 만들기 - 컨트롤러

## 디렉티브
### 사용할 내장 디렉티브

- ng-app
ng-app이 선언된 부분부터 angular를 사용한다고 angular에게 알려주는 작업이다.
```
<body> -> <body ng-app>
```
- ng-init
자바스크립트 변수나 함수를 초기화 하는데 사용
```
<body> -> <body ng-app ng-init="name = 'Chris'">
```

## 표현식
### expression
- {{ 변수 이름 }}

## 모듈과 컨트롤러
- script.js
```
import angular from 'angular';

(function(){
  var app = angular.module('todo', []);

  app.controller('TodoCtrl', ['$scope', function($scope){
    $scope.name = 'Yoojin';
  }]);
})();
```
> var app = angular.module('todo', []); : app이라는 변수에 todo라는 angular 모듈이 할당됨<br>
> app.controller('TodoCtrl', ['$scope',function($scope) :컨테이너 만들기 -> 모듈은 큰 컨테이너, 모듈에는 컨트롤러 서비스 등이 있다.<br>
> $scope : 컨트롤러와 html간의 연결고리 같은 역할을 한다.
 

- index.html
```
<!doctype html>

<html>
  <head>
    <link rel="stylesheet" href="lib/style.css">
    <script src="lib/script.js"></script>
  </head>

  <body ng-app="todo" ng-controller="TodoCtrl">
  
      <h1>Hello {{name}}</h1>
    
    </div>
  </body>
</html>
```

### 값 말고 객체로 만들어보기
- script.js
```
import angular from 'angular';

(function(){
  var app = angular.module('todo', []);

  app.controller('TodoCtrl', ['$scope', function($scope){
    $scope.todo = {
      title: 'training',
      completed: false,
      createdAt: Date.now()
    }
  }]);
})();
```
- index.html
```
{{todo}}
```
또는
```
<h3>{{todo.title}}</h3>
<p>{{todo.completed}}</p>
<date>{{todo.createdAt}}</date>
```
- `<input>` 필드 써보기
```
<input type="text" ng-model="todo.title">
```
> 이런식으로 `<input>`를 써서 데이터가 변경되면 실제 자바스크립트의 데이터도 변경된다.<br>
> ng-model은 자바스크립트의 변수와 바인딩 된다. 양방향 바인딩
------------------------------------
# To-Do 리스트 앱 만들기 - 내장 디렉티브

## ngRepeat
- 배열이랑 쓸 때 좋다. 반복문 처럼 사용할 수 있는 디렉티브
- script.js -> todo를 배열로 만든다.
```
$scope.todos = [
      {
      title: 'training1',
      completed: false,
      createdAt: Date.now()
      },
      {
      title: 'training2',
      completed: false,
      createdAt: Date.now()
      },
      {
      title: 'training3',
      completed: true,
      createdAt: Date.now()
      }
    ]
```
- index.html
```
<div ng-repeat="todo in todos">
        <input type="text" ng-model="todo.title">
        <input type="checkbox" ng-model="todo.completed">
        <date>{{todo.createdAt}}</date>
</div>
```
이때 리스트 태그인 `<li>`를 쓰면 더 좋다.
```
<ul>
        <li ng-repeat="todo in todos">
          <input type="text" ng-model="todo.title">
          <input type="checkbox" ng-model="todo.completed">
          <date>{{todo.createdAt}}</date>
        </li>
      </ul>
```

## ngFilter
- 날짜를 꾸며보자.
```
<date>{{todo.createdAt | date:'yyyy-MM-dd HH:mm:ss'}}</date>
```

## ngClick
- 목록들에게 버튼을 누르면 삭제하는 기능을 가진 버튼을 만들어보자.
- index.html
```
<button type="button">delete</button>
```
- 버튼 핸들러 ngClick 를 만들어보자
```
<button type="button" ng-click="remove(todo)">delete</button>
```
- script.js `app.controller` 안에 remove() 함수 정의하기
```
$scope.remove = function(todo){
    // find todo indexin todos
    var idx = $scope.todos.findIndex(function(item){
      return item.id === todo.id;
    })

    // remove from todos
    if(idx > -1)
    {
      $scope.todos.splice(idx, 1)
    }
  };
```

## 필터버튼
- todo.completed의 상태에 따라 리스트 보이기
```
<li ng-repeat="todo in todos | filter:{completed: all}">
```
> index.html에서 | filter:{completed: false/ true/ all} 이렇게 값을 넣어 필터링 할 수 있다.
또는
```
    <li ng-repeat="todo in todos | filter:statusFilter">
    ...
    </li>
</ul>
    <button ng-click="statusFilter={completed:true}">Completed</button>
    <button ng-click="statusFilter={completed:false}">Active</button>
    <button ng-click="statusFilter={}">All</button>
```
----------------------
# To-Do 리스트 앱 만들기 - 폼 만들기

## 폼 만들기 1
- 새 폼을 만들고 input 필드를 넣어 새로운 todotitle을 넣으면 script.js의 add 함수로 넘길 것이다.
```
<form name="todoForm" ng-submit="add(newTodoTitle)">
        <input type="text" ng-model="newTodoTitle">
        <button type="submit">추 가</button>
      </form>
```
> ng-click을 넣을 수도 있지만 form형태이기 때문에 submit을 쓰기로 했다.
> 이때, input필드에 placeholder를 쓰면 입력칸에 흐린 글씨로 써진다.
> autofocus는 자동으로 커서가 되어있다.
## 폼 만들기 2
- script.js add 함수 작성
```
$scope.add = function(newTodoTitle){
    // create new todo
    var newTodo = {
      title: newTodoTitle,
      completed: false,
      createdAt: Date.now()
    };

    // push into todos
    $scope.todos.push(newTodo);
  };
```
- 추가 후 빈 텍스트로 만들고 싶다면
```
$scope.newTodoTitle = "";
```

## 폼 검증
- angular에서 폼을 만들 때 name 속성에 "todoForm"이라는 값을 할당했다. 이는 controller에 scope변수에 할당이 된다.
- 즉, controller안의 scope변수 안에 todoForm이라는 또 하나의 변수가 추가 되었다.
- todoForm에 어떤 값이 할당되었는지 살펴보자.
```
<pre>{{todoForm | json}}</pre>
```
- 결과값
{
  "$error": {},
  "$name": "todoForm",
  "$dirty": false,
  "$pristine": true,
  "$valid": true,
  "$invalid": false,
  "$submitted": false
}
- dirty와 valid 키
> dirty 플래그는 input 필드에 무언가를 쓰면 true로 바뀐다. pristine은 반대이다.<br>
> valid는 폼의 입력 값이 valid하면 true 아니면 false.

- minlength=3을 추가하자.
```
<input type="text" ng-model="newTodoTitle" placeholder="input new todo" minlength="3">
```
> 인풋 폼에 3자리 이상이 들어와야 valid 값이 true가 된다.

- 3자리 이상 입력하지 못했을 때 경고 메세지 띄우기. `ng-show` 로 조건을 걸자.
```
<div ng-show="todoForm.$dirty && todoForm.$invalid">
          <div role="alert">input 3 words</div>
</div>
```
-----------------------
# To-Do 리스트 앱 만들기 - 디렉티브
- 지금까지 Angular module과 controller를 사용하여 index.html이라는 템플릿에 출력했다.
- 이번에는 디렉티브로 refactoring 하자.

## todoTitle
- index.html
```
<todo-title></todo-title>
```
- script.js
```
app.directive('todoTitle', function(){
  return {
    template:'todo title'
  }
});
```
> 아까 controller를 정의했듯이 이번에는 directive를 정의한다. template: 다음에는 문자열이 올 수도 있지만 html도 올 수 있다. 
` template:'<h1>todo title</h1>' `
## todoItem
- ng-repeat을 디렉티브로 바꿔보자.
- index.html
```
<todo-item></todo-item>
```
- script.js
```
app.directive('todoItem', function(){
  return {
    template : 
    '<input type="text" ng-model="todo.title">'+
     '<input type="checkbox" ng-model="todo.completed">'+
     '<date>{{todo.createdAt | date:'yyyy-MM-dd HH:mm:ss' }}</date>'+
    '<button type="button" ng-click="remove(todo)">delete</button>'
  }
});
```
- template가 길어질 경우 `templateUrl` 사용
```
templateUrl: todoItem.tpl.html
```
- 디렉티브만 별도의 파일 directive.js로 관리해보자.
- 이때, app이라는 변수는 directive.js에선 사용할 수 없다.
- 대신 Angular에서 아까 만들었던 'todo' 모듈에 접근할 수 있다.

- directive.js
```
angular.module('todo').directive('todoTitle', function(){
  return {
    template:'<h1>todo title</h1>'
  }
});

angular.module('todo').directive('todoItem', function(){
  return {
    templateUrl: 'todoItem.tpl.html'
    
  }
```
- index.html에서 로딩
```
<script src="directives.js"></script>
```

## todoFilters
- 필터 버튼들을 별도의 directive로 만들어보자.
- index.html
```
<todo-filters></todo-filters>
```
- directives.js
```
angular.module('todo').directive('todoFilters', function(){
  return {
    templateUrl: 'todoFilters.tpl.html'
  }
});
```
- todoFilters.tpl.html
```
<button ng-click="statusFilter={completed:true}">Completed</button>
<button ng-click="statusFilter={completed:false}">Active</button>
<button ng-click="statusFilter={}">All</button>
```
## todoForm
- directive를 이용해서 마지막으로 입력 폼 부분을 분리해보자.
- index.html
```
<todo-form></todo-form>
```
- directives.js
```

angular.module('todo').directive('todoForm', function(){
  return{
    templateUrl: 'todoForm.tpl.html'
  }
});
```
- todoForm.tpl.html
```
<form name="todoForm" ng-submit="add(newTodoTitle)">
  <input type="text" ng-model="newTodoTitle" placeholder="input new todo" minlength="3">
  <button type="submit">추 가</button>
  <div ng-show="todoForm.$dirty && todoForm.$invalid">
    <div role="alert">input 3 words</div>
    </div>
</form>
```

### 번외
- controller와 module도 따로 파일로 분리할 수 있다.
- controllers.js
```
app.controller('TodoCtrl', ['$scope', function($scope){
    $scope.todos = [
      {
      title: 'training1',
      completed: false,
      createdAt: Date.now()
      },
      {
      title: 'training2',
      completed: false,
      createdAt: Date.now()
      },
      {
      title: 'training3',
      completed: true,
      createdAt: Date.now()
      }
    ]

  $scope.remove = function(todo){
    // find todo indexin todos
    var idx = $scope.todos.findIndex(function(item){
      return item.id === todo.id;
    })

    // remove from todos
    if(idx > -1)
    {
      $scope.todos.splice(idx, 1)
    }
  };

  $scope.add = function(newTodoTitle){
    // create new todo
    var newTodo = {
      title: newTodoTitle,
      completed: false,
      createdAt: Date.now()
    };
    // push into todos
    $scope.todos.push(newTodo);
    $scope.newTodoTitle = "";
  }; 
}]);
```
- app.js (module.js보단 app이라고 함)
```
angular.module('todo', []);
```
-----------------------
# To-Do 리스트 앱 만들기 - 서비스
- controller를 refactoring 해볼 것이다.
1. 데이터를 관리하는 역할
2. View를 관리하는 역할

## todoStorage: get()
- services.js -> service말고 factory 함수를 이용한다.
```
angular.module('todo').factory('todoStorage', function(){
  var storage = {
    todos: [
      {
      title: 'training1',
      completed: false,
      createdAt: Date.now()
      },
      {
      title: 'training2',
      completed: false,
      createdAt: Date.now()
      },
      {
      title: 'training3',
      completed: true,
      createdAt: Date.now()
      }
    ],
    get: function(){
      return storage.todos;
    }
  }
  return storage;
});
```
- controllers.js
```
 $scope.todos = todoStorage.get();
```
## todoStorage: remove(), add()

### remove()
- services.js
```
remove: function(todo){
      // find todo indexin todos
      var idx = storage.todos.findIndex(function(item){
        return item.id === todo.id;
      })

      // remove from todos
      if(idx > -1)
      {
        storage.todos.splice(idx, 1)
      }
    }
```
- controllers.js
```
 $scope.remove = function(todo){
    todoStorage.remove(todo);
  };
```

### add()
- services.js
```
add: function(newTodoTitle){
      // create new todo
      var newTodo = {
        title: newTodoTitle,
        completed: false,
        createdAt: Date.now()
      };
      // push into todos
      storage.todos.push(newTodo);
    }
```
- controllers.js
```
$scope.add = functiong(newTodoTitle){
    todoStorage.add(newTodoTitle);
    $scope.newTodoTitle = "";
  }; 
```
## todoStroage: localStorage

- 실제 데이터를 메모리 상에 저장한다.
- 브라우저를 refresh를 하게 되면 데이터가 초기화 된다. 

### localStroage
- key, value 저장소

자바스크립트에서는 localStorage라는 함수를 사용할 수 있다.
- localStroage.setItem(key, value);
- localStroage.getItem(key); // value, localStorage[key] 접근 가능
- 입력은 무조건 string으로 처리됨(정수나, boolean 값으로 저장 불가)
- localStorage.length
- localStorage.key(value); // key
- 최대 약 5mb 용량

- 크롬은 SQLite 사용함
- 영구 보관
- sessionStorage는 새 탭, 새 윈도우로 범위가 제한된다는 점이 localStorage와 차이점

- services.js
```
angular.module('todo').factory('todoStorage', function(){
  var TODO_DATA = 'TODO_DATA';
  var storage = {
    todos: [],
    // private method
    _saveToLocalStorage: function(data){
      localStroage.setItem(TODO_DATA, JSON.stringify(data));
    },

    // private method
    _getFromLocalStrorage: function(){
      return JSON.parse(localStorage.getItem(TODO_DATA)) || [];
    },

    get: function(){
      angular.copy(storage._getFromLocalStrorage(), storage.todos)
      return storage.todos;
    },

    remove: function(todo){
      // find todo indexin todos
      var idx = storage.todos.findIndex(function(item){
        return item.id === todo.id;
      })

      // remove from todos
      if(idx > -1)
      {
        storage.todos.splice(idx, 1)
      }
    },

    add: function(newTodoTitle){
      // create new todo
      var newTodo = {
        title: newTodoTitle,
        completed: false,
        createdAt: Date.now()
      };
      // push into todos
      storage.todos.push(newTodo);
      storage._saveToLocalStorage(storage.todos);
    }  

  }
  return storage;
});
```
- remove 함수에 추가해서 삭제 데이터에 저장하기
```
remove: function(todo){
      // find todo indexin todos
      var idx = storage.todos.findIndex(function(item){
        return item.id === todo.id;
      })

      // remove from todos
      if(idx > -1)
      {
        storage.todos.splice(idx, 1)
        storage._saveToLocalStorage(storage.todos);
      }
    },
```

## todoStorage: update()
- 데이터 업데이트 로직 만들기
1. 체크박스 표시
2. 텍스트 인풋 필드 변경
- todoItem.tpl.html에 ng-click 설정
```
<input type="checkbox" ng-model="todo.completed" ng-click="update()">
```
- controllers.js에 update() 함수 구현
```
$scope.update = function(){
    todoStorage.update();
}
```
- services.js에 update() 함수 구현
```
update: function(){
    storage._saveToLocalStorage(storage.todos);
} 
```
- angular에서는 텍스트 필드에서 포커스아웃하게 되면 blur가 되는데 이 때 ng-blur를 통해 핸들러를 설정할 수 있다.
```
<input type="text" ng-model="todo.title" ng-blur="update()">
```