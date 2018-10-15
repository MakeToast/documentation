# Big O Notation
- 코딩 인터뷰 할 때 빅오 표현 방법을 사용해서 이야기 하면 좋다.
- 알고리즘 퍼포먼스를 이야기 할 때 상당히 좋은 방법이다. 
![Big O Complexity](https://cdn-images-1.medium.com/max/2000/1*HwLR-DKk0lYNEMpkH475kg.png)
         O(1) < O(log n) < O(n) < O(n log n) < O(n^2)
Good(faster) <---------------------------------> Bad(slower)

## Example - O(1)
```
public void printFirstItem(int[] arrayOfItems){
    System.out.println(arrayOfItems[0]);
}
```
- Other examples:
    * Push, Pop on Stack
    * Access hash table(하나의 키에만 접근하므로)

- Tip :
    * nO(1) = O(1) (인자를 상관하지 않는다.)
    * 2 * O(1) = 10 * O(1) = O(1) 

## Example - O(log n)
- Binary Search Tree Access, Search, Insertion, Deletion
    * Denote n = 8
    * log 8 = log 2^3 = 3
![binary tree](https://www.geeksforgeeks.org/wp-content/uploads/dist.png)

- Tip :
    * nO(log n) = O(log n)
    * 2 * O(log n) = 10 * O(log n) = O(log n)

## Example - O(n)
```
public void printAllItems(int[] arrrayOfItems){
    for (int item : arrayOfItems){
        System.out.println(item);
    }
}
```
- Other example:
    * traverse tree
    * traverse linked list

- Tip :
    * nO(n) = O(n)
    * 2 * O(n) = 10 * O(n) = O(n)

## Example - O(n log n)
- Quick Sort, Merge Sort, Heap Sort
    * Denote n = 4
    * log 8 = 2 * log 2^2 = 4
![merge sort](https://www.mcs.anl.gov/~itf/dbpp/text/img1152.gif)

- Tip :
    * n O(n log n) = O(n log n)
    * 2 * O(n log n) = 10 * O(n log n) = O(n log n)

## Example - O(n^2)
```
public void printAllPossibleOrderedPairs(int[] arrayOfItems){
    for(int firstItem : arrayOfItems){
        for(int secondItem : arrayOfItems){
            int[] orderedPair = new int[]{firstItem, secondItem};
            System.out.println(Arrays.toString(orderedPair));
        }
    }
}
```

- Other examples :
    * Insertion Sort
    * Bubble Sort
    * Selection Sort

- Tip :
    * n O(n^2) = O(n^2)
    * 2 * O(n^2) = 10 * O(n^2) = O(n^2)