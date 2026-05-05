import random
from utils.tsp_utils import generate_random_cities, total_distance, random_tour
from utils.knapsack_utils import generate_random_items, knapsack_value, random_solution
from algorithms.greedy import greedy_tsp_deterministic, greedy_tsp_nondeterministic
from algorithms.greedy import greedy_knapsack_deterministic, greedy_knapsack_nondeterministic
from algorithms.local_search import first_improvement_tsp, best_improvement_tsp
from algorithms.local_search import first_improvement_knapsack, best_improvement_knapsack
from algorithms.simulated_annealing import simulated_annealing_tsp, simulated_annealing_knapsack
from algorithms.genetic import genetic_tsp, genetic_knapsack

def print_separator(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def run_tsp():
    print_separator("TRAVELING SALESMAN PROBLEM (TSP)")
    n_cities = 15
    cities = generate_random_cities(n_cities)
    print(f"Nombre de villes: {n_cities}")
    
    print("\n--- GREEDY ALGORITHM ---")
    greedy_det = greedy_tsp_deterministic(cities)
    greedy_rand = greedy_tsp_nondeterministic(cities)
    print(f"  Deterministic: {total_distance(greedy_det, cities):.2f}")
    print(f"  Nondeterministic: {total_distance(greedy_rand, cities):.2f}")
    
    print("\n--- LOCAL SEARCH ---")
    init_tour = random_tour(n_cities)
    ls_first = first_improvement_tsp(cities, init_tour)
    ls_best = best_improvement_tsp(cities, init_tour)
    print(f"  First Improvement: {total_distance(ls_first, cities):.2f}")
    print(f"  Best Improvement: {total_distance(ls_best, cities):.2f}")
    
    print("\n--- SIMULATED ANNEALING ---")
    sa_tour = simulated_annealing_tsp(cities, init_tour)
    print(f"  Distance: {total_distance(sa_tour, cities):.2f}")
    
    print("\n--- GENETIC ALGORITHM ---")
    ga_tour = genetic_tsp(cities, pop_size=50, generations=200)
    print(f"  Distance: {total_distance(ga_tour, cities):.2f}")

def run_knapsack():
    print_separator("KNAPSACK PROBLEM")
    n_items = 10
    items = generate_random_items(n_items)
    capacity = sum(w for _, w in items) // 2
    print(f"Nombre d'objets: {n_items}")
    print(f"Capacite: {capacity}")
    
    print("\n--- GREEDY ALGORITHM ---")
    greedy_det = greedy_knapsack_deterministic(items, capacity)
    greedy_rand = greedy_knapsack_nondeterministic(items, capacity)
    print(f"  Deterministic: {knapsack_value(greedy_det, items, capacity)}")
    print(f"  Nondeterministic: {knapsack_value(greedy_rand, items, capacity)}")
    
    print("\n--- LOCAL SEARCH ---")
    init_sol = random_solution(n_items)
    ls_first = first_improvement_knapsack(items, capacity, init_sol)
    ls_best = best_improvement_knapsack(items, capacity, init_sol)
    print(f"  First Improvement: {knapsack_value(ls_first, items, capacity)}")
    print(f"  Best Improvement: {knapsack_value(ls_best, items, capacity)}")
    
    print("\n--- SIMULATED ANNEALING ---")
    sa_sol = simulated_annealing_knapsack(items, capacity, init_sol)
    print(f"  Value: {knapsack_value(sa_sol, items, capacity)}")
    
    print("\n--- GENETIC ALGORITHM ---")
    ga_sol = genetic_knapsack(items, capacity, pop_size=50, generations=100)
    print(f"  Value: {knapsack_value(ga_sol, items, capacity)}")

if __name__ == "__main__":
    random.seed(42)
    run_tsp()
    run_knapsack()
    print("\n" + "="*60)
    print("  Projet termine avec succes!")
    print("="*60)