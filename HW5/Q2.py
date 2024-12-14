from collections import deque

def bfs4farthest(start, n, adj):

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


def tree_center(n, edges):

    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    start = 1
    farthest_node, _ = bfs4farthest(start, n, adj)

    end_node, dist = bfs4farthest(farthest_node, n, adj)

    path = []
    node = end_node
    while node != -1:
        path.append(node)
        node = -1
        for neighbor in adj[path[-1]]:
            if dist[neighbor] == (dist[path[-1]] - 1):
                node = neighbor
                break

    path_length = len(path)
    if path_length % 2 == 1:
        center = path[path_length // 2]
    else:
        center = max(path[path_length // 2 - 1], path[path_length // 2])
    
    return center


n = int(input().strip())
edges = []
for _ in range(n - 1):
    minput = input()
    minput_clean = minput.strip().split()
    u, v = map(int, minput_clean)
    edges.append((u, v))

res = tree_center(n, edges)
print(res)
