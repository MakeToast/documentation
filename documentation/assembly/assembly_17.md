# 상태레지스터 PF AF

### P : 패리티 플래그

- 연산 결과에서 1로된 비트의 수가 짝수일 경우 참이 된다.

- crc32 : 파일을 체크할 수 있고 복구할 수 있는 방법
    - 오류가 난 것을 어떻게 알고 복구할까?
    - 원리는 패리티를 사용해서 안다.

- 패리티는 비트에서 1의 개수의 동등성을 유지시키는 것이다.
- 홀수 패리티 : 비트의 개수를 홀수개로 맞춰 동등성 유지
- 짝수 패리티 : 비트위 개수를 짝수개로 맞춰 동등성 유지
- example (홀수 패리티)
    - -4 : 1100 이고 패리티 비트 : 1 이라면
    - 11001 : 4자리 비트가 있는데 거기에 패리티 비트 1개까지 포함해서 1의 개수 3개로 홀수 개수를 유지
    - 데이터가 깨져서 10001 1의 개수 2개 -> 데이터가 깨졌음을 알 수 있다.

- 인텔 : 홀수 패리티
    - 하위 8비트만 신경 쓴다.  

### A : 보조 캐리 플래그

- 연산 결과 하위 4비트에서 비트 넘위를 넘어섰을 때(올림 또는 내림) 참이 된다. 이진화십진법(BCD)에서 사용
- BCD
    - 이진수 네자리를 묶어 십진수 한자리로 사용하는 기수법이다.
- example
    - MOV EAX, 9
    - MOV EBX, 9
    - ADD EAX, EBX
        - EAX : 12
        - A : 1
        - P : 1