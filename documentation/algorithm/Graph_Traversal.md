# Graph Traversal

## 그래프 순회
    - 순회(traversal)
        - 그래프의 모든 노드들을 방문하는 일
    - 대표적인 두 가지 방법
        - BFS (Breadth-First Search, 너비우선순회)
        - DFS (Depth-First Search, 깊이우선순회)

### 너비우선순회 (BFS)     
- BFS 알고리즘은 다음 순서로 노드들을 방문 (`동심원 형태`)
    - L0 = {s}, 여기서 s는 출발 노드
    - L1 = L0의 모든 이웃 노드들 (직접 에지로 연결되어 있는 노드)
    - L2 = L1의 이웃들 중 L0에 속하지 않는 노드들
    - ...
    - Li = Li-1의 이웃들 중 Li-2에 속하지 않는 노드들
- `큐`를 이용한 너비우선순회
    - 1. check the start node; (이미 방분된 노드라는 표시를 해라)
    - 2. insert the start node into the queue;
    ```
    while the queue is not empty do
        remove a node v from queue;
        for each unchecked neighbour w of v do
            check and insert w into the queue;
    ```
- BFS와 최단경로
    - s에서 Li에 속한 노드까지의 최단 경로의 길이는 i이다.
    - BFS를 하면서 각 노드에 대해서 최단 경로의 길이를 구할 수 있다.
    - 입력 : 방향 혹은 무방향 그래프 G=(V, E), 그리고 출발노드 s
    - 출력 : 모든 노드 v에 대해서
        - d[v] = s로부터 v까지의 최단 경로의 길이(에지의 개수)
        - ㅠ[v] = s로부터 v까지의 최단경로상에서 v의 직전 노드(predecessor)
- BFS 트리
    - 각 노드 v와 ㅠ[v]를 연결하는 에지들로 구성하는 트리
    - BFS 트리에서 s에서 v까지의 경로는 s에서 v까지 가는 최단 경로
    - 어떤 에지도 2개의 layer를 건너가지 않는다. (동일 레이어의 노드를 연결하거나, 혹은 1개의 layer를 건너간다.)
- 그래프가 disconnected이거나 혹은 방향 그래프라면 BFS에 의해서 모든 노드가 방문되지 않을 수도 있다.

### 깊이우선순회 (DFS)
- DFS 알고리즘은 다음 순서로 노드들을 방문
    1. 출발점 s에서 시작한다.
    2. 현재 노드를 visited로 mark하고 인접한 노드들 중 unvisited 노드가 존재하면 그 노드로 간다.
    3. 2번을 게속 반복한다.
    4. 만약 unvisited인 이웃 노드가 존재하지 않는 동안 계속해서 직전 노드로 되돌아간다.
    5. 다시 2번을 반복한다.
    6. 시작노드 s로 돌아오고 더 이상 갈 곳이 없으면 종료한다.
- 그래프가 disconnected이거나 혹은 방향 그래프라면 DFS에 의해서 모든 노드가 방문되지 않을 수도 있다.