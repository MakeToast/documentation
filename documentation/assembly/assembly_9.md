# 어셈블리어 add sub
- add : addition  || sub : substraction
- add [reg]/[mem], [즉시값] : reg/mem에 즉시값을 더한다.
- sub [reg]/[mem], [즉시값] : reg/mem에 즉시값을 뺀다.
- example : add [reg], [즉시값]
    - mov eax, 0 -> eax = 0
    - add eax, 10 -> eax = 10
        - eax += 10
    - add eax, 7 -> eax = 17
        - eax += 7
    
- example : add [reg], [reg]
    - mov ecx, 0 -> ecx = 0
    - mov ecx, eax -> ecx = eax = 17
    - add ecx. eax -> ecx = 2E
    - add eax, ecx -> eax = 45

- example : add [mem], [reg]
    - add dword ptr ds:[402000], eax 
    - add ecx, dword ptr ds:[402000] -> ecx = 73
    - add eax, dword ptr ds:[402000] -> eax = 8A

