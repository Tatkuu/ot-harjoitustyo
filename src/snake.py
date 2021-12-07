import pygame

class Snake:
    def __init__(self):
        self.body = []
        self.body.append(pygame.Rect(300, 300, 29, 29))
        self.body.append(pygame.Rect(300, 330, 29, 29))
        self.body.append(pygame.Rect(300, 360, 29, 29))
        self.direction = [0, -30]

    def draw_snake(self, screen):
        for x in self.body:
            pygame.draw.rect(screen, (255,0,0), x)

    def move_snake(self):
        for x in range(len(self.body) - 1, 0, -1):
            self.body[x].centerx = self.body[x - 1].centerx
            self.body[x].centery = self.body[x - 1].centery
        self.body[0].move_ip(self.direction)
        return self.body

    def check_bounds(self):
        x_cord = self.body[0].centerx
        y_cord = self.body[0].centery
        if x_cord > 630 or x_cord < 0 or y_cord > 630 or y_cord < 0:
            return True
        return False

    def change_direction(self, way):
        if way == "up":
            self.direction = [0, -30]
        if way == "down":
            self.direction = [0, 30]
        if way == "left":
            self.direction = [-30, 0]
        if way == "right":
            self.direction = [30, 0]

    def grow_snake(self):
        x = self.body[len(self.body) - 1].centerx - 14
        y = self.body[len(self.body) - 1].centery - 14
        self.body.append(pygame.Rect(x, y, 29, 29))

    def check_collision(self):
        snake = self.body
        for x in range(1, len(snake)):
            if pygame.Rect.contains(snake[0], snake[x]):
                return True
        return False
