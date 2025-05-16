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
        backrow: list[str] = [
            "rook",
            "knight",
            "bishop",
            "queen",
            "king",
            "bishop",
            "knight",
            "rook",
        ]

        startCol: int = 5
        for i, piece in enumerate(backrow):
            self.piecesLookup[(i + startCol, 0)] = pieceData("white", piece)
            self.piecesLookup[(i + startCol, 7)] = pieceData("black", piece)

        for i in range(5, 14):
            self.piecesLookup[(i, 1)] = pieceData("white", "pawn")
            self.piecesLookup[(i, 6)] = pieceData("black", "pawn")
