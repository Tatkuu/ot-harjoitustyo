import pygame
from classes.snake import Snake
from classes.snack import Snack
from help_functions.help_functions import *

def game():
    pygame.init()
    snake = Snake()
    snack = Snack(snake.body)
    screen = pygame.display.set_mode((630,630))
    clock = pygame.time.Clock()
    running = True
    way = "up"
    snack.change_spawn(snake.body)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = quit_game(event)
                if check_direction(event.key, way):
                    way = set_direction(event, snake, way)
                    break
        snake.move_snake()
        screen.fill([0, 0, 0])
        if snake.check_bounds() or snake.check_collision():
            break
        check_collision(snake, snack)
        snake.draw_snake(screen)
        snack.draw_snack(screen)
        pygame.display.update()
        clock.tick(6)

if __name__ == "__main__":
    game()
