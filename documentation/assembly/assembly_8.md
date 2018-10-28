# 증감 명령어 inc, dec

- inc : increment || dec :decrement
- inc [reg]/[mem] || dec [reg]/[mem] 
    - [reg] example
        - INC EAX | INC EBX | INC AX
        - MOV EAX, 0 -> EAX = 0
        - INC EAX -> EAX = 1

        - DEC EAX | DEX EBX | DEC AX
        - MOV EAX, 3 -> EAX = 3
        - DEC EAX -> EAX = 2
    - [mem] example
        - INC DWORD PTR DS:[402000]
        - INC WORD PTR DS:[402000]
        - INC BYTE PTR DS:[402000]
        - 가장 낮은 비트 부터 채워진다.

        - DEC DWORD PTR DS:[402000]
