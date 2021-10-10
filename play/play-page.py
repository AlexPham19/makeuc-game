from Troop import Troop
from Field import Field

field = Field()
field.__init__()

def afterOneTurn():

    return

def attack(oldI, oldJ, newI, newJ):
    oldMen = field.field[oldI][oldJ].getMen 
    newMen = field.field[newI][newJ].getMen
    if oldMen < newMen:
        changeMen(newI, newJ, 0)
        changeMen(oldI, oldJ, newMen - oldMen)
        changeNationality(oldI, oldJ, field.field[newI][newJ.getNationality])
    elif oldMen > newMen:
        changeMen(oldI, oldJ, 0)
        changeMen(newI, newJ, newMen - oldMen)
        changeNationality(newI, newJ, field.field[oldI][oldJ].getNationality)
    else:
        changeMen(oldI, oldJ, 0)
        changeMen(newI, newJ, 0)
    return

def swap(oldI, oldJ, newI, newJ):
    oldMen = field.field[oldI][oldJ].getMen
    changeMen(oldI, oldJ, field.field[newI][newJ].getMen)
    changeMen(newI, newJ, oldMen)
    return

def add(oldI, oldJ, newI, newJ):
    changeMen(newI, newJ, field.field[oldI][oldJ].getMen + field.field[newI][newJ].getMen)
    changeMen(oldI, oldJ, 0)
    return

def USBomb(i, j):
    if field.field[i][j].getMen >= 1000:
        changeMen(i, j, field.field[i][j].getMen / 2)
    else:
        changeMen(0)
        changeNationality(i, j, False)
    return

def VNScout(i, j):
    string = "This land has " + field.field[i][j].getMen + " US troops"
    return string

def VNStealth(i, j):
    changeMen(i, j, field.field[i][j].getMen * 2)
    if afterOneTurn():
        changeMen(i, j, field.field[i][j].getMen / 2)
    return

