# Selection Sort
- Worst case performance : O(n^2)
- Best case performance : O(n^2)
- Average case performance : O(n^2)
- Worst case space complexity : O(n) total, O(1) auxiliary

- example
    * | 4 | 6 | 1 | 3 | 5 | 2 |
       ---
    * Minimum value : 4
        * 6과 비교 -> Minimum value < 6
        * 1과 비교 ->  Minimum value > 1 -> Minimum value `스와핑`
        * Minimum value : 1
        * 3과 비교 -> Minimum value < 3
        * 5와 비교 -> Minimum value < 5
        * 2와 비교 -> Minimum value < 2
        * 현재 position과 Minimum value의 position `스와핑`
        
    * | 1 | 6 | 4 | 3 | 5 | 2 |
           ---
    * Minimum value : 6
        * 4와 비교 -> Minimum value > 4 -> Minimum value `스와핑`
        * Minimum value : 4
        * 3과 비교 -> Minimum value > 3 -> Minimum value `스와핑`
        * Minimum value : 3
        * 5와 비교 -> Minimum value < 5 
        * 2와 비교 -> Minimum value > 2 -> Minimum value `스와핑`
        * 현재 position과 Minimum value의 position `스와핑`

    * | 1 | 2 | 4 | 3 | 5 | 6 |
               ---
    * Minimum value : 4
        * 3과 비교 -> Minimum value > 3 -> Minimum value `스와핑`
        * Minimum value : 3
        * 5와 비교 -> Minimum value < 5 
        * 6과 비교 -> Minimum value < 6
        * 현재 position과 Minimum value의 position `스와핑`
    
    * | 1 | 2 | 3 | 4 | 5 | 6 |
                   ---
    * Minimum value : 4 
        * 5와 비교 -> Minimum value < 5 
        * 6과 비교 -> Minimum value < 6
        * 현재 position과 Minimum value의 position `스와핑`

    * | 1 | 2 | 3 | 4 | 5 | 6 |
                       ---
    * Minimum value : 5 
        * 6과 비교 -> Minimum value < 6
        * 현재 position과 Minimum value의 position `스와핑`
    
    * | 1 | 2 | 3 | 4 | 5 | 6 |
                           ---
    * Minimum value : 6 
        * 비교할 것이 없다.