# Sorting in linear time : Radix Sort

## Radix Sort
- n개의 d자리 정수들
- 가장 낮은 자리수부터 정렬
[radix sort](https://ds055uzetaobb.cloudfront.net/image_optimizer/22630368cbc032ea43967b2610e73ded399e22a4.png)

- 자릿수가 고정되어 있으니 안정성이 있다. (이때 데이터들 간의 상대적 순서는 보존되어야 한다.)
> 예) 170, 45, 75, 90, 2, 24, 802. 66 <br>
> 1의 자리만 보고 정렬 : 170, 90, 2, 802, 24, 45, 75, 66<br>
> 10의 자리만 보고 정렬 : 2, 802, 24, 45, 66, 170, 75, 90<br>
> 100의 자리만 보고 정렬 : 2, 24, 45, 66, 75, 90, 170, 802<br>
```
RADIX-SORT(A, d)
1. for i <- 1 to d
2.      do use a stable sort to sort array A on digit i
```
- 시간 복잡도 O(d(n+k))

## 정렬 알고리즘들
- O(n^2) : Bubble sort, Insertion sort, Selection sort
- worst O(n^2) abd average O(nlogn) : Quick sort
- O(nlong) : Merge sort, Heap sort
- O(n+k), O(d(n+k)) : Counting sort, Radix sort