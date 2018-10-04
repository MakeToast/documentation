# 선형시간 정렬 알고리즘

## Sorting in Linear Time
- Counting Sort
    * n개의 정수를 정렬하라. 단 모든 정수는 0에서 k사이의 정수이다.
    * 예 : n명의 학생들의 시험점수를 정렬하라. 단 모든 점수는 100이하의 양의 정수이다.
    > 길이 k인 배열에 각 정수의 개수를 count 한다.
    ```
    A |2|5|3|0|2|3|0|3|
    C |2|0|2|3|0|1|

    0 두개, 2 두개 ..

    결과 |0|0|2|2|3|3|3|5|
    ```
    - counting sort code
    ```
    Counting-Sort(A, B, k)
    1. for i <- 0 to k
    2.      do C[i] <- 0
    3. for j <- 1 to length[A]
    4.      do C[A[j]] <- C[A[j]] + 1
    5. > C[i] now contains the number of elements equla to i.
    6. for i <- 1 to k
    7.      do C[i] <- C[i] + C[i-1]
    8. > C[i] now contains the number of elements less than or equla to i.
    9. for j <- length[A] down to 1
    10.     do B[C[A[j]]] <- A[j]
    11.        C[A[j]] <- C[A[j]] - 1
    ```
    * 1, 2 초기화
    * 3, 4 배열의 숫자들 세기
    * 6, 7 누적합을 구하는 부분
    * 9, 10, 11 누적합을 이용해서 배열 A를 저장된 정렬할 데이터를 역으로 살펴보면서 배열 B에 저장

    - 시간복잡도
    * O(n+k), 또는 O(theta)(n) if k=O(n)
    * k가 클 경우 비실용적
    * Stable 정렬 알고리즘
        * "입력에 동일한 값이 있을 때 입력에 먼저 나오는 값이 출력에서도 먼저 나온다."
        * `Counting 정렬은 stable하다`
