# Dynamic Programming
    - Richard Bellman 발견
### Motivation
- Fibonacci Numbers
    ```
    int fib(int n)
    {
        if (n == 1 || n == 2)
            return 1;
        else
            return fib(n-2) + fib(n-1);
    }
    ```
    > Recursion -> 많은 계산이 중복됨 <br>
    - Memoization
    ```
    int fib(int n)
    {
        if (n == 1 || n == 2)
            return 1;
        else if (f[n] > -1) // 배열 f가 -1으로 초기화되어 있다고 가정
            return f[n];    // 즉 이미 계산된 값이라는 의미
        else{
            f[n] = f[n-1] + f[n-2]; // 중간 계산 결과를 caching
            return f[n];
        }
    }
    ```
    > 중간 계산 결과를 caching함으로써 중복 계산을 피함<br>
    - Dynamic Programming
    ```
    int fib(int n)
    {
        f[1] = f[2] = 1;
        for(int i = 3; i <= n; i++)
            f[n] = f[n-1] + f[n-2];
        return f[n];
    }
    ```
    > bottom-up방식으로 중복 계산을 피함<br>
- 이항 계수 (Binomial Coefficient)
    ```
    int binomial(int n, int k)
    {
        if (n == k || k == 0)
            return 1;
        else
            return binomial(n-1, k) + binomial(n-1, k-1);
    }
    ```
    > Recursion -> 많은 계산이 중복됨 <br>
    - Memoization
    ```
    int binomial(int n, int k)
    {
        if (n == k || k == 0)
            return 1;
        else if (binom[n][k] > -1) // 배열 binom이 -1로 초기화 되었다고 가정
            return binom[n][k];
        else{
            binom[n][k] = binomial(n-1, k) + binomial(n-1, k-1);
            return binom[n][k];
        }
    }
    ```
    - Dynamic Programming
    ```
    int binomial(int n, int k)
    {
        for(int i = 0; i <= n; i++)
        {
            for (int j = 0; j <= k && j <= i; j++)
            {
                if(k == 0 || n == k)
                    binom[i][j] = 1;
                else
                    binom[i][j] = binom[i-1][j-1] + binom[i-1][j];
            }
        }
        return binom[n][k];
    }
    ```
    - Memoization vs Dynamic Programming
        - 순환식의 값을 계산하는 기법들이다.
        - 둘 다 동적계획법의 일종으로 보기도 한다.
        - Memoizaiton은 `top-down`방식이며, `실제로 필요한 subproblem`만을 푼다.
        - Dynamic Programming은 `bottom-up`방식이며, recursion에 수반되는 overhead가 없다.

### Example
- 행렬 경로 문제
    - 정수들이 저장된 nxn 행렬의 좌상단에서 우하단까지 이동한다. 단 오른쪽이나 아래쪽 방향으로만 이동할 수 있다.
    - 방문한 칸에 있는 정수들의 합이 최소화되도록 하라.
    - Key Observation
        - (i, j)에 도달하기 위해서는 (i, j-1) 혹은 (i-1, j)를 거쳐야 한다.
        - 또한 (i, j-1) 혹은 (i-1, j)까지는 최선의 방법으로 이동해야 한다.
    - 순환식
        - L[i, j] : (1, 1)에서 (i, j)까지 이르는 최소합
        - if i = 1 and j = 1
            - mij
        - if j = 1
            - L[i-1, j] + mij
        - if i = 1
            - L[i, j-1] + mij
        - otherwise
            - min(L[i-1, j], L[i, j-1]) + mij
        - Recursive
            > 복잡함<br>
        ```
        int mat(int i, int j)
        {
            if ( i == 1 && j == 1 )
                return m[i][j];
            else if ( i == 1 )
                return mat(1, j-1) + m[i][j];
            else if ( j == 1 )
                return mat(i-1, 1) + m[i][j];
            else
                return Math.min(mat(i-1, j), mat(i, j-1)) + m[i][j];
        }
        ```
        - Memoization
            > 중복을 피할 수 있다.<br>
        ```
        int mat(int i, int j)
        {
            if (L[i][j] != -1)
                return L[i][j];
            if ( i == 1 && j == 1 )
                L[i][j] =  m[i][j];
            else if ( i == 1 )
                L[i][j] =  mat(1, j-1) + m[i][j];
            else if ( j == 1 )
                L[i][j] =  mat(i-1, 1) + m[i][j];
            else
                L[i][j] =  Math.min(mat(i-1, j), mat(i, j-1)) + m[i][j];
            return L[i][j];
        }
        ```
        - Bottom-Up
            > 시간복잡도: O(n^2)<br>
        ```
        int mat()
        {
            for (int i = 1; i <= n; i++){
                for(int j = 1; j <= n; j++){
                    if ( i == 1 && j == 1 )
                        L[i][j] =  m[1][1];
                    else if ( i == 1 )
                        L[i][j] =  L[i][j-1] + m[i][j];
                    else if ( j == 1 )
                        L[i][j] =  L[i-1][j] + m[i][j];
                    else
                        L[i][j] =  Math.min(L[i-1][j], L[i][j-1]) + m[i][j];
                }
            }
            return L[n][n];
        }
        ```
        - Common Trick
            > 시간복잡도: O(n^2)<br>
            > initialise L with L[0][j] = L[i][0] = infinite for all i and j<br>
            ```
            int mat()
            {
                for(int i = 1; i <= n; i++){
                    for(int j = 1; j <= n; j++){
                        if(i == 1 && j == 1)
                            L[i][j] = m[1][1];
                        else
                            L[i][j] = m[i][j] + Math.min(L[i-1][j], L[i][j-1]);
                    }
                }
                return L[n][n];
            }
            ```

### 동적계획법
1. 일반적으로 최적화문제(optimisation problem) 혹은 카운팅(counting) 문제에 적용됨
2. 주어진 문제에 대한 순환식을 정의한다.
3. 순환식을 memoization 혹은 bottom-up 방식으로 푼다.
- `subproblem들을 풀어서` 원래 문제를 푸는 방식. 그런 의미에서 분할정복법과 공통성이 있음
- 분할 정복법에서는 분할된 문제들이 서로 disjoint하지만 동적계획법에서는 그렇지 않음
- 즉 `서로 overlapping하는 subproblem들을 해결`함으로써 원래 문제를 해결

- 분할정복법 vs. 동적계획법
    - 분할정복법 : quicksort의 경우
        - pivot을 기준으로 분할된 두 subproblem은 서로 disjoint하다.
    - 동적계획법 : 행렬문제의 경우
        - 각각의 최적 해는 그 전의 최적 해를 조합해서 문제를 해결한다.

### Optimal Substructure
- 어떤 문제의 최적해가 그것의 `subproblem들의 최적해`로부터 효율적으로 구해질 수 있을 떄 그 문제는 `optimal substructure를 가진다`고 말한다.
- 분할정복법, 탐욕적기법, 동적계획법은 모두 문제가 가진 이런 특성을 이용한다. 

### Optimal Substructure를 확인하는 질문
- "최적해의 일부분이 그 부분에 대한 최적해인가?"
- 최단경로(shortest-path) 문제
    - s - v - u : 이 경로가 s에서 u까지의 최단경로라면 이 경로는 s에서 v까지의 최단 경로이다.
- 순환식은 optimal substructure를 표현한다.
    - d[u] = min ( d[v] + w(v, u) )
        - d[u] : u까지 가는 최단경로의 길이
        - d[v] : u에 인접한 모든 정점 v에 대해서 v까지 가는 최단경로의 길이
        - w(v, u) : 에지 (v, u)의 가중치
- 최장경로(Longest-Path) 문제
    - 노드를 중복 방문하지 않고 가는 가장 긴 경로
    - optimal substrcutre를 가지는가?
    - d[u] != max ( d[v] + w(v, u) )
        - u까지 가는 최장경로가 v를 지난다고 하더라도 그 경로상에서 v까지 가는 경로가 반드시 v까지 가는 최장경로가 아닐 수도 있으므로 이런 순환식은 성립하지 않는다.

### 행렬의 곱셈
- pxq 행렬 A와 qxr 행렬 B 곱하기
    ```
    for(int i = 0; i < p; i++){
        for(int j = 0; j < r; j++){
            C[i][j] = 0;
            for(int k = 0; k < q; k++)
                C[i][j] += A[i][k] * B[k][j];
        }
    }
    ```
    - 곱셈연산의 횟수 = pqr

- Matrix-Chain 곱하기
    - 행렬 A는 100x100, B는 100x5, C는 5x50
    - 세 행렬의 곱 ABC는 두 가지 방법으로 계산가능 (결합법칙이 성립)
        - (AB)C : 7500번의 곱셈이 필요 (10x100x5 + 10x5x50)
        - A(BC) : 75000번의 곱샘이 필요 (100x5x50 + 10x100x50)
    - 즉 곱하는 순서에 따라서 연산량이 다름
    - n개의 행렬의 곱 A1A2A3...An을 계산하는 최적의 순서는?
    - 여기서 Ai는 pk-1 x pk 행렬이다.
    - Optimal Substructure
        - A1A2A3...AkAk+1Ak+2...An
        - X : A1A2...Ak -> 앞부분의 곱 
        - Y : Ak+1Ak+2...An -> 뒷부분의 곱
        - Z : 최종결과 Z는 직전의 두 행렬 X와 Y의 곱이다.

        - m[i, j] : AiAi+1...Aj를 곱하는 최소곱셈 횟수
            - i == j
                - 0
            - i < j
                - i <= k <= j-1
                - min(m[i, k] + m[k+1, j] + pi-1pkpj)

        ```
        for(int i = 1; i <= n; i++)
            m[i][i] = 0;
        for(int r = 1; r <= n-1; r++){
            for(int i = 1; i <= n-r; i++){
                int j = i + r;
                m[i][j] = m[i+1][j] + p[i-1]*p[i]*p[j];
                for(int k = i+1; k <= j-1; k++){
                    if(m[i][j] > m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j])
                        m[i][j] = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
                }
            }
        }
        return m[1][n];
        ```
        - 시간복잡도 : O(n^3)
### Longest Common Subsequence(LCS)
- < bcdb >는 문자열 < abcbdab >의 subsequence이다.
- < bca >는 문자열 < abcbdab >와 < bdcaba >의 common subsequence이다.
- Longest common subsequence(LCS)
    - common subsequence들 중 가장 긴 것 
    - < bcba >는 < abcbdab >와 < bdcaba >의 LCS이다.
- 순환식
    - L[i, j] : 문자열 X = < x1x2...xi >와 Y = < y1y2...yj >의 LCS의 길이
    - 경우 1 : xi = yj
        - L[i, j] = L[i-1, j-1] + 1 
    - 경우 2 : xi != yj
        - L[i, j] = max(L[i-1, j], L[i, j-1])
    ```
    int lcs(int m, int n) // m : length of X, n : length of Y
    {
        for(int i = 0; i <= m; i++)
            c[i][0] = 0;
        for(int j = 0; j <= n; j++)
            c[0][j] = 0;
        for(int i = 0; i <= m; i++)
        {
            for(j = 0; j <= n; j++)
            {
                if(x[i] == y[j])
                    c[i][j] = c[i-1][j-1] + 1;
                else
                    c[i][j] = Math.max(c[i-1][j], c[i][j-1]);
            }
        }
        return c[m][n]
    }
    ```
    - 시간복잡도 : O(mn)