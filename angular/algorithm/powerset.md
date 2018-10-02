# Powerset

- 임의의 집합 data의 모든 부분집합을 출력하라.
> data = {a, b, c, d}<br>
> {공집합}, {a}, {b}, {c}, {d}, {a, b}, {a, c}, {a, d}, {b, c} ..., {a, b, c, d} 총 16개}<br>

- {a, b, c, d ,e, f}의 모든 부분집합을 나열하려면 a를 제외한 {b, c, d, e, f}의 모든 부분집합들을 나열하고 {b, c, d, e, f}의 모든 부분집합에 {a}를 추가한 집합들을 나열한다.

- {b, c, d, e ,f}의 모든 부분집합에 {a}를 추가한 집합들을 나열하려면 {c, d, e, f}의 모든 부분집합들에 {a}를 추가한 집합들을 나열하고 {c, d, e, f}의 모든 부분집합에 {a, b}를 추가한 집합들을 나열한다.

- {c, d, e, f}의 모든 부분집합에 {a}를 추가한 집합들을 나열하려면 {d, e, f}의 모든 부분집합들에 {a}를 추가한 집합들을 나열하고 {d, e, f}의 모든 부분집합에 {a, c}를 추가한 집합들을 나열한다.

### 어떤 집합의 모든 부분집합을 구하려면 원소 하나를 제외한 부분집합을 구해야 한다.

- 수도코드 1
```
powerSet(S) // S의 멱집합을 출력하라
if S is an empty set
    print nothing;
else
    let t be the first element of S:
    find all subsets of S-{t} by calling powerSet(S-{t});
    print the subsets;
    print the subsets with adding t;
```
> 개선할 점 : return 하지말고 출력하자. -> 메모리 문제떄문

- 수도코드 2
```
powreSet(P, S) // S의 멱집합을 구한 후 각각 집합 P를 합집합하여 출력하라
if S is an empty set
    print P;
else
    let t be the first element of S;
    powerSet(P, S-{t}); // t를 포함하지 않는 부분집합
    powerSet(P U {t}, S-{t}); // t를 포함하는 부분집합
```
> recursion 함수가 두 개의 집합을 매개변수로 받도록 설계해야 한다. 두 번째 집합의 모든 부분집합들에 첫번쨰 집합을 합집합하여 출력한다.<br>
> {c,d,e,f}는 집합 S: k번째부터 마지막 원소까지 연속된 원소들이고 {a, b}를 추가한 집합들은 집합 P : 처음부터 k-1번째 원소들 중 일부

```
private static char data[] = {'a', 'b', 'c', 'd', 'e', 'f'};
private static int n = data.length;
private static boolean [] include = new boolean[n];

public static void powerSet(int k){
    if(k == n){
        for(int i = 0; i < n; i++)
            if(include[i]) System.out.print(data[i] + " ");
        System.out.println();
        return;
    }
    include[k] = false;
    powerSet(k+1);
    include[k] = true;
    powerSset(k+1);
}
```
> data[k], ... , data[n-1]의 멱집합을 구한 후 각각에 include[i] = true, i = 0, ... ,k-1인 원소를 추가하여 출력하라<br>
> 처음 이 함수를 호출할 때는 powerSet(0)로 호출한다. 즉 P는 공집합이고 S는 전체집합이다.<br>
> 상태공간트리로 보면 include와 k는 트리상에서 현재 나의 위치를 표현한다.<br>
> if(k == n) : 만약 내 위치가 리프노드라면<br>
> include[k] = false; : 왼쪽으로 내려간다.<br>
> include[k] = true; : 오른쪽으로 내려간다.<br>