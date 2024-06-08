def main():
  n, m = map(int, input().split())

  graph = [[] for _ in range(n)]
  for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  scc_ids = [-1] * n
  scc_count = 0
  dfs_low = [float('inf')] * n
  dfs_num = [0] * n
  tarjan(graph, scc_ids, scc_count, dfs_low, dfs_num, 0, -1)

  vulnerable_states = 0
  for i in range(n):
    for neighbor in graph[i]:
      if scc_ids[i] != scc_ids[neighbor]:
        vulnerable_states += 1
        break

  total_states = 1 << n
  safe_states = total_states - vulnerable_states
  remainder = safe_states % (10**9 + 7)
  print(remainder)
def is_vulnerable_scc(graph, scc_ids, n, current_scc, removed_edge):
  modified_graph = [vertex[:] for vertex in graph]
  modified_graph[removed_edge[0]].remove(removed_edge[1])
  modified_graph[removed_edge[1]].remove(removed_edge[0])

  scc_ids_modified = [-1] * n
  scc_count_modified = 0
  dfs_low_modified = [float('inf')] * n
  dfs_num_modified = [0] * n
  tarjan(modified_graph, scc_ids_modified, scc_count_modified, dfs_low_modified, dfs_num_modified, 0, -1)

  return scc_count_modified > scc_count or scc_ids[current_scc] != scc_ids_modified[current_scc]
