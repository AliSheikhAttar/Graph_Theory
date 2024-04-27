from collections import defaultdict

def dfs_cycle(u, p):
    global cyclenumber

    if color[u] == 2:
        return

    if color[u] == 1:
        v = []
        cur = p
        v.append(cur)

        while cur != u:
            cur = par[cur]
            v.append(cur)
        if(len(v)%2 == 1):
            cycles[cyclenumber] = v 
            cyclenumber += 1 
        return

    par[u] = p
    color[u] = 1

    for v in graph[u]:
        if v == par[u]:
            continue
        dfs_cycle(v, u)

    color[u] = 2

def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)

def minimum_cut_edges_to_remove_odd_cycles():
    dfs_cycle(0, 0)
    odd_cycles = cycles[:]
    new_cycles = []
    counter = 0
    for i in range(cyclenumber):
        new_cycles.append([(odd_cycles[i][j], odd_cycles[i][(j+1)%len(odd_cycles[i])]) for j in range(len(odd_cycles[i]))])

    odd_cycles = new_cycles
    while len(odd_cycles) > 0:
        edge_counter = defaultdict(int)
        deleted_cycles = []
        for cycle in odd_cycles:
            unique_edges = set()
            for i in range(len(cycle)):
                unique_edges.add(cycle[i])

            for edge in unique_edges:
                if (edge[1], edge[0]) in edge_counter:
                    edge_counter[(edge[1], edge[0])] += 1
                else:
                    edge_counter[edge] += 1
                
        most_common = max(edge_counter, key=edge_counter.get)
        new_cycles = []
        for i in range(len(odd_cycles)):
            if not((most_common in odd_cycles[i]) or ((most_common[1], most_common[0]) in odd_cycles[i])):
                new_cycles.append(odd_cycles[i])
        odd_cycles = new_cycles
        
        counter += 1

    return counter

if __name__ == "__main__":
    edges_str = input()
    edges_list = set()
    i = 0
    N = 100000

    graph = [[] for i in range(N)]
    cycles = [[] for i in range(N)]
    color = [0] * N
    par = [0] * N
    cyclenumber = 0
    min_cut_edges = 0
    nodes = {}
    num_nodes = 0
    num_edges = 0

    for s in edges_str:
        if s not in nodes and s != ' ': 
            nodes[s] = num_nodes
            num_nodes += 1

    i = 0
    while i < (len(edges_str)-1):
        if (edges_str[i+1] != ' ' and edges_str[i-1] != ' ' and
            (nodes[edges_str[i]], nodes[edges_str[i+1]]) not in edges_list and
            (nodes[edges_str[i+1]], nodes[edges_str[i]]) not in edges_list):
            if nodes[edges_str[i]] == nodes[edges_str[i+1]]:
                min_cut_edges += 1
            else:
                edges_list.add((nodes[edges_str[i]], nodes[edges_str[i+1]]))
                addEdge(nodes[edges_str[i]], nodes[edges_str[i+1]])
            num_edges += 1
        i += 2

    min_cut_edges += minimum_cut_edges_to_remove_odd_cycles()

    if min_cut_edges == 0:
        print(int(num_nodes * (num_nodes - 1) / 2 - len(edges_list)))
    else:
        print(num_edges - min_cut_edges)
