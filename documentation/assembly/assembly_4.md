# 메모리 주소와 접근
- 메모리 한 바이트(8비트)에 주소 한 개가 들어가도록 설계했다.
- 인텔 32비트에서는 주소값을 32비트로 저장할 수 있다.
    - 32비트에서는 최대로 4GB의 공간을 사용할 수 있다.
        - 2^32 x 1 bypte = 2^2 x 2^30 x 1byte = 4GB
        - 1 KB = 1024 byte = 2^10 byte
        - 1 MB = 1024 KB = 2^20 byte
        - 1 GB = 1024 MB = 2^10 MB = 2^30 byte

- 어셈블리어의 메모리 접근
    - 어셈블리어에서 메모리에 주소를 지정하고 그 주소 안에 있는 데이터를 지정할 때
        - 대괄호를 쓰고 그 안에 주소를 넣는다. : [주소]
        - example
            - 402000번지에 접근해서 데이터 넣기 : mov [402000], AL
            - CL에 402000번지의 데이터를 넣기 : mov CL, [402000]
            - `주의해야 할 것`
                - mov mem1, mem2 XXXX!!!
                - 해결방법
                    - 메모리 1의 값을 레지스터에 먼저 옮기고 레지스터 값을 다시 메모리 2로 옮긴다.
                    - mov mem1, reg
                    - mov reg, mem2