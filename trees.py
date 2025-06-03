n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 5]]

M = []

for i in range(n):
    M.append([0] * n)
    # print("\n".join(M))

for u, v in A:
    M[u][v] = 1  # Undirected graph // There is no <-> between vertices

    # M[v][u] = 1 #basically add this if need to have <-> between vertices
print(M[3])
print(M)


# Convert array of edges to adjancency list /// HELPS LOOKUP FASTER ON THE CONNECTED VERTICES/NODES ON THE GIVEN VERTEX/NODE
from collections import defaultdict

D = defaultdict(list)
for u, v in A:
    D[u].append(v)
    # D[v].append(u) # <-- add if undirected
print(D[3])  # <-- faster lookup


# DFS with recursion O(V + E)


def dfs_recurs(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)  # <-- add to seen set to list kung ano na yung nakita
            dfs_recurs(nei_node)  # <-- recursion back to next neighbour


source = 0  # starting point
seen = set()
seen.add(source)
dfs_recurs(source)


# Iterative DFS with stack

source = 0  # starting point
seen = set()
seen.add(source)
stack = [source]  # <--- starting stack

while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)

# BFS with queue

source = 0

from collections import deque

seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)
