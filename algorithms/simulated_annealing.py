import math
import random
from .greedy import total_distance
from .local_search import two_opt_swap, knapsack_value_weight

# -------------------- SIMULATED ANNEALING POUR TSP --------------------
def simulated_annealing_tsp(cities, initial_tour, temp=1000, cooling=0.995, stopping_temp=0.1):
    tour = initial_tour[:]
    best_tour = tour[:]
    current_dist = total_distance(tour, cities)
    best_dist = current_dist
    
    while temp > stopping_temp:
        i, j = sorted(random.sample(range(len(tour)), 2))
        new_tour = two_opt_swap(tour, i, j)
        new_dist = total_distance(new_tour, cities)
        
        delta = current_dist - new_dist
        
        if delta > 0 or random.random() < math.exp(min(0, delta / temp)):
            tour = new_tour
            current_dist = new_dist
            if new_dist < best_dist:
                best_tour = tour[:]
                best_dist = new_dist
        
        temp *= cooling
    
    return best_tour

# -------------------- SIMULATED ANNEALING POUR KNAPSACK --------------------
def simulated_annealing_knapsack(items, capacity, initial_solution, temp=1000, cooling=0.995, stopping_temp=0.1):
    solution = initial_solution[:]
    best_sol = solution[:]
    current_val, current_w = knapsack_value_weight(solution, items, capacity)
    best_val = current_val
    
    while temp > stopping_temp:
        idx = random.randint(0, len(solution)-1)
        new_sol = solution[:]
        new_sol[idx] = 1 - new_sol[idx]
        new_val, new_w = knapsack_value_weight(new_sol, items, capacity)
        
        delta = new_val - current_val
        
        if delta > 0 or random.random() < math.exp(min(0, -delta / temp)):
            solution = new_sol
            current_val = new_val
            if new_val > best_val:
                best_sol = new_sol[:]
                best_val = new_val
        
        temp *= cooling
    
    return best_sol