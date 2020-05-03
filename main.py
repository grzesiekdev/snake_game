#!/usr/bin/env/python3
import time
import keyboard
from snake_game.snake import Snake
from snake_game.board import Board
import os


directions = {'LEFT_ARROW': 105, 'RIGHT_ARROW': 106, 'UP_ARROW': 103, 'DOWN_ARROW': 108}


def on_press(_: None):
    for code in keyboard._pressed_events:
        if code == directions['LEFT_ARROW']:
            snake.direction = 'left'
        elif code == directions['RIGHT_ARROW']:
            snake.direction = 'right'
        elif code == directions['UP_ARROW']:
            snake.direction = 'up'
        elif code == directions['DOWN_ARROW']:
            snake.direction = 'down'


def start_game(snake: Snake, board_obj: Board):
    snake.set_head()

    print('\n'.join(map(' '.join, board_obj.__str__())))
    keyboard.hook(on_press)
    while not snake.collision():
        print("SNAKE: ", snake.head_pos)
        print("BODY: ", snake.body_segments)
        print("APPLE: ", snake.apple_pos)

        snake.move()
        print('\n'.join(map(' '.join, board_obj.__str__())))
        snake.ate = False
        if snake.head_pos == snake.apple_pos:
            snake.eat_apple()
            snake.spawn_apple(board_obj)
        time.sleep(board_obj.SPEED)
        os.system('clear')
    print(f"Game over! Points: {snake.length}")


if __name__ == "__main__":
    board_obj = Board(15, 10, 0.3)  # Set: width, height, speed
    snake = Snake(board_obj.WIDTH // 2, board_obj.HEIGHT // 2, board_obj)  # Set: snake_game x and y position

    start_game(snake, board_obj)
