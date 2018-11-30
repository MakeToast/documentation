# Shortest Path

### 최단경로
- 가중치 (방향) 그래프 G = (V, E), 즉 모든 에지에 가중치가 있다.
- 경로 p = (v0, v1, ..., vk)의 길이는 경로상의 모든 에지의 가중치의 합
- 노드 u에서 v까지의 최단경로의 길이를 델타(u,v)라고 표시하자.

### 최단경로문제의 유형
- Single-source: (one-to-all)
    - 하나의 출발 노드 s로부터 다른 모든 노드까지의 최단 경로를 찾아라.
    - 예 : Dijkstra의 알고리즘
- Single-destination:
    - 모든 노드로부터 하나의 목적지 노드까지의 최단 경로를 찾아라.
    - Single-source 문제와 동일
- Single-pair: (one-to-one)
    - 주어진 하나의 출발 노드 s로부터 하나의 목적지 노드 t까지의 최단 경로를 찾아라.
    - 최악의 경우 시간복잡도에서 Single-source 문제보다 나은 알고리즘이 없음
- All-pairs: (all-to-all)
    - 모든 노드 쌍에 대해서 최단 경로를 찾아라.
    - Floyd 알고리즘

### 최단경로와 음수 가중치
- 음수 사이클이 있으면 최단 경로가 정의되지 않음
- 알고리즘에 따라 음수 가중치가 있어도 작동하는 경우도 있고 그렇지 않은 경우도 있음

### 최단경로의 기본 특성
- 최단 경로의 어떤 부분경로도 역시 최단 경로이다.
    - u - x - y - v
    - 이 경로가 u에서 v까지의 최단 경로라면, x-y 이 경로도 x에서 y까지의 최단 경로이다.
- 최단 경로는 사이클을 포함하지 않는다. (음수 사이클이 없다는 가정하에서)

### Single-source 최단경로문제
- 입력 : 음수 사이클이 없는 가중치 방향그래프 G=(V, E)와 출발 노드 s (V에 포함되는)
- 목적 : 각 노드 v (V에 포함되는)에 대해서 다음을 계산한다.
    - d[v] (distance estimate)
        - 처음에는 d[s] = 0, d[v] = 무한대 로 시작한다.
        - 알고리즘이 진행됨에 따라서 감소해간다. 하지만 항상 d[v] >= 델타(s, v)를 유지힌다.
        - 최종적으로 d[v] = 델타(s, v)가 된다.
    - ㅠ[v] : s에서 v까지의 최단경로상에서 v의 직전 노드 (predecessor)
        - 그런 노드가 없는 경우 ㅠ[v] = NIL.

- Relaxation
    - 그래프의 어떤 에지에 대해 Relax한다. 
        - d[u] = 5 : 현재까지 u로 가는 5인 경로
        - d[v] = 9 : 현재까지 v로 가는 9인 경로
        - (u,v) = 2 : u에서 v로 가는 길이 2
        - RELAX(u, v, w) : 현재 d[v]보다 d[u]+w로 가는 경로 비교
    ```
    RELAX(u, v, w)
        if d[v] > d[u] + w(u, v)
            then d[v] <- d[u] + w(u, v)
                ㅠ[v] <- u
    ```
- 대부분의 single-source 최단경로 알고리즘의 기본 구조
    1. 초기화 : d[s]=0, 노드 v != s에 대해서 d[v] = 무한대, ㅠ[v] = NIL.
    2. 에지들에 대한 반복적인 relaxation
- 알고리즘들 간의 차이는 어떤 에지에 대해서, 어떤 순서로 relaxation을 하느냐에 있음
```
Generic-Single-Source(G, w, s)
    INITIALISE-SINGLE-SOURCE(G, s)
    repeat
        for each edge (u, v) (E에 속하는)
            RELAX(u, v, w)
    until there is no change.
```
- s - v1 - v2 - ... - vi - v, 이것이 s에서 v까지의 최단 경로라면 
    - 첫 번째 반복에서 d(v1) = 델타(s, v1)이 됨
    - 두 번째 반복에서 d(v2) = 델타(s, v2)이 됨
    - i 번째 반복에서 d(vi) = 델타(s, vi)이 됨
    - 즉, n-1번의 반복으로 최단 경로를 찾을 수 있다.

- Bellman-Ford 알고리즘
    - 시간복잡도 O(nm)
```
BELLMAN-FORD(G, w, s)
    INITIALIZE-SINGLE-SOURCE(G,s)
    for i <- to |V[G]| - 1
        do for each edge (u, v) (E[G]에 포함되는)
            do RELAX(u, v, w)
    for each edge (u, v) (E[G]에 포함되는)
        do if d[v] > d[u] + w(u, v) // 음수 사이클이 존재한다는 의미
            then return FALSE
    return TRUE
```

- Dijkstra의 알고리즘
    - 음수 가중치가 없다고 가정
    - s로부터의 최단경로의 길이를 이미 알아낸 노드들의 집합 S를 유지. 맨 처음엔 S = 공집합
    - Loop invariant:
        - u (S에 속하지 않는)인 각 노드 u에 대해서 d(u)는 이미 S에 속한 노드들만 거쳐서 s로부터 u까지 가는 최단경로의 길이
    - 정리
        - d(u) = min v(S에 속하지 않는) d(v)인 노드 u에 대해서, d(u)는 s에서 u까지의 최단경로의 길이이다.
    - 증명
        - s에서 u까지 다른 최단경로가 존재한다고 했을 때 d(v) >= d(u)이므로 모순.
    - d(u)가 최소인 노드 u(S에 포함되지 않는) 를 찾고 ,S에 u를 추가
    - S가 변경되었으므로 다른 노드들의 d(v) 값을 갱신
    - d(v) = min{d(v), d(u) + w(u, v)}
    - 즉, 에지 (u, v)에 대해서 relaxation하면 Loop Invariant가 계속 유지됨.

    - 시간복잡도 O(n^2)
```
Dijkstra(G,w,s)
    for each u(V에 포함된) do
        d[u] <- 무한대
        ㅠ[u] <- NIL
    end.
    S <- {공집합}
    d[s] <- 0
    while |S| < n do // n-1번 반복
        find u (S에 속하지 않는) with the minimum d[u] value; // 최소값 찾기 O(n)
        S <- S 와 {u} 의 합집합
        for each v (S에 속하지 않는) adjacent to u do // degree(u) = O(n)
            if d[v] > d[u] + w(u, v) then
                d[v] <- d[u] + w(u, v)
                ㅠ[v] <- u
            end.
        end.
    end.
```
### all-to-all 최단경로 알고리즘
- Floyd-Warshall Algorithm
    - 가중치 방향 그래프 G = (V, E), V = {1, 2, 3, ..., n}
    - 모든 노드 쌍들간의 최단경로의 길이를 구함
    - dk[i, j]
        - 중간에 노드 집합 {1, 2, 3, ..., k}에 속한 노드들만 거쳐서 노드 i에서 j까지 가는 최단경로의 길이
    - 중간에 노드집합 {1,2, ..., k}에 속한 노드들만 거쳐서 노드 i에서 j까지 가는 최단경로는 두가지 경우가 있다 : 노드 k를 지나는 경우와 지나지 않는 경우
    ```
    FloydWarshall(G)
    {
        for i <- 1 to n
            for j <- 1 to n
                d0[i, j] <- wij;
        for k <- 1 to n
            for i <- 1 to n
                for j <- 1 to n
                    dk[i,j] <- min{dk-1[i,j], dk-1[i, k]+dk-1[k,j]};
    }
    ```
    - 시간복잡도 : O(n^3) -> 굳이 3차원 배열을 쓸 필요가 없다!
    ```
     FloydWarshall(G)
    {
        for i <- 1 to n
            for j <- 1 to n
                d[i, j] <- wij;
        for k <- 1 to n
            for i <- 1 to n
                for j <- 1 to n
                    d[i,j] <- min{d[i,j], d[i, k]+d[k,j]};
    }
    ```
    - 경로 찾기
    ```
    FloydWarshall(G)
    {
        for i <- 1 to n
            for j <- 1 to n
                d[i, j] <- wij;
                ㅠ[i, j] <- NIL;
        for k <- 1 to n
            for i <- 1 to n
                for j <- 1 to n
                    if d[i, j] > d[i, k]+d[k, j] then
                        d[i, j] = d[i, k]+d[k, j] 
                        ㅠ[i, j] = k;
    }
    ```