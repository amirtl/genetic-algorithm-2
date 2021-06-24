# genetic-algorithm-2
Solving N-Queens problem with genetic algorithm.
# explanation
- in parameters.txt there is an analysis for each parameter.
- I ran the code for 1000 times and made average and best case for each parameter.
# executation
run the code with python 2.
# algorithm
- We consider every case as gene like this : gene = [0,1,3,2,4,5,6,7]
- each line has one queen and gene[1] = 2 means we have a queen in row 1 and coloumn 2

1. first we make some Genes (input as number_of_the_population) randomly and sort them by their fitness and select the best 50% of them.
2. in each generation we make cross over and mutation
3. each cross over and mutation has a probability.
4. we make the number of cross overs half the size of the population
5. this is how the mutation work: it takes two different random number between 0 and 8. it swap the to indexes in the gene so that a new gene creates and in a probability they have the chance to mutate or not.
6. this is how the cross over works: it uses order recombination algorithm.
7. this is how the fitness function works: find the number of crashes in a gene with checking different diagonals.
7. we will add each new gene to our population.
8. after the mutations and cross overs we take the best 50% genes sorted with their fitnesses.
9. we stop the algorithm when the fitness is 0. 
