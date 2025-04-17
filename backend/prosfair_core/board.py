class Board:
    def __init__(self, width: int = 16, height: int = 8) -> None:
        self.grid: list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]
