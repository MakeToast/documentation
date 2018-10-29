# 레지스터로 주소 지정

- 메모리를 사용할 때 주소를 간접적으로 사용 시 레지스터 이용
- 주소값을 직접 작성 
    - mov dword ptr ds:[402000], 0
- 주소값을 레지스터에 넣고 레지스터 이름을 넣는다 
    - mov dword ptr[eax], 0

- example
    - eax : 402000
    - mov dword ptr ds:[eax], 402004
        - [402000] : 04 20 40 00
    - mov eax, dword ptr ds: [402000]
        - eax : 402004
    - mov dword ptr ds:[eax], 12345678
        - [402004] : 78 56 34 12
    > c언어에서 포인터 개념
    - int a = 0;
        - mov dword ptr ds:[402000], 0
    - int * p = &a;
        - mov dword ptr ds:[402004], 402000
    - *p = 4;
        - mov ebx, dword ptr ds:[402004]
        - mov dword ptr ds:[ebx], 4
        > int 형 포인터는 4바이트

    - 값을 읽어올 때도 마찬가지이다.
        - mov byte ptr ds:[ebx], 4
        - mov eax, dword ptr ds:[ebx]
- 정리 
    - mov에서 메모리 접근 할 때 메모리에 즉시값을 이용하지 않고 레지스터 안의 메모리 주소값을 사용한다.
