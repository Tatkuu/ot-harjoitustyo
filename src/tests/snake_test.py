import unittest
from snake import Snake

class TestSnake(unittest.TestCase):
    def test_check_snake_length(self):
        snake = Snake()

        length = len(snake.body)
        self.assertEqual(length, 1)

    def test_snake_is_moving(self):
        snake = Snake()

        snake.move_snake()
        x = snake.body[0].centerx
        y = snake.body[0].centery
        self.assertEqual([x, y], [315, 285])

    def test_change_direction(self):
        snake = Snake()

        snake.change_direction("left")
        snake.move_snake()
        x = snake.body[0].centerx
        y = snake.body[0].centery
        self.assertEqual([x, y], [285, 315])


