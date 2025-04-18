from dataclasses import dataclass


@dataclass
class pieceData:
    color: str
    type: str


class Board:

    def __init__(self, row: int = 8, col: int = 16) -> None:
        self.grid: list[list[int]] = [[0 for _ in range(col)] for _ in range(row)]
        self.piecesLookup: dict[tuple[int, int], pieceData | None] = {
            (rowPiece, colPiece): None
            for rowPiece in range(row)
            for colPiece in range(col)
        }

    def setup(self) -> None:
        """Called when the game is first being setup on the main board. Makes grid
        and pieces represent expected values at start of a game."""

        ...
