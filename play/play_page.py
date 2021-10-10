import pygame 
import yfinance as yf
import sys

class Troop:
    _isVN = False
    _numMen = 0
    def __init__(self, isVN, numMen):
        self._isVN = isVN
        self._numMen = numMen

    # Getters and Setters
    def changeMen(men):
        _numMen = men
    def changeNationality(isVn):
        _isVN = isVn

    def getMen():
        return _numMen
    def getNationality():
        return _isVN

class Field:
    field = [[]]
    def __init__(self):
        pass
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

    def getNationality(self, i, j):
        return field[i][j].getNationality()
    
    def getMen(self, i, j):
        return field[i][j].getMen()
    # End of getters and setters

field =  Field()
class PlayingPage:
    def __init__(self):
        pass
    screen_width, screen_height = 1000, 800

    white = (255,255,255) 
    green = (0, 255, 0)
    blue = (0, 0, 128)
    slategrey = (112, 128, 144)
    lightgrey = (165, 175, 185) 
    blackish = (10, 10, 10)
    color_light = (170,170,170) 
    color_dark = (100,100,100) 

    def run(self):
        print('Play Page')

# ---------------------------------------------

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

# def swap(oldI, oldJ, newI, newJ):
    # oldMen = field.field[oldI][oldJ].getMen
    # changeMen(oldI, oldJ, field.field[newI][newJ].getMen)
    # changeMen(newI, newJ, oldMen)
    # return

# def add(oldI, oldJ, newI, newJ):
#     changeMen(newI, newJ, field.field[oldI][oldJ].getMen + field.field[newI][newJ].getMen)
#     changeMen(oldI, oldJ, 0)
#     return