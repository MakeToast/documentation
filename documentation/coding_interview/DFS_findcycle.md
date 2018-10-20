# DFS, find cycle in undirect graph 

- example

    * Undirected Graph

                     ( 0 )
                    /      \
               ( 1 )      ( 2 )
                /          /   \
            ( 3 )      ( 4 ) -- ( 5 )
                        /    
                    ( 6 ) 

    stack : <br>
    current :<br>
    visited : <br>

    * stack 0<br>
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
     * append vertex 0 to visitedVertex <br>
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
     * vertex 2 is in visitedVertex and append vertex 4 to stack<br>
     stack : | 1 | 4 | 4 | <br>
     current : | 5 |<br>
     visited : | 0 | 2 |<br>
     * append vertex 5 to visitedVertex<br>
     stack : | 1 | 4 | 4 | <br>
     current :<br>
     visited : | 0 | 2 | 5 |<br>

     * pop<br>
     stack : | 1 | 4 | <br>
     current : | 4 |<br>
     visited : | 0 | 2 | 5 |<br>
     * append vertex 6 to stack and vertex 2 is in visitedVertex<br>
     stack : | 1 | 4 | 6 |<br>
     current : | 4 |<br>
     visited : | 0 | 2 | 5 |<br>
     * append vertex 4 to visitedVertex<br>
     stack : | 1 | 4 | 6 | <br>
     current :<br>
     visited : | 0 | 2 | 5 | 4 |<br>

     * pop<br>
     stack : | 1 | 4 | <br>
     current :| 6 |<br>
     visited : | 0 | 2 | 5 | 4 |<br>
     * vertex 4 is in visitedVertex<br>
     * append vertex 6 to visitedVertex<br>
     stack : | 1 | 4 |<br>
     current :<br>
     visited : | 0 | 2 | 5 | 4 | 6 |<br>

     * pop<br>
     stack : | 1 | 4 |<br>
     current :<br>
     visited : | 0 | 2 | 5 | 4 | 6 |<br>
     * vertex 2, 5, 6 is in visitedVertex<br>
     * append vertex 4 to visitedVertex<br>
     stack : | 1 | <br>
     current :<br>
     visited : | 0 | 2 | 5 | 4 | 6 | 4 |<br>

          * pop<br>
     stack :  <br>
     current : | 1 |<br>
     visited : | 0 | 2 | 5 | 4 | 6 | 4 |<br>
     * append vertex 3 to stack<br>
     stack : | 3 |<br>
     current : | 1 |<br>
     visited : | 0 | 2 | 5 | 4 | 6 | 4 |<br>
     * append vertex 1 to visitedVertex<br>
     stack : | 3 |<br>
     current : <br>
     visited : | 0 | 2 | 5 | 4 | 6 | 4 | 1 |<br>

     * pop<br>
     stack : <br>
     current : | 3 |<br>
     visited : | 0 | 2 | 5 | 4 | 6 | 4 | 1 |<br>
     * vertex 1 is in visitedVertex<br>
     * append vertex 3 to visitedVertex<br>
     stack : <br>
     current : <br>
     visited : | 0 | 2 | 5 | 4 | 6 | 4 | 1 | 3 |<br>

- 반복된 방문노드가 있다는 것은 그래프에 사이클이 있다는 것을 증명할 수 있다.