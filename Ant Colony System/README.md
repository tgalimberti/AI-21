# Ant Colony System Optimisation #

This is an implementation of the Ant Colony System applied to the Travelling Salesman Problem (TSP) using 2-opt local search based on the papers [[1]](https://people.idsia.ch/~luca/acs-ec97.pdf) and [[2]](https://people.idsia.ch/~luca/icec96-acs.pdf), as a project for the Artificial Intelligence Master's course at Università della Svizzera italiana. 

The TSP instances solved in `Ant Colony System for the TSP.ipynb` in order of increasing difficulty are: eil76, ch130 and d198.

Static hyperparameters:
1. Time per run = 180 seconds
2. Number of ants = 10
3. Starting pheromone = 1 / d_NN (edges assigned pheromone equal to the inverse of the nearest neighbour heuristic for that problem)
4. Local/global pheromone evaporation factor = 0.1
5. Candidate list size = 15

Variations in the runs
1. Variable exploration/exploitation weightings
2. With/without candidate lists 
3. Random number generator seed

*References*

[1] Ant Colony System: A Cooperative Learning
Approach to the Traveling Salesman Problem; Dorigo, Gambardella

[2] Solving Symmetric and Asymmetric TSPs
by Ant Colonies; Dorigo, Gambardella
