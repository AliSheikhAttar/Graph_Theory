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
        if self.e != 0 and self.n != 0:
            for i in range(self.e):
                edge = [int(_) for _ in input().split()]
                self.edges.append((edge[0], edge[1]))


class Solution:
    def __init__(self, e=0, n=1, edges=[]):
        self.adjacency = defaultdict(list)
        self.e = e
        self.n = n
        self.edges = edges
        self.visited = [False] * n
        self.answer = ""
        if n == 1:
            self.answer = "YES"
        elif n == 0 or (e == 0 and n != 1):
            self.answer = "NO"
        else:
            self.build_adjacency_list()
            if self.answer == "":
                if n > len(self.adjacency):
                    self.answer = False  # not connected
                else:
                    self.answer = self.check_graph() 

    def build_adjacency_list(self):
        for edge in self.edges:
            self.adjacency[edge[0]-1].append(edge[1]-1)
            self.adjacency[edge[1]-1].append(edge[0]-1)

    def check_graph(self):
        start_index = 0
        self.dfs(start_index)

        for visited in self.visited:
            if not visited:
                return False
        return self.is_eulerian()

    def dfs(self, start):
        stack = [start]
        self.visited[start] = True

        while stack:
            node = stack.pop()
            neighbours_list = self.adjacency[node]

            for neighbour in neighbours_list:
                if not self.visited[neighbour]:
                    stack.append(neighbour)
                    self.visited[neighbour] = True

    def is_eulerian(self):
        odd_vertex_counter = 0
        for i in range(self.n):
            if len(self.adjacency[i]) % 2 == 1:
                odd_vertex_counter += 1
                if odd_vertex_counter > 2:
                    return False
        return odd_vertex_counter == 0 or odd_vertex_counter == 2


q = question()
n, e = q.n, q.e
edges = q.edges
ans = Solution(e, n, edges)
res = ans.answer
if type(res) == bool:
    print("YES") if res else print("NO")
else:
    print(res)
