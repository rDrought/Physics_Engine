
import math
import pygame
import pymunk
import pymunk.pygame_util


pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH,HEIGHT))

def draw(space, window, draw_options, line):
    window.fill("black")
    if line:
        pygame.draw.line(window, "black", line[0], kine[1], 3) 
    space.debug_draw(draw_options)
    pygame.display.update()
   
def create_object(space, radius, mass, pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)
    shape.elasticity = 0.9
    shape.friction = 0.4
    space.add(body, shape)
    return shape
    
def calc_dist(p1, p2):
    return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)

def calc_angle(p1,p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    
def make_boundary(space, WIDTH, HEIGHT):
    rects = [
        [(WIDTH/2, HEIGHT -10), (WIDTH, 20)],
        [(WIDTH/2, 10), (WIDTH, 20)],
        [(10, HEIGHT/2), (20, HEIGHT)],
        [(WIDTH - 10, HEIGHT/2), (20, HEIGHT)]
             ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.color = (0,0,0,0)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)
    

def run(window, WIDTH, HEIGHT):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    
    space = pymunk.Space()
    space.gravity =(0, 981)

    make_boundary(space, WIDTH, HEIGHT)
    draw_options = pymunk.pygame_util.DrawOptions(window)
    
    pressed_pos = None
    ball = None

    while run:
        line - None
        if ball:
            line = [pressed_pos, pygame.mouse.get_pos()]
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pressed_pos = pygame.mouse.get_pos()
                    ball = create_object(space, 30, 10, pressed_pos)
                elif pressed_pos:
                    ball.body.apply_impulse_at_local_point((10000, 0), (0,0))
                    pressed_pos = None
                else:
                    space.remove(ball, ball.body)
                    ball = None
        draw(space, window, draw_options, line)
        space.step(dt)
        clock.tick(fps)
        
    pygame.quit()


        
if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)