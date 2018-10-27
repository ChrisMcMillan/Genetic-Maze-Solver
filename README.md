# Genetic-Maze-Solver
Utilizes genetic algorithm to solve a maze.

This code is a modification of the example code found at this
URL: https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3

This program uses a genetic algorithm to find a path through a maze, represented by
a matrix of string values. The program reads a individual's genes and uses them as
instructions to navigate the maze. The closer a individual gets to the end of the maze,
the more fit they are. The genetic algorithm is preformed on a population of individuals of until
one of them is fit enough to reach the end of the maze.

Flaws with program:
    There are some flaws with this program. This is obviously not the most efficient way of
solving a maze but the reason I did this is to experiment with genetic algorithms, not
find the most efficient maze navigator. Another flaw is that if the most fit individuals
have genes that cause them to back track through the maze, it can cause that gene sequence
to become prevalent in the population. This can prevent any individual, in the population,
from getting to the end of the maze. This will cause the program to loop indefinitely. A
way of circumventing this flaw is to increase the number of genes a individual can have. This
will decrease the likely hood that back tracking through maze will cause an infinite loop because
there are more possible moves for a gene sequence. However, this can result in many genes going unused.

Another possible solution is to increase the population size, possibility decreasing the likely hood
a back tracking gene sequence becomes prevalent in the population. A third possible solution is to
increase the mutation rate. This can prevent the homogenization of the population, which can stop
the back tracking gene sequence from staying prevalent for too long. However, I fear that increasing the
mutation rate too high will cause this program to become indistinguishable from a program that just randomly
guesses the right answer, rather then a program that uses the process of natural selection to work toward the
right answer.
