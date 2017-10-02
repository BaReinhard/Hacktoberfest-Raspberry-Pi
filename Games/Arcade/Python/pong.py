# TITLE: pong.py
#
# Discription: Have endless fun playing pong on your raspberry pi against the computer.
#
# Language: python3
# 
# Dependency: pygame, use pip3 install pygame
# 
# Run: python3 pong.py
#
# Author: Alec Matthews
# 
# Date: 10/01/17

import pygame, sys, random
from pygame.locals import*


def ballDirection():
     direction = random.randint(0,1)
     return direction

def randBounce():
     bounceSpeed = random.randint(0, 6)
     return bounceSpeed

def randSpeed():
     speed = random.randint(-2, 7)
     return speed


pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ball = {'rect':pygame.Rect(390, 240, 20, 20),'dir':None}
paddlePlayer= pygame.Rect(40, 185, 20, 130)
paddleComp = pygame.Rect(740, 185, 20, 130)

moveUp = False
moveDown = False

#ball*
LEFT = 4
RIGHT = 6
UPLEFT = 7
DOWNLEFT = 1
UPRIGHT = 9
DOWNRIGHT = 3

MOVESPEED = 9

BALLSPEED = 13

bounce = None

direction = ballDirection()

if direction == 1:
    ballLeft = True
elif direction == 0:
    ballLeft = False

if ballLeft == True:
          ball['dir'] = LEFT
elif ballLeft == False:
          ball['dir'] = RIGHT

while True:
     
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
         if event.type == KEYDOWN:
             if event.key == K_UP or event.key == ord('w'):
                 moveUp = True
                 moveDown = False
             if event.key == K_DOWN or event.key == ord('s'):
                 moveUp = False
                 moveDown = True

         if event.type == KEYUP:
             if event.key == K_ESCAPE:
                 pygame.quit()
                 sys.exit()
             if event.key == K_UP or event.key == ord('w'):
                 moveUp = False
             if event.key == K_DOWN or event.key == ord('s'):
                 moveDown = False
                
     windowSurface.fill(BLACK)
    
     if moveDown and paddlePlayer.bottom < WINDOWHEIGHT:
         paddlePlayer.top += MOVESPEED
     if moveUp and paddlePlayer.top > 0:
         paddlePlayer.top -= MOVESPEED
        
     
     if ball['rect'].colliderect(paddlePlayer):
          direct = ballDirection()
          if direct == 0:   
               ball['dir'] = UPRIGHT
          elif direct == 1:
               ball['dir'] = DOWNRIGHT

     if ball['rect'].colliderect(paddleComp):
          directTwo = ballDirection()
          if directTwo == 0:
               ball['dir'] = UPLEFT
          elif directTwo == 1:
               ball['dir'] = DOWNLEFT
          
     if ball['rect'].top < 0:
          if ball['dir'] == UPLEFT:
               ball['dir'] = DOWNLEFT
          elif ball['dir'] == UPRIGHT:
               ball['dir'] = DOWNRIGHT
     if ball['rect'].bottom > WINDOWHEIGHT:
          if ball['dir'] == DOWNLEFT:
               ball['dir'] = UPLEFT
          elif ball['dir'] == DOWNRIGHT:
               ball['dir'] = UPRIGHT
          
     if ball['dir'] == LEFT:
          ball['rect'].left -= BALLSPEED
     if ball['dir'] == RIGHT:
          ball['rect'].left += BALLSPEED
     if ball['dir'] == UPRIGHT:
          bounce = randBounce()
          ball['rect'].left += BALLSPEED
          ball['rect'].top -= bounce
     if ball['dir'] == UPLEFT:
          bounce = randBounce()
          ball['rect'].left -= BALLSPEED
          ball['rect'].top -= bounce
     if ball['dir'] == DOWNRIGHT:
          bounce = randBounce()
          ball['rect'].left += BALLSPEED
          ball['rect'].top += bounce
     if ball['dir'] == DOWNLEFT:
          bounce = randBounce()
          ball['rect'].left -= BALLSPEED
          ball['rect'].top += bounce
     
     if ball['rect'].left < 0:
          ball['rect'].left = 390
          ball['rect'].top = 190
          direction = ballDirection()
          if direction == 1:
               ballLeft = True
          elif direction == 0:
               ballLeft = False
          if ballLeft == True:
               ball['dir'] = LEFT
          elif ballLeft == False:
               ball['dir'] = RIGHT
               
     if ball['rect'].left > WINDOWWIDTH:
          ball['rect'].left = 390
          ball['rect'].top = 190
          direction = ballDirection()
          if direction == 1:
               ballLeft = True
          elif direction == 0:
               ballLeft = False
          if ballLeft == True:
               ball['dir'] = LEFT
          elif ballLeft == False:
               ball['dir'] = RIGHT
               
     if paddleComp.bottom < WINDOWHEIGHT:
          if paddleComp.centery < ball['rect'].centery:
               speed = randSpeed()
               paddleComp.centery += speed
     if paddleComp.top > 0:
          if paddleComp.centery > ball['rect'].centery:
               speedTwo = randSpeed()
               paddleComp.centery -= speedTwo

     pygame.draw.line(windowSurface, WHITE, (400, 0),(400, WINDOWHEIGHT), 1)
     pygame.draw.rect(windowSurface, WHITE, paddlePlayer)
     pygame.draw.rect(windowSurface, WHITE, paddleComp)
     pygame.draw.rect(windowSurface, WHITE, ball['rect'])

     pygame.display.update()
     mainClock.tick(40)
