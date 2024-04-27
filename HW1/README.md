# Q1
## Minimum Spanning Tree (MST)
A Minimum Spanning Tree (MST) of a weighted graph is a connected, undirected tree that connects all the vertices of the graph with the minimum possible total edge weight.

In other words, an MST is a subset of all the edges of the graph that connects all the vertices, ensuring that all vertices are accessible to each other and has the minimum possible total weight.

Input:
The input consists of a single line containing two natural numbers n and m, separated by a space, representing the number of vertices and the number of edges respectively.

- 1 ≤ n ≤ 2000
- 1 ≤ m ≤ 100000
The next m lines contain the description of each edge, consisting of two vertices and the weight of the edge.

Output:
The output of your program should only be the sum of the weights of the smallest edges in the minimum spanning tree.
**Example:**

**Input 1:**

5 6
2 4 1
1 2 383
3 4 962
2 3 868
4 5 866
3 5 391

**Output 1:**

1641

Example 2:

**Input 2:**

2 1
1 2 871

**Output 2:**
871