import random
import math

class Individual:

  MAX_FITNESS = 100

  """This possible genes a individual can have correspond with a movement
      direction. N = North E = East S = South W = West"""
  POSSIBLE_GENES = ["N", "E", "S", "W"]

  """The geneLength must be one more then the minimal amount of moves
      it would take to reach the end of the maze. This will allow the 
      algorithm calculate the fitness of a individual when they are at
      the end of the maze."""
  GENE_LENGTH = 9

  def __init__(self):
    self.fitness = 0
    self.genes = []

    for x in range(Individual.GENE_LENGTH):
        self.genes.append(random.choice(Individual.POSSIBLE_GENES))

  """Caculates the magnitude of the distance between the current
  location and the end of the maze location. The smaller the 
  magnitude is, the closer the current location is to the end of 
  the maze. Thus, the smaller the magnitude the higher the fitness 
  score the individual will receive."""
  def CalFitness(self, curLoc, endLoc, maxMag):
      x = curLoc[0] - endLoc[0]
      y = curLoc[1] - endLoc[1]

      x = x ** 2
      y = y ** 2

      mag = math.sqrt(x + y)
      fitMod = 1.0 - (mag / maxMag)
      fitness = Individual.MAX_FITNESS * fitMod
      fitness = int(round(fitness))

      self.fitness = fitness


  def MutateGene(self, index):
      self.genes[index] = random.choice(Individual.POSSIBLE_GENES)

  def CopyGenes(self, otherIndividual):

      for x in range(Individual.GENE_LENGTH):
          self.genes[x] = otherIndividual.genes[x]

      self.fitness = otherIndividual.fitness

  def PrintGenes(self):

      count = 0
      geneOutput = ""

      for item in self.genes:
          geneOutput += str(count) + ":" + item + " "
          count += 1

      return geneOutput
