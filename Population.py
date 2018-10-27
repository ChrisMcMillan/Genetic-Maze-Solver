from Individual import Individual

class Population:

    def __init__(self, popSize):

        self.popSize = popSize
        self.individuals = []
        self.fittest = 0

        for x in range(self.popSize):
            temp = Individual()
            self.individuals.append(temp)


    def FindTheFittest(self):

        fittestIndiv = self.individuals[0]

        for item in self.individuals:

            if(item.fitness > fittestIndiv.fitness):
                fittestIndiv = item

        self.fittest = fittestIndiv.fitness

        return fittestIndiv

    def FindTheSecoundFittest(self):

        mostFit = self.individuals[0]
        secoundMostFit = self.individuals[0]

        for item in self.individuals:

            if (item.fitness > mostFit.fitness):
                secoundMostFit = mostFit
                mostFit = item

            elif item.fitness > secoundMostFit.fitness:
                secoundMostFit = item

        return secoundMostFit

    def FindLeastFittest(self):

        leastFitIndiv = self.individuals[0]

        for item in self.individuals:

            if(item.fitness < leastFitIndiv.fitness):
                leastFitIndiv = item

        return leastFitIndiv

    def CalFitForWholePop(self, maze):

        for indiv in self.individuals:
            maze.RunGenesThroughMaze(indiv)

        self.FindTheFittest()


