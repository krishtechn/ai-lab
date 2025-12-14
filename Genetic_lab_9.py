import random

# Parameters
POP_SIZE = 6
GENES = 5
GENERATIONS = 10
MUTATION_RATE = 0.1

# Fitness function
def fitness(individual):
    x = int("".join(str(bit) for bit in individual), 2)
    return x**2

# Create initial population
def create_population():
    return [[random.randint(0,1) for _ in range(GENES)] for _ in range(POP_SIZE)]

# Selection (roulette wheel)
def select(pop):
    total_fitness = sum(fitness(ind) for ind in pop)
    probs = [fitness(ind)/total_fitness for ind in pop]
    return pop[random.choices(range(POP_SIZE), probs)[0]]

# Crossover (single point)
def crossover(parent1, parent2):
    point = random.randint(1, GENES-1)
    return parent1[:point] + parent2[point:]

# Mutation
def mutate(ind):
    for i in range(GENES):
        if random.random() < MUTATION_RATE:
            ind[i] = 1 - ind[i]
    return ind

# GA main loop
population = create_population()
for gen in range(GENERATIONS):
    new_pop = []
    for _ in range(POP_SIZE):
        p1 = select(population)
        p2 = select(population)
        child = crossover(p1, p2)
        child = mutate(child)
        new_pop.append(child)
    population = new_pop
    best = max(population, key=fitness)
    print(f"Generation {gen+1}: Best = {int(''.join(map(str,best)),2)} Fitness = {fitness(best)}")
