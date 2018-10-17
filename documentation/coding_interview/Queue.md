# Queue
`LAST IN FIRST OUT (LIFO)`

## Enqueue
> queue 에 데이터를 넣는 과정
```
def enqueue(self, item) :
    self.item.insert(0, item)
```
- example
    
    Queue : |                       |

    Data : | 1 || 2 || 3 || 4 |

    * Enqueue 1

    Queue : |                  | 1 | |
    
    * Enqueue 2

    Queue : |             | 2 | | 1 | |

    * Enqueue 3

    Queue : |       | 3 | | 2 | | 1 | |

    * Enqueue 4

    Queue : | | 4 | | 3 | | 2 | | 1 | |

## Dequeue
> queue에 데이터를 꺼내는 과정
```
def dequeue(self, item) :
    self.items.pop()
```
- example

    Queue : | | 4 | | 3 | | 2 | | 1 | |

    * Dequeue

    Queue : | | 4 | | 3 | | 2 |       |

    Data : | 1 |
    
    * Dequeue

    Queue : | | 4 | | 3 |             |

    Data : | 1 | | 2 |

    * Dequeue

    Queue : | | 4 |                   |

    Data : | 1 | | 2 | | 3 |

    * Dequeue

    Queue : |                         |

    Data : | 1 | | 2 | | 3 | | 4 |

## QUEUE Example
- Printer job queue
- BFS(Breadth First Search)