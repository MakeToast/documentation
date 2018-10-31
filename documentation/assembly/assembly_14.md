# JA JB에 N과 E 붙이기

- JA와 JB에 N을 붙일 수 있다.
    - J 다음에 N이 와야 한다.
    - JNA : JA 반대, 
        - JA : a > b라면 JNA : a <= b
        - JAE : a >= b
    - JNB : JB 반대, 
        - JB : a < b라면 JNB : a >= b
        - JBE : a <= b
    - JNA == JBE, C = 1 or Z = 1 일때 JUMP
    - JNB == JAE, C = 0, Z = 0 or C = 0, Z = 1 일때 JUMP
    - CF와 ZF 둘 중 하나를 본다.

    - JNBE = JA, JBE = a <= b 인데 N을 붙이면 a > b
    - JNAE = JB, JAE = a >= b 인데 N을 붙이면 a < b
- example
    - EAX = 2
    - CMP EAX, 2
        - 1 - 2 = -1
    - JBE(=JNA) SHORT 40100F
        - 1 <= 2 --> 점프
    - JAE(=JNB) SHORT 40100F
        - 1 <= 2 --> 조건 성립 x

    - EAX = 1
    - CMP EAX, 1
        - 1 - 1 = 0
    - JBE(=JNA) SHORT 40100F
        - 1 <= 1 --> 점프
    - JAE(=JNB) SHORT 40100F
        - 1 <= 1 --> 점프

    - EAX = 0
    - CMP EAX, 0
        - 1 - 0 = 1
    - JBE(=JNA) SHORT 40100F
        - 1 >= 0 --> 조건 성립 x
    - JAE(=JNB) SHORT 40100F
        - 1 >= 0 --> 점프

