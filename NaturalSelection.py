from Population import Population
from Individual import  Individual
import random

class NaturalSelection:

    def __init__(self, mutationRate):

        self.population = Population(10)
        self.mutationRate = mutationRate
        self.fittest = None
        self.secondFittest = None
        self.genCount = 0

    def MainProcess(self, maze):
        self.population.CalFitForWholePop(maze)
        print("Generation: " + str(self.genCount) + " Fittest: " + str(self.population.fittest))

        while(self.population.fittest < Individual.MAX_FITNESS):
            self.genCount += 1

            self.Selection()
            self.CrossOver()

            if random.uniform(0, 1) <= self.mutationRate:
                self.Mutation()

            self.AddFittestOffspring(maze)
            self.population.CalFitForWholePop(maze)
            print("Generation: " + str(self.genCount) + " Fittest: " + str(self.population.fittest) +
                  " Genes: " + self.population.FindTheFittest().PrintGenes())

        print("Solution found in generation " + str(self.genCount))
        print("Fitness: " + str(self.population.FindTheFittest().fitness))
        print("Genes: " + self.population.FindTheFittest().PrintGenes())

    #Picks the two fittest individuals for the cross over process.
    def Selection(self):

        self.fittest = self.population.FindTheFittest()
        self.secondFittest = self.population.FindTheSecoundFittest()

    """
    Picks a random point in an individual's gene list and swaps the genes
    of the two fittest individuals, up to that point.
    """
    def CrossOver(self):

        crossPoint = random.randint(0, Individual.GENE_LENGTH - 1)

        for i in range(crossPoint):
            temp = self.fittest.genes[i]
            self.fittest.genes[i] = self.secondFittest.genes[i]
            self.secondFittest.genes[i] = temp

    """If a mutation occurs, then this function pick a random 
    point in an individual's gene list and randomizes all the
    genes up to that point."""
    def Mutation(self):

        mutaionPoint = random.randint(0, Individual.GENE_LENGTH - 1)

        self.fittest.MutateGene(mutaionPoint)

        mutaionPoint = random.randint(0, Individual.GENE_LENGTH - 1)

        self.secondFittest.MutateGene(mutaionPoint)

    def FindFittestOffspring(self):

        if self.fittest.fitness > self.secondFittest.fitness:
            return self.fittest

        return self.secondFittest

    """Finds the least fit individual and replaces them with
    the most fit offspring."""
    def AddFittestOffspring(self, maze):

        maze.RunGenesThroughMaze(self.fittest)
        maze.RunGenesThroughMaze(self.secondFittest)

        leastFit = self.population.FindLeastFittest()
        leastFit.CopyGenes(self.FindFittestOffspring())





