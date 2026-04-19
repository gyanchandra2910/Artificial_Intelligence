vertex = ["A", "B", "C", "D"]
edges = [("A", "B", 4), ("B", "D", 15)]

def bellman(start_node):
    dist = {}
    parent = {}

    for v in vertex:
        # ERROR CORRECTED: 'vertex' ki jagah 'v' aayega
        dist[v] = 1e9
        parent[v] = None

    dist[start_node] = 0

    for i in range(len(vertex) - 1):
        for (u, v, w) in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
      
    return dist, parent

def print_path(parent, end_node):
    path = []
    while end_node != None:
        path.append(end_node)
        end_node = parent[end_node]

    # ERROR CORRECTED: Raasta seedha karne ke liye reverse karna zaroori hai
    path.reverse()
    return path

dist, parent = bellman("A")
path = print_path(parent, "D")

print("Path to D:", path)
print("Cost:", dist["D"])