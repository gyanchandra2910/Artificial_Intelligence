import random


graph = {
    'A': {'B': 12, 'C': 10, 'D': 19, 'E': 8},
    'B': {'A': 12, 'C': 3,  'D': 7,  'E': 6},
    'C': {'A': 10, 'B': 3,  'D': 2,  'E': 20},
    'D': {'A': 19, 'B': 7,  'C': 2,  'E': 4},
    'E': {'A': 8,  'B': 6,  'C': 20, 'D': 4}
}

# we are creating intermediate cities
cities = ['B', 'C', 'D', 'E']


#we are finding the cost of given route
def get_route_cost(route):
    cost = graph['A'][route[0]]
    for i in range(len(route)- 1):
        cost = cost + graph[route[i]][route[i + 1]]
        
    cost = cost + graph[route[-1]]['A']
    return cost


# we are creatign random 4 population in beginning by shuffling the 4 intermediate cities 
def create_population(size = 4):
    population = []
    for i in range(4):
        city = list(cities)
        random.shuffle(city)
        population.append(city)
    
    return population 


# we are crossovering the parent1 and parent2 in such a way that the same city is not in child twice
def crossover(parent1 , parent2):
    child = [parent1[0], parent1[1]]
    
    for city in parent2:
        if city not in child:
            child.append(city)
        
    return child


# we are mutating the route by swapping any two nodes in the route
def mutate(route):
    mutate_route = list(route)
    idx1, idx2 = random.sample(range(4), 2)

    temp = mutate_route[idx1]
    mutate_route[idx1] = mutate_route[idx2]
    mutate_route[idx2] = temp
    
    return mutate_route
    
# Here we have finally implemented genetic algo 
def genetic_algo():
    population = create_population(4)
    
    for i in range(30):
        population.sort(key = get_route_cost)
        
        best_par1 = population[0]
        best_par2 = population[1]
        new_child = crossover(best_par1, best_par2)
        child_after_mutation = mutate(new_child)
        
        population = [best_par1, best_par2, new_child, child_after_mutation]
        
        cur_best_route = get_route_cost(best_par1)
        print("For the iteration ", i , "The route is A->", best_par1[0], "->", best_par1[1], "->",
            best_par1[2],"->" ,best_par1[3], "with cost", cur_best_route)
        print("\n")
        

    population.sort(key=get_route_cost)
    opti_route = population[0]
    opti_cost = get_route_cost(opti_route)
    
    print("\n")
    print("For the last iteration ", "The route is A->", opti_route[0], "->", opti_route[1], "->",
            opti_route[2],"->" ,opti_route[3], "with cost", opti_cost)
    print(f"Minimum Cost  : {opti_cost}")


genetic_algo()










