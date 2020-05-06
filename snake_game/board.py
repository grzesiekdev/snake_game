class Board:
    def __init__(self, width: int, height: int, speed: float):
        self.WIDTH = width
        self.HEIGHT = height
        self.SPEED = speed
        self.board = self.__create_board()

    def __create_board(self) -> list:
        return [["□" for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]

    def __str__(self):
        return self.board
