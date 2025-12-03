#!/usr/bin/env python3
"""
Sudoku Game - A playable command-line Sudoku with puzzle generation
"""

import random
import os
import copy


class Sudoku:
    def __init__(self, difficulty='medium'):
        self.size = 9
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.solution = None
        self.difficulty = difficulty
        self.generate_puzzle()

    def print_board(self, board=None):
        """Display the Sudoku board with nice formatting"""
        if board is None:
            board = self.board

        print("\n    " + "  ".join(str(i) for i in range(1, 10)))
        print("  +" + "---+" * 9)

        for i in range(self.size):
            row_str = f"{i + 1} | "
            for j in range(self.size):
                if board[i][j] == 0:
                    row_str += ". "
                else:
                    row_str += f"{board[i][j]} "

                if (j + 1) % 3 == 0:
                    row_str += "| "

            print(row_str)

            if (i + 1) % 3 == 0:
                print("  +" + "---+" * 9)
        print()

    def is_valid(self, board, row, col, num):
        """Check if placing num at board[row][col] is valid"""
        # Check row
        if num in board[row]:
            return False

        # Check column
        if num in [board[i][col] for i in range(self.size)]:
            return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve(self, board):
        """Solve the Sudoku puzzle using backtracking"""
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, i, j, num):
                            board[i][j] = num

                            if self.solve(board):
                                return True

                            board[i][j] = 0

                    return False
        return True

    def generate_complete_board(self):
        """Generate a complete valid Sudoku board"""
        board = [[0 for _ in range(self.size)] for _ in range(self.size)]

        # Fill diagonal 3x3 boxes first (they don't affect each other)
        for box in range(0, self.size, 3):
            nums = list(range(1, 10))
            random.shuffle(nums)
            idx = 0
            for i in range(box, box + 3):
                for j in range(box, box + 3):
                    board[i][j] = nums[idx]
                    idx += 1

        # Solve the rest
        self.solve(board)
        return board

    def remove_numbers(self, board, difficulty):
        """Remove numbers based on difficulty level"""
        cells_to_remove = {
            'easy': 30,
            'medium': 40,
            'hard': 50,
            'expert': 60
        }

        remove_count = cells_to_remove.get(difficulty, 40)
        puzzle = copy.deepcopy(board)

        removed = 0
        attempts = 0
        max_attempts = remove_count * 10

        while removed < remove_count and attempts < max_attempts:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            if puzzle[row][col] != 0:
                backup = puzzle[row][col]
                puzzle[row][col] = 0

                # Check if puzzle still has unique solution
                test_board = copy.deepcopy(puzzle)
                if self.solve(test_board):
                    removed += 1
                else:
                    puzzle[row][col] = backup

            attempts += 1

        return puzzle

    def generate_puzzle(self):
        """Generate a new Sudoku puzzle"""
        complete_board = self.generate_complete_board()
        self.solution = copy.deepcopy(complete_board)
        self.board = self.remove_numbers(complete_board, self.difficulty)
        self.initial_board = copy.deepcopy(self.board)

    def check_win(self):
        """Check if the puzzle is solved correctly"""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
                if not self.is_valid(self.board, i, j, self.board[i][j]):
                    return False
        return True

    def play(self):
        """Main game loop"""
        print("\n" + "="*50)
        print("       WELCOME TO SUDOKU!")
        print("="*50)
        print(f"\nDifficulty: {self.difficulty.upper()}")
        print("\nHow to play:")
        print("  - Enter: row col number (e.g., '1 1 5' to place 5 at row 1, col 1)")
        print("  - Type 'solve' to see the solution")
        print("  - Type 'reset' to reset to initial puzzle")
        print("  - Type 'hint' to get a hint")
        print("  - Type 'quit' to exit")

        while True:
            self.print_board()

            if self.check_win():
                print("🎉 CONGRATULATIONS! You solved the puzzle! 🎉")
                break

            command = input("Enter your move: ").strip().lower()

            if command == 'quit':
                print("Thanks for playing!")
                break
            elif command == 'solve':
                print("\nHere's the solution:")
                self.print_board(self.solution)
                response = input("Continue playing? (y/n): ").strip().lower()
                if response == 'n':
                    break
            elif command == 'reset':
                self.board = copy.deepcopy(self.initial_board)
                print("Board reset to initial state!")
            elif command == 'hint':
                self.give_hint()
            else:
                try:
                    parts = command.split()
                    if len(parts) != 3:
                        print("Invalid input! Use format: row col number")
                        continue

                    row, col, num = map(int, parts)
                    row -= 1  # Convert to 0-indexed
                    col -= 1

                    if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                        print("Invalid values! Row and col must be 1-9, number must be 1-9")
                        continue

                    if self.initial_board[row][col] != 0:
                        print("You cannot change the initial numbers!")
                        continue

                    if self.is_valid(self.board, row, col, num):
                        self.board[row][col] = num
                        if num != self.solution[row][col]:
                            print("⚠️  Warning: This doesn't match the solution!")
                    else:
                        print("Invalid move! That number violates Sudoku rules.")

                except ValueError:
                    print("Invalid input! Use format: row col number (e.g., '1 1 5')")

    def give_hint(self):
        """Provide a hint by revealing one correct number"""
        empty_cells = [(i, j) for i in range(self.size)
                       for j in range(self.size)
                       if self.board[i][j] == 0]

        if not empty_cells:
            print("No empty cells to hint!")
            return

        row, col = random.choice(empty_cells)
        self.board[row][col] = self.solution[row][col]
        print(f"Hint: Placed {self.solution[row][col]} at row {row + 1}, col {col + 1}")


def main():
    """Main entry point"""
    print("\nSelect difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Expert")

    choice = input("\nEnter choice (1-4, default is 2): ").strip()

    difficulty_map = {
        '1': 'easy',
        '2': 'medium',
        '3': 'hard',
        '4': 'expert'
    }

    difficulty = difficulty_map.get(choice, 'medium')

    game = Sudoku(difficulty=difficulty)
    game.play()


if __name__ == "__main__":
    main()
