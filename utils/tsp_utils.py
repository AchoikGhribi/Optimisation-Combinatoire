import random
import math

def distance(city1, city2):
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

def total_distance(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[(i+1) % len(tour)]]) for i in range(len(tour)))

def random_tour(n):
    tour = list(range(n))
    random.shuffle(tour)
    return tour

def generate_random_cities(n_cities, width=100, height=100):
    return [(random.uniform(0, width), random.uniform(0, height)) for _ in range(n_cities)]