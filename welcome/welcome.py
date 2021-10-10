import pygame 
import yfinance as yf
import sys

#Initializing startscreen
pygame.init()
#Setting up clock 
clock = pygame.time.Clock()

# white color
white = (255,255,255) 

# green color
green = (0, 255, 0)

# blue color 
blue = (0, 0, 128)

# slate grey color
slategrey = (112, 128, 144)

# light grey  color
lightgrey = (165, 175, 185) 

# blackish color 
blackish = (10, 10, 10)

# light shade of the button 
color_light = (170,170,170) 

# dark shade of the button 
color_dark = (100,100,100) 

#Create the screen 
screen_width, screen_height = 760, 530
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hoangvippro6969")

# Width and height of the mouse
width = screen.get_width() 
height = screen.get_height() 

# The font of the text 
font = pygame.font.SysFont("comicsansms",30)
smallfont = pygame.font.SysFont("comicsansms", 14)
arial_font = pygame.font.SysFont('arial', 15)

# Menu text
player1 = arial_font.render('Player vs Bot', True, green, blue)
player2 = arial_font.render('Player 1 vs Player 2', True, green, blue)
option = arial_font.render('Options', True, green, blue)
credit = arial_font.render('Credits', True, green, blue)

# Format the form of the text
text = smallfont.render('quit', True, white)

# create a rectangular object for the
# text surface object
player1_Rect = player1.get_rect()
player2_Rect = player2.get_rect()
option_Rect = option.get_rect()
credit_Rect = credit.get_rect()
# set the center of the rectangular object.
player1_Rect.center = (width // 2, height // 2)
player2_Rect.center = (width // 2, height // 2)
option_Rect.center = (width // 2, height // 2)
credit_Rect.center = (width // 2, height // 2)
# Load image
icon_image = pygame.image.load(r"C:\Users\Admin\Desktop\MakeUC 21\makeuc-game\welcome\icon.jpg")
image = pygame.image.load(r"C:\Users\Admin\Desktop\MakeUC 21\makeuc-game\welcome\flag.png")
# Scale image 
scale_image = pygame.transform.scale(image, (759, 529))

# Set icon
pygame.display.set_icon(icon_image)

# Define the mouse
mouse = pygame.mouse.get_pos() 

# Game loop
while 1: 
    screen.fill(white)
    # 6 - draw the screen elements
    screen.blit(scale_image, (0,0))
    # 7 - update the screen
    pygame.display.flip()
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    screen.blit(player1, (width // 2, height // 2))
    screen.blit(player2, player2_Rect)
    screen.blit(option, option_Rect)
    screen.blit(credit, credit_Rect)
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

    if event.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= (width/2)+140 and height/2 <= mouse[1] <= (height/2)+40: 
                pygame.quit()  


screen.fill((60,25,60)) 
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    # if mouse is hovered on a button it 
    # changes to lighter shade 
if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
else: 
    pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
    # superimposing the text onto our button 
    screen.blit(text, (width/2+50,height/2)) 

pygame.display.update() 