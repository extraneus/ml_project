adj_list = {
    'A': ['B', 'D'],
    'B': ['C'],
    'C': [],
    'D': ['E', 'F'],
    'E': ['F', 'G'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

visited = {}
rec_stack = {}
has_cycle = False
dfs_traversal_output = []

for node in adj_list:
    visited[node] = False
    rec_stack[node] = False

def dfs_directed(u):
    global has_cycle
    visited[u] = True
    rec_stack[u] = True
    dfs_traversal_output.append(u)

    for neighbor in adj_list[u]:
        if not visited[neighbor]:
            dfs_directed(neighbor)
        elif rec_stack[neighbor]:
            # Cycle found!
            has_cycle = True

    rec_stack[u] = False

# To make sure we catch cycles in disconnected components too:
for node in adj_list:
    if not visited[node]:
        dfs_directed(node)

print("DFS Traversal Output:", dfs_traversal_output)
print("The directed graph contains a cycle." if has_cycle else "The directed graph does not contain a cycle.")
