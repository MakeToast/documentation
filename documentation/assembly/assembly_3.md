# 메모리
- 메모리란?
    - 메모리는 기억장치라는 뜻을 가진다.
    - 우리가 원하는 작업을 컴퓨터에서 처리하기 위해서는 처리대상의 내용이나 또는 처리 결과를 잠시 기억하고 있어야할 필요성이 생기는데 이때 메모리가 사용된다.
    - 주기억장치(메인메모리, RAM(Random Access Memory))
        - 전자소자로 만들어져 있고 기억할 내용이 전기적인 신호로 저장되기 때문에 HDD보다 빠르게 이용할 수 있다.
    - 메모리에는 새로운 정보를 기록할 수도 있고 기억되어 있는 내용을 필요에 따라 읽어낼 수도 있다.
    
![메모리계층](https://sonofgodcom.files.wordpress.com/2017/11/the-memory-hierarchy-28-638.jpg)

- 메모리는 속도에 비례하여 가격이 정해진다. 
    - 속도가 빠르면 가격이 비싸기 때문에 메모리 크기가 작아지고 속도가 느리면 가격이 싸기 때문에 큰 용량을 쓸 수 있다.
- 메모리에는 level 1에 해당하는 register부터 level n에 해당하는 HDD까지 많은 계층이 있는데 `memory hierarchy`라고 한다.
- `memory locality`
    - cpu가 메인 메모리의 특정 데이터를 필요로 할 때 
        - 한 번 쓰인 데이터는 여러번 쓰인다.
        - 쓰인 데이터 주변에 데이터가 호출된다.
    - 빠른 메모리에 자주 쓰이는 데이터를 넣으면 컴퓨터 속도가 향상되지만 비싸기 때문에 장단점을 갖는 메모리들을 계층적으로 쌓아올려 쓰인다.

    - 데이터가 전송될 때의 단위 : block