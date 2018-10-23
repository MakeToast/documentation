# 범용 레지스터

- 레지스터 
    * CPU 내에 있는 값을 저장할 수 있는 공간
    * RAM하고 다르다
    * 레지스트리(윈도우에서 다양한 시스템 설정하기 위한 것)와 다르다.

- 레지스터에 값을 넣는 형태 : mov reg, value
- 레지스터 안에 있는 값을 다른 레지스터의 값을 넣는 형태 : mov reg1, reg2
    - reg1과 reg2 공간의 크기는 같아야 한다

- 값을 넣는다 == `덮어쓴다`
    - example
        - mov eax, 0 : eax에 0 을 넣어라.
        - mov ebx, eax : ebx에 eax의 값을 넣어라.

### EAX

- EAX , AX , AH , AL 란?
    - 과거 CPU 16비트일 때, 
        - AX : 전체 공간 2바이트 
        - AX의 상위 1바이트 : AH (High)
        - AX의 하위 1바이트 : AL (Low)

    - 현재 CPU 32비트일 때,
        - EAX : Extended AX, 전체 공간 4바이트를 말함
        - EAX의 하위 2바이트 : AX 
            - AX의 상위 1바이트 : AH (High)
            - AX의 하위 1바이트 : AL (Low)

    - CPU 64비트일 때,
        - RAX

- example
    - MOV EAX, 12D687
        - 1234567 -> 12D687
        - 16진수로 2자리수가 한 바이트이다.
        - EAX : | 0 | 0 | 1 | 2 | D | 6 | 8 | 7 | 
            - AX : | D | 6 | 8 | 7 | 
            - AH : | D | 6 | 
            - AL : | 8 | 7 | 

