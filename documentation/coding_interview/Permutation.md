# Permutation_순열

- example
```
def perm(input, i) :
    if i == len(input) - 1 :
        print(input)
    else :
        for j in range(i, len(input)) :
            input[i], input[j] = input[j], input[i]
            perm(input, i+1)
            input[i], input[j] = input[j], input[i]

perm([1, 2, 3], 0)
```
| A | B | C |<br>

- 첫 번째 아이템 스와핑
    - A와 A 스와핑 : | A | B | C |<br>
        - 두 번째 아이템 스와핑
            - B와 B 스와핑 : | A | B | C |<br>
            - B와 C 스와핑 : | A | C | B |<br>

    - A와 B 스와핑 : | B | A | C |<br>
        - 두 번째 아이템 스와핑
            - A와 A 스와핑 : | B | A | C |<br>
            - A와 C 스와핑 : | B | C | A |<br>

    - A와 C 스와핑 : | C | B | A |<br>
        - 두 번째 아이템 스와핑
            - B와 B 스와핑 : | C | B | A |<br>
            - B와 A 스와핑 : | C | A | B |<br>

- 응용
    * 모든 경우의 수를 구할 때