# DFS(Depth First Search)

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

    * DFS 실행
    ```
    Stack[0]
    while stack :
        current = stack.pop()
        for neighbor in adjacencyList[current] :
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
        return visitedVertex
    ```

    stack : | 0 |<br>
    current :<br>
    visited : <br>

     * pop<br>
     stack : <br>
     current : | 0 |<br>
     visited : <br>
     * append vertex 1, 2 to stack<br>
     stack : | 1 | 2 | <br>
     current : | 0 |<br>
     visited : <br>
     * append vertex 0 to visitedVertex<br> 
     stack : | 1 | 2 | <br>
     current :<br>
     visited : | 0 |<br>

     * pop<br>
     stack : | 1 | <br>
     current :| 2 |<br>
     visited : | 0 |<br>
     * append vertex 4, 5 to stack<br>
     stack : | 1 | 4 | 5 | <br>
     current :| 2 |<br>
     visited : | 0 |<br>
     * append vertex 2 to visitedVertex<br>
     stack : | 1 | 4 | 5 | <br>
     current :<br>
     visited : | 0 | 2 |<br>

     * pop<br>
     stack : | 1 | 4 | <br>
     current : | 5 |<br>
     visited : | 0 | 2 |<br>
     * vertex 2 is in visitedVertex<br>
     * append vertex 5 to visitedVertex<br>
     stack : | 1 | 4 | <br>
     current :<br>
     visited : | 0 | 2 | 5 |<br>

     * pop<br>
     stack : | 1 |  <br>
     current : | 4 |<br>
     visited : | 0 | 2 | 5 |<br>
     * append vertex 6 to stack and vertex 2 is in visitedVertex<br>
     stack : | 1 | 6 |<br>
     current : | 4 |<br>
     visited : | 0 | 2 | 5 |<br>
     * append vertex 4 to visitedVertex<br>
     stack : | 1 | 6 | <br>
     current :<br>
     visited : | 0 | 2 | 5 | 4 |<br>

     * pop<br>
     stack : | 1 | <br>
     current :| 6 |<br>
     visited : | 0 | 2 | 5 | 4 |<br>
     * vertex 4 is in visitedVertex<br>
     * append vertex 6 to visitedVertex<br>
     stack : | 1 | <br>
     current :<br>
     visited : | 0 | 2 | 5 | 4 | 6 |<br>

     * pop<br>
     stack :  <br>
     current : | 1 |<br>
     visited : | 0 | 2 | 5 | 4 | 6 |<br>
     * append vertex 3 to stack<br>
     stack : | 3 |<br>
     current : | 1 |<br>
     visited : | 0 | 2 | 5 | 4 | 6 |<br>
     * append vertex 1 to visitedVertex<br>
     stack : | 3 |<br>
     current : <br>
     visited : | 0 | 2 | 5 | 4 | 6 | 1 |<br>

     * pop<br>
     stack : <br>
     current : | 3 |<br>
     visited : | 0 | 2 | 5 | 4 | 6 | 1 |<br>
     * vertex 1 is in visitedVertex<br>
     * append vertex 3 to visitedVertex<br>
     stack : <br>
     current : <br>
     visited : | 0 | 2 | 5 | 4 | 6 | 1 | 3 |<br>

- 응용
    * 게임 (체스게임 등)
    * 그래프 내에서 사이클이 있는지 없는지