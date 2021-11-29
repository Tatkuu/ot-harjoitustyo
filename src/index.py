import pygame
from snake import Snake

def check_direction(key, dir):
    if (key == pygame.K_UP and dir == "down" or key == pygame.K_DOWN and dir == "up"
    or key == pygame.K_RIGHT and dir == "left" or key == pygame.K_LEFT and dir == "right"):
        return False
    return True


pygame.init()




snake = Snake()
screen = pygame.display.set_mode((630,630))
clock = pygame.time.Clock()
dir = "up"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if check_direction(event.key, dir):
                if event.key == pygame.K_UP:
                    snake.change_direction("up")
                    dir = "up"
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("down")
                    dir = "down"
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("left")
                    dir = "left"
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("right")
                    dir = "right"
                break
    snake.move_snake()
    screen.fill([0, 0, 0])
    if snake.check_bounds():
        break
    snake.draw_snake(screen)
    pygame.display.update()
    clock.tick(3)
