import pygame
from snake import Snake


def check_direction(key, way):
    if key == pygame.K_UP and way == "down" or key == pygame.K_DOWN and way == "up":
        return False
    elif key == pygame.K_RIGHT and way == "left" or key == pygame.K_LEFT and way == "right":
        return False
    return True

def set_direction(event, snake, way):
    if event.key == pygame.K_UP:
        snake.change_direction("up")
        way = "up"
    elif event.key == pygame.K_DOWN:
        snake.change_direction("down")
        way = "down"
    elif event.key == pygame.K_LEFT:
        snake.change_direction("left")
        way = "left"
    elif event.key == pygame.K_RIGHT:
        snake.change_direction("right")
        way = "right"
    return way

def quit_game(event):
    if event.key == pygame.K_ESCAPE:
        return False
    return True

def game():
    pygame.init()
    snake = Snake()
    screen = pygame.display.set_mode((630,630))
    clock = pygame.time.Clock()
    running = True
    way = "up"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = quit_game(event)
                if check_direction(event, way):
                    way = set_direction(event, snake, way)
                    break
        snake.move_snake()
        screen.fill([0, 0, 0])
        if snake.check_bounds():
            break
        snake.draw_snake(screen)
        pygame.display.update()
        clock.tick(3)

if __name__ == "__main__":
    game()
