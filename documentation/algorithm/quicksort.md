# Quicksort(빠른정렬)
분할정복법의 2번째 정렬 : Quicksort 

- 분할 정복법
    * 분할 : 배열을 다음과 같은 조건ㅇ ㅣ만족되도록 두 부분으로 나눈다.
    > elements in lower parts <= elements in upper parts
    * 정복 : 각 부분을 순환적으로 정렬한다.
    * 합병 : nothing to do

- Quicksort 알고리즘
>- 정렬할 배열이 주어짐. 마지막 수를 기준(pivot)으로 삼는다.<br>
>- 기준보다 작은 수는 기준의 왼쪽에 나머지는 기준의 오른쪽에 오도록 재배치 `분할`한다.<br>
>- 기준의 왼쪽과 오른쪽을 각각 `순환적`으로 정렬한다. (정렬 완료)<br>

- Quicksort 알고리즘 개요
```
quicksort(A[], p, r)    --- A[p...r]을 정렬한다.
{
    if(p < r) then{
        q = partition(A, p, r);     --- 분할
        quicksort(A, p, q-1);       --- 왼쪽 부분배열 정렬
        quicksort(A, q+1, r);       --- 오른쪽 부분배열 정렬
    }
}

partition(A[], p, r)
{
    배열 A[p...r]의 원소들을 A[r]을 기준으로 양쪽으로 재배치하고
    A[r]이 자리한 위치를 return한다;
}
```

- partition을 어떻게 할 것인가?
```
if A[j] >= x
    j <- j+1;
else
    i <- i+1;
    exchange A[i] and A[j];
    j <- j+1;
```
```
Partition(A, p, r)
{
    x <- A[r];
    i <- p-1;
    for j<-p to r-1
        if A[j] <= x then
            i<-i+1;
            exchange A[i] and A[j];
    exchange A[i+1] and A[r];
    return i+1;
}
```
- 시간복잡도
    **최악**
    * 항상 한 쪽은 0개, 다른 쪽은 n-1개로 분할되는 경우
    * T(n)  = T(0)+T(n-1)+O(=theta)(n)<br>
            = T(n-1) + O(n)<br>
            = T(n-2) + T(n-1) + O(n-1) + O(n)<br>
            ...<br>
            = O(1) + O(2) + ... + O(n-1) + O(n)<br>
            = O(n^2)<br>
    * 이미 정렬된 입력 데이터 (마지막 원소를 피봇으로 선택하는 경우)

    **최선**
    * 항상 절반으로 분할되는 경우 (mergesort와 동일하다.)
    * T(n)  = 2T(n/2) + O(n)<br>
            = O(nlogn)<br>

- pivot의 선택
    * 첫번쨰 값이나 마지막 값을 피봇으로 선택
        * 이미 정렬된 데이터 혹은 거꾸로 정렬된 데이터가 최악인 경우
        * 현실의 데이터는 랜덤하지 않으므로 (거꾸로) 정렬된 데이터가 입력으로 들어올 가능성은 매우 높음
        * 따라서 좋은 방법이라고 할 수 없음
    * "Median of Three" : 매우 현실적인 갑셔
        * 첫번째 값과 마지막 값, 그리고 가운데 값 중에서 `중간값`을 피봇으로 선택
        * 최악의 경우 시간복잡도가 달라지지는 않음
    * Randomized Quicksort
        * 피봇을 `랜덤`하게 선택
        * no worst case instance, but worst case execution
        * 평균 시간복잡도 O(NlogN)