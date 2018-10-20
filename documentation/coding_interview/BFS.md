# BFS(Breadth First Search)

- example

    * Undirected Graph

                     ( 0 )
                    /      \
               ( 1 )      ( 2 )
                /          /   \
            ( 3 )       ( 4 ) ( 5 )
                        /    
                    ( 6 ) 
    
    * VERTEX LIST
        ```
        vertexList = ['0', '1', '2', '3', '4', '5', '6']
        ```

    * EDGE LIST
        ```
        edgeList = [(0,1), (0,2), (1,0), (1,3), (2,0), (2,4), (2,5), (3,1), (4,2), (4,6), (5,2), (6,4)]
        ```
    * ADJACENCY LIST
    ```
    vertexList = ['0', '1', '2', '3', '4', '5', '6']
    
    edgeList = [(0,1), (0,2), (1,0), (1,3), (2,0), (2,4), (2,5), (3,1), (4,2), (4,6), (5,2), (6,4)]

    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList :
        adjacencyList[edge[0]].append(edge[1])
    ```
    ```
    adjacencyList :
    [
        [1, 2],         // vertex 0
        [0, 3],         // vertex 1
        [0, 4, 5],      // vertex 2
        [1],            // vertex 3
        [2, 6],         // vertex 4
        [2],            // vertex 5
        [4]             // vertex 6
    ]
    ```
    * BFS 실행
    ```
    queue[0]
    while queue :
        current = queue.pop()
        for neighbor in adjacencyList[current] :
            if not neighbor in visitedList :
                queue.insert(0, neighbor)
        visitedList.append(current)

    return visitedList
    ```
    queue : | 0 |<br>
    current :<br>
    visited : <br>

     * pop<br>
     queue : <br>
     current : | 0 |<br>
     visited : <br>
     * insert neighbor in queue<br>
     queue : | 1 | 2 |<br>
     current : | 0 |<br>
     visited : <br>
     * append current in visitedList<br>
     queue : | 1 | 2 |<br>
     current : <br>
     visited : | 0 |<br>
    
     * pop<br>
     queue : | 2 |<br>
     current : | 1 |<br>
     visited : | 0 |<br>
     * insert neighbor in queue<br>
     queue : | 2 | 3 |<br>
     current : | 1 |<br>
     visited : | 0 |<br>
     * append current in visitedList<br>
     queue : | 2 | 3 |<br>
     current : <br>
     visited : | 0 | 1 |<br>

     * pop<br>
     queue : | 3 |<br>
     current : | 2 |<br>
     visited : | 0 | 1 |<br>
     * insert neighbor in queue<br>
     queue : | 3 | 4 | 5 |<br>
     current : | 2 |<br>
     visited : | 0 | 1 |<br>
     * append current in visitedList<br>
     queue : | 3 | 4 | 5 |<br>
     current : <br>
     visited : | 0 | 1 | 2 |<br>

     * pop<br>
     queue : | 4 | 5 |<br>
     current : | 3 |<br>
     visited : | 0 | 1 | 2 |<br>
     * insert neighbor in queue<br>
     * append current in visitedList<br>
     queue : | 4 | 5 |<br>
     current : <br>
     visited : | 0 | 1 | 2 | 3 |<br>

     * pop<br>
     queue : | 5 |<br>
     current : | 4 |<br>
     visited : | 0 | 1 | 2 | 3 |<br>
     * insert neighbor in queue<br>
     queue : | 5 | 6 |<br>
     current : | 4 |<br>
     visited : | 0 | 1 | 2 | 3 |<br>
     * append current in visitedList<br>
     queue : | 5 | 6 |<br>
     current : <br>
     visited : | 0 | 1 | 2 | 3 | 4 |<br>

     * pop<br>
     queue : | 6 |<br>
     current : | 5 |<br>
     visited : | 0 | 1 | 2 | 3 | 4 |<br>
     * insert neighbor in queue<br>
     * append current in visitedList<br>
     queue : | 6 |<br>
     current : <br>
     visited : | 0 | 1 | 2 | 3 | 4 | 5 |<br>

     * pop<br>
     queue : <br>
     current : | 6 |<br>
     visited : | 0 | 1 | 2 | 3 | 4 | 5 |<br>
     * insert neighbor in queue<br>
     * append current in visitedList<br>
     queue : <br>
     current : <br>
     visited : | 0 | 1 | 2 | 3 | 4 | 5 | 6 |<br>

- 응용
    * 최근접경로 (다익스트라 알고리즘)
    * 페이스북에 알 수 있는 친구


