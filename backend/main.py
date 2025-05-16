from prosfair_core.board import Board


def main():

    board = Board()
    board.initialSetup()
    print(board.piecesLookup)


if __name__ == "__main__":
    main()
