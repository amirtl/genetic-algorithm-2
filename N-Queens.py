#solving TSP using genetic algorithm

import random

#generates a random number between 1 and the number of cities minus 1.
def Rand_City(size):
    return random.randint(0, size-1)

#checks if a city was seen before of not.
def Is_New(Gene, city):
    for c in Gene:
        if c == city:
            return False
    
    return True

#find the fitness using the given matrix
def Find_Fitness(Gene):
    nxn = []
    c = []
    for i in range(len(Gene)):
        c.append(0)
    for i in range(len(Gene)):
        nxn.append(c[:])
        nxn[i][Gene[i]] = 1

    fitness = 0
    for i in range(len(Gene)):
        j = len(Gene) - i - 1
        k = 0
        queens = 0
        while k <= i:
            if nxn[k][j] == 1:
                queens += 1
            k += 1
            j += 1
        if queens > 1:
            fitness += (queens * (queens-1))

        j = i
        k = len(Gene) - 1
        queens = 0
        if j != len(Gene) - 1:
            while j >= 0:
                if nxn[k][j] == 1:
                    queens += 1
                k -= 1
                j -= 1
            if queens > 1:
                fitness += (queens * (queens-1))

        j = 0
        k = i
        queens = 0
        while k >= 0:
            if nxn[k][j] == 1:
                queens += 1
            k -= 1
            j += 1
        if queens > 1:
            fitness += (queens * (queens-1))

        j = len(Gene) - 1 - i
        k = len(Gene) - 1
        queens = 0
        if j != 0:
            while j <= len(Gene) - 1:
                if nxn[k][j] == 1:
                    queens += 1
                k -= 1
                j += 1
            if queens > 1:
                fitness += (queens * (queens-1))

    return fitness

#generates a Gene randomly or generates a path randomly
def Create_Gene(size):
    Gene = []
    for i in range(size):
        while True:
            new_city = Rand_City(size)
            if Is_New(Gene, new_city):
                Gene += [new_city]
                break
    
    return Gene



def Give_2_rand_number(size):
    while True:
        change1 = Rand_City(size)
        change2 = Rand_City(size)
        if change1 != change2:
            break
    if change1 > change2:
        temp = change1
        change1 = change2
        change2 = temp
    
    return change1, change2


#gets 2 cities and swap them to make a mutation.
def Mutation(Gene):
    change1, change2 = Give_2_rand_number(len(Gene))
    temp = Gene[change1]
    Gene[change1] = Gene[change2]
    Gene[change2] = temp

    return Gene

def CrossOver(Gene1, Gene2):
    n = len(Gene1)
    i, j = Give_2_rand_number(n)
    mark = [0]*n
    new_gene = [0]*n
    
    for k in range(i, j+1):
        new_gene[k] = Gene1[k]
        mark[Gene1[k]] = 1

    p_old = (j+1)%n
    p_new = p_old
    
    for _ in range(n):
        if mark[Gene2[p_old]] == 1:
            p_old = p_old+1
            p_old = p_old%n
            continue
        
        if new_gene[p_new] == True:
            break
        
        new_gene[p_new] = Gene2[p_old]
        mark[Gene2[p_old]] = 1
        p_old, p_new = p_old+1, p_new+1
        p_old, p_new = p_old%n, p_new%n
        
    return new_gene


def TSP(size, number_of_first_population, N, Mutation_Probability, Cross_Over_Probability):
    Population = []
    #generate the first population
    for _ in range(number_of_first_population):
        Gene = Create_Gene(size)
        Fitness = Find_Fitness(Gene)
        Population.append((Gene,Fitness))

    Population.sort(key=lambda x:x[1])
    Population = Population[:(len(Population)*N)/100+1]
    print("Best initial population:")    
    print(Population[0][0])
    print("Cost:")
    print(Population[0][1])

    generation = 2
    #repeats untill the best fitness does not change for N times
    while(Population[0][1] != 0):
        new_population = Population
        #make a cross over between 2 genes that have not been cross overed before for half of the size of the population
        crossed_over = []
        for _ in range(len(new_population)/2):
            if Rand_City(101) >= Cross_Over_Probability:
                while True:
                    i, j =  Give_2_rand_number(len(new_population))
                    if Is_New(crossed_over, i) and Is_New(crossed_over, j):
                        crossed_over += [i]
                        crossed_over += [j]
                        break
                new_gene = CrossOver(new_population[i][0][:], new_population[j][0][:])
                new_fitness = Find_Fitness(new_gene)
                Population.append((new_gene, new_fitness))

        #make a mutation in each parent and consider them as a child and append them to the generation
        for i in range(len(new_population)):
            if Rand_City(101) >= Mutation_Probability:
                new_gene = Mutation(new_population[i][0][:])
                new_fitness = Find_Fitness(new_gene)
                Population.append((new_gene, new_fitness))
        
        #sort the generation by the fitness
        Population.sort(key=lambda x:x[1])
        #choose the N% of best fitnesses
        Population = Population[:(len(Population)*N)/100 + 1]

        print("generation number: ", generation)
        print("best population:")    
        print(Population[0][0])
        print("cost:")
        print(Population[0][1])
        generation += 1


size = 8 #number of queens
number_of_first_population = size*2
N = 50 #N%  of the best fitnesses will be chosen
Mutation_Probability = 50 #every gene have 50% probability to mutate
Cross_Over_Probability = 50
TSP(size, number_of_first_population, N, Mutation_Probability, Cross_Over_Probability)