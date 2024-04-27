
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        self.matchR = [-1] * self.ROW

    def bpm(self, u, seen, matchR):
        for v in range(self.ROW):
            if self.graph[u][v] and not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v], seen, matchR):
                    matchR[v] = u
                    return True
        return False

    def max_bpm(self):
        matchR = [-1] * self.ROW
        result = 0
        for i in range(self.ROW):
            seen = [False] * self.ROW
            if self.bpm(i, seen, matchR):
                result += 1
        return result


def create_adjacency_matrix(edges, num_nodes):
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for edge in edges:
        u, v = edge
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1
    return adjacency_matrix


edges_str = input()
edges_list = set()
nodes = {}
num_nodes = 0
for s in edges_str:
    if s not in nodes and s != ' ': 
        nodes[s] = num_nodes
        num_nodes += 1

i = 0
while(i < (len(edges_str)-1)):
    if( (edges_str[i+1] != ' ' and edges_str[i-1]!= ' ')              and
        (nodes[edges_str[i]],nodes[edges_str[i+1]]) not in edges_list and
        (nodes[edges_str[i+1]],nodes[edges_str[i]]) not in edges_list
    ):
        edges_list.add((nodes[edges_str[i]],nodes[edges_str[i+1]]))
    i+=2



adjacency_matrix = create_adjacency_matrix(edges_list, num_nodes)

g = Graph(adjacency_matrix)
max_matching = g.max_bpm()
print(int(max_matching/2))
