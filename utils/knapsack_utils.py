import random

def knapsack_value(solution, items, capacity):
    total_w = sum(items[i][1] for i in range(len(solution)) if solution[i])
    if total_w > capacity:
        return 0
    return sum(items[i][0] for i in range(len(solution)) if solution[i])

def random_solution(n_items):
    return [random.choice([0, 1]) for _ in range(n_items)]

def generate_random_items(n_items, max_value=50, max_weight=20):
    return [(random.randint(1, max_value), random.randint(1, max_weight)) for _ in range(n_items)]