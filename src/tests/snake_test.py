import unittest
from classes.snake import Snake
from classes.snack import Snack

class TestSnake(unittest.TestCase):
    def test_check_snake_length(self):
        snake = Snake()

        length = len(snake.body)
        self.assertEqual(length, 1)

    def test_snake_is_moving(self):
        snake = Snake()

        snake.move_snake()
        x_cord = snake.body[0].centerx
        y_cord = snake.body[0].centery
        self.assertEqual([x_cord, y_cord], [315, 285])

    def test_change_direction(self):
        snake = Snake()

        snake.change_direction("left")
        snake.move_snake()
        x_cord = snake.body[0].centerx
        y_cord = snake.body[0].centery
        self.assertEqual([x_cord, y_cord], [285, 315])

    def test_check_snack_spawn(self):
        snack = Snack()
        snake = Snake()
        x = snack.x
        y = snack.y
        snack.change_spawn(snake.body)
        self.assertNotEqual([x, y], [snack.x, snack.y])

    def test_grow_snake(self):
        snake = Snake()
        length = len(snake.body)
        snake.grow_snake()
        self.assertGreater(len(snake.body), length)
