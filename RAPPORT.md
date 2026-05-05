# Rapport du Projet d'Optimisation Combinatoire

## Informations Générales

- **Matière** : Optimisation Combinatoire et Algorithmes
- **Master** : 1 Intelligence Artificielle
- **Année** : 2025/2026
- **Étudiant** : GHRIBI ACHOIK
- **Lien du code** : https://github.com/AchoikGhribi/Optimisation-Combinatoire

---

## 1. Objectif du Projet

Implémenter en Python les algorithmes d'optimisation combinatoire suivants pour résoudre deux problèmes classiques (TSP et Knapsack) :

1. Greedy (déterministe et non-déterministe)
2. Local Search (first-improvement et best-improvement)
3. Simulated Annealing (Recuit simulé)
4. Genetic Algorithm (Algorithme génétique)

---

## 2. Problèmes Traités

### 2.1 TSP (Traveling Salesman Problem)

Trouver le plus court chemin qui visite toutes les villes une seule fois.

**Complexité** : NP-difficile

### 2.2 Knapsack (Sac à dos)

Maximiser la valeur des objets dans un sac de capacité limitée.

**Contrainte** : Σ poids ≤ Capacité

**Complexité** : NP-difficile

---

## 3. Algorithmes Implémentés

### 3.1 Greedy Algorithm

| Version | Principe |
|---------|----------|
| Déterministe | Choisit toujours la meilleure option locale |
| Non-déterministe | Choisit aléatoirement parmi les k meilleures options |

### 3.2 Local Search

| Version | Principe |
|---------|----------|
| First Improvement | Applique la première amélioration trouvée |
| Best Improvement | Explore tout le voisinage et prend la meilleure amélioration |

**Voisinage utilisé** : 2-opt pour TSP, flip de bit pour Knapsack

### 3.3 Simulated Annealing

Accepte parfois des solutions moins bonnes pour éviter les optimums locaux.

**Paramètres** :
- Température initiale : 1000
- Refroidissement : 0.995
- Température d'arrêt : 0.1

### 3.4 Genetic Algorithm

Inspiré de l'évolution biologique.

**Paramètres** :
- Population : 100 individus
- Générations : 500 (TSP), 200 (Knapsack)
- Croisement : Order Crossover (TSP), 1 point (Knapsack)
- Mutation : 2% (TSP), 5% (Knapsack)
- Élitisme : 2 meilleurs individus

---

## 4. Résultats Expérimentaux

### 4.1 Résultats TSP (15 villes)

| Algorithme | Distance |
|------------|----------|
| Greedy Déterministe | 330.86 |
| Greedy Non-déterministe | 618.17 |
| Local Search (First) | 284.91 |
| Local Search (Best) | 284.91 |
| Simulated Annealing | 284.91 |
| Genetic Algorithm | 284.91 |

### 4.2 Résultats Knapsack (10 objets, capacité 51)

| Algorithme | Valeur |
|------------|--------|
| Greedy Déterministe | 234 |
| Greedy Non-déterministe | 234 |
| Local Search (First) | 234 |
| Local Search (Best) | 234 |
| Simulated Annealing | 242 |
| Genetic Algorithm | 242 |

---

## 5. Analyse des Résultats

### 5.1 TSP

- Le **Greedy déterministe** donne un meilleur résultat que le non-déterministe.
- La **recherche locale** améliore significativement la solution (de 330 à 284).
- **Recuit simulé** et **Génétique** n'ont pas amélioré davantage sur cette petite instance.

### 5.2 Knapsack

- Le **Greedy** atteint 234.
- Les algorithmes avancés (**Recuit simulé** et **Génétique**) trouvent une meilleure solution : 242.
- **Gain** : +8 par rapport au Greedy.

---

## 6. Conclusion

| Algorithme | Rapidité | Qualité | Évite optimum local |
|------------|----------|---------|---------------------|
| Greedy |  Très rapide |  Moyenne |  Non |
| Local Search |  Rapide |  Bonne |  Non |
| Simulated Annealing |  Moyenne |  Très bonne |  Oui |
| Genetic |  Moyenne |  Très bonne |  Oui |

**Meilleurs algorithmes** : Simulated Annealing et Genetic Algorithm.

---
### Structure du projet
Optimisation-Combinatoire/
│
├── algorithms/
│ ├── init.py
│ ├── greedy.py
│ ├── local_search.py
│ ├── simulated_annealing.py
│ └── genetic.py
│
├── utils/
│ ├── init.py
│ ├── tsp_utils.py
│ └── knapsack_utils.py
│
├── data/
│ └── (dossiers pour les instances)
│
├── main.py
├── requirements.txt
├── README.md
└── RAPPORT.md

