# Heap과 Heapsort

### 기본 연산 : MAX-HEAPIFY
- 전체를 힙으로 만들어라!
    * 유일하게 루트만이 heap property를 만족안함
    * 트리의 전체 모양은 complete binary tree임
    * 왼쪽 부트리(subtree)는 그 자체로 heap이고 오른쪽 부트리(subtree)도 그 자체로 heap일 때
    * 두 자식들 중 더 큰 쪽이 나보다 크면 exchange한다.

### MAX-HEAPIFY : recursive version
```
MAX-HEAPIFY(A, i) // 노드 i를 루트로하는 서브트리를 heapify한다.
{
    if there is no child of A[i]
        return;
    k <- index of the biggest child of i;
    if A[i] >= A[k] // 부모가 자식보다 크면 heapify 만족
        return;
    exchange A[i] and A[k];
    MAX-HEAPIFY(A, k);
}
```

### MAX-HEAPIFY : iterative version
```
MAX-HEAPIFY(A, i)
{
    while A[i] has a child do // A[i]가 자식을 가지고 있는 동안 
        k <- index of the biggest child of i;
        if A[i] >= A[k] // 부모가 자식보다 크면 heapify 만족
            return;
        exchange A[i] and A[k];
        i = k;
    end.
}
```