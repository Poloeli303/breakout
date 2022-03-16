import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Breakout.mum")

px = 320
py = 470

bx = 350
by = 250
bVx = 5
bVy = 5


class Brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
    def draw(self):
        if self.alive is True:
            pygame.draw.rect(screen, (255, 0, 0), (self.xpos, self.ypos, 50, 20), 2)
    def collide(self, x, y):
        if self.alive is True:
            if x+20 > self.xpos and x<self.xpos+50 and y+20 > self.ypos and y < self.ypos+20:
                self.alive = False
                return True

doExit = False
clock = pygame.time.Clock()

b1 = Brick(20,20)
b2 = Brick(80, 20)
b3 = Brick(140, 20)
b4 = Brick(200, 20)
b5 = Brick(260, 20)
b6 = Brick(320,20)
b7 = Brick(380, 20)
b8 = Brick(440, 20)
b9 = Brick(500, 20)
b10 = Brick(560, 20)
b11 = Brick (620, 20)
b12 = Brick(20,45)
b13 = Brick(80, 45)
b14 = Brick(140, 45)
b15 = Brick(200, 45)
b16 = Brick(260, 45)
b17 = Brick(320,45)
b18 = Brick(380, 45)
b19 = Brick(440, 45)
b20 = Brick(500, 45)
b21 = Brick(560, 45)
b22 = Brick (620, 45)
b23 = Brick(20,70)
b24 = Brick(80, 70)
b25 = Brick(140, 70)
b26 = Brick(200, 70)
b27 = Brick(260, 70)
b28 = Brick(320,70)
b29 = Brick(380, 70)
b30 = Brick(440, 70)
b31 = Brick(500, 70)
b32 = Brick(560, 70)
b33 = Brick (620, 70)

while not doExit:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        px -= 7
    if keys[pygame.K_RIGHT]:
        px+=7

    
    bx += bVx
    by += bVy
    
    if bx < 0 or bx + 20 > 700:
        bVx *= -1 
    if by < 0 or by + 20 > 500:
        bVy *= -1
        
    if b1.collide(bx, by):
        bVy *=-1
    if b2.collide(bx, by):
        bVy *=-1
    if b3.collide(bx, by):
        bVy *=-1
    if b4.collide(bx, by):
        bVy *=-1
    if b5.collide(bx, by):
        bVy *=-1
    if b6.collide(bx, by):
        bVy *=-1
    if b7.collide(bx, by):
        bVy *=-1
    if b8.collide(bx, by):
        bVy *=-1
    if b9.collide(bx, by):
        bVy *=-1
    if b10.collide(bx, by):
        bVy *=-1
    if b11.collide(bx, by):
        bVy *=-1
    if b12.collide(bx, by):
        bVy *=-1
    if b13.collide(bx, by):
        bVy *=-1
    if b14.collide(bx, by):
        bVy *=-1
    if b15.collide(bx, by):
        bVy *=-1
    if b16.collide(bx, by):
        bVy *=-1
    if b17.collide(bx, by):
        bVy *=-1
    if b18.collide(bx, by):
        bVy *=-1
    if b19.collide(bx, by):
        bVy *=-1
    if b20.collide(bx, by):
        bVy *=-1
    if b21.collide(bx, by):
        bVy *=-1
    if b22.collide(bx, by):
        bVy *=-1
    if b23.collide(bx, by):
        bVy *=-1
    if b24.collide(bx, by):
        bVy *=-1
    if b25.collide(bx, by):
        bVy *=-1
    if b26.collide(bx, by):
        bVy *=-1
    if b27.collide(bx, by):
        bVy *=-1
    if b28.collide(bx, by):
        bVy *=-1
    if b29.collide(bx, by):
        bVy *=-1
    if b30.collide(bx, by):
        bVy *=-1
    if b31.collide(bx, by):
        bVy *=-1
    if b32.collide(bx, by):
        bVy *=-1
    if b33.collide(bx, by):
        bVy *=-1
    if bx < px + 50 and by + 20 > py and by < py + 50:
        bVy *= -1

                    
    screen.fill((0,0,0)) 

    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
    b11.draw()
    b12.draw()
    b13.draw()
    b14.draw()
    b15.draw()
    b16.draw()
    b17.draw()
    b18.draw()
    b19.draw()
    b20.draw()
    b21.draw()
    b22.draw()
    b23.draw()
    b24.draw()
    b25.draw()
    b26.draw()
    b27.draw()
    b28.draw()
    b29.draw()
    b30.draw()
    b31.draw()
    b32.draw()
    b33.draw()

    pygame.draw.rect(screen, (255, 0, 0), (px, py, 50, 20), 2)
    pygame.draw.circle(screen, (0, 0, 255), (bx, by), 6)
    pygame.display.flip()
pygame.quit()
