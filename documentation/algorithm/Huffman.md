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