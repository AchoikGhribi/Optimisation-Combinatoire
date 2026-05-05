import random
from .greedy import total_distance

# -------------------- LOCAL SEARCH POUR TSP --------------------
def two_opt_swap(tour, i, j):
    return tour[:i] + tour[i:j+1][::-1] + tour[j+1:]

def first_improvement_tsp(cities, initial_tour):
    tour = initial_tour[:]
    n = len(tour)
    improved = True
    while improved:
        improved = False
        for i in range(n-1):
            for j in range(i+1, n):
                new_tour = two_opt_swap(tour, i, j)
                if total_distance(new_tour, cities) < total_distance(tour, cities):
                    tour = new_tour
                    improved = True
                    break
            if improved:
                break
    return tour

def best_improvement_tsp(cities, initial_tour):
    tour = initial_tour[:]
    improved = True
    while improved:
        improved = False
        best_tour = tour
        best_dist = total_distance(tour, cities)
        for i in range(len(tour)-1):
            for j in range(i+1, len(tour)):
                new_tour = two_opt_swap(tour, i, j)
                new_dist = total_distance(new_tour, cities)
                if new_dist < best_dist:
                    best_dist = new_dist
                    best_tour = new_tour
                    improved = True
        tour = best_tour
    return tour

# -------------------- LOCAL SEARCH POUR KNAPSACK --------------------
def knapsack_value_weight(solution, items, capacity):
    total_v = 0
    total_w = 0
    for i, selected in enumerate(solution):
        if selected:
            total_v += items[i][0]
            total_w += items[i][1]
    return (total_v, total_w) if total_w <= capacity else (0, total_w)

def first_improvement_knapsack(items, capacity, initial_solution):
    solution = initial_solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(len(solution)):
            new_sol = solution[:]
            new_sol[i] = 1 - new_sol[i]
            new_value, _ = knapsack_value_weight(new_sol, items, capacity)
            old_value, _ = knapsack_value_weight(solution, items, capacity)
            if new_value > old_value:
                solution = new_sol
                improved = True
                break
    return solution

def best_improvement_knapsack(items, capacity, initial_solution):
    solution = initial_solution[:]
    improved = True
    while improved:
        improved = False
        best_sol = solution
        best_val, _ = knapsack_value_weight(solution, items, capacity)
        for i in range(len(solution)):
            new_sol = solution[:]
            new_sol[i] = 1 - new_sol[i]
            new_val, _ = knapsack_value_weight(new_sol, items, capacity)
            if new_val > best_val:
                best_val = new_val
                best_sol = new_sol
                improved = True
        solution = best_sol
    return solution