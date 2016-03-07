import pygame
import math
import sys
from pygame import *
import random
import dumbmenu as dm
DISPLAY = (1500, 1400)
DEPTH = 32
FLAGS = 0

def main():
    pygame.init()
    screen = display.set_mode(DISPLAY, FLAGS, DEPTH)
    display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()
    up = down = left = right = attack = False
    entities = pygame.sprite.Group()
    platforms = []
    level_num = 4
    x = y = 0
    time_passed = 0
    level = [
    "PPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P               P       P",
    "P              RP       P",
    "P            PPPP       P",
    "P                       F",
    "Pf         P          b F",
    "PPPPPPPPPPPPPPPPPPPPPPPPP"]

    level1 = [
    "PPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "B                       F",
    "Bf                    b F",
    "PPPPPPPPPPllPPPPPPPPPPPPP"]

    level2 = [
    "PPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "P                       P",
    "B                       F",
    "Bf                xP  b F",
    "PPPPPPPPPPPPPPPPPPPPPPPPP"]

    level3 = [
    "PPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                       P",
    "P                       P",
    "P                       F",
    "P                     b F",
    "P                     PPP",
    "P                       P",
    "P                   P   P",
    "P                   PlllP",
    "P                 PPPPPPP",
    "P                 P     P",
    "P       PllllPP         P",
    "P      PPPPPPPPP        P",
    "PP           P          P",
    "PPPP         P  P       P",
    "PPPPPP       P   P      P",
    "P         PPPP          P",
    "B       PPP         PlllP",
    "Bf    PPP         xPllllP",
    "PPPPPPPPPPPPPPPPPPPPPPPPP"]

    level4 = [
    "PPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                       P",
    "P                       P",
    "B                       P",
    "Bf                      P",
    "PPP                     P",
    "P                       P",
    "P                       P",
    "P                   PlllP",
    "H                   PlllP",
    "H                   PlllP",
    "PP      PllllPP     PlllP",
    "PllllllPPPPPPPP   PPPPPPP",
    "PPlllllllllllP          P",
    "PPPPlllllllllP          P",
    "PPPPPPPllllllP x     S  P",
    "P     PPPPPPPPPPPPPPP   P",
    "F                       P",
    "F b                 x   P",
    "PPPPPPPPPPPPPPPPPPPPPPPPP"]

    shop = [
    "PPPPPPPPPPP",
    "P         P"
    "P         P",
    "P         P",
    "P         P",
    "P         P",
    "P         B",
    "PR     f  B",
    "PPPPPPPPPPP"
    ]

    choose = dm.dumbmenu(screen, [
                        'Start Game',
                        'Quit Game'], 128, 128, None, 64, 1.4, (255, 255, 255), (255, 0, 0))
    if choose == 1:
        pygame.quit()

    levels = [shop, level, level1, level2, level3, level4]

    player = Player(0, 0)
    time_passed = 0
    player.win = True
    shopping = False
    while 1:
        screen.fill((0, 0, 0))
        print level_num
        level_current = levels[level_num]
        if player.shop:
            level_current = levels[0]
        player_start = [0, 0]
        enemy_list = []
        blockers = []
        for row in level_current:
            for col in row:
                if col == "P" or col == "p":
                    p = Platform(x, y)
                    platforms.append(p)
                    entities.add(p)
                if col == "S":
                    s = Blocker(x, y)
                    blockers.append(s)
                if col == "H":
                    s = Shop(x, y)
                    platforms.append(s)
                if col == "R":
                    s = Merchant(x, y)
                    platforms.append(s)
                    entities.add(s)
                if col == "F":
                    e = ExitBlock(x, y)
                    platforms.append(e)
                    entities.add(e)
                if col == "B":
                    e = BackBlock(x, y)
                    platforms.append(e)
                    entities.add(e)
                if col == "l":
                    l = LavaBlock(x,y)
                    platforms.append(l)
                    entities.add(l)
                if col == "x":
                    enemy = Enemy(x,y)
                    enemy_list.append(enemy)
                    entities.add(enemy)
                if col == "b" and player.back:
                    player_start = [x,y]
                if col == "f" and (player.win or player.shop):
                    player_start = [x, y]
                    print player_start
                x += 50
            y += 50
            x = 0

        player.shop = False
        entities.add(player)
        player.rect.bottomleft = (player_start[0], player_start[1])
        while 1:
            for e in pygame.event.get():
                if e.type == QUIT: pygame.quit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit()
                if e.type == KEYDOWN and e.key == K_UP:
                    up = True
                if e.type == KEYDOWN and e.key == K_DOWN:
                    down = True
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True
                if e.type == KEYDOWN and e.key == K_a:
                    attack = True

                if e.type == KEYUP and e.key == K_UP:
                    up = False
                if e.type == KEYUP and e.key == K_DOWN:
                    down = False
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False
                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                if e.type == KEYUP and e.key == K_a:
                    attack = False

            screen.fill((0,0,0))

            player.update(up, down, left, right, attack, platforms, enemy_list, entities, timer)
            for enemy in enemy_list:
                enemy.update(platforms, blockers)
            for projectile in player.projectiles:
                projectile.update()
                projectile.collide(enemy_list, platforms, entities, player)

            if player.dead:
                entities.empty()
                x = y = 0
                platforms = []
                enemy_list = []
                level_num = 0
                player.dead = False
                player.win = True
                break

            elif player.win:
                level_num += 1
                entities.empty()
                x = y = 0
                platforms = []
                enemy_list = []
                break

            elif player.back:
                if not shopping:
                    level_num -= 1
                shopping = False
                entities.empty()
                x = y = 0
                platforms = []
                enemy_list = []
                break

            elif player.shop:
                shopping = True
                entities.empty()
                x = y = 0
                platforms = []
                enemy_list = []
                break

            #screen.fill((0,0,0))
            entities.draw(screen)
            pygame.display.flip()
            timer.tick(30)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class shadow_bolt(Entity):
    def __init__(self, x, y, dir):
        self.rect = Rect(x,y,30,30)
        self.image = pygame.image.load("Fire1.png")
        self.anim_count = 0
        self.anim = ("Fire1.png", "Fire2.png", "Fire3.png")
        self.dir = dir
        Entity.__init__(self)

    def update(self):
        self.anim_count += 1
        if self.anim_count > 18:
            self.anim_count = 0
        self.rect.left += self.dir*16
        self.image = pygame.image.load(self.anim[self.anim_count/9])

    def collide(self, enemy_list, platforms, entities, player):
        for p in platforms:
            if sprite.collide_rect(self, p):
                entities.remove(self)
                player.projectiles.remove(self)
                del self
                return
        for e in enemy_list:
            if sprite.collide_rect(self, e):
                entities.remove(self)
                player.projectiles.remove(self)
                entities.remove(e)
                enemy_list.remove(e)
                del e
                del self
                return

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.x_vel = 0
        self.y_vel = 0
        self.anim_count = 0
        self.on_ground = False
        self.walking = ("Xeno/Walk/1.png", "Xeno/Walk/2.png", 'Xeno/Walk/3.png', 'Xeno/Walk/4.png')
        self.attacking = []
        self.anim = self.walking
        for i in range(0, 15):
            self.attacking.append("Xeno/Fight/"+str(i)+".png")
        self.image = Surface((100, 100))
        self.image.convert_alpha()
        self.rect = Rect(x, y, 80, 80)
        self.dead = False
        self.win = False
        self.shop = False
        self.back = False
        self.projectiles = []
        self.dir = 1
        self.attack_time = 0
        self.anim_max = 18
        self.anim_iter = 6
        self.inv = []
        self.gold = 250

    def update(self, up, down, left, right, attack, platforms, enemy_list, entities, timer):
        if self.anim == self.attacking:
            if self.anim_count >= 8:
                self.anim = self.walking
                self.anim_max = 18
                self.anim_iter = 6
                self.anim_count = 0
        kill = None
        self.win = False
        self.back = False
        if up:
            # only jump if on the ground
            if self.on_ground: self.y_vel -= 20
        if down:
            pass
        if left:
            self.x_vel = -10
            self.anim_count += 1
            if self.anim_count > self.anim_max:
                self.anim_count = 0
            anim_image = pygame.image.load(self.anim[self.anim_count/self.anim_iter]).convert_alpha()
            self.image = anim_image
            self.image = pygame.transform.flip(self.image, True, False)
            self.dir = -1
        if right:
            self.x_vel = 10
            self.anim_count += 1
            if self.anim_count > self.anim_max:
                self.anim_count = 0
            anim_image = pygame.image.load(self.anim[self.anim_count/self.anim_iter]).convert_alpha()
            self.image = anim_image
            self.dir = 1
        if not self.on_ground:
            # fall if not on the ground
            self.y_vel += 1.5
            if up:
                self.y_vel -= 0.1
            # cant fall faster than 30
            if self.y_vel > 30: self.y_vel = 30
        if not(left or right):
            self.x_vel = 0
            if self.anim == self.attacking:
                self.anim_count += 1
                if self.anim_count > self.anim_max:
                    self.anim_count=0
                anim_image = pygame.image.load(self.anim[self.anim_count/self.anim_iter]).convert_alpha()
                self.image = anim_image
                if self.dir == -1:
                    self.image = pygame.transform.flip(self.image, True, False)
        if attack and pygame.time.get_ticks() > self.attack_time+1000:
            self.anim = self.attacking
            self.anim_iter = 2
            self.anim_max = 8
            self.attack(left, right, entities)
            self.attack_time = pygame.time.get_ticks()
        else:
            pass
        # move x
        self.rect.left += self.x_vel
        # check collisions in x
        self.collide(self.x_vel, 0, platforms, enemy_list)
        # move y
        self.rect.top += self.y_vel
        # set us not on ground
        self.on_ground = False;
        # check collisions in y
        self.collide(0, self.y_vel, platforms, enemy_list)

        return kill

    def attack(self, left, right, entities):
        if self.dir == -1:
            projectile = shadow_bolt(self.rect.left+10, self.rect.bottom-50, self.dir)
        if self.dir ==  1:
            projectile = shadow_bolt(self.rect.right-10, self.rect.bottom-50, self.dir)
        entities.add(projectile)
        self.projectiles.append(projectile)


    def collide(self, x_vel, y_vel, platforms, enemy_list):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, LavaBlock):
                    self.dead = True
                if isinstance(p, ExitBlock):
                    self.win = True
                if isinstance(p, BackBlock):
                    self.back = True
                if isinstance(p, Shop):
                    self.shop = True
                if x_vel > 0: self.rect.right = p.rect.left
                if x_vel < 0: self.rect.left = p.rect.right
                if y_vel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.y_vel = 0
                if y_vel < 0:
                    self.rect.top = p.rect.bottom
                    self.onRoof = True
                    self.y_vel = 0
                if y_vel < 0: self.rect.top = p.rect.bottom
        for enemy in enemy_list:
            if sprite.collide_rect(self, enemy):
                self.dead = True

class Enemy (Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.x_vel = 10
        self.stop = False
        self.image = pygame.image.load("enemy.png")
        self.on_ground=True
        #self.image.convert()
        #self.image.fill(Color("#00FF00"))
        self.rect = Rect(x, y, 50, 50)

    def update(self, platforms, blockers):
        if self.stop:
            # fall if not on the ground
            self.x_vel = 0-self.x_vel
        self.stop = False;

        # move x
        self.rect.left += self.x_vel
        # check collisions in x
        self.collide(self.x_vel, platforms, blockers)

    def collide(self, x_vel, platforms, blockers):
        for p in platforms + blockers:
            if sprite.collide_rect(self, p):
                if x_vel > 0:
                    self.rect.right = p.rect.left
                    self.stop = True
                    self.image = pygame.transform.flip(self.image, True, False)
                if x_vel < 0:
                    self.rect.left = p.rect.right
                    self.stop = True
                    self.image = pygame.transform.flip(self.image, True, False)

class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("background/obj_stoneblock00"+str(random.randrange(1, 10))+".png")
        self.rect = Rect(x, y, 50, 50)

    def update(self):
        pass



class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill((0,0,0))

class Blocker(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = ((0,0,0))


class Merchant(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("chest3.png")

class Shop(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill((0,0,0))

class BackBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill((0,0,0))

class LavaBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("lava.png")




#run the program		
main()