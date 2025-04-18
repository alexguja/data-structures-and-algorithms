# Classic Data Structures and Algorithms in Python

# Algorithms

- [ ] Two Pointers
- [x] Binary Search
- [ ] Sorting
  - [x] Insertion Sort
  - [x] Heapsort
  - [x] Merge Sort
  - [ ] Quicksort
  - [ ] Randomised Quicksort
  - [ ] Counting Sort
  - [ ] Radix Sort
- [ ] Sliding Window
- [ ] Rabin-Karp
- [x] Breadth First Search
- [x] Depth First Search
- [ ] Topological Sort
- [ ] Dijkstra's Algorithm
- [ ] Bellman-Ford Algorithm
  

# Data Structures

- [ ] Dynamic Array
- [x] Linked List
- [x] Stack
- [x] Queue
- [x] Hash Table
- [x] Binary Heap
- [x] Binary Search Tree
- [ ] AVL Tree
- [ ] Graph
- [x] Trie



## Binary Heaps
The concept of the _binary heap_ was introduced by J. W. J. Williams in 1964. He described the heap data structure in his paper "Algorithm 232: Heapsort". The heap data structure is an array that can be viewed as a nearly complete binary tree. Each element of the heap corresponds to an element in the array. The tree is filled on all levels except possibly the lowest, which is filled from the left up to a point.

![alt text](docs/heap.png)


- The root of the heap is given by the first element of an array $H$ (i.e. $H[0]$). 
- Given an index $i$ of the array $H$, we can compute the indices of the parent node, and the left and right children nodes. 
  - The parent of the node at index $i$ is given by the index $⌊(i-1)/2⌋$.  
  - The left child of the node at index $i$ is given by the index $2i + 1$.
  - The right child of the node at index $i$ is given by the index $2i + 2$.

There are two types of binary heaps: min-heaps and max-heaps.
- In a max-heap the key of a parent node is always greater than or equal to the keys of its children nodes, or $H[parent(i)] ≥ H[i]$. 
- In a min-heap, the key of a parent node is always less than or equal to the keys of its children nodes, or $H[parent(i)] ≤ H[i]$.

These conditions are known as the _heap invariant_ for max-heaps and min-heaps respectively.


The height of a heap node is defined as the number of edges on the longest simple downward path from the node to a leaf. The height of the heap is determined by the height of its root.
The height of a heap can be estimated by $O(lg(n))$ where $n$ is the number of elements in the heap.
Most of the heap operations run in proportion to its height, so the running time is usually $O(lg(n))$.


- For $n$ elements, the number of levels in a heap needed to store the the elements can be determined by $L(n) = 1 + ⌊lg(n)⌋$ where $L(n)$ is the number of levels.
- The running time of heapsort is $O(n \lg n)$.

### Visualising Heap Operations

#### Insert

![heap-insert](docs/heap-insert.png)


#### Extract Max

![heap-extract-max](docs/extract-max.png)


#### Max Heapify

![max-heapify](docs/max-heapify.png)


### Heaps Summary


| Operation        | Time Complexity | Notes                                                          |
| ---------------- | --------------- | -------------------------------------------------------------- |
| `insert`         | $O(\lg n)$      | Maintaining the heap invariant takes $O(\lg n)$                |
| `extract_max`    | $O(\lg n)$      | Maintaining the heap invariant takes $O(\lg n)$                |
| `increase_key`   | $O(\lg n)$      | Maintaining the heap invariant takes $O(\lg n)$                |
| `delete`         | $O(\lg n)$      | Maintaining the heap invariant takes $O(\lg n)$                |
| `max_key`        | $O(1)$          | Constant time                                                  |
| `max_hapify`     | $O(\lg n)$      | Proportional to the height of the heap $O(h) , h = \lg n$      |
| `build_max_heap` | $O(n)$          | Proportional to the size of the array                          |
| `heapsort`       | $O(n \lg n)$    | Maintaining the heap invariant for n nodes  takes $O(n \lg n)$ |


## References
[1] - CLRS Introduction to Algorithms
