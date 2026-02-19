import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickable Squares")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

