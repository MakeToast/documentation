# Heap의 다른 응용 : 우선순위 큐

- 최대 우선순위 큐 (maximum priority queue : FIFO)는 다음의 두 가지 연산을 지원하는 자료구조
    * INSERT(x) : 새로운 원소 x를 삽입
    * EXTRACT_MAX() : 최대값을 삭제하고 반환
- 최소 우선순위 큐 (minimum priority queue)는 EXTRACT-MAX 대신 EXTRACT-MIN을 지원하는 자료구조
- MAX HEAP을 이용하여 최대 우선순위 큐를 구현

## INSERT
```
MAX-HEAP-INSERT(A, key) // A : Heap
{
    heap_size = heap_size + 1;
    A[heap_size] = key;
    i = heap_size;
    while( i > 1 and A[PARENT(i)] < A[i])   // 루트 노드가 아니고 부모 노드에 저장된 값보다 크다면
    {
        exchange A[i] and A[PARENT(i)];
        i = PARENT(i);
    }
}
```
- 시간복잡도 O(logn)

## EXTRACT_MAX()
```
HEAP-EXTRACT-MAX(A)
    if heap-size[A] < 1 // heap is empty
        then error "heap underflow"
    max <- A[1]
    A[1] <- A[heap-size[A]]
    hea-size[A] <- heap-size[A] - 1
    MAX-HEAPIFY(A, 1)
    return max
```
- 시간 복잡도 O(logn)