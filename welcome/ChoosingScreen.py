import pygame 
import yfinance as yf
import sys
from pygame import mixer
#Play mechanism

mixer.init()

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

#Basic mechanism
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


#------------------------------------------------------------------------

class ChoosingScreen:
    def __init__(self):
        pass
    screen_width, screen_height = 1200, 720

    white = (255,255,255) 
    green = (0, 255, 0)
    blue = (0, 0, 128)
    red = (255,0,0)
    slategrey = (112, 128, 144)
    lightgrey = (165, 175, 185) 
    blackish = (10, 10, 10)
    color_light = (170,170,170) 
    color_dark = (100,100,100) 

        
    def run(self):
        clock = pygame.time.Clock()


        #Create the screen 
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Width and height of the mouse
        width = screen.get_width() 
        height = screen.get_height() 

        # The font of the text 
        font = pygame.font.SysFont("comicsansms",40)
        smallfont = pygame.font.SysFont("comicsansms",30)
        arial_font = pygame.font.SysFont('arial', 50)
        largefont = pygame.font.SysFont('arial', 70)
        # Menu text
        welcome = font.render('Welcome', True, self.red)
        _exit = font.render('Quit', True, self.green, self.color_dark)
        play = largefont.render('Play', True, self.green, self.color_dark)
        option = arial_font.render('Musik', True, self.green, self.color_dark)
        credit = smallfont.render('Credit: Quan Pham, Cat Luong, Hoang Nguyen, Trung Nguyen', True, self.green, self.color_dark)

        # create a rectangular object for the
        # text surface object
        welcome_Rect = welcome.get_rect()
        exit_Rect = _exit.get_rect()
        play_Rect = play.get_rect()
        option_Rect = option.get_rect()
        credit_Rect = credit.get_rect()
        # set the center of the rectangular object.
        welcome_Rect.center = (width // 2, height // 11)
        play_Rect.center = (width // 2, height // 11 * 3)
        option_Rect.center = (width // 2, height // 11 * 5)
        exit_Rect.center = (width // 2, height // 11 * 7)
        credit_Rect.center = (width // 2, height // 11 * 9)
        # Load image
        icon_image = pygame.image.load(r"welcome/icon.jpg")
        imageVN = pygame.image.load(r"welcome/flag.png")
        imageUS = pygame.image.load(r"welcome/usa.png")
        # Scale image 
        scale_image_vn = pygame.transform.scale(imageVN, (self.screen_width // 2, self.screen_height // 2))
        scale_image_us = pygame.transform.scale(imageUS, (self.screen_width // 2, self.screen_height // 2))
        # Set icon
        pygame.display.set_icon(icon_image)
        mixer.music.load("play\Bachomusic.wav")

        while 1: 
            # Define the mouse
            mouse = pygame.mouse.get_pos() 
            screen.fill(self.blackish)
            # 6 - draw the screen elements
            screen.blit(scale_image_vn, (0, height // 4))
            screen.blit(scale_image_us, (width // 2, height // 4))

            screen.blit(welcome, welcome_Rect)
            screen.blit(_exit, exit_Rect)
            screen.blit(play, play_Rect)
            screen.blit(option, option_Rect)
            screen.blit(credit, credit_Rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if exit_Rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    d = PlayingPage()
                    d.run()
                    pygame.quit()
                    exit(0)
                if option_Rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                      mixer.music.set_volume(0.7)
                      if mixer.music.get_busy(): 
                          mixer.music.pause()
                      else: 
                          mixer.music.play()
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)    