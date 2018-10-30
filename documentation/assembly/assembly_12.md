# 조건분기명령어 JZ(JE) 상태레지스터 ZF
- JMP말고 여러가지가 있다.
- 공통적으로 인자를 하나, 주소를 받는다.

- JMP 주소 : 무조건 점프
- JZ 주소 : 조건 점프
    - J = JUMP, Z = 0
    - 이전의 결과가 0라면 점프해라
    - 상태 레지스터 Z가 1일 때 점프한다.
    - 상태 레지스터 : 레지스터 이름이 한 글자이고 1비트이다.
            - C P A Z S T D O
    - example
        - mov eax, 1
            - eax : 1
            - Z : 0
        - inc eax
            - eax : 2
            - Z : 0
        - jz 401005
            - eax = 2이므로 jz안함
            - Z : 0
        - dec eax
            - eax : 1
            - Z : 0
        - dec eax
            - eax : 0
            - Z : 1
        - jz 401009
            - eax = 0이므로 jz함

- JE 주소 : 조건 점프
    - J : JUMP, E : EQUAL
    - 같으면 점프를 해라.
    - 비교하는 어셈블리어 : CMP
        - CMP eax, 0 (크기가 같아야 한다)
        - 같으면 상태레지스터 Z를 1로 만들어준다.  
        - CMP는 내부적으로 - (subtract)로 구성
        - CMP eax, 0 vs sub eax, 0
        > sub명령어는 eax에 0을 뺀 후 eax에 저장하지만 cmp는 빼기를 한 결과를 버린다.

- JE와 JZ는 같은 기계어이다.
