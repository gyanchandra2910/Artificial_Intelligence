from itertools import permutations

# List of cities
cities = ["A","B","C","D","E","F","G","H"]

graph = {
    "A": {"B":4,"C":10,"H":5},
    "B": {"A":4,"C":11,"D":15},
    "C": {"A":10,"B":11,"D":13,"E":3,"H":11},
    "D": {"B":15,"C":13,"E":6,"F":5},
    "E": {"C":3,"D":6,"F":2,"G":5},
    "F": {"D":5,"E":2,"G":8},
    "G": {"F":8,"E":5,"H":7},
    "H": {"A":5,"C":11,"G":7}
}


for u in cities:
    for v in cities:
        if u != v and v not in graph[u]:
            graph[u][v] = 999999  


def tsp(start):
    other_cities = [c for c in cities if c != start]
    min_cost = float('inf')
    best_path = []

    for perm in permutations(other_cities):
        cost = 0
        path = [start] + list(perm) + [start]  
        for i in range(len(path)-1):
            cost += graph[path[i]][path[i+1]]
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return min_cost, best_path

start_city = "A"
cost, path = tsp(start_city)

print("Shortest TSP path:", path)
print("Minimum cost:", cost)
