# 조건분기명령어 JNE JA JB 상태레지스터 CF
- JE  JZ
- JNE JNZ : N 은 NOT
    - 0이 아닐 때 JUMP

    - example
        - MOV EAX, 1   
            - EAX = 1
        - CMP EAX, 1
            - 1- 1 = 0, Z(제로 플래그) = 1
        - JNE SHORT 401005
            - JNE는 Z가 0일때 점프
        - CMP EAX, 0
            - 1-0 = 1, Z = 0
        - JNE SHORT 401005
            - Z=0이므로 점프
    
- JA : ABOVE
- JB : BELOW
    - example
        - CMP EAX, 0
            - 1-0 = 0
        - JB SHORT 40100F
            - EAX가 0보다 작으면 점프
        - JA SHORT 40100F
            - EAX가 0보다 크면 점프

- JA, JB는 어떤 조건에 의해서 작동을 할까?
    - CF : Carry 비트 
    > 비트 자리수가 넘어가는 연산이 있으면 캐리비트 세팅 된다.
