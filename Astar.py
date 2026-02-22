import pygame
import sys



pygame.init()
WIDTH, HEIGHT = 902, 1200
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
            "position":(x,y),
            "startorend":0
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
click = 1
while True:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for j in sq:
                if click == 1:
                    if j["rect"].collidepoint(event.pos):
                        j["select"] = not j["select"]
                        j["startorend"] = 1
                        click=2
                elif click == 2:
                    if j["rect"].collidepoint(event.pos):
                        j["select"] = not j["select"]
                        j["startorend"] = 2
                        click+=1
    start = sq[0]["position"]
    end = sq[0]["position"]
    for i in sq:
        color = (50, 50, 50)
        if i["startorend"] == 1:
            color = (255, 0, 0)
            start = i["position"]
            
            
        if i["startorend"] == 2:
            color = (0, 0, 255)
            end = i["position"]
            
        pygame.draw.rect(screen, color, i["rect"])
        pygame.draw.rect(screen, color, i["rect"])
        
    print (start)
    print(end)    
    pygame.display.flip()
    clock.tick(60)

"""
mouse_pos: gather the position of the mouse
first for loop is used to determine if the window is closed and if it is you quit the program
second for loop is drawing the squeres onto the screen using position and color
----------------------------------------------
"""



