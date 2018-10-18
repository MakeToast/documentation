# Binary Search Tree[BST]
- Search, Delete, Insert : O(log n)

## Binary Search Tree
![Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/2000px-Binary_search_tree.svg.png)
- The left sub-tree of a node has a key less than or equal to its parent node's key.
- The right sub-tree of a node has a key greater than or equal to its parent node's key.

## Node
- 트리는 노드들의 집합체이다. 즉, 노드들이 서로 연결된 것이 트리이다.
```
class Node :
    def __init__(self, item) :
        self.val = item
        self.left = None
        self.right = None
```
    [ None ] -- ( 10 ) -- [ None ]
> 10이라는 노드를 만들 때 노드의 left, right child는 None이라고 설정

## ADD
```
def add(self, item) :
    if self.head.val is None :
        self.head.val = item
    else :
        self.__add_node(self.head, item)
    
def __add_node(self, cur, item) :
    if cur.val >= item :
        if cur.left is not None :
            slef.__add_node(cur.left, item)
        else
            cur.left = Node(item)
    else :
        if cur.right is not None :
            self.__add_node(cur.right, item)
        else :
            cur.right = Node(item)
```
- example : add node '21' 

    * BST

                ( 27 )
                /   \
            ( 20 )  ( 30 )
                \
                ( 22 )

    * 21 < 27

                ( 27 )
                /   \
            ( 20 )  ( 30 )
    
    * 21 > 20

            ( 20 )
                \
                ( 22 )
    
    * 21 < 22

                ( 22 )
                /
            ( 21 )

    * result

                ( 27 )
                /   \
            ( 20 )  ( 30 )
                \
                ( 22 )
                /
            ( 21 )

## SEARCH
```
def search(self, item) :
    if self.head.val is None :
        return False
    else :
        return self.__search_node(self.head, item)

def __search_node(self, cur, item) :
    if cur.val == item :
        return True
    else :
        if cur.val >= item :
            if cur.left is not None :
                return self.__search_node(cur.left, item)
            else :
                return False
        else :
            if cur.right is not None :
                return self.__search_node(cur.right, item)
            else :
                return False
```
- example : search node '19'

    * BST

                     ( 27 )
                    /      \
               ( 14 )      ( 35 )
                /   \       /   \
            ( 10 ) ( 19 ) ( 31 ) ( 42 )

    * 19 < 27

                    ( '27' )
                    /      \
               ( 14 )      ( 35 )
                /   \       /   \
            ( 10 ) ( 19 ) ( 31 ) ( 42 )
    
    * 19 > 14

                    ( 27 )
                    /      \
               ( '14' )      ( 35 )
                /   \       /   \
            ( 10 ) ( 19 ) ( 31 ) ( 42 )

    * find 19

                    ( 27 )
                    /      \
               ( 14 )      ( 35 )
                /   \       /   \
            ( 10 ) ( "19" ) ( 31 ) ( 42 )

## REMOVE (1/3) 
### Node to be removed has no child
> 그냥 지우면 된다.

- example : remove node '10'

    * BST

                     ( 27 )
                    /      \
               ( 14 )      ( 35 )
                /   \       /   \
          ( "10" ) ( 19 ) ( 31 ) ( 42 )

    * result

                     ( 27 )
                    /      \
               ( 14 )      ( 35 )
                    \       /   \
                    ( 19 ) ( 31 ) ( 42 )

## REMOVE (2/3) 
### Node to be removed has one child
> 자식을 조상한테 붙여주면 된다.

- example : remove node '31'

    * BST

                     ( 27 )
                    /      \
               ( 14 )      ( 35 )
                /   \       /   \
            ( 10 ) ( 19 ) ("31") ( 42 )
                          /
                      ( 30 )

    * result

                     ( 27 )
                    /      \
               ( 14 )      ( 35 )
                /   \       /   \
            ( 10 ) ( 19 ) ( 30 ) ( 42 )
                        
## REMOVE (3/3) 
### Node to be removed has two child
> 오른쪽에 있는 서브트리에서 가장 왼쪽에 있는 자식을 지울 자리에 넣는다.

- example : remove node '35'

    * BST

                     ( 27 )
                    /      \
               ( 14 )      ( "35" )
                /   \       /   \
            ( 10 ) ( 19 ) ( 31 ) ( 42 )
                          /       /   \
                      ( 30 )  ( 40 ) ( 45 )
    
    * result

                     ( 27 )
                    /      \
               ( 14 )      ( 40 )
                /   \       /   \
            ( 10 ) ( 19 ) ( 31 ) ( 42 )
                          /          \
                      ( 30 )         ( 45 )
