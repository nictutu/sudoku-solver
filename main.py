from solver import solve_sudoku
from utils import input_puzzle, print_board

def main():
    puzzle = input_puzzle()
    print("Solving the Sudoku puzzle...")
    if solve_sudoku(puzzle):
        print("Sudoku puzzle solved successfully:")
        print_board(puzzle)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
