# HEAP
- Time Complexity: Run time: worst-case O(n log n) 
- O(1) for get root value(max, min value)
- Space Complexity: Heapsort is an **in-place algorithm**
> 힙을 구성하는데 걸리는 시간 O(n log n)<br>
> 가장 큰 값과 가장 작은 값을 구할 때는 단 한번의 access만으로 그 값을 구할 수 있다.<br>
> heapsort은 또 다른 메모리를 필요로하지 않는 **in-place algorithm**이다.

## HEAP TREE
- A binary heap is a complete binary tree which satisfies the heap ordering property. The ordering can be one of two types: Min-heap, Max-heap.
![min heap max heap example](https://i2.wp.com/www.techiedelight.com/wp-content/uploads/2016/11/Min-Max-Heap.png?zoom=2.625&resize=368%2C214)
- max-heap property : the value of each node is less than or equal to the value of its parent, with the maximum-value element at the root.

### Use Array as a data structure of heap tree
![heap tree example](http://www.algolist.net/img/binary-heap-array-mapping.png)

- 일반적인 트리를 힙으로 만드는데는 아래 두 가지만 알면 된다.
    * heapify : 일반적인 트리를 힙 트리로 바꾸는 과정
    * siftdown : parent와 child 간의 대소관계를 보고 스와핑해주는 과정

## HEAPIFY
```
def heapify(a, size) :
    p = (size//2) - 1
    while p >= 0 :
        siftdown(a, p, size)
        p -= 1
```
> p는 자식이 있는 노드의 마지막 값 -> performance를 좋게 만들 수 있다.

## SIFTDOWN
```
def siftdown(a, i, size) :
    l = 2*i+1 # left child node
    r = 2*i+2 # right child node
    largest = i
    if l <= size-1 and a[l] > a[i] : 
        largest = l
    if r <= size-1 and a[r] > a[largest] :
        largest = r
    if largest != i :
        swap(a, i, largest)
        siftdown(a, largest, size)
```
