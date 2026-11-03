# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
radius = 40
player_pos = pygame.Vector2(screen.get_width()// 2 + radius , screen.get_height() // 2 + radius) # v= dr / dt <=> dr = v * dt 
v = pygame.Vector2(40,40) 
a = pygame.Vector2(0,0) # a = dv / dt <=> dv = a * dt 
mass = 1 
force= pygame.Vector2(1, -11) # F = ma <=> a = F/m 

p = mass * v
a = force * 1/mass
print(a)

trail = [player_pos]
def mag(vec: pygame.Vector2) -> int:
    return int(pygame.math.Vector2.magnitude(vec))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    if len(trail) >= 100: 
        trail.pop(0)
    trail.append((player_pos.x, player_pos.y))
   
    pygame.draw.circle(screen, "red", player_pos, radius)
    pygame.draw.lines(screen, "white",False, trail, width=4)
    v += a * dt
    player_pos += v * dt
    p = mass * v - p
    if player_pos[0] + radius >= screen.get_width():
        player_pos[0] = screen.get_width() - radius  # Snap edge to wall
        v[0] *= -1                                    # Reverse horizontal direction

    elif player_pos[0] - radius <= 0:
        player_pos[0] = radius                       # Snap edge to wall
        v[0] *= -1 

    if player_pos[1] + radius >= screen.get_height():
        player_pos[1] = screen.get_height() - radius 
        v[1] *= -1                                   

   
    elif player_pos[1] - radius <= 0:
        player_pos[1] = radius                       
        v[1] *= -1                                    
    
    print(mag(player_pos), mag(a), mag(force), mag(v), len(trail), p)
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

    
    dt = clock.tick(60) / 1000

pygame.quit()