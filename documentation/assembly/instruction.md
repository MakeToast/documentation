- JO : Jump if overflow 
    - OF = 1
- JNO : Jump if not overflow
    - OF = 0
- JS : Jump if sign
    - SF = 1
- JNS : Jump if not sign
    - SF = 0
- JE JZ : Jump if equal / Jump if zero
    - ZF = 1
- JNE JNZ : Jump if not equal / Jump if not zero
    - ZF = 0
- JB JNAE JC : Jump if below / Jump if not above or equal / Jump if carry
    - CF = 1
    - unsigned
- JNB JAE JNC : Jump if not below / Jump if above or equal / Jump if not carry
    - CF = 0
    - unsigned
- JBE JNA : Jump if below or equal / Jump if not above
    - CF = 1 or ZF = 1
    - unsigned
- JA JNBE : Jump if above / Jump if not below or equal
    - CF = 0 and ZF = 0
    - unsigned
- JL JNGE : Jump if less / Jump if not greater or equal
    - SF <> OF
    - signed
- JGE JNL : Jump if greater or equal / Jump if not less
    - SF = OF
    - signed
- JLE JNG : Jump if less or equal / Jump if not greater
    - ZF = 1 or SF <> OF
    - signed
- JG JNLE : Jump if greater / Jump if not less or equal
    - ZF = 0 and SF = OF
    - signed
- JP JPE : Jump if parity / Jump if parity even
    - PF = 1
- JNP : Jump if not parity / Jump if parity odd
    - PF = 0
- JCXZ JECXZ : Jump if %CX register is 0 / Jump if %ECX register is 0
    - %CX = 0
    - %ECX = 0