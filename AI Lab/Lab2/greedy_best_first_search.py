import heapq

heuristic = {
    "A" : 8,
    "B" : 6,
    "C" : 5,
    "D" : 3,
    "E" : 2,
    "F" : 1,
    "G" : 0,
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
heapq.heappush(queue, (heuristic['A'], 'A', ['A'], 0))
visited = set()

while queue:
    h, current , path, cost = heapq.heappop(queue)
    
    if current in visited:
        continue
    visited.add(current)
    
    if current == "G":
        print("The total cost is ", cost)
        print("The path is ", path)
        break
        
        
    for neighbour, weight in graph[current]:
        if neighbour not in visited:
            new_wt = cost + weight
            heapq.heappush(queue, (heuristic[neighbour], neighbour, path + [neighbour], new_wt))
    

