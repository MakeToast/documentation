# stack, push, pop : register esp
- stack
    - 제한적으로 접근할 수 있는 나열 구조
    - 한쪽 끝에서만 자료를 넣거나 뺼 수 있는 선형구조 (LIFO : Last in First out)
    - push : 자료를 밀어 넣는다.
    - pop : 자료를 꺼낸다.
- esp : stack의 맨 윗부분을 가리키고 있다.

- example
    - esp : [0018FF84]
    - push 1
        - esp : [0018FF80]
        - [0018FF80] : 1
    - pop eax
        - esp : [0018FF84] 

    - push 하면 주소값이 점점 작아지고 pop하면 주소값이 점점 커진다.(4바이트씩)
- 스택을 왜 쓸까?
    - C언어에서 함수 호출 할 떄 쓰인다.