import pygame
from classes.snake import Snake
from classes.snack import Snack
from help_functions.help_functions import *

def game():
    pygame.init()
    snake = Snake()
    snack = Snack(snake.body)
    text = pygame.font.SysFont('Arial', 25)
    screen = pygame.display.set_mode((630,630))
    buttons = []
    buttons.append(pygame.Rect(215, 140, 200, 100))
    buttons.append(pygame.Rect(215, 310, 200, 100))
    clock = pygame.time.Clock()
    running = True
    play = False
    way = "up"
    snack.change_spawn(snake.body)
    start_screen(text, buttons, screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                clickxy = pygame.mouse.get_pos()
                if buttons[0].collidepoint(clickxy):
                    play = True
                if buttons[1].collidepoint(clickxy):
                    exit()
            if event.type == pygame.KEYDOWN:
                if not quit_game(event):
                    exit()
                if event.key == pygame.K_SPACE:
                    play = True
                if play == True:
                    if check_direction(event.key, way):
                        way = set_direction(event, snake, way)
                        break
        if play == True:
            snake.move_snake()
            screen.fill([0, 0, 0])
            if snake.check_bounds() or snake.check_collision():
                running = False
            check_collision(snake, snack)
            snake.draw_snake(screen)
            snack.draw_snack(screen)
        pygame.display.update()
        clock.tick(6)
        if not running:
            snake = Snake()
            snack = Snack(snake.body)
            way = "up"
            screen.fill([0, 0, 0])
            start_screen(text, buttons, screen)
            screen.blit(text.render('GAME OVER', True, (255,0,0)), (235, 100))
            running = True
            play = False


if __name__ == "__main__":
    game()
