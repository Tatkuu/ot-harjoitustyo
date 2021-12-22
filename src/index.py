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
    score = 0
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
            screen.fill([54, 54, 54])
            if snake.check_bounds() or snake.check_collision():
                running = False
            if check_collision(snake, snack):
                score = 1000 + (score * 1.035)
            snake.draw_snake(screen)
            snack.draw_snack(screen)
            screen.blit(text.render('Score:', True, (255,0,0)), (10, 10))
            screen.blit(text.render(str(int(score)), True, (255,0,0)), (90, 12))
        pygame.display.update()
        clock.tick(6)
        if not running:
            snake = Snake()
            snack = Snack(snake.body)
            way = "up"
            screen.fill([54, 54, 54])
            start_screen(text, buttons, screen)
            screen.blit(text.render('GAME OVER', True, (255,0,0)), (235, 50))
            screen.blit(text.render('Your Score:', True, (255,0,0)), (225, 100))
            screen.blit(text.render(str(int(score)), True, (255,0,0)), (360, 102))
            score = 0
            running = True
            play = False


if __name__ == "__main__":
    game()
