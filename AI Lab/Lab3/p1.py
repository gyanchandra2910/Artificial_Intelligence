import heapq
Graph = {
    "A" : [("B", 12), ("D", 19), ("E", 8), ("C", 10)],
    "B" : [("A", 12), ("C", 3), ("E", 6), ("D", 7)],
    "C" : [("A", 10), ("B", 3), ("D", 2), ("E", 20)], 
    "D" : [("B", 7), ("A", 19), ("C", 2), ("E", 4)],
    "E" : [("D", 4), ("B", 6), ("A", 8), ("C", 20)]
}

def distance_to_nearest_unvisited(current_node, visited):
    nearest_dist = 1e9
    found = False
    for neighbor, weight in Graph[current_node]:
        if neighbor not in visited:
            if weight < nearest_dist:
                nearest_dist = weight
                found = True
    return nearest_dist if found else 0

def MST_cost(visited):
    unvisited_nodes = [n for n in Graph.keys() if n not in visited]
    if len(unvisited_nodes) < 2:
        return 0
    
    mst_cost = 0
    nodes_in_mst = set()
    nodes_in_mst.add(unvisited_nodes[0]) 
    
    while len(nodes_in_mst) < len(unvisited_nodes):
        min_edge = 1e9
        next_node = None
        
        
        for u in nodes_in_mst:
            for v, weight in Graph[u]:
                if v in unvisited_nodes and v not in nodes_in_mst:
                    if weight < min_edge:
                        min_edge = weight
                        next_node = v
        if next_node:
            mst_cost += min_edge
            nodes_in_mst.add(next_node)
        else:
            break 
    return mst_cost

def distance_from_unvisited_to_start(visited, start_node):
    nearest_dist = 1e9
    found = False
    
    for node in Graph.keys():
        if node not in visited:
            for neighbor, weight in Graph[node]:
                if neighbor == start_node:
                    if weight < nearest_dist:
                        nearest_dist = weight
                        found = True
    return nearest_dist if found else 0

start_node = "A"
queue = []

initial_h = distance_to_nearest_unvisited("A", {start_node}) + MST_cost({start_node}) + distance_from_unvisited_to_start({start_node}, start_node)
heapq.heappush(queue, (initial_h, start_node, 0, [start_node], {start_node}))

while queue:
    f, current_node, g, path, visited = heapq.heappop(queue)
    
    if len(visited) == len(Graph):
        for neighbor, weight in Graph[current_node]:
            if neighbor == start_node:
                total_cost = g + weight
                final_path = path + [start_node]
                print("Final Path:", final_path)
                print("Total Cost:", total_cost)
                exit() 

    for neighbor, weight in Graph[current_node]:
        if neighbor not in visited:
            new_g = g + weight
            new_path = path + [neighbor]
            new_visited = visited.copy()
            new_visited.add(neighbor)
            
            # 1. Dist to nearest unvisited (from neighbor)
            h1 = distance_to_nearest_unvisited(neighbor, new_visited)
            # 2. MST of remaining unvisited
            h2 = MST_cost(new_visited)
            # 3. Dist from unvisited back to Start
            h3 = distance_from_unvisited_to_start(new_visited, start_node)
            
            h = h1 + h2 + h3
            new_f = new_g + h
            
            heapq.heappush(queue, (new_f, neighbor, new_g, new_path, new_visited))
            