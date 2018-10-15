# N-Queens Problems

## 상태공간트리
- 상태공간 트리란 찾는 해를 포함하는 트리
- 즉 해가 존재한다면 그것은 반드시 이 트리의 어떤 한 노드에 해당함
- 따라서 이 트리를 체계적으로 탐색하면 해를 구할 수 있음
- 상태공간 트리의 모든 노드를 탐색해야 하는 것은 아님

## 되추적 기법(Backtracking)
- 상태공간 트리를 깊이 우선 방식으로 탐색하여 해를 찾는 알고리즘.

```
int [] cols = new int [N+1];
boolean queens( int level ){
    if (!promising(level))
        return false;
    else if(level == N)
        return true;
    for(int i = 1; i <=N; i++){
        cols[level+1] = i;
        if(queens(level+1))
            return true;
    }
    return false;
}

boolean promisin(int level){
    for(int i = 1; i < level; i++){
        if(cols[i] == cols[level]) // 같은 열
            return false;
        else if (level-i == Math.abs(cols[level]-cols[i]))// 같은 대각선
            return false;
    }
    return true;
}
```
> level - 지금까지 놓은 말의 개수