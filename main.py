import random as rnd
mutation_rate = 0.05
class Chromosome:
    def __init__(self, feature_1, feature_2, feature_3):
        self.feature_1 = feature_1 #[-1000 10000]
        self.feature_2 = feature_2 #[-200 200]
        self.feature_3 = feature_3 #[+, -, *, /]
        self.fitness = float('inf')

    def map_to_operator(self, val):
        if val == 0:
            return "+"
        if val == 1:
            return "-" 
        if val == 2:
            return "*"
        if val == 3:
            return "/"

    def set_fitness(self, new_fitness):
        self.fitness= new_fitness
    
    def get_fitness(self):
        return self.fitness

    def crossover(self, other):
        d = bool(rnd.randint(0,1))
        return Chromosome((self.feature_1 + other.feature_1) / 2,\
             (self.feature_2 + other.feature_2) / 2,\
            self.feature_3 if d else other.feature_3)

    def mutate(self):
        chance = rnd.random()
        if chance < mutation_rate:
            self.feature_1 += rnd.randint(-100, 100)
            if self.feature_1 >1000:
                self.feature_1 = 1000
            elif self.feature_1 < -1000:
                self.feature_1 = -1000
            self.feature_2 += rnd.randint(-30, 30)
            if self.feature_2 >200:
                self.feature_2 = 200
            elif self.feature_2 < -200:
                self.feature_2 = -200
            self.feature_3 += rnd.randint(-2, 2)
            if self.feature_3 > 3:
                self.feature_3 = 3
            elif self.feature_3 < 0:
                self.feature_3 = 0

    def eval(self):
        if self.map_to_operator(self.feature_3) == "+":
            return self.feature_1 + self.feature_2
        if self.map_to_operator(self.feature_3) == "-":
            return self.feature_1 - self.feature_2
        if self.map_to_operator(self.feature_3) == "*":
            return self.feature_1 * self.feature_2
        if self.map_to_operator(self.feature_3) == "/" and self.feature_2 !=0:
            return self.feature_1 / self.feature_2
        else:
            return float('inf')
    
    def __str__(self):
        return str(self.feature_1) + "" + self.map_to_operator(self.feature_3)\
            + "" + str(self.feature_2) + " = " + str(self.eval())

answer = 42
population = []
pop_size = 100
for i in range (pop_size):
    population.append(Chromosome(rnd.randint(-1000, 1000), \
        rnd.randint(-200, 200), rnd.randint(0, 3)))

average_population_fitness = float('inf')
while average_population_fitness > 0.1:
    pop_sum = 0

    for p in population:
        f= abs(p.eval() - answer)
        p.set_fitness(f)
        pop_sum +=f
    average_population_fitness = pop_sum / len(population)

    population.sort(key=lambda x : x.get_fitness())

    print("average population fitness: " + str(average_population_fitness)\
        + " best individual: " + str(population[0]))

    for j in range(1, 21):
        new_offspring = population[j -1].crossover(population[j +1])
        new_offspring.mutate()
        population[len(population) - j] = new_offspring