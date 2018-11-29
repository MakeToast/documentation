# MST 알고리즘
### Kruskal의 알고리즘
- 에지들을 가중치의 오름차순으로 정렬한다.
- 에지들을 그 순서대로 하나씩 선택해간다. 단, 이미 선택된 에지들과 사이클(cycle)을 형성하면 선택하지 않는다.
- n-1개의 에지가 선택되면 종료한다.

### 왜 MST가 찾아지는가?
- Kruskal의 알고리즘의 임의의 한 단계를 생각해보자.
- A를 현재까지 알고리즘이 선택한 에지의 집합이라고 하고, A를 포함하는 MST가 존재한다고 가정하자.

### 사이클 검사
- 초기 상태 : 선택된 에지 없음
- 각각의 연결요소를 하나의 집합으로 표현
    1. 가중치가 최소인 에지를 고려한다.
    2. 에지의 두 노드가 서로 다른 집합에 속함
    3. 그 두 노드를 선택하고 그 노드가 속한 집합을 합집합하여 하나의 집합으로 만든다.
    ```
    MST-KRUSKL(G, w)
        A 는 공집합
        for each vertex v (V[G]에 속하는)          // 각각의 노드들을 유일한 원소로
            do MAKE-SET(v)                      // 가지는 집합들을 만들어라.
        sort the edges of E into nondecreasing order by weight w
        for each edge (u, v) (E에 속하는), taken in nondecreasing order by weight
            do if FIND-SET(u) != FIND-SET(v)    // 노드 v가 속한 집합을 찾아라
                then A <-  A 와 {(u,v)} 합집합
                    UNION(u, v)                 // u와 v가 속한 두 집합을 하나로 합친다.
    ```
