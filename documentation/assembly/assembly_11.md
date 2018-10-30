 # 메모리 주소 지정 방식

- [402000] : 메모리 번지수 지정
- [eax] : 레지스터 이름이 올 수 있다.
    - = 레지스터 안의 값을 메모리 주소로 사용한다.
- offset
    - 동일 오브젝트 안에서 오브젝트 처음부터 주어진 요소나 지점까지의 변위차를 나타내는 정수형
    - 즉, 기준 주소에서 얼만큼 떨어진 곳인지 지칭하는 말
    - example : c언어
        > 배열이 있고 처음 주소를 0이라고 하자.<br>
        > 0 1 2 3 4 5 ... 주소가 1바이트씩 커진다고 할 때 0에서 1까지 이동하려면 0 + 1을 해야한다.<br>

- example : 레지스터에 주소값 넣기
    - 기준 주소 : 402000  

    - mov ebx, 402000
        - ebx : 기준 주소 / + 숫자 : 오프셋
    - mov byte ptr ds:[ebx+0], 0
        - 402000 -> 00 00 00 00 00 00
    - mov byte ptr ds:[ebx+1], 1
        - 402000 -> 00 01 00 00 00 00
    - mov byte ptr ds:[ebx+2], 2
        - 402000 -> 00 01 02 00 00 00
    - mov byte ptr ds:[ebx+3], 3
        - 402000 -> 00 01 02 03 00 00
    - mov byte ptr ds:[ebx+4], 4
        - 402000 -> 00 01 02 03 04 00
    - mov byte ptr ds:[ebx+5], 5
        - 402000 -> 00 01 02 03 04 05
       
- example : 레지스터에 오프셋 넣기
    - mov ecx, 0
    - mov byte ptr ds:[402000+ecx], cl
        - 402000 -> 00 00 00 
    - inc ecx
        - ecx : 1
    - mov byte ptr ds:[402000+ecx], cl
        - 402000 -> 00 01 00
    - inc ecx
        - ecx : 2
    - mov byte ptr ds:[402000+ecx], cl
        - 402000 -> 00 01 02

- example 
    - 4 바이트씩 넣고 싶으면
     mov ecx, 0
    - mov dword ptr ds:[402000+ecx*4], ecx
        - 402000 -> 00 00 00 00 00 00 00 00 00 00 00 00 
    - inc ecx
        - ecx : 1
    - mov dword ptr ds:[402000+ecx*4], ecx
        - 402000 -> 00 00 00 00 01 00 00 00 00 00 00 00 
    - inc ecx
        - ecx : 2
    - mov dword ptr ds:[402000+ecx*4], ccx
        - 402000 -> 00 00 00 00 01 00 00 00 02 00 00 00 

- 규칙
    - [base 주소 + offset + index * scale(크기)]
        - base주소 : 메모리 안에서 기준이 되는 주소
        - offset : 거리
        - [] 안에 쓸 수 있는 register 개수 : 최대 2개
        - index는 반드시 레지스터여야 한다.
        - scale : 원하는 크기만큼 곱하면 된다.