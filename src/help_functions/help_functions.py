import pygame

def check_collision(snake, snack):
    if snake.body[0].centerx + 1 == snack.x and snake.body[0].centery + 1 == snack.y:
        snack.change_spawn(snake.body)
        snake.grow_snake()

def check_direction(key, way):
    if (key == pygame.K_UP and way == "down" or key == pygame.K_DOWN and way == "up" or
    key == pygame.K_RIGHT and way == "left" or key == pygame.K_LEFT and way == "right"):
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
