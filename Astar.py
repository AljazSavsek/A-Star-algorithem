import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 902, 902
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickable Squares")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

#------creating squers--------
size = 10
padding = 2

sq=[]
for row in range(90):
    for col in range(90):
        x = col * (size + padding) + padding
        y = row * (size + padding) + padding
        rect = pygame.Rect(x,y,size,size)
        sq.append({
            "rect": rect
        })

#print (sq)
# this is the main part which creates the metrix 
while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in sq:
        pygame.draw.rect(screen, (30, 30, 30), i["rect"])
        pygame.draw.rect(screen, (50, 50, 50), i["rect"])



    pygame.display.flip()
    clock.tick(60)