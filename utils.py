def input_puzzle():
    puzzle = []
    print("Enter the Sudoku puzzle row by row, with 0 for empty cells:")
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").split()))
                if len(row) != 9:
                    raise ValueError("Each row must have exactly 9 numbers.")
                puzzle.append(row)
                break
            except ValueError as e:
                print(e)
                print("Please enter the row again.")
    return puzzle

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
