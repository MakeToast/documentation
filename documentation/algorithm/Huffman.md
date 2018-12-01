# Huffman Coding
- 가령 6개의 문자 a, b, c, d, e, f로 이루어진 파일이 있다고 하자. 문자의 총 개수는 100,000개이고 각 문자의 등장 횟수는 다음과 같다.
- 고정길이 코드를 사용하면 각각의 문자를 표현하기 위해서 3비트가 필요하며, 따라서 파일의 길이는 300,000비트가 된다.
- 위 테이블의 가변길이 코드를 사용하면 224,000비트가 된다. (압축효과가 더 좋아졌다.)
- fixed length code == prefix code

### Prefix code
- 어떤 codeword도 다른 codeword의 prefix가 되지 않는 코드 (여기서 codeword란 하나의 문자에 부여된 이진코드를 말함)
- 모호함이 없이 decode가 가능함
- prefix code는 하나의 이진트리로 표현 가능함

### Huffman Coding Algorithm
![Huffman Coding](http://www.ktword.co.kr/img_data/1443_1.JPG)

### Run-Length Encoding
- 런(run)은 동일한 문자가 하나 혹은 그 이상 연속해서 나오는 것을 의미한다. 예를 들어 스트링 s = "aaabba"는 다음과 같은 3개의 run으로 구성된다: "aaa", "bb", "a".
- run-length encoding에서는 각각의 run을 그 "run을 구성하는 문자"와 "run의 길이"의 순서쌍 (n, ch)로 encoding한다. 여기서 ch가 문자이고 n은 길이이다. 가령 위의 문자열 s는 다음과 같이 코딩된다: 3a2b1a.
- Run-Length Encoding은 길이가 긴 run들이 많은 경우에 효과적이다.

### Huffman Method with Run-Length Encoding
- 파일을 구성하는 각각의 run들을 하나의 super-symbol로 본다. 이 super-symbol들에 대해서 Huffman coding을 적용한다.
- 예를 들어 AAABAACCAABA은 5개의 super-symbol들 AAA, B, AA, CC, 그리고 A로 구성되며 각 super-symbol의 등장횟수는 다음과 같다.
    - symbol     : A C A B A
    - run length : 3 2 1 1 2
    - frequency  : 1 1 1 2 2

- 제 1단계 : Run과 frequency 찾기
    - 압축할 파일을 처음부터 끝까지 읽어서 파일을 구성하는 run들과 각 run들의 등장횟수를 구한다.
    - 먼저 각 run들을 표현할 하나의 클래스 class Run을 정의한다. 클래스 run은 적어도 세 개의 데이터 멤버 symbol, runLen, 그리고 freq를 가져야 한다. 여기서 symbol은 byte타입이고 나머지는 정수들이다.
    - 인식한 run들은 하나의 ArrayList에 저장한다.
    - 적절한 생성자와 equals 메서드를 구현한다.
    - 데이터 파일을 적어도 두 번 읽어야 한다. 한 번은 run들을 찾기 위해서 그리고 다음은 실제로 압축을 수행하기 위해서.
    - 여기서 RandomAccessFile을 이용해서 데이터 파일을 읽어본다.
    - Run 인식하기
    - 1. 파일의 첫 byte를 읽고 이것을 start_symbol이라고 한다.
    - 2. 파일의 끝에 도달하거나 혹은 start_symbol와 다른 byte가 나올 때까지 연속해서 읽는다. 현재까지 읽은 byte수를 count라고 하자. 이 예에서는 지금 byte=4이다.
    - 3. (start_symbol, count-1)인 run이 하나 인식되었다. 이 run을 저장하고 가장 마지막에 읽은 byte를 start_symbol로, count=1로 reset하고 다시 반복한다.
