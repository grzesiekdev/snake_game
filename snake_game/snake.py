import collections
from .board import Board
import random


class Snake:
    def __init__(self, x_pos: int, y_pos: int, board_obj: Board):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.head_pos = [self.x_pos, self.y_pos]

        self.body_segments = collections.deque()  # doubly end operations, faster than lists
        self.length = 0
        self.apple_pos = [0, 0]
        self.coords = [0, 0]
        self.ate = False
        self.direction = 'up'
        self.spawn_apple(board_obj)
        self.board_obj = board_obj

    def set_empty_square(self) -> None:
        self.board_obj.board[self.y_pos][self.x_pos] = "□"

    def set_head(self) -> None:
        self.board_obj.board[self.y_pos][self.x_pos] = "■"

    def draw_body(self) -> None:
        self.body_segments.appendleft(self.coords)
        self.board_obj.board[self.body_segments[0][1]][self.body_segments[0][0]] = "&"
        if not self.ate:
            self.board_obj.board[self.body_segments[self.length][1]][self.body_segments[self.length][0]] = "□"
            self.set_head()
            self.body_segments.pop()

    def move(self) -> None:
        self.coords = [self.x_pos, self.y_pos]
        self.set_empty_square()

        if self.direction == "right":
            self.x_pos += 1
        if self.direction == "left":
            self.x_pos -= 1
        if self.direction == "up":
            self.y_pos -= 1
        if self.direction == "down":
            self.y_pos += 1

        self.set_head()
        if self.length >= 1:
            self.draw_body()

        self.head_pos = [self.x_pos, self.y_pos]

    def spawn_apple(self, board_obj: Board) -> None:
        while True:
            x = random.randint(0, board_obj.WIDTH-2)
            y = random.randint(0, board_obj.HEIGHT-2)
            apple_pos = [x, y]
            if apple_pos not in self.body_segments and apple_pos != self.head_pos:
                break
        self.apple_pos = [x, y]
        board_obj.board[y][x] = "●"

    def eat_apple(self) -> None:
        self.length += 1
        self.ate = True

    def collision(self) -> bool:
        return self.head_pos in self.body_segments or self.y_pos in [self.board_obj.HEIGHT-1, -1] \
                or self.x_pos in [self.board_obj.WIDTH-2, -1]
