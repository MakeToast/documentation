# DAG (Directed Acyclic Graph)

### Directed Acyclic Graph
- DAG는 방향 사이클(directed cycle)이 없는 방향 그래프. (자기 자신으로 돌아올 수 없다.)
- 예: 작업들의 우선순위
### 위상정렬 (topological ordering)
- DAG에서 노드들의 순서화 v1, v2, ..., vn, 단, 모든 에지 (vi, vj)에 대해서 i < j가 되도록.
- 일반적으로 답이 하나가 아니다.
> 어떤 노드에 대해서 들어오는 에지 : incoming<br>
> 어떤 노드에 대해서 들어오는 에지 : outgoing<br>
> 어떤 노드에서 들어오는 에지의 개수 : indegree<br>
> 어떤 노드에서 나가는 에지의 개수 : outdegree<br>
- 위상정렬 알고리즘1
    ```
    topologicalsort1(G)
    {
        for <- 1 to n{
            진입간선(incoming edge)이 없는(indegree = 0) 임의의 정점 u를 선택한다; // indegree가 0인지 아닌지 알아야 한다.
            A[i] <- u;
            정점 u와 u의 진출간선(coutgoing edge)을 모두 제거한다;
        }
        > 배열 A[1...n]에는 정점들을 위상정렬되어 있다.
    }
    ```
    - 수행시간 : O(n+m)
    1. indegree = 0 인 노드가 존재하지 않으면?
    2. 실제로 어떻게 구현하는 것이 좋은가?
- 위상정렬 알고리즘2
    ```
    topologicalsort2(G)
    {
        for each v(V에 있는 v)
            visited[v] <- No; // 아직 아무 노드도 출력되지 않았다.
        make an empty linked list R;
        for each v(V에 있는 v) // 정점의 순서는 상관없음
            if (visited[v] = NO) then
                DFS-TS(v, R);
    }
    DFS-TS(v, R)
    {
        visited[v] <- YES;
        for each x adjacent to v do
            if (visited[x] = NO) then
                DFS-TS(x, R);
        add v at the front of the linked list R; // v를 맨 앞에 추가
    }
    ```
    - 알고르즘이 끝나면 연결 리스트 R에는 정점들이 위상정렬된 순서로 매달려 있다.
    - 수행시간 : O(n+m)