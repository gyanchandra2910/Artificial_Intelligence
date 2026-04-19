import heapq

heuristic = {
    "A" : 80,
    "B" : 0,
    "C" : 50,
    "D" : 70,
    "E" : 40,
    "F" : 0,
    "G" : 60,
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

# start_node = "A"
queue = []
# Push format: (SORTING_KEY, Node, Path, BOOKKEEPING_VALUE)
# Hum sirf 'heuristics' ko sorting key bana rahe hain.

heapq.heappush(queue, (0 , 'B', ['B'], 0))
visited = set()

while queue:
    h, current , path, cost = heapq.heappop(queue)
    
    if current in visited:
        continue
    visited.add(current)
    
    if current == "F":
        print("The total cost is ", cost)
        print("The path is ", path)
        break
        
        
    for neighbour, weight in graph[current]:
        if neighbour not in visited:
            new_g = cost + weight 
            new_f = new_g + heuristic[neighbour]
            heapq.heappush(queue, (new_f, neighbour, path + [neighbour], new_g))
    

