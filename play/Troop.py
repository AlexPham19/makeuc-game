import pygame
 
class Troop:
    _isVN = False
    _numMen = 0
    _isProtected = False
    def __init__(self, isVN, numMen, isProtected):
        self._isVN = isVN
        self._numMen = numMen
        self._isProtected = isProtected
    # Getters and Setters
    def changeMen(men):
        _numMen = men
    def changeNationality(isVn):
        _isVN = isVn
    def changeProtect(protect):
        _isProtected = protect

    def getMen():
        return _numMen
    def getNationality():
        return _isVN
    def getProtect():
        return _isProtected



        
