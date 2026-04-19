import heapq

heuristic = {
    "A" : 80, "B" : 0, "C" : 50, "D" : 70,
    "E" : 40, "F" : 0, "G" : 60,
}

graph = {
    "A" : [("B",6), ("C", 3)],
    "B" : [("A", 6), ("D", 2)],
    "C" : [("A", 3), ("D", 4),("E",7)],
    "D" : [("B", 2), ("C", 4), ("E", 1),("F", 5)],
    "E" : [("C", 7), ("D", 1), ("F", 2)],
    "F" : [("D", 5), ("E", 2), ("G", 3)],
    "G" : [("F", 3)],
}

pq = []
visited = set()

heapq.heappush(pq, (0, "B", ["B"], 0))

while len(pq) > 0:
    heur, node, path, cost = heapq.heappop(pq)

    if node in visited:
        continue
    visited.add(node)

    if node == "F":
        print("Total Cost:", cost)
        print("Path:", path)
        break   # ERROR 3 FIXED: Yahan break lagana zaroori hai
  
    for neigh, wt in graph[node]:
        if neigh not in visited: # Pro-tip: Visited check yahan bhi kar liya kar
            # new_heu asal mein tera f(n) = g(n) + h(n) hai
            new_heu = (cost + wt) + heuristic[neigh] 
            
            # ERRORS 1 & 2 FIXED: Naya heuristic (new_heu) aur Padosi (neigh) daala!
            heapq.heappush(pq, (new_heu, neigh, path + [neigh], cost + wt))