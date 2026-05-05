import random
from .greedy import total_distance
from .local_search import knapsack_value_weight

# -------------------- GENETIC POUR TSP --------------------
def create_population_tsp(pop_size, n_cities):
    return [random.sample(range(n_cities), n_cities) for _ in range(pop_size)]

def order_crossover(p1, p2):
    size = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end+1] = p1[start:end+1]
    pos = 0
    for gene in p2:
        if gene not in child:
            while child[pos] is not None:
                pos += 1
            child[pos] = gene
    return child

def mutate_swap(tour, prob=0.02):
    if random.random() < prob:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_tsp(cities, pop_size=100, generations=500, mutation_prob=0.02):
    n = len(cities)
    pop = create_population_tsp(pop_size, n)
    for _ in range(generations):
        pop = sorted(pop, key=lambda t: total_distance(t, cities))
        new_pop = pop[:2]
        while len(new_pop) < pop_size:
            p1, p2 = random.choices(pop[:pop_size//2], k=2)
            child = order_crossover(p1, p2)
            child = mutate_swap(child, mutation_prob)
            new_pop.append(child)
        pop = new_pop
    return min(pop, key=lambda t: total_distance(t, cities))

# -------------------- GENETIC POUR KNAPSACK --------------------
def create_population_knapsack(pop_size, n_items):
    return [[random.randint(0,1) for _ in range(n_items)] for _ in range(pop_size)]

def crossover_knapsack(p1, p2):
    point = random.randint(1, len(p1)-1)
    return p1[:point] + p2[point:]

def mutate_knapsack(solution, prob=0.05):
    for i in range(len(solution)):
        if random.random() < prob:
            solution[i] = 1 - solution[i]
    return solution

def genetic_knapsack(items, capacity, pop_size=100, generations=200, mutation_prob=0.05):
    n = len(items)
    pop = create_population_knapsack(pop_size, n)
    for _ in range(generations):
        pop = sorted(pop, key=lambda sol: knapsack_value_weight(sol, items, capacity)[0], reverse=True)
        new_pop = pop[:2]
        while len(new_pop) < pop_size:
            p1, p2 = random.choices(pop[:pop_size//2], k=2)
            child = crossover_knapsack(p1, p2)
            child = mutate_knapsack(child, mutation_prob)
            new_pop.append(child)
        pop = new_pop
    return max(pop, key=lambda sol: knapsack_value_weight(sol, items, capacity)[0])