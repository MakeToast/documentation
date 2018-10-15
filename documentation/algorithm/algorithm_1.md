# Recursion의 개념과 기본 예제 1

## What is Recursion?

- 자기 자신을 호출하는 함수 : 무한루프
```
void func(...)
{
    func(...);
}
```
- recusrion은 항상 무한루프에 빠질까?
> recursion이 항상 무한루프에 빠지는 것은 아니다.
```
public class Code{
    public static void main(String[] args){
        int n = 4;
        func(n);
    }

    public static void func(int k){
        if(k <= 0)
            return;
        else{
            System.out.println("Hello");
            func(k-1);
        }
    }
}
```
> `base case` : 적어도 하나의 recursion에 빠지지 않는 경우가 존재해야 한다.<br>
> `recursive case `: recursion을 반복하다보면 결국 base case로 수렴해야 한다.

- Fibonacci Number
```
public int fibonacci(int n){
    if(n < 2)
        return n;
    else
        return fibonacci(n-1) + fibonacci(n-2);
}
```

- 최대공약수 : Euclid Method
```
public static double gcd(int m, int n){
    if(m < n)
    {
        int tmp = m;
        m = n;
        n = tmp;
    }
    if(m % n == 0)
        return n;
    else
        return gcd(n, m%n);
}
```
> m>=n 인 두 양의 정수 m과 n에 대해서 m이 n의 배수이면 gcd(m,n)=n이고, 그렇지 않으면 gcd(m,n)=gcd(n,m%n)이다.

- Euclid Method 단순한 버전
```
public static int gcd(int p, int q){
    if(q==0)
        return p;
    else
        return gcd(q, p%q);
}
```
- 문자열의 길이 계산
```
public static int length(String str){
    if(str.equals(""))
        return 0;
    else
        return 1+length(str.sbustring(1))
}
```
> example<br>
length("ace") -> 1+lenght("ce") -> 1+length("e") -> 1+length("")

- 문자열의 프린트
```
public static void printChars(string str){
    if(str.length() == 0)
        return;
    else
    {
        System.out.print(str.charAt(0));
        return printChars(str.substring(1));
    }
}
```
- 문자열을 뒤집어 프린트
```
public static void printCharsReverse(String str){
    if(str.length() == 0)
        return;
    else{
        printCharsReverse(str.substring(1));
        System.out.print(str.charAt(0));
    }
}
```
- 2진수로 변환하여 출력
```
public void printInBinary(int n){
    if(n < 2)
        System.out.print(n);
    else
    {
        printInBinary(n/2);
        System.out.print(n%2);
    }
}
```
- 배열의 합 구하기(data[n-1]+...+data[0])
```
public static int sum(int n, int [] data){
    if(n <= 0)
        return 0;
    else
        return sum(n-1. data) + data[n-1];
}
```
- 데이터파일로부터 n개의 정수 읽어오기
```
public void readFrom(int n, int [] data, Scanner in){
    if(n== 0)
        return 0;
    else
    {
        readFrom(n-1, data, in);
        data[n-1] = in.nextInt();
    }
}
```
### Recursion vs Iteration
- 모든 순환함수는 반복문으로 변경 가능
- 그 역도 성립함. 즉 모든 반복문은 recursion으로 표현 가능함
- 순환함수는 복잡한 알고리즘을 단순하고 알기쉽게 표현하는 것을 가능하게 함.
- 하지만 함수 호출에 따른 오버헤드가 있다.(매개변수 전달, 액티베이션 프레임 생성 등)

## Desigin Recursion(순환 알고리즘의 설계)

- 적어도 하나의 `base case`, 즉 순환되지 않고 종료되는 case가 있어야 함
- 모든 case는 결국 base case로 수렴해야 함

### 암시적(implicit) 매개변수를 `명시적(explicit) 매개변수`로 바꾸어라

```
int search(int [] data, int n, int target){
    for(int i = 0; i < n; i++)
    {
        if(data[i] == target)
            return i;
    }
    return -1;
}
```
> 이 함수는 data[0]에서 data[n-1] 사이에서 target을 검색한다. 하지만 검색 구간의 시작 인덱스 0은 보통 생략한다. 즉 `암시적 매개변수`이다.

- 매개변수의 명시화 : 순차탐색
```
int search(int [] data, int begin, int end, int target){
    if(begin > end) 
        return -1;
    else if(target == data[begin])
        return begin;
    else
        return search(data, begin+1, end, target)
}
```
> begin을 설정해주지 않으면 0부터 찾기 때문에 반복적인 일을 여러번 한다. 따라서 검색구간의 시작점을 명시적으로 지정한다.

- 순차 탐색 : 다른 버전 1
```
int search(int [] data, int begin, int end, int target){
    if(begin > end)
        return -1;
    else if(target == data[end])
        return end;
    else
        return search(data, begin, end-1, target);
}
```
- 순차 탐색 : 다른 버전 2(binary search와 다름)
```
int search(int [] data, int begin, int end, int target){
    if(begin > end)
        return -1;
    else
    {
        int middle = (begin+end)/2;
        if(data[middle] == target)
            return middle;
        int index = search(data, begin, middle-1, target);
        if(index != -1)
            return index;
        else
            return search(data, middle+1, end, target);
    }
}
```
- 매개변수의 명시화 : 최대값 찾기
```
int findMax(int [] data, int begin, int end){
    if(begin == end)
        return data[begin];
    else
        return Math.max(data[begin], findMax(data, begin+1, end));
}
```
- 최대값 찾기 : 다른 버전
```
int findMax(int [] data, int begin, int end){
    if(begin == end)
        return data[begin];
    else{
        int middle = (begin+end)/2;
        int max1 = findMax(data, begin, middle);
        intt max2 = findMax(data, middle+1, end);
        return Math.max(max1, max2);
    }
}
```
- Binary Search
```
public static int binarySearch(String[] items, string target, int begin, int end){
    if(begin > end)
        return -1;
    else{
        int middle = (begin+end)/2;
        int comResult = target.compareTo(items[middle]);
        if(comResult == 0)
            return middle;
        else if(comResult < 0)
            return binarySearch(items, target, begin, middle-1)
        else
            return binarySearch(items, target, middle+1, end);
    }
}
```