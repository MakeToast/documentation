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


