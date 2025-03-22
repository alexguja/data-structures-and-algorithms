## Linked Lists

A _linked list_ is a data structure that stores objects in a linear order.
Unlike an array, a linked list does not store its elements in contiguous memory locations. Instead, each element in a linked list is stored in a node that contains a pointer to the next node in the sequence.
Linked lists come in various forms, such as singly linked lists, doubly linked lists, and circular linked lists. 

### Terminology
- The first element or node of a linked list is called the _head_ of the list.
- The last element or node of a linked list is called the _tail_ of the list.
- A linked list is _empty_ if it does not contain any elements.
- The _size_ of a linked list is the number of elements it contains.
- A linked list is _circular_ if the last node points to the first node.
- A linked list is _singly linked_ if each node contains a reference to the next node.
- A linked list is _doubly linked_ if each node contains references to the next and previous nodes.
- A linked list is _sorted_ if its elements are arranged in a increasing or decreasing order.
- A linked list is _unsorted_ if its elements are not arranged in any particular order.



### List Operations Summary

| Operation    | Unsorted, Singly Linked | Sorted, Singly Linked | Unsorted, Doubly Linked | Sorted, Doubly Linked |
| ------------ | ----------------------- | --------------------- | ----------------------- | --------------------- |
| `prepend(x)` | $O(1)$                  | $O(n)$                | $O(1)$                  | $O(n)$                |
| `append(x)`  | $O(1)$                  | $O(n)$                | $O(1)$                  | $O(n)$                |
| `find(k)`    | $O(n)$                  | $O(n)$                | $O(n)$                  | $O(n)$                |
| `delete(x)`  | $O(n)$                  | $O(n)$                | $O(1)$                  | $O(1)$                |
| `minimum()`  | $O(n)$                  | $O(1)$                | $O(n)$                  | $O(1)$                |
| `maximum()`  | $O(n)$                  | $O(1)$                | $O(n)$                  | $O(1)$                |

