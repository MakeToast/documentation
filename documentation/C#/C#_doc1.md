# Hello C#
```
using System;

namespace C_
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello C#!");
            Console.WriteLine(args.Length);
            Console.ReadKey();
        }
    }
}
```
- C#의 확장자 : .cs
- 프로그램의 실행은 항상 Main()에서 시작
- `using` 키워드 
    - `using` namespace
    > namespace를 사용한다.<br>
- `static void Main(string[] args)` : 함수의 프로토타입
    - `string[]` args : Main 함수가 어떤 기능을 하기 위해서 받아야 하는 인자가 있다. 인자기 있어도 꼭 써야 하는 것은 아니다.
- `Console.WriteLine()` : 콘솔 화면에 프린트하기
- `Console.ReadKey()` :  콘솔에 키보드 값이 들어올 때까지 기다린다.