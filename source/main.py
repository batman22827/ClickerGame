# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random,sys
from pygame.color import THECOLORS

WIDTH = 800
HEIGHT = 600
FPS = 30

class Color():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.animation_set = [pygame.transform.scale(pygame.image.load(f"data/r{i}.png"),(350,350)) for i in range(1, 2)]
        pygame.init()
        pygame.mixer.music.load('data/click.ogg')
        self.font = pygame.font.SysFont('couriernew', 40)
        self.i = 0
        self.image = self.animation_set[self.i // 12]
        self.rect = self.image.get_rect().center
        self.balance = 0
        
        pygame.sprite.Sprite.__init__(self)
    def update(self):
        text = self.font.render(str(f'Score:{self.balance}'), True, THECOLORS['purple'])
        window.blit(text, (50, 50))
       
    def click(self):
        rect = pygame.Rect(*window.get_rect().center, 150, 150).inflate(350, 320)
        if (rect.collidepoint(pygame.mouse.get_pos())):
            self.balance+=1

            self.image = pygame.transform.scale(pygame.image.load('data/r2.png'), (350,350))
            self.rect = self.image.get_rect().center
            window.blit(self.image, self.image.get_rect().center)
        
            pygame.display.update()
            pygame.mixer.music.play()
            pygame.time.wait(100)
            self.image = pygame.transform.scale(pygame.image.load('data/r1.png'), (350,350))

        

window = pygame.display.set_mode((WIDTH, HEIGHT))

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        if event.type == pygame.MOUSEBUTTONDOWN:           
                player.click()    

    window.fill(THECOLORS['pink'])
    all_sprites.update()
    
    

    all_sprites.draw(window)
    
    pygame.display.flip()
    clock.tick(60)