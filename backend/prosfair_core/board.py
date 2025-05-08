from dataclasses import dataclass


@dataclass
class pieceData:
    color: str
    type: str


class Board:

    grid: list[list[int]]
    piecesLookup: dict[tuple[int, int], pieceData | None]

    def __init__(self, row: int = 8, col: int = 16) -> None:
        self.grid = [[0 for _ in range(col)] for _ in range(row)]
        self.piecesLookup = {
            (colPiece, rowPiece): None
            for colPiece in range(col)
            for rowPiece in range(row)
        }

    def initialSetup(self) -> None:
        """Called when the game is first being setup on the main board. Makes grid
        and pieces represent expected values at start of a game."""
        self.piecesLookup[(5, 0)] = pieceData("white", "rook")
        self.piecesLookup[(6, 0)] = pieceData("white", "knight")
        ...
