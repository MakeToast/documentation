# Linked List
> 링크드리스트는 노드들이 연결된 데이터 구조이다.
## Node
```
class Node :
    def __init__(self, item) :
        self.val = item
        self.next = None 
```
- Node  : | val | next |

## Linked List = Linked Node
-  &nbsp; &nbsp; &nbsp;First&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Second &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Third<br>
| val | next | -> | val | next | -> | val | next |
> First node is the head of liked list

### ADD
```
def add(self, item) :
    cur = self.head
    while cur.next is not None : 
        cur = cur.next
    cur.next = Node(item)
```
| 1 | next | -> | 2 | next |

- 3 추가
    *  cur : 1 노드 가르킴
    * cur.next 는 2 노드 즉 None이 아니다.
        * cur : 2 노드 가르킴
        * cur.next는 None
    * cur.next : Node(3)<br>
     | 1 | next | -> | 2 | next | -> | 3 | next |

### PRINT
```
def printlist(self) :
    cur = self.head
    while cur is not None :
        print(cur.val)
        cur = cur.next
```
| val 1 | next | -> | val 2 | next |
- 링크드리스트 출력
    * cur : val 1 노드 가리킴
    * cur은 val 1 노드, 즉 None이 아니다.
        * val 1 출력
        * cur : val 2 노드 가리킴
        * val 2 출력
        * cur : None<br>
    Val 1 Val 2 

### REMOVE
```
def remove(self, item) :
    if self.head.val == item :
        self.head = self.head.next
    else :
        cur = self.head
        while cur.next is not None :
            if cur.val == item :
                self.removeItem(item)
                return
            cur = cur.next
        print("item does not exist in linked list")

def removeItem(self, item) :
    cur = self.head
    while cur.next is not None :
        if cur.next.val == item :
            nextnode = cur.next.next
            cur.next = nextnode
            break
```
| 1 | next | -> | 2 | next | -> | 3 | next |

- head를 지우는 경우 : 1 삭제
    * self.head : 1 노드
    * self.head = self.head.next : 2 노드가 self.head가 된다. <br>
    | 2 | next | -> | 3 | next |

- 중간 노드를 지우는 경우 : 2 삭제
    * cur : 1 노드 가르킴
    * cur.next는 2 노드이고 None이 아니다.
        * cur.val != 2
        * cur = cur.next : 2 노드 가리킴
        * cur.val == 2
            * removeItem() 함수로 들어감
    
    * cur = self.head 즉 1 노드
    * cur.next는 2 노드이고 None이 아니다.
        * cur.next.val == 2
            * nextnode = cur.next.next : 3 노드
            * cur.next = nextnode : 1 노드의 next가 3 노드 가리킴<br>
    | 1 | next | -> | 3 | next |

### REVERSE
```
def reverse(self) :
    prev = None
    cur = self.head
    while cur is not None :
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    self.head = prev
```
| 1 | next | -> | 2 | next | -> | 3 | next |

- 거꾸로 만들기 : 1-2-3 -> 3-2-1
    * prev : None
    * cur : 1 노드
    * cur 은 None이 아니다
        * next : 2 노드
        * cur.next = prev : cur.next는 None
        * prev : 1 노드
        * cur : 2 노드<br>
        None <- | 1 | next | -no link- | 2 | next | -> | 3 | next |
        * next : 3 노드
        * cur.next = prev : cur.next는 1 노드
        * prev : 2 노드
        * cur : 3 노드<br>
        None <- | 1 | next | <- | 2 | next | - | 3 | next |
        * next = None
        * cur.next = prev : cur.next는 2 노드
        * prev : 3 노드
        * cur : None
        None <- | 1 | next | <- | 2 | next | <- | 3 | next |
    * self.head = prev : self.head는 3노드