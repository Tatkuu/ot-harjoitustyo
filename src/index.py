import pygame
from snake import Snake

pygame.init()

snake = Snake()
screen = pygame.display.set_mode((630,630))
clock = pygame.time.Clock()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
	snake.move_snake()
	screen.fill([0, 0, 0])
	if snake.check_bounds():
		break
	snake.draw_snake(screen)
	pygame.display.update()
	clock.tick(3)
