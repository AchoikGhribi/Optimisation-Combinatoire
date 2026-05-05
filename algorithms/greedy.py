import random
import math

# -------------------- FONCTIONS UTILES POUR TSP --------------------
def distance(city1, city2):
    """Calcule la distance Euclidienne entre deux villes"""
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

def total_distance(tour, cities):
    """Calcule la distance totale d'un tour TSP"""
    return sum(distance(cities[tour[i]], cities[tour[(i+1) % len(tour)]]) for i in range(len(tour)))

# -------------------- GREEDY POUR TSP --------------------
def greedy_tsp_deterministic(cities, start=0):
    n = len(cities)
    unvisited = set(range(n))
    tour = [start]
    unvisited.remove(start)
    while unvisited:
        last = tour[-1]
        nearest = min(unvisited, key=lambda city: distance(cities[last], cities[city]))
        tour.append(nearest)
        unvisited.remove(nearest)
    return tour

def greedy_tsp_nondeterministic(cities, start=None, k=3):
    n = len(cities)
    if start is None:
        start = random.randint(0, n-1)
    unvisited = set(range(n))
    tour = [start]
    unvisited.remove(start)
    while unvisited:
        last = tour[-1]
        candidates = sorted(unvisited, key=lambda city: distance(cities[last], cities[city]))[:k]
        chosen = random.choice(candidates)
        tour.append(chosen)
        unvisited.remove(chosen)
    return tour

# -------------------- GREEDY POUR KNAPSACK --------------------
def greedy_knapsack_deterministic(items, capacity):
    indexed = [(i, items[i][0]/items[i][1]) for i in range(len(items))]
    indexed.sort(key=lambda x: x[1], reverse=True)
    solution = [0] * len(items)
    current_w = 0
    for idx, _ in indexed:
        w = items[idx][1]
        if current_w + w <= capacity:
            solution[idx] = 1
            current_w += w
    return solution

def greedy_knapsack_nondeterministic(items, capacity, k=3):
    indexed = [(i, items[i][0]/items[i][1]) for i in range(len(items))]
    indexed.sort(key=lambda x: x[1], reverse=True)
    top_k = indexed[:k]
    chosen_idx = random.choice(top_k)[0]
    solution = [0] * len(items)
    solution[chosen_idx] = 1
    current_w = items[chosen_idx][1]
    remaining = [i for i in range(len(items)) if i != chosen_idx]
    remaining.sort(key=lambda i: items[i][0]/items[i][1], reverse=True)
    for idx in remaining:
        w = items[idx][1]
        if current_w + w <= capacity:
            solution[idx] = 1
            current_w += w
    return solution