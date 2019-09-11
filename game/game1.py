import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")


display_height=600
display_width=800
crash_count=0

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('race3')

black = ( 0,0,0)
white = (255,255,255)

red = (255,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)

carwidth=389


clock = pygame.time.Clock()
crashed = False

roadimg= pygame.image.load('road1.png')
carimg= pygame.image.load('bhai1.png')
manimg= pygame.image.load('dead1.png')

pause = False
    



def car(x,y):
    game_display.blit(carimg, (x,y))
def text_objects(text,font):
    textsurface = font.render(text, True, red)
    return textsurface, textsurface.get_rect()
def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf',70)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = ((display_width/2),(display_height/2))
    game_display.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    
    
def crash():
   
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
   
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("arey bhai bhai bhai", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    game_display.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
def game_loop():
    x =(display_width * .45)
    y =(display_height * .3)
    y_change = 0
    x_change = 0
    game_exit = False

    while not game_exit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

    ##        print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_UP :
                    y_change=0
                if event.key == pygame.K_DOWN:
                    y_change=0    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT :
                    x_change=0
                if event.key == pygame.K_RIGHT:
                    x_change=0
                            
        x += x_change
        y += y_change      
        game_display.blit(roadimg, (00,00))
        game_display.blit(manimg, (0,-40))
        car(x,y)
        if x<-30 or x >  .45*display_width+20 :
            crash()
        if y<-300 or y> .3*display_height+30:
            crash()
            
        pygame.display.update()
        clock.tick(60)
        

print('man image=',manimg.get_rect().size)
print('car image=',carimg.get_rect().size)
game_loop()

pygame.quit()
quit()
