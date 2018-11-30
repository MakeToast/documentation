# MST 알고리즘
### Prim의 알고리즘
- 임의의 노드를 출발노드로 선택
- 출발 노드를 포함하는 트리를 점점 키워감.
- 매 단계에서 이미 트리에 포함된노드와 포함되지 않은 노드를 연결하는 에지들 중 가장 가중치가 작은 에지를 선택

### 왜 MST가 찾아지는가?
- Prim의 알고리즘의 임의의 한 단계를 생각해보자.
- A를 현재까지 알고리즘이 선택한 에지의 집합이라고 하고, A를 포함하는 MST가 존재한다고 가정하자.

### 가중치가 최소인 에지 찾기
- VA: 이미 트리에 포함된 노드들
- VA에 아직 속하지 않은 각 노드 v에 대해서 다음과 같은 값을 유지
    - key(v) : 이미 VA에 속한 노드와 자신을 연결하는 에지들 중 가중치가 최소인 에지 (u, v)의 가중치
    - ㅠ(v) : 그 에지 (u, v)의 끝점 u
- 가중치가 최소인 에지를 찾는 대신 key값이 최소인 노드를 찾는다.
- key 값이 최소인 노드 f를 찾고, 에지 (f, ㅠ(f)를 선택한다.
    ```
    MST-Prim(G, w, r)
        for each u (V에 포함되는) do
            key[u] <- 무한대
            ㅠ[u] <- NIL
        end.
        VA <- {r}
        key[r] <- 0
        while |VA| < n do // while문 n-1번 반복
            find u (VA에 포함되지 않는) with the minimum key value; // 최소값 찾기 O(n)
            VA <- VA 와 {u}의 합집합
            for each v (VA에 포함되지 않는) adjacent to u do // degree(u) = O(n)
                if key[v] > w(u, v) then
                    key[v] <- w(u, v)
                    ㅠ[v] <- u
                end.
            end.
        end.
    ```
    - 시간복잡도 : O(n^2)
### Key값이 최소인 노드 찾기
- 최소 우선순위 큐를 사용
    - V-VA에 속한 노드들을 저장
    - Extract-Min: key값이 최소인 노드를 삭제하고 반환

### Prim의 알고리즘: 시간복잡도
- 이진 힙(binary heap)을 사용하여 우선순위 큐를 구현한 경우
- while loop:
    - n번의 Extract-Min 연산 : O(nlogn)
    - m번의 Decrease-Key 연산 : O(mlogn)
- 따라서 시간복잡도 : O(nlogn + mlong) = O(mlogn)
- 우선순위 큐를 사용하지 않고 단순하게 구현할 경우 : O(n^2)
- Fibonacci 힙을 사용하여 O(m+nlogn)에 구현 가능