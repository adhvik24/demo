"""
Rubik's Cube Solver
A simple implementation of a 3x3x3 Rubik's Cube with basic solving capabilities
"""

import random
from typing import List, Tuple
from copy import deepcopy


class RubiksCube:
    """Represents a 3x3x3 Rubik's Cube"""
    
    def __init__(self):
        # Initialize solved cube
        # Faces: U (Up/White), D (Down/Yellow), F (Front/Green), 
        #        B (Back/Blue), L (Left/Orange), R (Right/Red)
        self.faces = {
            'U': [['W'] * 3 for _ in range(3)],  # White
            'D': [['Y'] * 3 for _ in range(3)],  # Yellow
            'F': [['G'] * 3 for _ in range(3)],  # Green
            'B': [['B'] * 3 for _ in range(3)],  # Blue
            'L': [['O'] * 3 for _ in range(3)],  # Orange
            'R': [['R'] * 3 for _ in range(3)],  # Red
        }
        self.move_history = []
    
    def rotate_face_clockwise(self, face: str):
        """Rotate a face 90 degrees clockwise"""
        f = self.faces[face]
        self.faces[face] = [[f[2][0], f[1][0], f[0][0]],
                            [f[2][1], f[1][1], f[0][1]],
                            [f[2][2], f[1][2], f[0][2]]]
    
    def rotate_face_counterclockwise(self, face: str):
        """Rotate a face 90 degrees counterclockwise"""
        f = self.faces[face]
        self.faces[face] = [[f[0][2], f[1][2], f[2][2]],
                            [f[0][1], f[1][1], f[2][1]],
                            [f[0][0], f[1][0], f[2][0]]]
    
    def move_U(self):
        """Rotate upper face clockwise"""
        self.rotate_face_clockwise('U')
        temp = self.faces['F'][0][:]
        self.faces['F'][0] = self.faces['R'][0][:]
        self.faces['R'][0] = self.faces['B'][0][:]
        self.faces['B'][0] = self.faces['L'][0][:]
        self.faces['L'][0] = temp
        self.move_history.append('U')
    
    def move_U_prime(self):
        """Rotate upper face counterclockwise"""
        self.rotate_face_counterclockwise('U')
        temp = self.faces['F'][0][:]
        self.faces['F'][0] = self.faces['L'][0][:]
        self.faces['L'][0] = self.faces['B'][0][:]
        self.faces['B'][0] = self.faces['R'][0][:]
        self.faces['R'][0] = temp
        self.move_history.append("U'")
    
    def move_D(self):
        """Rotate down face clockwise"""
        self.rotate_face_clockwise('D')
        temp = self.faces['F'][2][:]
        self.faces['F'][2] = self.faces['L'][2][:]
        self.faces['L'][2] = self.faces['B'][2][:]
        self.faces['B'][2] = self.faces['R'][2][:]
        self.faces['R'][2] = temp
        self.move_history.append('D')
    
    def move_D_prime(self):
        """Rotate down face counterclockwise"""
        self.rotate_face_counterclockwise('D')
        temp = self.faces['F'][2][:]
        self.faces['F'][2] = self.faces['R'][2][:]
        self.faces['R'][2] = self.faces['B'][2][:]
        self.faces['B'][2] = self.faces['L'][2][:]
        self.faces['L'][2] = temp
        self.move_history.append("D'")
    
    def move_F(self):
        """Rotate front face clockwise"""
        self.rotate_face_clockwise('F')
        temp = [self.faces['U'][2][0], self.faces['U'][2][1], self.faces['U'][2][2]]
        self.faces['U'][2][0] = self.faces['L'][2][2]
        self.faces['U'][2][1] = self.faces['L'][1][2]
        self.faces['U'][2][2] = self.faces['L'][0][2]
        self.faces['L'][0][2] = self.faces['D'][0][0]
        self.faces['L'][1][2] = self.faces['D'][0][1]
        self.faces['L'][2][2] = self.faces['D'][0][2]
        self.faces['D'][0][0] = self.faces['R'][2][0]
        self.faces['D'][0][1] = self.faces['R'][1][0]
        self.faces['D'][0][2] = self.faces['R'][0][0]
        self.faces['R'][0][0] = temp[0]
        self.faces['R'][1][0] = temp[1]
        self.faces['R'][2][0] = temp[2]
        self.move_history.append('F')
    
    def move_F_prime(self):
        """Rotate front face counterclockwise"""
        self.rotate_face_counterclockwise('F')
        temp = [self.faces['U'][2][0], self.faces['U'][2][1], self.faces['U'][2][2]]
        self.faces['U'][2][0] = self.faces['R'][0][0]
        self.faces['U'][2][1] = self.faces['R'][1][0]
        self.faces['U'][2][2] = self.faces['R'][2][0]
        self.faces['R'][0][0] = self.faces['D'][0][2]
        self.faces['R'][1][0] = self.faces['D'][0][1]
        self.faces['R'][2][0] = self.faces['D'][0][0]
        self.faces['D'][0][0] = self.faces['L'][0][2]
        self.faces['D'][0][1] = self.faces['L'][1][2]
        self.faces['D'][0][2] = self.faces['L'][2][2]
        self.faces['L'][0][2] = temp[2]
        self.faces['L'][1][2] = temp[1]
        self.faces['L'][2][2] = temp[0]
        self.move_history.append("F'")
    
    def move_R(self):
        """Rotate right face clockwise"""
        self.rotate_face_clockwise('R')
        temp = [self.faces['U'][0][2], self.faces['U'][1][2], self.faces['U'][2][2]]
        self.faces['U'][0][2] = self.faces['F'][0][2]
        self.faces['U'][1][2] = self.faces['F'][1][2]
        self.faces['U'][2][2] = self.faces['F'][2][2]
        self.faces['F'][0][2] = self.faces['D'][0][2]
        self.faces['F'][1][2] = self.faces['D'][1][2]
        self.faces['F'][2][2] = self.faces['D'][2][2]
        self.faces['D'][0][2] = self.faces['B'][2][0]
        self.faces['D'][1][2] = self.faces['B'][1][0]
        self.faces['D'][2][2] = self.faces['B'][0][0]
        self.faces['B'][0][0] = temp[2]
        self.faces['B'][1][0] = temp[1]
        self.faces['B'][2][0] = temp[0]
        self.move_history.append('R')
    
    def move_R_prime(self):
        """Rotate right face counterclockwise"""
        self.rotate_face_counterclockwise('R')
        temp = [self.faces['U'][0][2], self.faces['U'][1][2], self.faces['U'][2][2]]
        self.faces['U'][0][2] = self.faces['B'][2][0]
        self.faces['U'][1][2] = self.faces['B'][1][0]
        self.faces['U'][2][2] = self.faces['B'][0][0]
        self.faces['B'][0][0] = self.faces['D'][2][2]
        self.faces['B'][1][0] = self.faces['D'][1][2]
        self.faces['B'][2][0] = self.faces['D'][0][2]
        self.faces['D'][0][2] = self.faces['F'][0][2]
        self.faces['D'][1][2] = self.faces['F'][1][2]
        self.faces['D'][2][2] = self.faces['F'][2][2]
        self.faces['F'][0][2] = temp[0]
        self.faces['F'][1][2] = temp[1]
        self.faces['F'][2][2] = temp[2]
        self.move_history.append("R'")
    
    def move_L(self):
        """Rotate left face clockwise"""
        self.rotate_face_clockwise('L')
        temp = [self.faces['U'][0][0], self.faces['U'][1][0], self.faces['U'][2][0]]
        self.faces['U'][0][0] = self.faces['B'][2][2]
        self.faces['U'][1][0] = self.faces['B'][1][2]
        self.faces['U'][2][0] = self.faces['B'][0][2]
        self.faces['B'][0][2] = self.faces['D'][2][0]
        self.faces['B'][1][2] = self.faces['D'][1][0]
        self.faces['B'][2][2] = self.faces['D'][0][0]
        self.faces['D'][0][0] = self.faces['F'][0][0]
        self.faces['D'][1][0] = self.faces['F'][1][0]
        self.faces['D'][2][0] = self.faces['F'][2][0]
        self.faces['F'][0][0] = temp[0]
        self.faces['F'][1][0] = temp[1]
        self.faces['F'][2][0] = temp[2]
        self.move_history.append('L')
    
    def move_L_prime(self):
        """Rotate left face counterclockwise"""
        self.rotate_face_counterclockwise('L')
        temp = [self.faces['U'][0][0], self.faces['U'][1][0], self.faces['U'][2][0]]
        self.faces['U'][0][0] = self.faces['F'][0][0]
        self.faces['U'][1][0] = self.faces['F'][1][0]
        self.faces['U'][2][0] = self.faces['F'][2][0]
        self.faces['F'][0][0] = self.faces['D'][0][0]
        self.faces['F'][1][0] = self.faces['D'][1][0]
        self.faces['F'][2][0] = self.faces['D'][2][0]
        self.faces['D'][0][0] = self.faces['B'][2][2]
        self.faces['D'][1][0] = self.faces['B'][1][2]
        self.faces['D'][2][0] = self.faces['B'][0][2]
        self.faces['B'][0][2] = temp[2]
        self.faces['B'][1][2] = temp[1]
        self.faces['B'][2][2] = temp[0]
        self.move_history.append("L'")
    
    def move_B(self):
        """Rotate back face clockwise"""
        self.rotate_face_clockwise('B')
        temp = [self.faces['U'][0][0], self.faces['U'][0][1], self.faces['U'][0][2]]
        self.faces['U'][0][0] = self.faces['R'][0][2]
        self.faces['U'][0][1] = self.faces['R'][1][2]
        self.faces['U'][0][2] = self.faces['R'][2][2]
        self.faces['R'][0][2] = self.faces['D'][2][2]
        self.faces['R'][1][2] = self.faces['D'][2][1]
        self.faces['R'][2][2] = self.faces['D'][2][0]
        self.faces['D'][2][0] = self.faces['L'][0][0]
        self.faces['D'][2][1] = self.faces['L'][1][0]
        self.faces['D'][2][2] = self.faces['L'][2][0]
        self.faces['L'][0][0] = temp[2]
        self.faces['L'][1][0] = temp[1]
        self.faces['L'][2][0] = temp[0]
        self.move_history.append('B')
    
    def move_B_prime(self):
        """Rotate back face counterclockwise"""
        self.rotate_face_counterclockwise('B')
        temp = [self.faces['U'][0][0], self.faces['U'][0][1], self.faces['U'][0][2]]
        self.faces['U'][0][0] = self.faces['L'][2][0]
        self.faces['U'][0][1] = self.faces['L'][1][0]
        self.faces['U'][0][2] = self.faces['L'][0][0]
        self.faces['L'][0][0] = self.faces['D'][2][0]
        self.faces['L'][1][0] = self.faces['D'][2][1]
        self.faces['L'][2][0] = self.faces['D'][2][2]
        self.faces['D'][2][0] = self.faces['R'][2][2]
        self.faces['D'][2][1] = self.faces['R'][1][2]
        self.faces['D'][2][2] = self.faces['R'][0][2]
        self.faces['R'][0][2] = temp[0]
        self.faces['R'][1][2] = temp[1]
        self.faces['R'][2][2] = temp[2]
        self.move_history.append("B'")
    
    def execute_move(self, move: str):
        """Execute a move by notation"""
        move_map = {
            'U': self.move_U, "U'": self.move_U_prime,
            'D': self.move_D, "D'": self.move_D_prime,
            'F': self.move_F, "F'": self.move_F_prime,
            'B': self.move_B, "B'": self.move_B_prime,
            'L': self.move_L, "L'": self.move_L_prime,
            'R': self.move_R, "R'": self.move_R_prime,
        }
        if move in move_map:
            move_map[move]()
        else:
            raise ValueError(f"Invalid move: {move}")
    
    def scramble(self, num_moves: int = 20):
        """Scramble the cube with random moves"""
        moves = ['U', "U'", 'D', "D'", 'F', "F'", 'B', "B'", 'L', "L'", 'R', "R'"]
        self.move_history = []
        for _ in range(num_moves):
            move = random.choice(moves)
            self.execute_move(move)
        return self.move_history
    
    def is_solved(self) -> bool:
        """Check if the cube is solved"""
        for face in self.faces.values():
            first_color = face[0][0]
            for row in face:
                for color in row:
                    if color != first_color:
                        return False
        return True
    
    def get_state(self) -> dict:
        """Get current state of the cube"""
        return deepcopy(self.faces)
    
    def display(self):
        """Display the cube in a readable format"""
        print("\n    U (Up/White)")
        for row in self.faces['U']:
            print("    " + " ".join(row))
        
        print("\nL   F   R   B")
        for i in range(3):
            print(f"{' '.join(self.faces['L'][i])} {' '.join(self.faces['F'][i])} "
                  f"{' '.join(self.faces['R'][i])} {' '.join(self.faces['B'][i])}")
        
        print("\n    D (Down/Yellow)")
        for row in self.faces['D']:
            print("    " + " ".join(row))
        print()


class SimpleSolver:
    """A simple solver using basic algorithms"""
    
    def __init__(self, cube: RubiksCube):
        self.cube = cube
        self.solution = []
    
    def solve(self) -> List[str]:
        """
        Attempt to solve the cube using a simplified approach
        Note: This is a basic implementation and may not solve all configurations
        """
        self.solution = []
        
        # For demonstration, we'll implement a very basic solving strategy
        # A full solver would implement layer-by-layer or CFOP method
        
        # This is a placeholder that demonstrates the structure
        # Real implementation would be much more complex
        
        return self.solution
    
    def reverse_scramble(self, scramble_moves: List[str]) -> List[str]:
        """
        Reverse a scramble sequence to solve the cube
        This works if we know the scramble sequence
        """
        reverse_map = {
            'U': "U'", "U'": 'U',
            'D': "D'", "D'": 'D',
            'F': "F'", "F'": 'F',
            'B': "B'", "B'": 'B',
            'L': "L'", "L'": 'L',
            'R': "R'", "R'": 'R',
        }
        
        solution = [reverse_map[move] for move in reversed(scramble_moves)]
        
        for move in solution:
            self.cube.execute_move(move)
            self.solution.append(move)
        
        return solution


def main():
    """Main function to demonstrate the Rubik's Cube solver"""
    print("=" * 50)
    print("Rubik's Cube Solver")
    print("=" * 50)
    
    # Create a new cube
    cube = RubiksCube()
    
    print("\n1. Initial solved state:")
    cube.display()
    print(f"Is solved: {cube.is_solved()}")
    
    # Scramble the cube
    print("\n2. Scrambling cube with 10 moves...")
    scramble_moves = cube.scramble(10)
    print(f"Scramble sequence: {' '.join(scramble_moves)}")
    cube.display()
    print(f"Is solved: {cube.is_solved()}")
    
    # Solve the cube
    print("\n3. Solving cube...")
    solver = SimpleSolver(cube)
    solution = solver.reverse_scramble(scramble_moves)
    print(f"Solution sequence: {' '.join(solution)}")
    cube.display()
    print(f"Is solved: {cube.is_solved()}")
    
    print("\n" + "=" * 50)
    print("Demo complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
