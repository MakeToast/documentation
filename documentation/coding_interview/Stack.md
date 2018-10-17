# Stack
`FIRST IN FIRST OUT`

## PUSH
```
def push(self, item) :
    if len(self.items) < self.max :
        self.items.append(item)
    else :
        print("abort push in order to prevent stack overflow")
```
- example

    Data              Stack
    | 1 |           |       |
    | 2 |           |       |
    | 3 |           |       |
    | 4 |           |_______|

    * PUSH 1

    Data              Stack
                    |       |
    | 2 |           |       |
    | 3 |           |       |
    | 4 |           | | 1 | |

    * PUSH 2

    Data              Stack
                    |       |
                    |       |
    | 3 |           | | 2 | |
    | 4 |           | | 1 | |

    * PUSH 3

    Data              Stack
                    |       |
                    | | 3 | |
                    | | 2 | |
    | 4 |           | | 1 | |

    * PUSH 4

    Data              Stack
                    | | 4 | |
                    | | 3 | |
                    | | 2 | |
                    | | 1 | |

## STACK OVERFLOW
> 스택이 가득 찼을 때 또 다른 value를 넣으려고 하면 스택에 값을 담을 공간이 없다. 따라서 이 스택은 프로그램에 에러를 야기할 수 있다.

## POP
```
def pop(self) :
    if len(self.items) > 0 :
        self.items.pop()
    else
        print("stack is empty, abort pop to prevent stack underflow")
```

- example
                          Stack
                        | | 4 | |
                        | | 3 | |
                        | | 2 | |
                        | | 1 | |

    * POP

        Data              Stack
                        |       |
                        | | 3 | |
                        | | 2 | |
        | 4 |           | | 1 | |

    * POP

        Data              Stack
                        |       |
                        |       |
        | 3 |           | | 2 | |
        | 4 |           | | 1 | |

    * POP

        Data              Stack
                        |       |
        | 2 |           |       |
        | 3 |           |       |
        | 4 |           | | 1 | |
    
    * POP

        Data              Stack
        | 1 |           |       |
        | 2 |           |       |
        | 3 |           |       |
        | 4 |           |       |

## STACK UNDERFLOW
> 스택에 아무런 값이 없는데 값을 빼내려고 하면 에러가 난다.

## STACK EXAMPLE
- Browser back button
- DFS(Depth First Search)