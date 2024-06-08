 
from collections import defaultdict
 
class question:
    def __init__(self) -> None:
        self.inputing()

    def inputing(self):
        self.raw = [int(_) for _ in input().split()]
        self.assinging_values()
        self.save_edges()
    
    def assinging_values(self):
        self.n, self.e = self.raw[0], self.raw[1]
        self.edges = []

    def save_edges(self):
        if self.e != 0:
            for i in range(self.e):
                edge = [int(_) for _ in input().split()]
                if (edge[0], edge[1]) not in self.edges and (edge[1], edge[0]) not in self.edges and (edge[0] != edge[1]):
                    self.edges.append((edge[0], edge[1]))
# Python program to find bridges in a given undirected graph
#Complexity : O(V+E)

#This class represents an undirected graph using adjacency list representation

class Solution:
    def __init__(self, e=0, n=1, edges=[]):
        self.adjancy = defaultdict(list)
        self.e = e
        self.n = n
        self.Time = 0
        self.edges = edges
        self.visited = [False] * n
        self.answer = 0
        if (n == 0 or e==0 or n == 1):
            self.answer = 0
        else:
            self.build_adjacency_list()
            self.bridge()

    def build_adjacency_list(self):
        for edge in self.edges:
            self.adjancy[edge[0]-1].append(edge[1]-1)
            self.adjancy[edge[1]-1].append(edge[0]-1)

 
    '''A recursive function that finds and prints bridges
    using DFS traversal
    u --> The vertex to be visited next
    visited[] --> keeps track of visited vertices
    disc[] --> Stores discovery times of visited vertices
    parent[] --> Stores parent vertices in DFS tree'''
    def bridgeUtil(self,u, visited, parent, low, disc):

        # Mark the current node as visited and print it
        visited[u]= True

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        #Recur for all the vertices adjacent to this vertex
        for v in self.adjancy[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[v] == False :
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])


                ''' If the lowest vertex reachable from subtree
                under v is below u in DFS tree, then u-v is
                a bridge'''
                if low[v] > disc[u]:
                    # print ("%d %d" %(u,v))
                    self.answer +=1
    
                    
            elif v != parent[u]: # Update low value of u for parent function calls.
                low[u] = min(low[u], disc[v])


    # DFS based function to find all bridges. It uses recursive
    # function bridgeUtil()
    def bridge(self):
 
        # Mark all the vertices as not visited and Initialize parent and visited, 
        # and ap(articulation point) arrays
        visited = [False] * (self.n)
        disc = [float("Inf")] * (self.n)
        low = [float("Inf")] * (self.n)
        parent = [-1] * (self.n)

        # Call the recursive helper function to find bridges
        # in DFS tree rooted with vertex 'i'
        for i in range(self.n):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc)
        
 
# Create a graph given in the above diagram


#This code is contributed by Neelam Yadav

q = question()
n, e = q.n, q.e
edges = q.edges
ans = Solution(e,n, edges)
res = ans.answer
print(res)