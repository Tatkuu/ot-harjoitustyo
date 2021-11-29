import pygame

class Snake:
    def __init__(self):
        self.body = []
        self.body.append(pygame.Rect(300, 300, 30, 30))
        self.direction = [0, -30]

    def draw_snake(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.body[0])

    def move_snake(self):
        self.body[0].move_ip(self.direction)

    def check_bounds(self):
        x = self.body[0].centerx
        y = self.body[0].centery
        if x > 630 or x < 0 or y > 630 or y < 0:
            return True
        return False

    def change_direction(self, dir):
        if dir == "up":
            self.direction = [0, -30]
        if dir == "down":
            self.direction = [0, 30]
        if dir == "left":
            self.direction = [-30, 0]
        if dir == "right":
            self.direction = [30, 0]
