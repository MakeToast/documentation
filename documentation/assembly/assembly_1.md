# 어셈블리어의 구성
- 어셈블리어는 일단 명령어(OpCode <operation>)와 오퍼랜드(피연산자, Operand)로 이루어져 있습니다.
- "XX를 ~~해라" 라고 한다면
    * "~~"는 명령어(operator)에 해당되고
    * "XX"는 오퍼랜드에 해당합니다.

## 명령어 mov
- mov 를 보면 move가 연상이 되는데 즉 이동시킬 때 사용한다.
- 명령어 : mov `register 이름`, 값
    - 값이 register 공간에 넣는다.
    - register 이름에는 EAX, EBX, ECX, EDX 들어간다.
    - 쉬운 예시
        - `mov` `[상자]`, `사과` : 사과를 상자에 넣어라. 

- MOV EAX, 1
    - MOV : Operator, 이동해라
    - EAX : Operand, EAX에
    - 1 : Operand, 1을
    > Operand는 , 로 구분되고 여러개를 넣을 수 있다. 

- 기계적으로 이해
    - CPU, RAM, Hardware
    - CPU 
        - 연산이 일어난다.
        - 저장 공간, register(레지스터)가 있다. 읽기쓰기 속도 굉장히 빠르다.
    - RAM
        - CPU의 register의 용량이 작기 때문에 RAM에 프로그램이 올라간다.
    
    - RAM에 저장된 프로그램의 데이터를 CPU에서 읽어서 register에 저장해서 연산을 한 후 다시 RAM에 저장된 프로그램에 쓴다.

