import pygame
import random

class Snack():
    def __init__(self, snake):
        self.x = 0
        self.y = 0
        self.change_spawn(snake)

    def change_spawn(self, snake):
        snackx = random.randint(1, 21)*30
        snacky = random.randint(1, 21)*30
        check = True
        while check:
            check = False
            for x in snake:
                if snackx == x.centerx and snacky == x.centery:
                    snackx = random.randint(1, 21)*30
                    snacky = random.randint(1, 21)*30
                    check = True
        self.x = snackx - 15
        self.y = snacky - 15

    def draw_snack(self, screen):
        pygame.draw.circle(screen, [255, 255, 255], [self.x, self.y], 11, 0)

