from Troop import Troop

class Field:
    field = [[]]
    def __init__(self):
        self.initialize()

    def initialize(self):
        for i in range(4):
            array = []
            for j in range(2):
                array.append(Troop(False, 0, False))
            for j in range(2):
                array.append(Troop(True, 0, False))
            self.field.append(array)

    # Getters and Setters
    def changeNationality(self, i, j, isVN):
        field[i][j].changeNationality(isVN)

    def changeMen(self, i, j, numMen):
        field[i][j].changeMen(numMen)

    def changeProtect(self, i, j, isProtected):
        field[i][j].changeProtect(isProtected)

    def getNationality(self, i, j):
        return field[i][j].getNationality()
    
    def getMen(self, i, j):
        return field[i][j].getMen()
    
    def getProtect(self, i, j):
        return field[i][j].getProtect()
    # End of getters and setters
