import unittest
import os.path
import sys
from collections import deque
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from snake_game.snake import Snake
from snake_game.board import Board


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.board_1 = Board(3, 4, 0.2)
        self.board_2 = Board(0, 0, 0.2)

        self.board_for_snake = Board(5, 5, 0.3)
        self.snake = Snake(self.board_for_snake.WIDTH // 2, self.board_for_snake.HEIGHT // 2, self.board_for_snake)


class TestInit(TestMain):
    def test_inital_create_board(self):
        board_1 = [["□", "□", "□"], ["□", "□", "□"], ["□", "□", "□"], ["□", "□", "□"]]
        self.assertEqual(board_1, self.board_1.board)

        board_2 = []
        self.assertEqual(board_2, self.board_2.board)

    def test_initial_snake(self):
        self.assertEqual(2, self.snake.x_pos)
        self.assertEqual(2, self.snake.y_pos)

        self.assertIn(self.snake.apple_pos[0], range(0, self.board_for_snake.HEIGHT))
        self.assertIn(self.snake.apple_pos[1], range(0, self.board_for_snake.WIDTH))


class TestSnake(TestMain):
    def test_move(self):

        self.snake.direction = 'right'

        # Delete apple from map, 'cause we test only moving now
        self.board_for_snake.board[self.snake.apple_pos[1]][self.snake.apple_pos[0]] = '□'

        for _ in range(2):
            self.assertEqual(self.board_for_snake.board[self.snake.y_pos][self.snake.x_pos-1], '□')
            self.snake.move()
            self.assertEqual(self.board_for_snake.board[self.snake.y_pos][self.snake.x_pos], '■')

        self.snake.direction = 'down'
        for _ in range(2):
            self.assertEqual(self.board_for_snake.board[self.snake.y_pos+1][self.snake.x_pos], '□')
            self.snake.move()
            self.assertEqual(self.board_for_snake.board[self.snake.y_pos][self.snake.x_pos], '■')

        self.snake.direction = 'left'
        for _ in range(2):
            self.assertEqual(self.board_for_snake.board[self.snake.y_pos][self.snake.x_pos - 1], '□')
            self.snake.move()
            self.assertEqual(self.board_for_snake.board[self.snake.y_pos][self.snake.x_pos], '■')

        self.snake.direction = 'up'
        for _ in range(2):
            self.assertEqual(self.board_for_snake.board[self.snake.y_pos - 1][self.snake.x_pos], '□')
            self.snake.move()
            self.assertEqual(self.board_for_snake.board[self.snake.y_pos][self.snake.x_pos], '■')

    def test_draw_body(self):
        self.snake.apple_pos = [3, 3]

        self.snake.direction = 'right'
        self.snake.move()

        self.snake.direction = 'down'
        for _ in range(2):
            self.snake.check_if_ate()
            self.snake.move()

        self.assertEqual(self.snake.body_segments, deque([[3, 3]]))

    def test_spawn_apple(self):
        for row in self.board_for_snake.board:
            for cell in row:
                if cell == '●':
                    self.assertIn('●', self.board_for_snake.board[self.snake.apple_pos[1]][self.snake.apple_pos[0]])

    def test_eat_apple(self):
        self.snake.eat_apple()

        self.assertEqual(self.snake.length, 1)
        self.assertTrue(self.snake.ate)

        for _ in range(3):
            self.snake.eat_apple()

        self.assertEqual(self.snake.length, 4)

    def test_collision(self):
        self.snake.y_pos = -1
        self.assertTrue(self.snake.collision())

        self.snake.x_pos = -1
        self.assertTrue(self.snake.collision())

        self.snake.y_pos = self.board_for_snake.HEIGHT
        self.assertTrue(self.snake.collision())

        self.snake.x_pos = self.board_for_snake.WIDTH
        self.assertTrue(self.snake.collision())


if __name__ == '__main__':
    unittest.main()

