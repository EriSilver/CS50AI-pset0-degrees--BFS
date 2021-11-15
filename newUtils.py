class Queue():
    def __init__(self):
        self.frontier = []
        self.moviesExplored = []
        self.personsExplored = []

    def newFrontier(self, array):
        self.frontier = array

    def addMovie(self, movieId):
        self.moviesExplored += [movieId]

    def addPerson(self, personId):
        self.personsExplored += [personId]