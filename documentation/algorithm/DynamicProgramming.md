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
