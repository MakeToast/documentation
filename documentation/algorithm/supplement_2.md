# Binary Search Tree

- tree의 node에 저장된 값
```
typedef Place * Item;
```

- tree의 node 정의
```
strudt tnode {
    Item data;
    struct tnode * left, * right;
};
typedef strcut tnode Node;
```

- 하나의 tree 정의
```
typedef struct bst{
    Node * root;
    CompareFtnType compareFtn;
} BST;
```

- BST 하나 만드는 함수
```
BST * create_bst(int (*f) (Item, Item))
{
    BST * tree = (BST *)malloc(sizeof(BST));
    tree->root = NULL;
    tree->compareFtn = f;
    return tree;
}
```

- BST에 node 추가하는 함수
```
bool insert(BST * tree, Item item)
{
    Node * p = tree->root, *q = NULL;
    while(p!=NULL){
        int result = tree->compareFtn(p->data, item);
        q = p;
        if (result == 0)
            return false;
        else if(result > 0)
            p = p->left;
        else
            p = p->right;
    }
    Node * tmp = (Nulde *)malloc(sizeof(Node));
    tmp->data = item;
    tmp->left = NULL;
    tmp->right = NULL;

    if(q==NULL){ // tree가 비었다.
        tree->root = tmp;
        return ;
    }

    int result = tree->compareFtn(q->data, item);
    if(result > 0)
        q->left = tmp;
    else
        p->right = tmp;
    return true;
}
```
- BST에 node 서치하는 함수
```

Item search(BST * tree, Item item)
{
    Node * p = tree->root;
    while(p!=NULL){
        int result = tree->compareFtn(p->data, item);
        if(result == 0){
            return p-> data;
        }
        else if(result > 0){
            p = p -> left;
        }
        else{
            p = p -> right;
        }
    }
    return NULL;
}
```
- BST에 node 삭제하는 함수
```
Item remove(BST * tree, Item item);
```
