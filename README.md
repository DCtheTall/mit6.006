# Implementations of Algorithms Covered in MIT 6.006

by Dylan Cutler (DCtheTall)

## Topics Covered

- 1D and 2D Peak Finding ([lecture 1](#lecture-1))
- Document Distance ([lecture 2](#lecture-2))
- Insertion Sort ([lecture 2](#lecture-2))
- Mergesort ([lecture 3](#lecture-3))
- Max Heaps ([lecture 4](#lecture-4))
- Heapsort ([lecture 4](#lecture-4))
- Binary Search Trees ([lecture 5](#lecture-5))
- AVL Trees ([lecture 6](#lecture-6))
- Counting Sort ([lecture 7](#lecture-7))
- Radix Sort ([lecture 7](#lecture-7))
- Hash Table with Chaining ([lecture 8](#lecture-8))
- Rolling Hashes ([lecture 9](#lecture-9))
- Karp-Rabin Text Search ([lecture 9](#lecture-9))
- Hash Table with Probing ([lecture 10](#lecture-10))
- Catalan Numbers ([lecture 11](#lecture-11))
- Karatsuba Multiplication ([lecture 11](#lecture-11))
- Breadth-First Search ([lecture 13](#lecture-13))
- Depth-First Search ([lecture 14](#lecture-14))
- Graph Cycle Detection ([lecture 14](#lecture-14))
- Topological Sort ([lecture 14](#lecture-14))
- Shortest Path Algorithm for a Directed Acyclic Graph ([lecture 16](#lecture-16))
- Dijkstra's Shortest Path Algorithm ([lecture 16](#lecture-16))
- Bellman-Ford Shortest Path Algorithm ([lecture 17](#lecture-17))
- Single Target Dijkstra's Algorithm ([lecture 18](#lecture-18))
- Bi-Directional Dijkstra's Algorithm ([lecture 18](#lecture-18))
- Goal Directed Dijkstra's Algorithm ([lecture 18](#lecture-18))
- Fibonacci Numbers ([lecture 19](#lecture-19))
- Memoization ([lecture 19](#lecture-19))
- Dynamic Programming ([lecture 19](#lecture-19), [lecture 20](#lecture-20), [lecture 21](#lecture-21))

## Lecture 1

### `peakfinding.py`

This program has implementations of algorithms for finding a peak in
a 1-D or 2-D array of integers.

## Lecture 2

### `docdist<i>.py`

Each program in this file calculates the distance between two articles from
Wikipedia. Each program incrementally improves the performance of the
calculation.

## Lecture 3

### `insertionsort.py`

This program contains 2 implementations of insertion sort.

### `mergesort.py`

This program contains 2 implementations of merge sort, the
second being a recursive functional implementation.

## Lecture 4

### `heapsort.py`

This program contains an implementation applying the max heap invariant
to Python lists. It also has an implementation of heapsort.

## Lecture 5

### `bst.py`

This program is an implementation of a binary search tree.

## Lecture 6

### `avl.py`

This program contains an implementation of an AVL tree, a self-balancing
binary search tree.

## Lecture 7

### `countingsort.py`

This program contains an implementation of counting sort, a linear time sorting
algorithm for integers.

### `radixsort.py`

This program contains 2 implementations of radix sort, a linear time sorting
algorithm for integers. One implementation is generalized for using any base
integer for the buckets, the other is an optimized binary radix sort.

## Lecture 8

### `hashtable.py`

This program is an implementation of a hash table which uses chaining linked
lists to handle collisions.

## Lecture 9

### `karprabin.py`

This program has an implementation of Karp-Rabin text search, which uses rolling
hashes to efficiently find if a string is a substring of another.

## Lecture 10

### `hashtable.py`

This program is an implementation of a hash table which uses probing to handle
collisions.

## Lecture 11

### `catalan.py`

This program contains a function which can find the terms in the
[Catalan number sequence](https://en.wikipedia.org/wiki/Catalan_number).

### `karatsuba.py`

This program contains an implementation of Karatsuba multiplication, a
divide-and-conquer high precision multiplication algorithm.

## Lecture 13

### `bfs.py`

This program contains 2 implementations of breadth-first search.

## Lecture 14

### `dfs.py`

This program contains 2 implementations of depth-first search. One is a
recursive implementation and another using a stack.

### `cycles.py`

This program contains an implementation of an algorithm which uses
depth-first search to detect if a graph contains any cycles.

### `topologicalsort.py`

This program contains an implementation of topological sorts for
directed, acyclic graphs (DAGs).

## Lecture 16

### `topologicalsort.py`

This program contains an implementation of an algorithm which uses
topological sort to find the shortest path to each vertex from a
given source vertex.

### `dijkstra.py`

This program contains an implementation of Dijkstra's single source
shortest path algorithm.

## Lecture 17

### `bellmanford.py`

This program contains an implementation of Bellman-Ford's shortest path
algorithm. It will raise an exception if the graph has a negative weight
cycle.

## Lecture 18

### `singletarget.py`

This program contains an implementation of a single-target Dijkstra's
shortest path algorithm to find the shortest path between a source vertex
and target vertex.

### `bidirectional.py`

This program contains an implementation of a bi-directional single target
Dijkstra's shortest path algorithm. It initiates two searches, one from
the source vertex the other from the target vertex. It halts when each search
finds a common vertex, and then finds the shortest bridge between the two
vertices. The proof of correctness is covered in lecture.

### `goaldirected.py`

This program contains an implementation of a goal-directed single-target
Dijkstra's shortest path algorithm. It uses a heuristic to improve the
speed of single-target Dijkstra's algorithm when it searches a large graph.

## Lecture 19

### `fibonacci.py`

This program contains 3 functions which compute the n^th Fibonacci number:

1. A naive recursive algorithm.
2. A dynamic programming algorithm which uses a memoization table.
3. A bottom-up dynamic programming algorithm.

## Lecture 20

### `blackjack.py`

This program contains an algorithm for playing the best game of blackjack
possible given that you know the order of the deck.

### `justify.py`

This program contains an algorithm for justifying lines in a paragraph
of text.

## Lecture 21

### `distance.py`

This program contains an implementation of computing the minimum edit distance
between two strings.

### `knapsack.py`

This program contains a solution to the knapsack problem: given a knapsack
with a given capacity, what are the highest value items you can take given
that the weight of the items cannot exceed the capacity.

### `matrices.py`

This program contains an algorithm for finding the optimal matrix multiplication
order for finding the product of multiple matrices.

## Other algorithms

This repository also has implementations of the following algorithms not covered in
lecture:

- A* search
- Iterated-Depth Depth-First Search (IDDFS)
- Red-Black tree
