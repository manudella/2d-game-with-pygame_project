import pygame
import os
import math
import time
import json

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1300, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Castle Clash")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


HEALTH_FONT = pygame.font.SysFont('franklingothicmedium', 40)
WINNER_FONT = pygame.font.SysFont('franklingothicmedium', 100)

FPS = 60
VEL = 5
BARRAK_WIDTH, BARRAK_HEIGHT = 145, 120
MINE_WIDTH, MINE_HEIGHT = 150, 125
WALL_WIDTH, WALL_HEIGHT = 250, 200
TOWER_WIDTH, TOWER_HEIGHT = 150, 375
ARCHER_WIDTH, ARCHER_HEIGHT = 45, 45


#ICONS

SWORD_image = pygame.image.load(
    os.path.join('data', 'sword.png'))
SWORD = pygame.transform.scale(
    SWORD_image, (50, 50))

BOW_image = pygame.image.load(
    os.path.join('data', 'bow.png'))
BOW = pygame.transform.scale(
    BOW_image, (50, 50))

PICKAXE_image = pygame.image.load(
    os.path.join('data', 'pickaxe.png'))
PICKAXE = pygame.transform.scale(
    PICKAXE_image, (50, 50))

RESOURCES_image = pygame.image.load(
    os.path.join('data', 'resources.png'))
RESOURCES = pygame.transform.scale(
    RESOURCES_image, (50, 50))
 

#BARRAKS

BARRAK_1_image = pygame.image.load(
    os.path.join('data', 'barrak1.png'))
BARRAK_1 =pygame.transform.scale(
    BARRAK_1_image, (BARRAK_WIDTH, BARRAK_HEIGHT))

BARRAK_2_image = pygame.transform.flip(pygame.image.load(
    os.path.join('data', 'barrak2.png')),True,False)
BARRAK_2 =pygame.transform.scale(
    BARRAK_2_image, (BARRAK_WIDTH, BARRAK_HEIGHT))


#MINES

MINE_1_image = pygame.image.load(
    os.path.join('data', 'mine.gif'))
MINE_1 =pygame.transform.scale(
    MINE_1_image, (MINE_WIDTH, MINE_HEIGHT))

MINE_2_image = pygame.transform.flip(pygame.image.load(
    os.path.join('data', 'mine.gif')),True,False)
MINE_2 =pygame.transform.scale(
    MINE_2_image, (MINE_WIDTH, MINE_HEIGHT))

#WALLS

WALL_1_image = pygame.transform.flip(pygame.image.load(
    os.path.join('data', 'wall1.png')),True,False)
WALL_1 =pygame.transform.scale(
    WALL_1_image, (WALL_WIDTH, WALL_HEIGHT))

WALL_2_image = pygame.image.load(
    os.path.join('data', 'wall2.png'))
WALL_2 =pygame.transform.scale(
    WALL_2_image, (WALL_WIDTH, WALL_HEIGHT))

#TOWERS

TOWER_1_image = pygame.transform.flip(pygame.image.load(
    os.path.join('data', 'atower1.png')),True,False)
TOWER_1 =pygame.transform.scale(
    TOWER_1_image, (TOWER_WIDTH, TOWER_HEIGHT))

TOWER_2_image = pygame.image.load(
    os.path.join('data', 'atower2.png'))
TOWER_2 =pygame.transform.scale(
    TOWER_2_image, (TOWER_WIDTH, TOWER_HEIGHT))

BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('data', 'background.gif')), (WIDTH+40, HEIGHT+40))

GROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('data', 'ground.png')), (WIDTH, 370))

HEAL_WALL_1=1000
HEAL_WALL_2=1000


class wall_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = HEAL_WALL_1
        self.image= pygame.transform.flip(pygame.image.load(
        os.path.join('data', 'nothing.png')),True,False)
        self.image= pygame.transform.scale(
        self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (MINE_WIDTH+BARRAK_WIDTH+100, HEIGHT-170)
        
    def gets_hit_by_sword(self):
        self.health += -2
        
    def gets_hit_by_arrow(self):
        self.health += -1
        
    def collision_1(self):
        self.colliding_1 = True
        
    def not_collision_1(self):
        self.colliding_1 = False

    def in_range_1(self):
        self.range_1 = False

    def not_in_range_1(self):
        self.range_1 = False

    def update(self):
        self.rect.x += 0

class wall_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = HEAL_WALL_2
        self.image= pygame.image.load(
        os.path.join('data', 'nothing.png'))
        self.image= pygame.transform.scale(
        self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH-MINE_WIDTH-BARRAK_WIDTH-WALL_WIDTH+150, HEIGHT-170)
        self.colliding_2=False
        self.range_2=False
        
    def gets_hit_by_sword(self):       
        self.health += -2
        
    def gets_hit_by_arrow(self):
        self.health += -1
                           
    def collision_2(self):
        self.colliding_2 = True
        
    def not_collision_2(self):
        self.colliding_2 = False

    def in_range_2(self):
        self.range_2 = False

    def not_in_range_2(self):
        self.range_2 = False

    def update(self):
        self.rect.x += 0
        
        
        
class TOWER_ARCHER_2(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        
        self.images.append(pygame.image.load((os.path.join('data', 'archer1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer9.png'))))
        self.index = 0
        self.image = self.images[self.index]
        
        self.image = pygame.transform.scale(
            self.image, (ARCHER_WIDTH, ARCHER_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH-300, HEIGHT / 3 - 13)
        self.colliding_2 = False
        self.range_2 = False
        self.speedx_2 = -3
        self.speedy_2 = 5
        
    def not_collision_2(self):
        self.colliding_2 = False
        
    def collision_2(self):
        self.colliding_2 = False

    def in_range_2(self):
        self.range_2 = True

    def not_in_range_2(self):
        self.range_2 = False
        
    def shoot(self):
        arrow_2 = DIAG_ARROW_2(self.rect.centerx, self.rect.centery, self.speedx_2, self.speedy_2)        
        arrows_2.add(arrow_2)
        
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(
            self.image, (ARCHER_WIDTH, ARCHER_HEIGHT))
        
        self.rect.x += 0
        if self.rect.left > WIDTH:
            self.rect.right = 0

class TOWER_ARCHER_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.images.append(pygame.image.load((os.path.join('data', 'archer1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer9.png'))))
        self.index = 0
        self.image = self.images[self.index]
        self.image =  pygame.transform.flip(pygame.transform.scale(
            self.image, (ARCHER_WIDTH, ARCHER_HEIGHT)),True,False)

        self.rect = self.image.get_rect()

        self.rect.center = (300, HEIGHT / 3 - 13)
        self.colliding_1 = False
        self.range_1 = False
        self.speedx_1= 3
        self.speedy_1= 5
        
    def not_collision_1(self):
        self.colliding_1 = False
        
    def collision_1(self):
        self.colliding_1 = False
        
    def in_range_1(self):
        self.range_1 = True

    def not_in_range_1(self):
        self.range_1 = False
        
    def shoot(self):
        arrow_1 = DIAG_ARROW_1(self.rect.centerx, self.rect.centery, self.speedx_1, self.speedy_1)        
        arrows_1.add(arrow_1)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image =  pygame.transform.flip(pygame.transform.scale(
            self.image, (ARCHER_WIDTH, ARCHER_HEIGHT)),True,False)
        
        self.rect.x += 0
        
        if self.rect.left > WIDTH:
            self.rect.right = 0


class ARCHER_2(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        
        self.images.append(pygame.image.load((os.path.join('data', 'archer1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer9.png'))))
        
        self.index = 0

        self.image = self.images[self.index]
        
        self.image = pygame.transform.scale(
            self.image, (ARCHER_WIDTH, ARCHER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH-450, WIDTH-863)
        self.colliding_2=False
        self.range_2=False
        self.health=20
        
    def gets_hit_by_sword(self):
        self.health += -2
        
    def gets_hit_by_arrow(self):
        self.health += -1
                    
    def collision_2(self):
        self.colliding_2 = True
        
    def not_collision_2(self):
        self.colliding_2 = False

    def in_range_2(self):
        self.range_2 = True

    def not_in_range_2(self):
        self.range_2 = False
        
    def shoot(self):
        arrow_2 = ARROW_2(self.rect.centerx, self.rect.centery)
        arrows_2.add(arrow_2)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(
            self.image, (ARCHER_WIDTH, ARCHER_HEIGHT))
        
        if self.colliding_2==False and self.range_2==False:
            if self.rect.x > 0 and self.rect.x < WIDTH - ARCHER_WIDTH:
                self.rect.x += -1
                
            elif self.rect.x == WIDTH - ARCHER_WIDTH:
                self.rect.x == WIDTH - ARCHER_WIDTH
                
        elif self.colliding_2==True or self.range_2==True:
            self.rect.x+=0


class ARCHER_1(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        
        self.images.append(pygame.image.load((os.path.join('data', 'archer1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'archer9.png'))))
        
        self.index = 0

        self.image = self.images[self.index]
        
        self.image =  pygame.transform.flip(pygame.transform.scale(
            self.image, (ARCHER_WIDTH, ARCHER_HEIGHT)),True,False)
        self.rect = self.image.get_rect()
        self.rect.center = (450, WIDTH-863)
        self.colliding_1=False
        self.range_1=False
        self.health=20
        
    def shoot(self):
        arrow_1 = ARROW_1(self.rect.centerx, self.rect.centery)
        arrows_1.add(arrow_1)
        
    def gets_hit_by_sword(self):
        self.health += -2
        
    def gets_hit_by_arrow(self):
        self.health += -1
                    
    def collision_1(self):
        self.colliding_1 = True

    def in_range_1(self):
        self.range_1 = True

    def not_in_range_1(self):
        self.range_1 = False
        
    def not_collision_1(self):
        self.colliding_1 = False
        
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image =  pygame.transform.flip(pygame.transform.scale(
            self.image, (ARCHER_WIDTH, ARCHER_HEIGHT)),True,False)

        if self.colliding_1==True or self.range_1==True:
            self.rect.x+=0
            
            
        elif self.colliding_1==False and self.range_1==False:
            
            if self.rect.x > 0 and self.rect.x < WIDTH - ARCHER_WIDTH:
                self.rect.x += 1
            elif self.rect.x == WIDTH - ARCHER_WIDTH:
                self.rect.x == WIDTH - ARCHER_WIDTH


                
        

class SWORDSMAN_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman9.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman10.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman11.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman12.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman13.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman14.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman15.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman16.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman17.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman18.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman19.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman20.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman21.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman22.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman23.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman24.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman25.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman26.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman27.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman28.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman29.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman30.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman31.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman32.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman33.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman34.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman35.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman36.png'))))
        
        self.index = 0

        self.image = self.images[self.index]
        
        self.image = pygame.transform.scale(
            self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (450, HEIGHT-170)
        self.colliding_1=False
        self.range_1=False
        self.health=30
        
    def gets_hit_by_sword(self):
        self.health += -2
        
        
    def gets_hit_by_arrow(self):
        self.health += -1
                    
    def collision_1(self):
        self.colliding_1 = True
        
    def not_collision_1(self):
        self.colliding_1 = False

    def in_range_1(self):
        self.range_1 = False

    def not_in_range_1(self):
        self.range_1 = False
        
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(
            self.image, (70, 70))

        if self.colliding_1==False:

            if self.rect.x > 0 and self.rect.x < WIDTH - ARCHER_WIDTH:
                self.rect.x += 1
            elif self.rect.x == WIDTH - ARCHER_WIDTH:
                self.rect.x == WIDTH - ARCHER_WIDTH
        elif self.colliding_1==True:
            self.rect.x+=0

class SWORDSMAN_2(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.images=[]
        
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman9.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman10.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman11.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman12.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman13.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman14.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman15.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman16.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman17.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman18.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman19.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman20.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman21.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman22.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman23.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman24.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman25.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman26.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman27.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman28.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman29.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman30.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman31.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman32.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman33.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman34.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman35.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'swordsman36.png'))))
        
        self.index = 0

        self.image = self.images[self.index]
        self.image = pygame.transform.flip(pygame.transform.scale(
            self.image, (70, 70)),True,False)
        self.rect = self.image.get_rect()
        self.colliding_2=False
        self.rect.center = (WIDTH-450, HEIGHT-170)
        self.range_2=False
        self.health=30
        
    def gets_hit_by_sword(self):
        self.health += -2
             
    def gets_hit_by_arrow(self):
        self.health += -1

    def collision_2(self):
        self.colliding_2 = True

    def not_collision_2(self):
        self.colliding_2 = False
        
    def in_range_2(self):
        self.range_2 = False

    def not_in_range_2(self):
        self.range_2 = False
        
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image = pygame.transform.flip(pygame.transform.scale(
            self.image, (70, 70)),True,False)

        if self.colliding_2==False:
            if self.rect.x > 0:
                self.rect.x += -1
            elif self.rect.x == 0:
                self.rect.x == 0
        elif self.colliding_2==True:
            self.rect.x += 0

class WORKER_WALL_2(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        
        self.images.append(pygame.image.load((os.path.join('data', 'miner1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner9.png'))))

        
        self.index = 0

        self.image = self.images[self.index]

        self.image =  pygame.transform.flip(pygame.transform.scale(
            self.image, (100, 100)),True,False)
        self.rect = self.image.get_rect()
        
        self.rect.center = (WIDTH-200, WIDTH-880)
        

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image =  pygame.transform.flip(pygame.transform.scale(
            self.image, (100, 100)),True,False)
        
        if self.rect.x > WIDTH-350:
            self.rect.x += -1
        else:
            self.rect.x += 0
            
        
class WORKER_WALL_1(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        
        self.images.append(pygame.image.load((os.path.join('data', 'miner1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner9.png'))))

        
        self.index = 0

        self.image = self.images[self.index]
        
        self.image =  pygame.transform.flip(pygame.transform.scale(
            self.image, (100, 100)),True,False)
        self.rect = self.image.get_rect()
        self.rect.center = (200, WIDTH-880)
        

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(
            self.image, (100, 100))

        if self.rect.x < 250:
            self.rect.x += 1
        else:
            self.rect.x += 0

class WORKER_MINE_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        
        self.images.append(pygame.image.load((os.path.join('data', 'miner1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner9.png'))))
        
        self.index = 0

        self.image = self.images[self.index]
        
        self.image = pygame.transform.scale(
            self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH-200, WIDTH-880)
        

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(
            self.image, (100, 100))
        
        if self.rect.x < WIDTH-150:
            self.rect.x += 1
            
        else:
            self.rect.x += 0
    
            
            

class WORKER_MINE_1(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        
        self.images.append(pygame.image.load((os.path.join('data', 'miner1.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner2.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner3.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner4.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner5.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner6.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner7.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner8.png'))))
        self.images.append(pygame.image.load((os.path.join('data', 'miner9.png'))))

        
        self.index = 0

        self.image = self.images[self.index]
        
        self.image =  pygame.transform.flip(pygame.transform.scale(
            self.image, (100, 100)),True,False)
        self.rect = self.image.get_rect()
        self.rect.center = (200, WIDTH-880)
        

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        self.image = pygame.transform.flip(pygame.transform.scale(
            self.image, (100, 100)),True,False)
        if self.rect.x > 50:
            self.rect.x += -1
        else:
            self.rect.x += 0
        

class ARROW_1(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load((os.path.join('data', 'arrow1.png')))
        
        self.image =pygame.transform.scale(
        self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
       
    def update(self):
        if self.rect.x > 0 and self.rect.x < WIDTH - ARCHER_WIDTH:
            self.rect.x += 3
        elif self.rect.x == WIDTH - ARCHER_WIDTH:
            self.rect.x == WIDTH - ARCHER_WIDTH
            
            
class ARROW_2(pygame.sprite.Sprite):

        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load((os.path.join('data', 'arrow2.png')))
        
            self.image =pygame.transform.scale(
            self.image, (10, 10))
            self.rect = self.image.get_rect()
            self.rect.centery = y
            self.rect.centerx = x

        def update(self):
            if self.rect.x > 0 and self.rect.x < WIDTH - ARCHER_WIDTH:
                self.rect.x += -3
            elif self.rect.x == WIDTH - ARCHER_WIDTH:
                self.rect.x == WIDTH - ARCHER_WIDTH
                

class DIAG_ARROW_1(pygame.sprite.Sprite):

    def __init__(self,x,y,speedx_1,speedy_1):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load((os.path.join('data', 'diag_arrow1.png')))
        
        self.image =pygame.transform.scale(
        self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedx = speedx_1
        self.speedy = speedy_1

        
    def update(self):
        if self.rect.x > 0 and self.rect.x < WIDTH - ARCHER_WIDTH:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        elif self.rect.x == WIDTH - ARCHER_WIDTH:
            self.rect.x == WIDTH - ARCHER_WIDTH
            
class DIAG_ARROW_2(pygame.sprite.Sprite):
        def __init__(self,x,y,speedx_2,speedy_2):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load((os.path.join('data', 'diag_arrow2.png')))
        
            self.image =pygame.transform.scale(
            self.image, (10, 10))
            self.rect = self.image.get_rect()
            self.rect.centery = y
            self.rect.centerx = x
            self.speedx = speedx_2
            self.speedy = speedy_2

        def update(self):
            if self.rect.x > 0 and self.rect.x < WIDTH - ARCHER_WIDTH:
                self.rect.x += self.speedx
                self.rect.y += self.speedy
            elif self.rect.x == WIDTH - ARCHER_WIDTH:
                self.rect.x == WIDTH - ARCHER_WIDTH



def draw_window(N_S_1,N_S_2,N_A_1,N_A_2,N_W_1,N_W_2,M_W_1,M_W_2,W_W_1,W_W_2):
    WIN.blit(BACKGROUND, (-40, -40))
    WIN.blit(GROUND, (0, 240))
    global resources_1
    global resources_2

    resources_1_text = HEALTH_FONT.render(
        "Resources: " + str(resources_1), 1, WHITE)
    resources_2_text = HEALTH_FONT.render(
        "Resources: " + str(resources_2), 1, WHITE)
    WIN.blit(resources_2_text, (WIDTH - resources_2_text.get_width() - 80, 10))
    WIN.blit(resources_1_text, (10, 10))
    
    N_S_1_text = HEALTH_FONT.render(
        str(N_S_1), 1, WHITE)
    N_S_2_text = HEALTH_FONT.render(
        str(N_S_2), 1, WHITE)
    N_A_1_text = HEALTH_FONT.render(
        str(N_A_1), 1, WHITE)
    N_A_2_text = HEALTH_FONT.render(
        str(N_A_2), 1, WHITE)
    N_W_1_text = HEALTH_FONT.render(
        str(N_W_1), 1, WHITE)
    M_W_1_text = HEALTH_FONT.render(
        str(M_W_1), 1, WHITE)
    W_W_1_text = HEALTH_FONT.render(
        str(W_W_1), 1, WHITE)
    N_W_2_text = HEALTH_FONT.render(
        str(N_W_2), 1, WHITE)
    M_W_2_text = HEALTH_FONT.render(
        str(M_W_2), 1, WHITE)
    W_W_2_text = HEALTH_FONT.render(
        str(W_W_2), 1, WHITE)

    
    WIN.blit(N_S_1_text, (MINE_WIDTH-10, HEIGHT-BARRAK_HEIGHT-210))
    WIN.blit(N_A_1_text, (MINE_WIDTH-10, HEIGHT-BARRAK_HEIGHT-250))
    WIN.blit(N_W_1_text, (MINE_WIDTH-10, HEIGHT-BARRAK_HEIGHT-290))
    WIN.blit(M_W_1_text, (20, HEIGHT-BARRAK_HEIGHT-180))
    WIN.blit(W_W_1_text, (400, HEIGHT-BARRAK_HEIGHT-230))
    
    WIN.blit(N_S_2_text, (WIDTH-MINE_WIDTH-BARRAK_WIDTH+50, HEIGHT-BARRAK_HEIGHT-210))
    WIN.blit(N_A_2_text, (WIDTH-MINE_WIDTH-BARRAK_WIDTH+50, HEIGHT-BARRAK_HEIGHT-250))
    WIN.blit(N_W_2_text, (WIDTH-MINE_WIDTH-BARRAK_WIDTH+50, HEIGHT-BARRAK_HEIGHT-290))
    WIN.blit(M_W_2_text, (WIDTH-100, HEIGHT-BARRAK_HEIGHT-180))
    WIN.blit(W_W_2_text, (WIDTH-500, HEIGHT-BARRAK_HEIGHT-230))

    WIN.blit(SWORD, (MINE_WIDTH-10+30, HEIGHT-BARRAK_HEIGHT-210))
    WIN.blit(SWORD, (WIDTH-MINE_WIDTH-BARRAK_WIDTH+50+30, HEIGHT-BARRAK_HEIGHT-210))

    WIN.blit(BOW, (MINE_WIDTH-10+30, HEIGHT-BARRAK_HEIGHT-250))
    WIN.blit(BOW, (WIDTH-MINE_WIDTH-BARRAK_WIDTH+50+30, HEIGHT-BARRAK_HEIGHT-250))

    WIN.blit(PICKAXE, (MINE_WIDTH-10+30, HEIGHT-BARRAK_HEIGHT-290))
    WIN.blit(PICKAXE, (WIDTH-MINE_WIDTH-BARRAK_WIDTH+50+30, HEIGHT-BARRAK_HEIGHT-290))
    WIN.blit(PICKAXE, (20+30, HEIGHT-BARRAK_HEIGHT-180))
    WIN.blit(PICKAXE, (400+30, HEIGHT-BARRAK_HEIGHT-230))
    WIN.blit(PICKAXE, (WIDTH-100+30, HEIGHT-BARRAK_HEIGHT-180))
    WIN.blit(PICKAXE, (WIDTH-500+30, HEIGHT-BARRAK_HEIGHT-230))

    WIN.blit(RESOURCES, (280,10))
    WIN.blit(RESOURCES, (WIDTH-60,10))
    
    WIN.blit(BARRAK_1, (MINE_WIDTH-20, HEIGHT-BARRAK_HEIGHT-150))
    WIN.blit(BARRAK_2, (WIDTH-MINE_WIDTH-BARRAK_WIDTH+20, HEIGHT-BARRAK_HEIGHT-150))

    WIN.blit(MINE_1, (0, HEIGHT-BARRAK_HEIGHT-150-(MINE_HEIGHT-BARRAK_HEIGHT)))
    WIN.blit(MINE_2, (WIDTH-MINE_WIDTH, HEIGHT-BARRAK_HEIGHT-150-(MINE_HEIGHT-BARRAK_HEIGHT)))

    WIN.blit(TOWER_1, (MINE_WIDTH+BARRAK_WIDTH-70, HEIGHT-BARRAK_HEIGHT-380))
    WIN.blit(TOWER_2, (WIDTH-MINE_WIDTH-BARRAK_WIDTH-WALL_WIDTH+170, HEIGHT-BARRAK_HEIGHT-380))

    WIN.blit(WALL_1, (MINE_WIDTH+BARRAK_WIDTH, HEIGHT-BARRAK_HEIGHT-180))
    WIN.blit(WALL_2, (WIDTH-MINE_WIDTH-BARRAK_WIDTH-WALL_WIDTH, HEIGHT-BARRAK_HEIGHT-180))



tower_archer_1 = pygame.sprite.Group()
tower_archer_1.add(TOWER_ARCHER_1())
tower_archer_2 = pygame.sprite.Group()
tower_archer_2.add(TOWER_ARCHER_2())

archers_1= pygame.sprite.Group()
archers_2= pygame.sprite.Group()

swordsmen_1= pygame.sprite.Group()
swordsmen_2= pygame.sprite.Group()

walls_1=pygame.sprite.Group()
walls_2=pygame.sprite.Group()
walls_1.add(wall_1())
walls_2.add(wall_2())

all_sprites_1 = pygame.sprite.Group()
all_sprites_2 = pygame.sprite.Group()
all_sprites_1.add(wall_1())
all_sprites_2.add(wall_2())

arrows_1=pygame.sprite.Group()
arrows_2=pygame.sprite.Group()

workers_wall_1=pygame.sprite.Group()
workers_wall_2=pygame.sprite.Group()
workers_mine_1=pygame.sprite.Group()
workers_mine_2=pygame.sprite.Group()


def train_swordsman_1(keys_pressed):
    global N_S_1
    global resources_1
    if keys_pressed[pygame.K_w] and resources_1 >= 10:
        resources_1 += -10
        N_S_1 += 1
        pygame.time.delay(100)

def train_swordsman_2(keys_pressed):
    global N_S_2
    global resources_2
    if keys_pressed[pygame.K_o] and resources_2 >= 10:
        resources_2 += -10
        N_S_2 += 1
        pygame.time.delay(100)

def train_archer_1(keys_pressed):
    global N_A_1
    global resources_1
    if keys_pressed[pygame.K_e] and resources_1 >= 10:
        resources_1 += -10
        N_A_1 += 1
        pygame.time.delay(100)

def train_archer_2(keys_pressed):
    global N_A_2
    global resources_2
    if keys_pressed[pygame.K_i] and resources_2 >= 10:
        resources_2 += -10
        N_A_2 += 1
        pygame.time.delay(100)

def train_worker_1(keys_pressed):
    global N_W_1
    global resources_1
    if keys_pressed[pygame.K_q] and resources_1 >= 10:
        resources_1 += -1
        N_W_1 += 1
        pygame.time.delay(100)

def train_worker_2(keys_pressed):
    global N_W_2
    global resources_2
    if keys_pressed[pygame.K_p] and resources_2 >= 10:
        resources_2 += -1
        N_W_2 += 1
        pygame.time.delay(100)

def spawn_worker_wall_1(keys_pressed):
    global N_W_1
    global W_W_1
    if keys_pressed[pygame.K_s] and  N_W_1> 0:
        workers_wall_1.add(WORKER_WALL_1())
        N_W_1 += -1
        W_W_1 += 1
        pygame.time.delay(60)

def spawn_worker_wall_2(keys_pressed):
    global N_W_2
    global W_W_2
    if keys_pressed[pygame.K_k] and  N_W_2 > 0:
        workers_wall_2.add(WORKER_WALL_2())
        N_W_2 += -1
        W_W_2 += 1
        pygame.time.delay(60)

def spawn_worker_mine_1(keys_pressed):
    global N_W_1
    global M_W_1
    if keys_pressed[pygame.K_a] and  N_W_1 > 0:
        workers_mine_1.add(WORKER_MINE_1())
        N_W_1 += -1
        M_W_1 += 1
        pygame.time.delay(60)

def spawn_worker_mine_2(keys_pressed):
    global N_W_2
    global M_W_2
    if keys_pressed[pygame.K_l] and  N_W_2> 0:
        workers_mine_2.add(WORKER_MINE_2())
        N_W_2 += -1
        M_W_2 += 1
        pygame.time.delay(60)
               
def spawn_swordsman_1(keys_pressed):
    global N_S_1
    if keys_pressed[pygame.K_d] and N_S_1 > 0:
        all_sprites_1.add(SWORDSMAN_1())
        swordsmen_1.add(SWORDSMAN_1())
        N_S_1 += -1
        pygame.time.delay(60)

def spawn_swordsman_2(keys_pressed):
    global N_S_2
    if keys_pressed[pygame.K_j] and N_S_2 > 0:
        all_sprites_2.add(SWORDSMAN_2())
        swordsmen_2.add(SWORDSMAN_2())
        N_S_2 += -1
        pygame.time.delay(60)

def spawn_archer_1(keys_pressed):
    global N_A_1
    if keys_pressed[pygame.K_f] and N_A_1 > 0:
        all_sprites_1.add(ARCHER_1())
        archers_1.add(ARCHER_1())
        N_A_1 += -1
        pygame.time.delay(60)

def spawn_archer_2(keys_pressed):
    global N_A_2
    if keys_pressed[pygame.K_h] and N_A_2 > 0:
        all_sprites_2.add(ARCHER_2())
        archers_2.add(ARCHER_2())
        N_A_2 += -1
        pygame.time.delay(60)

def unleash_1(keys_pressed):
    global N_A_1
    global N_S_1
    global N_W_1
    if keys_pressed[pygame.K_z]:
        for swordsman in range(N_S_1):
            all_sprites_1.add(SWORDSMAN_1())
            swordsmen_1.add(SWORDSMAN_1())
            N_S_1 += -1
        for archer in range(N_A_1):
            all_sprites_1.add(ARCHER_1())
            archers_1.add(ARCHER_1())
            N_A_1 += -1
        for worker in range(N_W_1):
            workers_wall_1.add(WORKER_WALL_1())
            N_W_1 += -1
        
        pygame.time.delay(60)

def unleash_2(keys_pressed):
    global N_A_2
    global N_S_2
    global N_W_2
    if keys_pressed[pygame.K_m]:
        for swordsman in range(N_S_2):
            all_sprites_2.add(SWORDSMAN_2())
            swordsmen_2.add(SWORDSMAN_2())
            N_S_2 += -1
        for archer in range(N_A_2):
            all_sprites_2.add(ARCHER_2())
            archers_2.add(ARCHER_2())
            N_A_2 += -1
        for worker in range(N_W_2):
            workers_wall_2.add(WORKER_WALL_2())
            N_W_2 += -1
        
        pygame.time.delay(60)

def paused(keys_pressed):
    global pause
    if keys_pressed[pygame.K_SPACE]:
        pause = not pause
        pygame.time.delay(60)

def load_state(keys_pressed):
    if keys_pressed[pygame.K_b]:
        global resources_1
        global resources_2
        global N_S_1
        global N_S_2
        global N_A_1
        global N_A_2
        global N_W_1
        global N_W_2
        with open('state.txt') as state_file:
            state = json.load(state_file)

        resources_1=state["resources_1"]
        resources_2=state["resources_2"]
        
        N_S_1=state["N_S_1"]
        N_S_2=state["N_S_2"]
        N_A_1=state["N_A_1"]
        N_A_2=state["N_A_2"]
        N_W_1=state["N_W_1"]
        N_W_2=state["N_W_2"]
        
        num_swordsmen_1=state["num_swordsmen_1"]
        for ns in range(num_swordsmen_1):
            all_sprites_1.add(SWORDSMAN_1())
            swordsmen_1.add(SWORDSMAN_1()) 
        
        num_swordsmen_2=state["num_swordsmen_2"]
        for ns in range(num_swordsmen_2):
            all_sprites_2.add(SWORDSMAN_2())
            swordsmen_2.add(SWORDSMAN_2())
            
        
        num_archers_1=state["num_archers_1"]
        for na in range(num_archers_1):
            all_sprites_1.add(ARCHER_1())
            archers_1.add(ARCHER_1())
        
        num_archers_2=state["num_archers_2"]
        for na in range(num_archers_2):
            all_sprites_2.add(ARCHER_2())
            archers_2.add(ARCHER_2())
        
        num_workers_mine_1=state["num_workers_mine_1"]
        for nw in range(num_workers_mine_1):
            workers_mine_1.add(WORKER_MINE_1())
            
        num_workers_mine_2=state["num_workers_mine_2"]
        for nw in range(num_workers_mine_2):
            workers_wmine_2.add(WORKER_MINE_2())
        
        num_workers_wall_1=state["num_workers_wall_1"]
        for nw in range(num_workers_wall_1):
            workers_wall_1.add(WORKER_WALL_1())
        
        num_workers_wall_2=state["num_workers_wall_2"]
        for nw in range(num_workers_wall_2):
            workers_wall_2.add(WORKER_WALL_2())

        
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

milliseconds_delay = 500 # 0.5 seconds
worker_delay= 1000

arrow_event_1 = pygame.USEREVENT + 1
arrow_event_2 = pygame.USEREVENT + 2
sword_event_1 = pygame.USEREVENT + 3
sword_event_2 = pygame.USEREVENT + 4

pygame.time.set_timer(arrow_event_2, milliseconds_delay)
pygame.time.set_timer(arrow_event_1, milliseconds_delay)
pygame.time.set_timer(sword_event_2, milliseconds_delay)
pygame.time.set_timer(sword_event_1, milliseconds_delay)


diag_arrow_event_1 = pygame.USEREVENT + 9

diag_arrow_event_2 = pygame.USEREVENT + 10

pygame.time.set_timer(diag_arrow_event_2, milliseconds_delay)
pygame.time.set_timer(diag_arrow_event_1, milliseconds_delay)

gain_health_event_1 = pygame.USEREVENT + 11
pygame.time.set_timer(gain_health_event_1, worker_delay)

gain_health_event_2 = pygame.USEREVENT + 12
pygame.time.set_timer(gain_health_event_2, worker_delay)

gain_resources_event_1 = pygame.USEREVENT + 13
pygame.time.set_timer(gain_resources_event_1, worker_delay)

gain_resources_event_2 = pygame.USEREVENT + 14
pygame.time.set_timer(gain_resources_event_2, worker_delay)




#INITIAL_STATE

N_S_1=1
N_S_2=1
N_A_1=1
N_A_2=1
N_W_1=1
N_W_2=1
M_W_1=0
M_W_2=0
W_W_1=0
W_W_2=0

resources_1 = 15
resources_2 = 15

pause=False
  

def main():
    
    global pause 

    clock = pygame.time.Clock()
    run = True
    
    while pause == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        paused(keys_pressed)  
    

    while run and not pause:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                global resources_1
                global resources_2
                global N_S_1
                global N_S_2
                global N_A_1
                global N_A_2
                global N_W_1
                global N_W_2
                
                wall_health_1=1000
                for wall_1 in walls_1:
                    wall_health_1= wall_1.health
                    
                wall_health_2=1000
                for wall_2 in walls_2:
                    wall_health_2= wall_2.health
                    
                num_swordsmen_1=0
                for swordsman_1 in swordsmen_1:
                    num_swordsmen_1 += 1
                    
                num_archers_1=0
                for archer_1 in archers_1:
                    num_archers_1 += 1
                    
                num_workers_mine_1=0
                for worker_mine_1 in workers_mine_1:
                    num_workers_mine_1 += 1
                    
                num_workers_wall_1=0
                for worker_wall_1 in workers_wall_1:
                    num_workers_wall_1 += 1
                
                num_swordsmen_2=0
                for swordsman_2 in swordsmen_2:
                    num_swordsmen_2 += 1
                
                num_archers_2=0
                for archer_2 in archers_2:
                    num_archers_2 += 1
                
                num_workers_mine_2=0
                for worker_mine_2 in workers_mine_2:
                    num_workers_mine_2 += 1
                    
                num_workers_wall_2=0
                for worker_wall_2 in workers_wall_2:
                    num_workers_wall_2 += 1
                
                state = {
                    'resources_1':resources_1,
                    'resources_2':resources_2,
                    'wall_health_1':wall_health_1,
                    'wall_health_2':wall_health_2,
                    'N_S_1':N_S_1,
                    'N_S_2':N_S_2,
                    'N_A_1':N_A_1,
                    'N_A_2':N_A_2,
                    'N_W_1':N_W_1,
                    'N_W_2':N_W_2,
                    'num_swordsmen_1':num_swordsmen_1,
                    'num_swordsmen_2':num_swordsmen_2,
                    'num_archers_1':num_archers_1,
                    'num_archers_2':num_archers_2,
                    'num_workers_mine_1':num_workers_mine_1,
                    'num_workers_mine_2':num_workers_mine_2,
                    'num_workers_wall_1':num_workers_wall_1,
                    'num_workers_wall_2':num_workers_wall_2
                    }
                
                with open('state.txt','w') as state_file:
                    json.dump(state,state_file)
                    
                pygame.quit()
            
                
            elif event.type == arrow_event_2:
                for ARCHER_2 in archers_2:
                    if ARCHER_2.range_2==True:
                        ARCHER_2.shoot()
                    
            elif event.type == arrow_event_1:
                for ARCHER_1 in archers_1:
                    if ARCHER_1.range_1==True:
                        ARCHER_1.shoot()

            elif event.type == diag_arrow_event_2:
                for TOWER_ARCHER_2 in tower_archer_2:
                    if TOWER_ARCHER_2.range_2==True:
                        TOWER_ARCHER_2.shoot()
                    
            elif event.type == diag_arrow_event_1:
                for TOWER_ARCHER_1 in tower_archer_1:
                    if TOWER_ARCHER_1.range_1==True:
                        TOWER_ARCHER_1.shoot()

            elif event.type == sword_event_2:
                for SWORDSMAN_2 in swordsmen_2:
                    if pygame.sprite.spritecollide(SWORDSMAN_2,all_sprites_1,False):                    
                        sword_hit_list = pygame.sprite.spritecollide(SWORDSMAN_2,all_sprites_1, False)
                        for enemy in sword_hit_list:
                            enemy.gets_hit_by_sword()
                    
            elif event.type == sword_event_1:
                for SWORDSMAN_1 in swordsmen_1:
                    if pygame.sprite.spritecollide(SWORDSMAN_1,all_sprites_2,False):                    
                        sword_hit_list = pygame.sprite.spritecollide(SWORDSMAN_1,all_sprites_2, False)
                        for enemy in sword_hit_list:
                            enemy.gets_hit_by_sword()


            elif event.type == gain_health_event_2:
                for WORKER_2 in workers_wall_2:
                    for WALL_2 in walls_2:
                        WALL_2.health += 1
                    
            elif event.type == gain_health_event_1:
                for WORKER_1 in workers_wall_1:
                    for WALL_1 in walls_1:
                        WALL_1.health += 1

            elif event.type == gain_resources_event_2:
                for WORKER_2 in workers_mine_2:
                    resources_2 += 1
                    
            elif event.type == gain_resources_event_1:
                for WORKER_1 in workers_mine_1:
                    resources_1 += 1

        
                    

        tower_archer_1.update()
        tower_archer_1.draw(WIN)
        tower_archer_2.update()
        tower_archer_2.draw(WIN)
        
        all_sprites_1.add(swordsmen_1)
        all_sprites_1.add(archers_1)
        all_sprites_1.add(walls_1)
        
        all_sprites_2.add(swordsmen_2)
        all_sprites_2.add(archers_2)
        all_sprites_2.add(walls_2)
        
        all_sprites_1.update()
        all_sprites_1.draw(WIN)
        
        all_sprites_2.update()
        all_sprites_2.draw(WIN)
        
        arrows_1.update()
        arrows_1.draw(WIN)
        arrows_2.update()
        arrows_2.draw(WIN)
        
        workers_mine_1.update()
        workers_mine_1.draw(WIN)
        workers_mine_2.update()
        workers_mine_2.draw(WIN)
        workers_wall_1.update()
        workers_wall_1.draw(WIN)
        workers_wall_2.update()
        workers_wall_2.draw(WIN)
        
        pygame.display.flip()
        winner_text = ""
        
        for wall_1 in walls_1 :
            if wall_1.health <= 0:
                winner_text = "Player 1 Wins!"

        for wall_2 in walls_2 :
            if wall_2.health <= 0:
                winner_text = "Player 2 Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break
        

        keys_pressed = pygame.key.get_pressed()
        spawn_swordsman_1(keys_pressed)
        spawn_swordsman_2(keys_pressed)
        spawn_archer_1(keys_pressed)
        spawn_archer_2(keys_pressed)
        train_swordsman_1(keys_pressed)
        train_swordsman_2(keys_pressed)
        train_archer_1(keys_pressed)
        train_archer_2(keys_pressed)
        train_worker_1(keys_pressed)
        train_worker_2(keys_pressed)
        spawn_worker_mine_1(keys_pressed)
        spawn_worker_mine_2(keys_pressed)
        spawn_worker_wall_1(keys_pressed)
        spawn_worker_wall_2(keys_pressed)
        paused(keys_pressed)
        load_state(keys_pressed)
        unleash_1(keys_pressed)
        unleash_2(keys_pressed)
        
        
        draw_window(N_S_1,N_S_2,N_A_1,N_A_2,N_W_1,N_W_2,M_W_1,M_W_2,W_W_1,W_W_2)

        for wall_1 in walls_1:
            pygame.draw.rect(WIN, RED, pygame.Rect(30, HEIGHT-50, int(wall_1.health)/2, 30))

        for wall_2 in walls_2:
            pygame.draw.rect(WIN, RED, pygame.Rect((WIDTH-(int(wall_2.health)/2))-30, HEIGHT-50, int(wall_2.health)/2, 30))
        
        for SWORDSMAN_1 in all_sprites_1:
            if pygame.sprite.spritecollide(SWORDSMAN_1,all_sprites_2,False):
               SWORDSMAN_1.collision_1()
               
            else:
                SWORDSMAN_1.not_collision_1()
                


        for SWORDSMAN_2 in all_sprites_2:
            if pygame.sprite.spritecollide(SWORDSMAN_2,all_sprites_1,False):
                SWORDSMAN_2.collision_2()

            else:
                SWORDSMAN_2.not_collision_2()
        
                

        for SWORDSMAN_2 in all_sprites_2:
            if SWORDSMAN_2.health<=0:
                SWORDSMAN_2.kill()

        for SWORDSMAN_1 in all_sprites_1:
            if SWORDSMAN_1.health<=0:
                SWORDSMAN_1.kill()


                
        for ARCHER_1 in all_sprites_1:
            for ARCHER_2 in all_sprites_2:
                if math.fabs(ARCHER_2.rect.x-ARCHER_1.rect.x)<300:
                    ARCHER_1.in_range_1()
                elif math.fabs(ARCHER_2.rect.x-ARCHER_1.rect.x)>=300:
                    ARCHER_1.not_in_range_1()
                    
        for ARCHER_2 in all_sprites_2:
            for ARCHER_1 in all_sprites_1:
                if math.fabs(ARCHER_1.rect.x-ARCHER_2.rect.x)<300:
                    ARCHER_2.in_range_2() 
                elif math.fabs(ARCHER_1.rect.x-ARCHER_2.rect.x)>=300:
                    ARCHER_2.not_in_range_2()

        for TOWER_ARCHER_1 in tower_archer_1:
            for ARCHER_2 in all_sprites_2:
                if math.fabs(ARCHER_2.rect.x-TOWER_ARCHER_1.rect.x)<300:
                    TOWER_ARCHER_1.in_range_1()
                elif math.fabs(ARCHER_2.rect.x-TOWER_ARCHER_1.rect.x)>=300:
                    TOWER_ARCHER_1.not_in_range_1()
                    
        for TOWER_ARCHER_2 in tower_archer_2:
            for ARCHER_1 in all_sprites_1:
                if math.fabs(ARCHER_1.rect.x-TOWER_ARCHER_2.rect.x)<300:
                    TOWER_ARCHER_2.in_range_2() 
                elif math.fabs(ARCHER_1.rect.x-TOWER_ARCHER_2.rect.x)>=300:
                    TOWER_ARCHER_2.not_in_range_2()



        for ARCHER_1 in all_sprites_1:
            if pygame.sprite.spritecollide(ARCHER_1,all_sprites_2,False):
                ARCHER_1.collision_1() 
            elif not(pygame.sprite.spritecollide(ARCHER_1,all_sprites_2,False)) and ARCHER_1.range_1==False:
                ARCHER_1.not_collision_1()

        for ARROW_1 in arrows_1:
            if pygame.sprite.spritecollide(ARROW_1,all_sprites_2,False):
                ARROW_1.kill()
                arrow_hit_list = pygame.sprite.spritecollide(ARROW_1,all_sprites_2 , False)
                for enemy in arrow_hit_list:
                    enemy.gets_hit_by_arrow()
                    pygame.time.delay(1)

                
        for ARROW_2 in arrows_2:
            if pygame.sprite.spritecollide(ARROW_2,all_sprites_1,False):
                ARROW_2.kill()
                arrow_hit_list = pygame.sprite.spritecollide(ARROW_2,all_sprites_1 , False)
                for enemy in arrow_hit_list:
                    enemy.gets_hit_by_arrow()
                    pygame.time.delay(1)

        for DIAG_ARROW_1 in arrows_1:
            if pygame.sprite.spritecollide(DIAG_ARROW_1,all_sprites_2,False):
                DIAG_ARROW_1.kill()
                arrow_hit_list = pygame.sprite.spritecollide(DIAG_ARROW_1,all_sprites_2 , False)
                for enemy in arrow_hit_list:
                    enemy.gets_hit_by_arrow()
                    pygame.time.delay(1)

                
        for DIAG_ARROW_2 in arrows_2:
            if pygame.sprite.spritecollide(DIAG_ARROW_2,all_sprites_1,False):
                DIAG_ARROW_2.kill()
                arrow_hit_list = pygame.sprite.spritecollide(ARROW_2,all_sprites_1 , False)
                for enemy in arrow_hit_list:
                    enemy.gets_hit_by_arrow()
                    pygame.time.delay(1)
            
                  

    main()


if __name__ == "__main__":
    main()
