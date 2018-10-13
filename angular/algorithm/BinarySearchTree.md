# 이진검색트리 Binary Search Tree

- Dynamic Set (여러가지 데이터를 가지고 있는 집합, Dictionary or Search Structure)
    * 여러 개의 키 (key) 저장
    * 다음과 같은 연산들을 지원하는 자료구조
        * INSERT : 새로운 키의 삽입
        * SEARCH : 키 탐색
        * DELETE : 키 삭제
    * 예 : 심볼 테이블

- 다양한 방법들
    * 정렬된 혹은 정렬되지 않은 배열 혹은 연결 리스트를 사용할 경우 INSERT, SEARCH, DELETE 중 적어도 하나는 O(n)
    * 이진탐색트리(Binary Search Tree), 레드-블랙 트리, AVL-트리 등에 기반한 구조들
    * Direct Address Table, 해쉬 테이블 등 

- 검색트리
    * Dynamic set을 트리의 형태로 구현
    * 일반적으로 SEARCH, INSERT, DELETE 연산이 트리의 높이(height)에 비례하는 시간복잡도를 가진다.
    * 이진탐색트리(Binary Search Tree), 레드-블랙 트리(red-black tree), B-트리 등

- 이진검색트리(BST)
    * 이진 트리이면서
    * 각 노드에 하나의 키를 저장
    * 각 노드 v에 대해서 그 노드의 왼쪽부트리(subtree)에 있는 키들은 key[v]보다 작거나 같고 오른쪽 부트리에 있는 값은 크거나 같다.

- SEARCH : recursion
```
Tree-SEARCH(x, k) // x 노드 k 찾는 값
    if x == NULL or k == key[x]
        then return x
    if k < key[x]
        then return TREE-SEARCH(left[x], k)
    else
        return TREE-SEARCH(right[x], k)
```
> 시간복잡도 O(h) : h는 트리의 높이
- SEARCH : iterative 
```
ITERATIVE-TREE-SEARCH(x, k)
    while x != NULL and k != key[x]
        do if k < key[x]
            then x <- left[x]
            else
                x <- right[x]
    return x
```
> 시간복잡도 O(h) : h는 트리의 높이

- 최소값
    * 최소값은 항상 가장 왼쪽 노드에 존재
    * 시간복잡도 O(h)
```
TREE-MINIMUN(x)
    while left[x] != NULL
        do x <- left[x]
    return x
```
- 최대값
    * 최대값은 항상 가장 오른쪽 노드에 존재
    * 시간복잡도 O(h)
```
TREE-MAXIMUM(x)
    while right[x] != NULL
        do x <- right[x]
    return x
```

- Successor
* 노드 x의 successor란 key[x]보다 크면서 가장 작은 키를 가진 녿,
* 모든 키들이 서로 다르다고 가정
* 3가지 경우
    * 노드 x의 오른쪽 부트리가 존재할 경우, 오른쪽 부트리의 최소값
    * 오른쪽 부트리가 없는 경우, 어떤 노드 y의 왼쪽 부트리의 최대값이 x가 되는 그런 노드 y가 x의 successor
        * 부모를 따라 루트까지 올라가면서 처음으로 누군가의 왼쪽 자식이 되는 노드
    * 그런 노드 y가 존재하지 않을 경우 successor가 존재하지 않음(즉, x가 최대값)
* 시간복잡도 O(h)
```
TREE-SUCCESSOR(x)
    if right[x] != NULL
        then return TREE-MINIMUM(right[x])
    y <- p[x]
    while y != NULL and x == right[y]
        do x <- y
           y <- p[y]
    return y
```

- Predecessor
* 노드 x의 predecessor란 key[x]보다 작으면서 가장 큰 키를 가진 노드
* Successor와 반대

- INSERT
* 시간복잡도 O(h)
```
TREE-INSERT(T, z) // T : tree, z : insert node
    y <- NULL
    x <- root[T]
    while x != NULL
        do y <- x
            if key[z] < key[x]
                then x <- left[x]
            else x <- right[x]
    p[z] <- y
    if y == NULL
        then root[T] <- z
        else if key[z] < key[y]
            then left[y] <- z
        else right[y] <- z
```

- DELETE
* Case 1 : 자식노드가 없는 경우 - 그냥 삭제
* Case 2 : 자식노드가 1개인 경우 - 자신의 자식노드를 원래 자신의 위치로
* Case 3 : 자식노드가 2개인 경우 
    * 1. successor의 값을 삭제하려는 노드로 copy
    * 2. successor 노드 대신 삭제한다(Case 1 or 2에 해당)
* 시간복잡도 O(h)
```
TREE-DELETE(T, z) // T : tree, z : delete node
    if left[z] == NULL or right[z] == NULL
        then y <- z
        else y <- TREE-SUCCESSOR(z)
    if left[y] != NULL
        then x <- left[y]
        else x <- right[y]
    if x != NULL
        then p[x] <- p[y]
    if p[y] == NULL
        then root[T] <- x
        else if y == left[p[y]]
            then left[p[y]] <- x
            else right[p[y]] <- x
    if y != z
        then key[z] <- key[y]
            copy y's satelite data into z
    return y
```  

- BST
* 각종 연산의 시간복잡도 O(h)
* 그러나, 최악의 경우 트리의 높이 h=O(n)
* 균형잡힌(balanced) 트리
    * 레드-블랙 트리 등
    * 키의 삽입이나 삭제시 추가로 트리의 균형을 잡아줌으로써 높이를 O(log2n)으로 유지