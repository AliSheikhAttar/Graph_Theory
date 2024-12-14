from collections import deque, defaultdict

def bfs4farthest(start, adj):

    farthest_node = start
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])


    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
                if dist[neighbor] > dist[farthest_node]:
                    farthest_node = neighbor

    return farthest_node, dist


def tree_diameter(n, edges):
    if n == 1:
        return 0
    
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    start_node = 1
    farthest_node0, _ = bfs4farthest(start_node, adj)
    
    farthest_node1, dist = bfs4farthest(farthest_node0, adj)
    
    return dist[farthest_node1]


n = int(input().strip())
edges = []
for _ in range(n - 1):
    minput = input()
    minput_clean = minput.strip().split()
    u, v = map(int, minput_clean)
    edges.append((u, v))

res = tree_diameter(n, edges)
print(res)

