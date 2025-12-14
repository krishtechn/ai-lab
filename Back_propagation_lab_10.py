import random

# Parameters
POP_SIZE = 4
GENES = 5
GENERATIONS = 5
MUTATION_RATE = 0.1

# Fitness function: f(x) = x^2
def fitness(ind):
    x = int("".join(map(str, ind)), 2)
    return x**2

# Create initial population
population = [[random.randint(0,1) for _ in range(GENES)] for _ in range(POP_SIZE)]

for gen in range(GENERATIONS):
    # Selection (roulette wheel)
    total = sum(fitness(ind) for ind in population)
    probs = [fitness(ind)/total for ind in population]
    new_pop = []
    for _ in range(POP_SIZE):
        p1 = population[random.choices(range(POP_SIZE), probs)[0]]
        p2 = population[random.choices(range(POP_SIZE), probs)[0]]
        # Crossover (single point)
        point = random.randint(1, GENES-1)
        child = p1[:point] + p2[point:]
        # Mutation
        child = [1-bit if random.random()<MUTATION_RATE else bit for bit in child]
        new_pop.append(child)
    population = new_pop
    best = max(population, key=fitness)
    print(f"Gen {gen+1}: Best = {int(''.join(map(str,best)),2)}, Fitness = {fitness(best)}")
