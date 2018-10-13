# 트리와 이진트리 (Tree and Binary Tree)

## Tree
- 계층적인 구조를 표현
    * 조직도
    * 디렉토리와 서브디렉토리 구조
    * 가계도
    ![tree](https://t1.daumcdn.net/cfile/tistory/2672FD3D5892B6BE0E)
- 트리는 노드(Node)들과 노들을 연결하는 링크(link)들로 구성됨
> 맨 위의 노드를 "루트(root)"라고 부르고 노드들을 연결하는 선을 "link", "edge", "branch" 등으로 부른다.
- 부모-자식 관계 
- 형제관계 : 루트노드를 제외한 트리의 모든 노드들은 유일한 부모 노드를 가진다.
- 리프(leaf) 노드 : 자식이 없는 노드들을 leaf노드라고 하고 리프노트가 아닌 노드들을 내부(internal)노드라고 부른다.
- 조상-자손 관계 : 부모-자식 관계를 확장한 것이 조상-자손 관계이다.
- 부트리(subtree) : 트리에서 어떤 한 노드와 그 노드의 자손들로 이루어진 트리
- 레벨 : 루트는 level 1 밑으로 갈 수록 level 2. 3 ...
- 높이 : 서로 다른 레벨의 갯수

- 트리의 기본적인 성질
    * 노드가 N개인 트리는 항상 N-1개의 링크(link)를 가진다.
    * 트리에서 루트에서 어떤 노드로 가는 경로는 유일하다. 또한 임의의 두 노드간의 경로도 유일하다. (같은 노드를 두 번 이상 방문하지 않는다는 조건하에)

## Binary Tree
- 이진트리의 개념
    * 이진 트리에서 각 노드는 최대 2개의 자식을 가진다.
    * 각각의 자식 노드는 자신이 부모의 왼쪽 자식인지 오른쪽 자식인지가 지정된다.(자식이 한 명인 경우에도)
    ![binary tree](https://t1.daumcdn.net/cfile/tistory/2116B34557D7E5A22C)
- 이진트리의 응용 : Expression Tree
![expression tree](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Expression_Tree.svg/1280px-Expression_Tree.svg.png)
- 이진트리의 응용 : Huffman code
![huffman code](https://kamilmysliwiec.com/wp-content/uploads/2017/04/chart.png)
- Full and Complete Binary Trees
    ![Full and Complete Binary Trees](https://www.differencebetween.com/wp-content/uploads/2011/05/DifferenceBetween_Full_Binary_Tree.jpg)
    * 높이가 h인 full binary tree는 2^h-1개의 노드를 가진다.
    * 노드가 N개인 full 혹은 complete 이진 트리의 높이는 O(logN)이다. (노드가 N개인 이진트리의 높이는 최악의 경우 N이 될 수도 있다.)
- 이진트리의 표현
* 연결구조(Linked Structure) 표현
![binary tree linked structure representation example](http://interactivepython.org/runestone/static/Java/_images/simpleBST.png)
각 노드에 하나의 데이터 필드와 왼쪽자식(left), 오른쪽 자식(right), 그리고 부모노드 (p)의 주소 저장 (부모 노드의 주소는 반드시 필요한 경우가 아니면 보통 생략함)
- 이진트리의 순회(traversal)
    * 순회 : 이진 트리의 노든 노드를 방문하는 일
    * 중순위(inorder) 순회
    * 선순위(preorder) 순회
    * 후순위(postorder) 순회
    * 레벨오더(level-order) 순회

![example tree](https://www.geeksforgeeks.org/wp-content/uploads/2009/06/tree12.gif)
- 이진트리의 Inorder - 순회
1. left
2. root
3. right
    * result : 4-2-5-1-3
```
INORDER-TREE-WALK(x)
if x != NULL
    then INORDER-TREE-WALK(left[x])
        print key[x]
        INORDER-TREE-WALK(right[x])
```
- 이진트리의 Preorder - 순회
1. root
2. left
3. right
    * result : 1-2-4-5-3
```
PREORDER-TREE-WALK(x)
if x != NULL
    then print key[x]
        PREORDER-TREE-WALK(left[x])
        PREORDER-TREE-WALK(right[x])
```
- 이진트리의 Postorder - 순회
1. left
2. right
3. root
    * result : 4-5-2-3-1
```
POSTORDER-TREE-WALK(x)
if x != NULL
    then POSTORDER-TREE-WALK(left[x])
        POSTORDER-TREE-WALK(right[x])
        print key[x]
```
- level-order 순회
* 레벨 순으로 방문, 동일 레벨에서는 왼쪽에서 오른쪽 순서로
* 큐(queue)를 이용하여 구현
```
LEVEL-ORDER-TREE-TRAVERSAL()
    visit the root;
    Q <- root;          // Q is a queue
    while Q is not empty do
        v <- dequeue(Q);
        visit children of v;
        enqueue children of v into Q;
    end.
end.
```