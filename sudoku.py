import random

class Sudoku:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.original_grid = [[0 for _ in range(9)] for _ in range(9)]

    def print_grid(self):
        """Print the Sudoku grid in a readable format"""
        print("\n    0 1 2   3 4 5   6 7 8")
        print("  +-------+-------+-------+")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("  +-------+-------+-------+")
            print(f"{i} |", end="")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" |", end="")
                if self.grid[i][j] == 0:
                    print(" .", end="")
                else:
                    print(f" {self.grid[i][j]}", end="")
            print(" |")
        print("  +-------+-------+-------+")

    def is_valid_move(self, row, col, num):
        """Check if a number can be placed at the given position"""
        # Check row
        if num in self.grid[row]:
            return False

        # Check column
        for i in range(9):
            if self.grid[i][col] == num:
                return False

        # Check 3x3 subgrid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve(self):
        """Solve the Sudoku puzzle using backtracking"""
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(row, col, num):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

    def generate_puzzle(self, difficulty=40):
        """Generate a Sudoku puzzle by removing numbers from a solved grid"""
        # Fill the grid with a valid solution
        self.fill_grid()

        # Copy the solved grid
        self.original_grid = [row[:] for row in self.grid]

        # Remove numbers to create the puzzle
        cells_to_remove = difficulty
        while cells_to_remove > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.grid[row][col] != 0:
                self.grid[row][col] = 0
                cells_to_remove -= 1

    def fill_grid(self):
        """Fill the grid with a valid Sudoku solution using backtracking"""
        numbers = list(range(1, 10))
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_valid_move(i, j, num):
                            self.grid[i][j] = num
                            if self.fill_grid():
                                return True
                            self.grid[i][j] = 0
                    return False
        return True

    def is_complete(self):
        """Check if the puzzle is solved"""
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return False
        return True

    def play(self):
        """Main game loop"""
        print("Welcome to Sudoku!")
        print("Enter moves as: row col num (e.g., 0 1 5)")
        print("Enter 'q' to quit")

        while not self.is_complete():
            self.print_grid()
            try:
                move = input("Enter your move: ").strip()
                if move.lower() == 'q':
                    print("Thanks for playing!")
                    return

                row, col, num = map(int, move.split())
                if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                    print("Invalid input. Row and column must be 0-8, number 1-9.")
                    continue

                if self.original_grid[row][col] != 0:
                    print("You cannot change the original numbers!")
                    continue

                if not self.is_valid_move(row, col, num):
                    print("Invalid move! That number violates Sudoku rules.")
                    continue

                self.grid[row][col] = num

            except ValueError:
                print("Invalid input format. Use: row col num")

        print("Congratulations! You solved the Sudoku puzzle!")
        self.print_grid()

if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.generate_puzzle()
    sudoku.play()