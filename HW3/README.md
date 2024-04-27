# Q1
## common algorithm

Suppose we have a simple graph G with n vertices and m edges, where the vertices are numbered from 1 to n.

A graph is called Eulerian if it has a "trail" in which each edge of G appears exactly once.

A trail is a sequence of edges like e1, e2, ..., ek, such that for each 2 ≤ i ≤ k, we have ei-1 ∩ ei ≠ ∅.

You are given a graph, and you are asked to determine whether this graph is Eulerian or not.

**Input:**
The input consists of two integers n and m separated by a space in the first line, representing the number of vertices and edges of graph G respectively.

- 1 ≤ n ≤ 100000
- 0 ≤ m ≤ min{(n−1)2, 100000}

The next m lines contain two integers ui and vi separated by a space each, indicating the existence of an edge ui vi in graph G.

- 1 ≤ ui ≠ vi ≤ n

It is guaranteed that the given graph is simple, meaning there is at most one edge between any two vertices.

**Output:**
Print "YES" in a single line if the graph G is Eulerian, otherwise print "NO".

**Example:**

**Input 1:**
3 3
1 2
1 3
2 3


**Output 1:**
YES


Explanation: Yes, because the following sequence exists:
{1,2}, {2,3}, {1,3}

**Input 2:**
4 2
1 2
3 4


**Output 2:**
NO


Explanation: No, because this graph has only two edges that do not share any commonality. So, it's impossible to construct a sequence where both edges appear and each consecutive pair of edges have non-empty intersection.

**Input 3:**
5 5
1 2
2 3
3 4
4 5
5 3


**Output 3:**
YES


Explanation: Yes, because the following sequence exists:
{1,2}, {2,3}, {3,4}, {4,5}, {3,5}

# Q2
## Cut Edge

Saein wants to challenge himself with a question, so Porya gives him a task to find the value of the edge connectivity in a graph. For this purpose, Porya gives Saein two integers n and m, where n is the number of vertices and m is the number of edges. Then, in the next m lines, two integers are given to Saein, representing the endpoints of each edge. Note that the vertices are numbered from 1 to n.

Also, to make the question harder for Saein, Porya tells him that the input graph may not be simple, which means it may have multiple edges and loops.

**Input:**
The input consists of a single line containing two natural numbers n and m separated by a space.

- 1 ≤ n ≤ 100000
- 1 ≤ m ≤ min{(n+1)2, 500000}

**Output:**
Your program should print the value of the edge connectivity in the output.

**Example:**

**Input 1:**
5 14
3 4
1 3
3 5
1 2
1 4
2 5
2 4
3 5
2 4
2 3
1 4
2 5
4 5
1 2


**Output 1:**
0

# Q3 

## The dual graph

The dual graph of graph G is a graph with one vertex for each region of graph G. Between two vertices in the dual graph, there is an edge if the two regions of graph G are separated by one edge; thus, for each edge e of graph G, there is an edge in the dual graph that connects the regions on either side of edge e.

In this question, the input is the graph G, and we want to find its dual.

For naming the vertices of the dual graph, we proceed as follows: each region is examined to which vertices it is bounded, and the first English character of the region is selected as the name of that vertex. For example, if the region bounded by vertices a, b, c, d, the name a is selected as the name of that vertex.

If a has been selected before, the number 1 is selected instead of it for naming the vertex.

If a is selected as the name of the vertices of the dual graph three times, the first time a, the second time 1, and the third time 2 are selected as the name of that vertex, and so on.

The region outside the graph is displayed in the dual with the name of the vertex x.

The graph does not include multiple edges.

**Input:**
The input consists of the vertices of graph G in the first line, followed by the edges of the graph in the next lines.

**Output:**
The output consists of the vertices of the dual graph in the first line, followed by the edges of the graph in the next lines.

The order of the edges in the output is such that the edges containing numbers come first (the smaller number comes first), and then the edges containing only letters come (the letter that appears earlier in the alphabet comes first).

**Example:**

**Input 1:**
abc
ab
ac
bc



**Output 1:**
ax
ax


Explanation: The vertices of the graph are a, b, c, and the edges are ab, ac, bc. The vertex bounded by abc is named a, and the vertex outside the graph is named x. Only one edge exists, so it appears in the second line, starting with a and then x.

**Input 2:**
abcde
ab
ac
cd
bd
ae
ec



**Output 2:**
ax1
a1
x1
ax


Explanation: The vertex bounded by aec is named a, and the vertex bounded by abcd is named 1. In each line, the English characters come first, followed by the numbers, and the English characters that appear earlier in the alphabet are displayed first. There is only one edge, so it appears in the second line, starting with a and then x.

# Q4

## Revolutionary Country (Optional)


The map of Saayeen's country consists of n cities connected by m roads. Saayeen, who fears the revolutionaries taking over much of the country, wants to investigate the resistance of the map to partitioning. We say the country is susceptible to partitioning if there is a road such that by removing it, all cities of a region are occupied by the insurgents. Among all 2^(2n) ways that the insurgents can occupy some cities, we want to know the number of ways in which the country is not susceptible to partitioning.

Print the remainder of this number by 10^9 + 7.

**Input:**
The first line of input contains two natural numbers n and m separated by a space. In the next m lines, each line contains two natural numbers indicating two cities connected by a road.

1 ≤ n ≤ 100000
1 ≤ m ≤ 300000

It is guaranteed that from each city, it is possible to travel to any other city using the roads. Also, no road connects a city to itself, and there is at most one road between any two cities.

**Output:**
Print the remainder of the number of ways that the country is not susceptible to partitioning by 10^9 + 7.

**Example:**

**Input 1:**
3 2
1 2
2 3


**Output 1:**
2


**Explanation 1:**
In this image, we see two cases where the country is not susceptible to partitioning.

**Input 2:**
4 4
1 2
2 3
3 1
1 4


**Output 2:**
7