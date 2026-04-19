# TC : O((V + E)logV)
v = {"A","B","C","D","E","F","G","H"}

graph = {
    "A" : [("B",4),("C",10),("H",5)],
    "B" : [("A",4),("C",11),("D",15)],
    "C" : [("A",10),("B",11),("D",13)],
    "D" : [("B",15),("C",13),("E",6),("F",5)],
    "E" : [("C",3),("D",6),("F",2),("G",5)],
    "F" : [("D",5),("E",2),("G",8)],
    "G" : [("F",8),("E",5),("H",7)],
    "H" : [("A",5),("C",11),("G",7)],
}

import heapq
def dijkstra(source):
    
    dist = {}
    parent = {}
    for vertex in v:
        dist[vertex] = 999999
        parent[vertex] = None
    
    dist[source] = 0
    pq =[]
    heapq.heappush(pq,(0,source))
    while len(pq) > 0:
        cur_wt , u = heapq.heappop(pq)
        
        if cur_wt > dist[u]:
            continue
        
        for edge in graph[u]:
            neighbour = edge[0]
            wt = edge[1]
            if dist[u] + wt < dist[neighbour]:
                dist[neighbour] = dist[u]  + wt
                parent[neighbour] = u
                heapq.heappush(pq,(dist[neighbour], neighbour))
                
                
    return dist, parent


def print_path(parent, dest):
    path = []
    while dest is not None:
        path.append(dest)
        dest = parent[dest]
        
    path.reverse()
    return path
    


source = "A"
dist, parent = dijkstra(source)

print("Source vertex : ", source)
print()

for vertex in sorted(v):
    if vertex != source :
        path = print_path(parent, vertex)
        print("Shortest path to", vertex ," : ", end = " ")
        for i in range(len(path)):
            print(path[i], end = "")
            if i != len(path) - 1:
                print(" - > ", end = "")
            
        print(" | cost =", dist[vertex])
            















                
        
        