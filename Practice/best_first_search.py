import heapq

heuristic = {
  "A" : 8,
  "B" : 6,
  "C" : 5,
  "D" : 3, 
}

# Graph mein C aur D ko bhi khali list de do, taaki KeyError na aaye
graph =  {
  "A" : [("B", 6), ("C", 3)],
  "B" : [("A", 6), ("D", 2)],
  "C" : [], # C aage kahin nahi jata
  "D" : []  # D hamara goal hai
}

visited = set()

pq = []
heapq.heappush(pq, (heuristic["A"], "A", ["A"], 0))
# ERROR 1 FIXED: visited["A"] hata diya, loop khud add kar lega

while len(pq) > 0:
  heu, node, path, cost = heapq.heappop(pq)

  # ERROR 3 FIXED: Asli Visited Logic (Agar pehle ja chuke toh skip maaro)
  if node in visited:
      continue
  visited.add(node)

  # ERROR 5 FIXED: Goal "D" kar diya kyunki G list mein nahi hai
  if node == "D":
    print("Path:", path)
    print("Cost:", cost)
    break
  
  # ERROR 4 FIXED: Ab KeyError nahi aayega kyunki graph poora hai
  for near_node, val in graph[node]:
    if near_node not in visited: # Padosi ko pehle check kar lo
        wt = cost + val
        # ERROR 2 FIXED: path + [near_node] kiya (List + List)
        heapq.heappush(pq, (heuristic[near_node], near_node, path + [near_node], wt))