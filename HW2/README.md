# Q1
## Bipartite graph

We have a graph G and we don't know if it's bipartite or not!

To define graph G, we are given a sequence of letters as input, where each pair of adjacent letters represents an edge. For example, if "abcd" is given as input, it means we have edges from vertex a to b and from c to d.

However, if we want, for example, vertex d to be an isolated vertex in this graph, we separate it from the rest of the vertices with a space. So "abc d" means we go from vertex a to b, from b to c, and vertex d is isolated.

What we want to do is, if the graph is not bipartite, convert it to bipartite by deleting the minimum number of edges, and then print the number of remaining edges as output. {If it's bipartite, calculate the number of complementary edges and print it as output}

**Example:**

**Input 1:**
abacdedfsopwkslskc

**Output 1:**
57

**Input 2:**
kjhgfyfhjklkohufyykpjhgyfhjkphitdyjkpjogyfjkjhgfdfghkljhhgfg

**Output 2:**
14

**Input 3:**
abacbcbebddeegeffgghhigiijkjkljllnlmmnnpnopororqoqqtsqstsuuvuwvwwxwyxyzx

**Output 3:**
25


# Q2

## Maximum matching

We know that a matching can have one of the following three forms:

- **Maximal Matching:** A matching that is not a subset of any other matching.
- **Maximum Matching:** A matching that has the maximum possible number of edges.
- **Perfect Matching:** A matching that covers all the vertices.

Now, suppose the input is as in the previous question. Output the number of edges in the maximum matching.

**Example:**

**Input 1:**
abacbcbebddeegeffgghhigiijkjkljllnlmmnnpnopororqoqqtsqstsuuvuwvwwxwyxyzx

**Output 1:**
13


**Input 2:**
abacdedfsopwkslskc

**Output 2:**
5