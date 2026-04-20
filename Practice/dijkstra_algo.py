import heapq

vertex = ["A", "B", "C", "D", "E", "F", "G", "H"]

# ERROR CORRECTED: Added "C" so that graph[node] doesn't give KeyError
graph = {
    "A" : [("B", 4), ("C", 10)],
    "B" : [("A", 4), ("C", 11)],
    "C" : [("A", 10), ("B", 11)] 
}

def dijkstra(start_node):
    parent = {}
    dist = {}
    for v in vertex:
        parent[v] = None
        dist[v] = 1e9
        
    dist[start_node] = 0 # ERROR CORRECTED: Starting distance must be 0
    
    pq = []
    heapq.heappush(pq, (0, start_node))

    while len(pq) > 0:
        d, node = heapq.heappop(pq) # ERROR CORRECTED: Passed 'pq' inside heappop

        # Safety check agar koi node graph dictionary mein nahi hai
        if node not in graph:
            continue

        for n_node, val in graph[node]:
            if (d + val < dist[n_node]):
                parent[n_node] = node
                dist[n_node] = d + val
                
                # ERROR CORRECTED: Passed 'pq' and dist[n_node] instead of full dist dict
                heapq.heappush(pq, (dist[n_node], n_node)) 

    return parent, dist

def res_path(parent, dest):
    path = []
    while dest != None:
        path.append(dest)
        dest = parent[dest]

    path.reverse()
    return path


parent, dist = dijkstra("A")
ans = res_path(parent, "C")

print("Path to C :", ans)
print("Total Cost:", dist["C"])



def dijstra (startNode):
    dist = {}
    parent = None

    for v in vertex:
        parent[v] = None
        dist[v] = 1e9

    pq = []
    heapq.heappush(pq, (0, startNode, path))

    while len(pq) > 0:

        cost, node, path = heapq.heappop()

        for neighbour, wt in graph[node]:
            if cost + wt < dist[neighbour]:
                dist[neighbour] = cost + wt
                parent[neighbour] = node
                 