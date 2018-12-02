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
