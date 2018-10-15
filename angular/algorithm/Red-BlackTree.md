# Red-Black Tree

- 레드-블랙 트리
* 이진탐색트리의 일종
* 균형잡힌 트리 : 높이가 O(log2n)
* SEARCH, INSERT, DELETE 연산을 최악의 경우에도 O(log2n) 시간에 지원
![Red-Black Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Red-black_tree_example.svg/1000px-Red-black_tree_example.svg.png)
* 각 노드의 하나의 키, 왼쪽 자식, 오른쪽 자식, 그리고 부모노드의 주소를저장
* 자식 노드가 존재하지 않을 경우 NIL 노드라고 부르는 특수한 노드가 있다고 가정
* 따라서 모든 리프노드는 NIL 노드
* 루트의 부모도 NIL노드라고 가정
* 노드들은 내부노드와 NIL노드로 분류

- 레드-블랙 트리의 정의
* 다음의 조건을 만족하는 이진탐색트리 :
    1. 각 노드는 **red** 혹은 **black**이고,
    2. 루트노드는 **black**이고,
    3. 모든 리프노드(즉, NIL노드)는 **black**이고,
    4. red노드의 자식노드들은 전부 **black**이고(즉, red노드는 연속되어 등장하지 않고),
    5. __모든 노드에 대해서 그 노드로부터 자손인 리프노드에 이르는 모든 경로에는 동일한 개수의 black노드가 존재한다.__

- 레드-블랙 트리의 높이
* 노드 x의 높이 h(x)는 자신으로부터 리프노드까지의 가장 긴 경로에 포함된 에지의 갯수
* 노드 x의 블랙-높이 bh(x)는 x로부터 리프노드까지의 경로상의 블랙노드의 개수이다. (노드 x 자신은 불포함)
* 높이가 h인 노드의 블랙-높이는 bh>=h/2이다.
    * 조건4에 의해 레드노드는 연속될 수 없기 때문에 당연하다
* 노드 x를 루트로하는 임의의 부트리는 적어도 2^bh(x) - 1 개의 내부노드를 포함한다. (수학적 귀납법)
* n개의 내부노드를 가지는 레드블랙트리의 높이는 2*log2(n+1)이하이다.

- Left and Right Rotation
* 시간복잡도 O(1)
* 이진탐색트리의 특성을 유지

- Left Rotation
* y = right[x] != NIL이라고 가정
* 루트노드의 부모도 NIL이라고 가정
```
LEFT-ROTATE(T, x)
    y <- right[x]           // Set y
    right[x] <- left[y]     // turn y's left subtree into x's right subtree
    p[left[y]] <- x
    p[y] <- p[x]
    if p[x] == nil[T]
        then root[T] <- y
        else if x == left[p[x]]
            then left[p[x]] <- y
            else right[p[x]] <- y
    left[y] <- x             // put x on y's left
    p[x] <- y
```

- INSERT
* 보통의 BST에서처럼 노드를 INSERT한다.
* 새로운 노드 z를 red노드로 한다.
* RB-INSERT-FIXUP을 호출한다.

```
RB-INSERT(T,z)  // T : red-black tree, z : insert node
    y <- nil[T]
    x <- root[T]
    while x != nil[T]
        do y <- x
            if key[z] < key[x]
                then x <- left[x]
                else x <- right[x]
    p[z] <- y
    if y == nil[T]
        then root[T] <- z
        else if key[z] < key[y]
            then left[y] <- z
            else right[y]  <- z
    left[z] <- nil[T]
    right[z] <- nil[T]
    color[z] <- RED
    RB-INSERT-FIXUP(T, z)
```

- RB-INSERT-FIXUP
* 위반될 가능성이 있는 조건들
    * 1 조건. OK
    * 2 조건. 만약 z가 루트노드라면 위반, 아니라면 OK.
    * 3 조건. OK.
    * 4 조건. z의 부모 p[z]가 red이면 위반.
    * 5 조건. OK
* Loop Invariant :
    * z는 red노드
    * 오직 하나의 위반만이 존재한다 :
        * 조건 2: z가 루트노드이면서 red이거나 또는
        * 조건 4: z와 그 부모 p[z]가 둘 다 red이거나.
* 종료조건:
    * 부모노드 p[z]가 black이되면 종료한다. 조건2가 위반일 경우 z를 블랙으로 바꿔주고 종료한다.
```
RB-INSERT-FIXUP(T, z)
    while color[p[z]] == RED
        do if p[z] == left[p[p[z]]]
            then y <- right[p[p[z]]]
                if color[y] == RED
                    then color[p[z]] <- BLACK
                        color[y] <- BLACK
                        color[p[p[z]]] <- RED
                        z <- p[p[z]]
                    else if z == right[p[z]]
                        then z <- p[z]
                            LEFT-ROTATE(T, z)
                        color[p[z]] <- BLACK
                        color[p[p[z]]] <- RED
                        RIGHT-ROTATE(T, p[p[z]])
        else (same as then clause with "right" and "left" exchanged)
    color[root[T]] <- BLACK
```