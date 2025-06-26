
import pygame
import time
import math
# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

size = 10

n = WIDTH // size 
m = HEIGHT //  size 

red = blue = green = 0


def init_matrix():
    matrix = []
    for _ in range(n):
        temp = []
        for _ in range(m):
            temp.append(0)
        matrix.append(temp)
    return matrix

def draw(screen: pygame.Surface):
    for i in range(n):
        for j in range(m):
            color = "white" if matrix[i][j] == 0 else (red, blue, green)
            pygame.draw.rect(screen, color, (i * size, j * size, size, size))



def change_state(matrix):
    temp = init_matrix()
    for i in range(n):
        for j in range(m):
            
            if matrix[i][j] == 1:
                # Try to move down
                if j + 1 < m and matrix[i][j + 1] == 0:
                    temp[i][j + 1] = 1
                # Try to move down-left
                elif i - 1 >= 0 and j + 1 < m and matrix[i - 1][j + 1] == 0:
                    temp[i - 1][j + 1] = 1
                # Try to move down-right
                elif i + 1 < n and j + 1 < m and matrix[i + 1][j + 1] == 0:
                    temp[i + 1][j + 1] = 1
                else:
                    temp[i][j] = 1
    return temp

    
    
    
matrix = init_matrix()
is_down = False
star_time = time.time()
while running:

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_down = True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            is_down = False
        


    if is_down:
        x, y = event.pos[0] // size, event.pos[1] // size
        print(x, y)

        if 0 <= y < m and 0 <= x < n:
            matrix[x][y] = 1 

        

    # RENDER YOUR GAME HERE
    draw(screen)
    matrix = change_state(matrix)
    
    t = time.time() - star_time
    red = int((math.sin(t) + 1) / 2 * 255)
    green = int((math.sin(t + 2) + 1) / 2 * 255)
    blue = int((math.sin(t + 4) + 1) / 2 * 255)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()