import sys
import pygame
import time
import math

pygame.init()

def xpos(t):
    '''Ballens posisjon som funksjon av tid i x-retning'''
    return 5 + 31*t - 3*t**2

def ypos(t):
    '''Ballens posisjon som funksjon av tid i y-retning'''
    return 12*t - 5*t**2

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 400
BALL_RADIUS = 10
SCALE_FACTOR = 10

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
RED = pygame.Color(255,0,0)
FORESTGREEN = pygame.Color(34,139,34)
SKYBLUE = pygame.Color(135, 206, 235)

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
screen.fill(FORESTGREEN)
pygame.display.set_caption('Oppgave 7: Utspark fra 5-meter')

clock = pygame.time.Clock()

t = 0
dt = 0.05
T_MAX = 2.4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Regner ut ny ballposisjon
    y = int(DISPLAY_HEIGHT - BALL_RADIUS - ypos(t)*SCALE_FACTOR - 100)
    x = xpos(t)*SCALE_FACTOR

    # Tegner himmelen på nytt for å slette forrige ballposisjon
    pygame.draw.rect(screen, SKYBLUE, (0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT - 100))
    # Tegner ball i ny posisjon
    pygame.draw.circle(screen, WHITE, (x, y), BALL_RADIUS)
    # Oppdaterer displayet
    pygame.display.flip()

    clock.tick(30) # FPS

    if t > T_MAX: 
        # Starter animasjonen på nytt. Liten bug: det ligger en flekk
        # av ballen igjen på banen, gidder ikke å fikse det :-)
        t = 0
    else:
        # Neste tidsskritt
        t += dt

