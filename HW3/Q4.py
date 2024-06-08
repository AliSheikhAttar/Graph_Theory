def dfs(node, visited, adjacency_list):
    visited[node] = True
    group_size = 1
    for neighbor in adjacency_list[node]:
        if not visited[neighbor]:
            group_size += dfs(neighbor, visited, adjacency_list)
    return group_size

def main():
    n, m = map(int, input().split())
    adjacency_list = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    visited = [False] * (n+1)
    result = 1
    MOD = 10**9 + 7
    for i in range(1, n+1):
        if not visited[i]:
            group_size = dfs(i, visited, adjacency_list)
            if group_size > 1:  # Only modify result if group size is greater than 1
                result *= (pow(2, group_size, MOD) - 1) % MOD
                result %= MOD

    print((result + MOD - 1) % MOD)

if __name__ == "__main__":
    main()
