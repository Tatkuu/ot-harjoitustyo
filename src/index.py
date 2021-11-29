import pygame
from snake import Snake

def check_direction(key, way):
    if (key == pygame.K_UP and way == "down" or key == pygame.K_DOWN and way == "up"
    or key == pygame.K_RIGHT and way == "left" or key == pygame.K_LEFT and way == "right"):
        return False
    return True

pygame.init()
snake = Snake()
screen = pygame.display.set_mode((630,630))
clock = pygame.time.Clock()
way = "up"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if check_direction(event.key, way):
                if event.key == pygame.K_UP:
                    snake.change_wayection("up")
                    way = "up"
                elif event.key == pygame.K_DOWN:
                    snake.change_wayection("down")
                    way = "down"
                elif event.key == pygame.K_LEFT:
                    snake.change_wayection("left")
                    way = "left"
                elif event.key == pygame.K_RIGHT:
                    snake.change_wayection("right")
                    way = "right"
                break
    snake.move_snake()
    screen.fill([0, 0, 0])
    if snake.check_bounds():
        break
    snake.draw_snake(screen)
    pygame.display.update()
    clock.tick(3)
