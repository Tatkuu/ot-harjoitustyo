import pygame
from snake import Snake

def check_direction(key, Dir):
    if (key == pygame.K_UP and Dir == "down" or key == pygame.K_DOWN and Dir == "up"
    or key == pygame.K_RIGHT and Dir == "left" or key == pygame.K_LEFT and Dir == "right"):
        return False
    return True

pygame.init()
snake = Snake()
screen = pygame.display.set_mode((630,630))
clock = pygame.time.Clock()
Dir = "up"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if check_direction(event.key, Dir):
                if event.key == pygame.K_UP:
                    snake.change_direction("up")
                    Dir = "up"
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("down")
                    Dir = "down"
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("left")
                    Dir = "left"
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("right")
                    Dir = "right"
                break
    snake.move_snake()
    screen.fill([0, 0, 0])
    if snake.check_bounds():
        break
    snake.draw_snake(screen)
    pygame.display.update()
    clock.tick(3)
