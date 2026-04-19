# TC = O(V * E)
V = ["A","B","C","D","E","F","G","H"]

edges = [
    ("A","B",4), ("A","C",10), ("A","H",5),
    ("B","C",11), ("B","D",15),
    ("C","D",13),
    ("D","E",6), ("D","F",5),
    ("E","F",2), ("E","G",5),
    ("F","G",8),
    ("G","H",7)
]

def bellman_ford(source):
    dist = {}
    parent = {}

    for v in V:
        dist[v] = 999999
        parent[v] = None

    dist[source] = 0

    for i in range(len(V) - 1):
        for (u, v, w) in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    return dist, parent

def print_path(parent, dest):
    path = []
    while dest is not None:
        path.append(dest)
        dest = parent[dest]
    path.reverse()
    return path

source = "A"
dist, parent = bellman_ford(source)

print("Source:", source)

for v in V:
    if v != source:
        path = print_path(parent, v)
        print(v, ":", path, "Cost =", dist[v])
