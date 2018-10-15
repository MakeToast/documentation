# Comparison Sort

## 정렬 알고리즘의 유형

- Comparison sort
    * 데이터들간의 `상대적 크기관계`만을 이용해서 정렬하는 알고리즘
    * 따라서 데이터들간의 크기 관계가 정의되어 있으면 어떤 데이터에든 적용가능(문자열, 알파벳, 사용자 정의 객체 등)
    * 버블소트, 삽입정렬, 합병정렬, 퀵소트, 힙정렬 등
- Non-comparison sort
    * 정렬할 데이터에 대한 `사전지식`을 이용 - 적용에 제한
    * Bucket sort
    * Radix sort

## 정렬문제의 하한

- 하한(Lower bound)
    * 입력된 데이터를 한번씩 다 보기위해서 최소 O(n)의 시간복잡도 필요
    * 합병정렬과 힙정렬 알고리즘들의 시간복잡도는 O(nlogn)
    * 어떤 comparison sort 알고리즘도 O(nlongn)보다 나을 수 없다.

## Decision Tree
- 임의의 comparison sort가 있다고 하자.
> n 개의 데이터가 정렬을 하기 위해서 값들을 비교해 하는데 전체 과정을 트리로 만들 수 있는데 그것을 Decision Tree라고 한다.<br>
* Leaf 노드의 개수는 n! 왜냐하면 모든 순열(permutation)에 해당하므로
* 최악의 경우 시간복잡도는 트리의 높이
* full binary tree 형태로 만들 때 높이가 낮아지면서 시간복잡도가 작아질 것이다.
* 트리의 높이는
    * height >= logn! = O(nlogn)

[Decision Tree](https://upload.wikimedia.org/wikipedia/commons/4/48/DecisionCalcs.jpg)

