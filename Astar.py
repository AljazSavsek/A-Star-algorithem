import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 902, 902
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickable Squares")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)
"""
--------------------MATRIX--------------------
here i create a matrix with which i then
create squeres in pygame.
"""
size = 10
padding = 2

sq=[]
for row in range(90):
    for col in range(90):
        x = col * (size + padding) + padding
        y = row * (size + padding) + padding
        rect = pygame.Rect(x,y,size,size)
        sq.append({
            "select":False,
            "rect": rect,
            "position":(x,y)
        })
"""
first i declere the size of squeres and the padding around them
row: is created with first for loop
col: is created with second for loop
rect: in a veriable with which i declare the position and size
sq[]: in which are saved the positions and type of squres it needs to create
----------------------------------------------
"""
#print (sq)
"""
---------------------MAIN---------------------
this is the part you need to create metrix on the screen 
"""
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

"""
mouse_pos: gather the position of the mouse
first for loop is used to determine if the window is closed and if it is you quit the program
second for loop is drawing the squeres onto the screen using position and color
----------------------------------------------
"""



