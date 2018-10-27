class Maze:

    def __init__(self):
        """
        S = Start of maze
        E = End of maze
        _ = Empty space
        # = Wall
        """
        self.maze = [
            ["_", "_", "#", "#", "_", "#"],
            ["#", "_", "_", "#", "_", "#"],
            ["#", "#", "_", "#", "_", "E"],
            ["#", "_", "_", "_", "_", "#"],
            ["#", "_", "#", "_", "#", "#"],
            ["S", "_", "#", "_", "_", "#"]
        ]

        """
        The maxMag is the magnitude of the space that is furthest away 
        from the end of the maze. 
        """
        self.maxMag = 6.0

        self.startLocation = self.FindCharLocation("S")
        self.currentLocation = self.startLocation
        self.endLocation = self.FindCharLocation("E")

    def FindCharLocation(self, targetChar):

        for x in range(len(self.maze)):
            for y in range(len(self.maze[x])):
                if self.maze[x][y] == targetChar:
                    return [x, y]

        return None

    def PrintMaze(self):

        for x in self.maze:
            row = ""
            for y in x:
                row += y
                row += " "

            print(row)

    """
        Moves the self.currentLocation through the maze base on the individual's 
    gene sequence. If the self.currentLocation makes a invalid move then
    the individual's fitness is calculated based on self.currentLocation's
    current distance to the end of the maze.
    """
    def RunGenesThroughMaze(self, individual):

        self.currentLocation = self.startLocation

        for aGene in individual.genes:

            possibleMove = None

            if aGene == "N":
                possibleMove = [self.currentLocation[0] - 1, self.currentLocation[1]]
            elif aGene == "E":
                possibleMove = [self.currentLocation[0], self.currentLocation[1] + 1]
            elif aGene == "S":
                possibleMove = [self.currentLocation[0] + 1, self.currentLocation[1]]
            elif aGene == "W":
                possibleMove = [self.currentLocation[0], self.currentLocation[1] - 1]
            else:
                print("Warning! Invalid gene detected: " + aGene)


            if self.CheckForVaildMove(possibleMove):
                self.currentLocation = possibleMove
            else:
                individual.CalFitness(self.currentLocation, self.endLocation, self.maxMag)
                break

    def CheckForVaildMove(self, posibleMove):

        if (posibleMove[0] >= 0 and posibleMove[0] < len(self.maze) and
                posibleMove[1] >= 0 and posibleMove[1] < len(self.maze[0])):

            if self.maze[posibleMove[0]][posibleMove[1]] != "#":
                return True

        return False
