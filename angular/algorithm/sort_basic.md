# 정렬 알고리즘

## 종류
- Bubble sort
- Insertion sort
- Selection sort
> simple, slow
- Quicksort
- Merge sort
- Heap sort
> fast
- Radix sort
> 위의 알고리즘들과는 약간 다름 O(N)

## 기본적인 정렬 알고리즘

### Selection Sort
- 각 루프마다
     * 최대 원소를 찾는다.
     * 최대 원소와 맨 오른쪽 원소를 교환한다.
     * 맨 오른쪽 원소를 제외한다.
- 하나의 원소만 남을 때까지 위의 루프를 반복

- 수도코드
```
selectionSort(A[], n) // 배열 A[1...n]을 정렬한다.
{
    for last <- n downto 2{     --- (1)
        A[1...last] 중 가장 큰 수 A[k]를 찾는다. --- (2)
        A[k] <-> A[last]; // A[k]와 A[last] 값 교환 --- (3)
    }
}
```
- 수행시간 :
    * (1)의 for 루프는 n-1번 반복
    * (2)에서 가장 큰 수를 찾기 위한 비교횟수 : n-1, n-2, ..., 2, 1
    * (3)의 교환은 상수시간 작업
- 시간복잡도 T(n)=(n-1)+(n-2)+...+2+1 = O(n^2)

### Bubble sort
- 수도 코드
```
bubblesort(A[], n) // 배열 A[1...n]을 정렬한다.
{
    for last <- n downto 2 {    --- (1)
        for i <- 1 to last -1   --- (2)
            if(A[i] > A[i+1]) then A[1] <-> A[i+1]; // 교환     --- (3)
    }
}
```
- 수행시간:
    * (1)의 for 루프는 n-1번 반복
    * (2)의 for 루프는 n-1, n-2,..., 2, 1번 반복
    * (3)의 교환은 상수시간 작업
- 시간복잡도 T(n) = (n-1)+(n-2)+...+2+1 = O(n^2)

### Insertion sort
- 수도 코드
```
insertionsort(A[], n) // 배열 A[1...n]을 정렬한다.
{
    for i <- 2 to n {   --- (1)
        A[1...i]의 적당한 자리에 A[i]를 삽입한다.   --- (2)
    }
}
```
- 수행시간 :
    * (1)의 for 루프는 n-1 번 반복
    * (2)의 삽입은 최악의 경우는 i-1번 비교
- 최악의 경우 : T(n) = (n-1)+(n-2)+...+2+1 = O(n^2)