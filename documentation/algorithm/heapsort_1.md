# Heap과 Heapsort

- 최악의 경우 시간복잡도 O(nlogn)
- Sorts in place : 추가 배열 불필요
- 이진 힙(binary heap) 자료구조를 사용 

## Heap의 정의
- Heap은 
    * complete binary tree이면서
    * heap property를 만족해야 한다.

- `max` heap property : 부모는 자식보다 `크`거나 같다.
- `min` heap property : 부모는 자식보다 `작`거나 같다.

### Full vs Complete Binary Trees
- `full binary tree` : 모든 레벨에 노드들이 꽉 차 있는 형태
- `complete binary tree` : 마지막 레벨을 제외하면 완전히 꽉 차있고, 마지막 레벨에는 가장 오른쪽부터 연속된 몇 개의 노드가 비어있을 수 있다.

### Heaps
- 동일한 데이터를 가진 서로 다른 힙. 즉 힙은 유일하지 않음

### Heap의 표현
- 힙은 일차원 배열로 표현가능 : A[1...n] // n은 노드의 개수
    * 루트 노드 A[1].
    * A[i]의 부모 = A[i/2]
    * A[i]의 왼쪽 자식 = A[2i]
    * A[i]의 오른쪽 자식 = A[2i+1]