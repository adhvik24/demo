"""
Rubik's Cube Solver Implementation
Represents a 3x3x3 Rubik's cube and provides solving algorithms
"""

import copy
from typing import List, Tuple, Dict


class RubiksCube:
    """
    Represents a 3x3x3 Rubik's Cube with standard color notation:
    W (White), Y (Yellow), R (Red), O (Orange), B (Blue), G (Green)
    """

    def __init__(self):
        """Initialize a solved cube"""
        # Each face is represented as a 3x3 matrix
        # Faces: Front, Back, Left, Right, Up, Down
        self.cube = {
            'F': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # Front (Red)
            'B': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # Back (Orange)
            'L': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # Left (Green)
            'R': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # Right (Blue)
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # Up (White)
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]   # Down (Yellow)
        }
        self.move_history = []

    def rotate_face_clockwise(self, face: List[List[str]]) -> List[List[str]]:
        """Rotate a face 90 degrees clockwise"""
        return [[face[2][0], face[1][0], face[0][0]],
                [face[2][1], face[1][1], face[0][1]],
                [face[2][2], face[1][2], face[0][2]]]

    def rotate_face_counterclockwise(self, face: List[List[str]]) -> List[List[str]]:
        """Rotate a face 90 degrees counterclockwise"""
        return [[face[0][2], face[1][2], face[2][2]],
                [face[0][1], face[1][1], face[2][1]],
                [face[0][0], face[1][0], face[2][0]]]

    def F(self):
        """Front face clockwise rotation"""
        self.cube['F'] = self.rotate_face_clockwise(self.cube['F'])

        temp = [self.cube['U'][2][0], self.cube['U'][2][1], self.cube['U'][2][2]]
        self.cube['U'][2] = [self.cube['L'][2][2], self.cube['L'][1][2], self.cube['L'][0][2]]
        self.cube['L'][0][2] = self.cube['D'][0][0]
        self.cube['L'][1][2] = self.cube['D'][0][1]
        self.cube['L'][2][2] = self.cube['D'][0][2]
        self.cube['D'][0] = [self.cube['R'][2][0], self.cube['R'][1][0], self.cube['R'][0][0]]
        self.cube['R'][0][0] = temp[0]
        self.cube['R'][1][0] = temp[1]
        self.cube['R'][2][0] = temp[2]

        self.move_history.append('F')

    def F_prime(self):
        """Front face counterclockwise rotation"""
        self.cube['F'] = self.rotate_face_counterclockwise(self.cube['F'])

        temp = [self.cube['U'][2][0], self.cube['U'][2][1], self.cube['U'][2][2]]
        self.cube['U'][2] = [self.cube['R'][0][0], self.cube['R'][1][0], self.cube['R'][2][0]]
        self.cube['R'][0][0] = self.cube['D'][0][2]
        self.cube['R'][1][0] = self.cube['D'][0][1]
        self.cube['R'][2][0] = self.cube['D'][0][0]
        self.cube['D'][0] = [self.cube['L'][2][2], self.cube['L'][1][2], self.cube['L'][0][2]]
        self.cube['L'][0][2] = temp[2]
        self.cube['L'][1][2] = temp[1]
        self.cube['L'][2][2] = temp[0]

        self.move_history.append("F'")

    def R(self):
        """Right face clockwise rotation"""
        self.cube['R'] = self.rotate_face_clockwise(self.cube['R'])

        temp = [self.cube['F'][0][2], self.cube['F'][1][2], self.cube['F'][2][2]]
        self.cube['F'][0][2] = self.cube['D'][0][2]
        self.cube['F'][1][2] = self.cube['D'][1][2]
        self.cube['F'][2][2] = self.cube['D'][2][2]
        self.cube['D'][0][2] = self.cube['B'][2][0]
        self.cube['D'][1][2] = self.cube['B'][1][0]
        self.cube['D'][2][2] = self.cube['B'][0][0]
        self.cube['B'][0][0] = self.cube['U'][2][2]
        self.cube['B'][1][0] = self.cube['U'][1][2]
        self.cube['B'][2][0] = self.cube['U'][0][2]
        self.cube['U'][0][2] = temp[0]
        self.cube['U'][1][2] = temp[1]
        self.cube['U'][2][2] = temp[2]

        self.move_history.append('R')

    def R_prime(self):
        """Right face counterclockwise rotation"""
        self.cube['R'] = self.rotate_face_counterclockwise(self.cube['R'])

        temp = [self.cube['F'][0][2], self.cube['F'][1][2], self.cube['F'][2][2]]
        self.cube['F'][0][2] = self.cube['U'][0][2]
        self.cube['F'][1][2] = self.cube['U'][1][2]
        self.cube['F'][2][2] = self.cube['U'][2][2]
        self.cube['U'][0][2] = self.cube['B'][2][0]
        self.cube['U'][1][2] = self.cube['B'][1][0]
        self.cube['U'][2][2] = self.cube['B'][0][0]
        self.cube['B'][0][0] = self.cube['D'][2][2]
        self.cube['B'][1][0] = self.cube['D'][1][2]
        self.cube['B'][2][0] = self.cube['D'][0][2]
        self.cube['D'][0][2] = temp[0]
        self.cube['D'][1][2] = temp[1]
        self.cube['D'][2][2] = temp[2]

        self.move_history.append("R'")

    def U(self):
        """Up face clockwise rotation"""
        self.cube['U'] = self.rotate_face_clockwise(self.cube['U'])

        temp = [self.cube['F'][0][0], self.cube['F'][0][1], self.cube['F'][0][2]]
        self.cube['F'][0] = [self.cube['R'][0][0], self.cube['R'][0][1], self.cube['R'][0][2]]
        self.cube['R'][0] = [self.cube['B'][0][0], self.cube['B'][0][1], self.cube['B'][0][2]]
        self.cube['B'][0] = [self.cube['L'][0][0], self.cube['L'][0][1], self.cube['L'][0][2]]
        self.cube['L'][0] = temp

        self.move_history.append('U')

    def U_prime(self):
        """Up face counterclockwise rotation"""
        self.cube['U'] = self.rotate_face_counterclockwise(self.cube['U'])

        temp = [self.cube['F'][0][0], self.cube['F'][0][1], self.cube['F'][0][2]]
        self.cube['F'][0] = [self.cube['L'][0][0], self.cube['L'][0][1], self.cube['L'][0][2]]
        self.cube['L'][0] = [self.cube['B'][0][0], self.cube['B'][0][1], self.cube['B'][0][2]]
        self.cube['B'][0] = [self.cube['R'][0][0], self.cube['R'][0][1], self.cube['R'][0][2]]
        self.cube['R'][0] = temp

        self.move_history.append("U'")

    def D(self):
        """Down face clockwise rotation"""
        self.cube['D'] = self.rotate_face_clockwise(self.cube['D'])

        temp = [self.cube['F'][2][0], self.cube['F'][2][1], self.cube['F'][2][2]]
        self.cube['F'][2] = [self.cube['L'][2][0], self.cube['L'][2][1], self.cube['L'][2][2]]
        self.cube['L'][2] = [self.cube['B'][2][0], self.cube['B'][2][1], self.cube['B'][2][2]]
        self.cube['B'][2] = [self.cube['R'][2][0], self.cube['R'][2][1], self.cube['R'][2][2]]
        self.cube['R'][2] = temp

        self.move_history.append('D')

    def D_prime(self):
        """Down face counterclockwise rotation"""
        self.cube['D'] = self.rotate_face_counterclockwise(self.cube['D'])

        temp = [self.cube['F'][2][0], self.cube['F'][2][1], self.cube['F'][2][2]]
        self.cube['F'][2] = [self.cube['R'][2][0], self.cube['R'][2][1], self.cube['R'][2][2]]
        self.cube['R'][2] = [self.cube['B'][2][0], self.cube['B'][2][1], self.cube['B'][2][2]]
        self.cube['B'][2] = [self.cube['L'][2][0], self.cube['L'][2][1], self.cube['L'][2][2]]
        self.cube['L'][2] = temp

        self.move_history.append("D'")

    def L(self):
        """Left face clockwise rotation"""
        self.cube['L'] = self.rotate_face_clockwise(self.cube['L'])

        temp = [self.cube['F'][0][0], self.cube['F'][1][0], self.cube['F'][2][0]]
        self.cube['F'][0][0] = self.cube['U'][0][0]
        self.cube['F'][1][0] = self.cube['U'][1][0]
        self.cube['F'][2][0] = self.cube['U'][2][0]
        self.cube['U'][0][0] = self.cube['B'][2][2]
        self.cube['U'][1][0] = self.cube['B'][1][2]
        self.cube['U'][2][0] = self.cube['B'][0][2]
        self.cube['B'][0][2] = self.cube['D'][2][0]
        self.cube['B'][1][2] = self.cube['D'][1][0]
        self.cube['B'][2][2] = self.cube['D'][0][0]
        self.cube['D'][0][0] = temp[0]
        self.cube['D'][1][0] = temp[1]
        self.cube['D'][2][0] = temp[2]

        self.move_history.append('L')

    def L_prime(self):
        """Left face counterclockwise rotation"""
        self.cube['L'] = self.rotate_face_counterclockwise(self.cube['L'])

        temp = [self.cube['F'][0][0], self.cube['F'][1][0], self.cube['F'][2][0]]
        self.cube['F'][0][0] = self.cube['D'][0][0]
        self.cube['F'][1][0] = self.cube['D'][1][0]
        self.cube['F'][2][0] = self.cube['D'][2][0]
        self.cube['D'][0][0] = self.cube['B'][2][2]
        self.cube['D'][1][0] = self.cube['B'][1][2]
        self.cube['D'][2][0] = self.cube['B'][0][2]
        self.cube['B'][0][2] = self.cube['U'][2][0]
        self.cube['B'][1][2] = self.cube['U'][1][0]
        self.cube['B'][2][2] = self.cube['U'][0][0]
        self.cube['U'][0][0] = temp[0]
        self.cube['U'][1][0] = temp[1]
        self.cube['U'][2][0] = temp[2]

        self.move_history.append("L'")

    def B(self):
        """Back face clockwise rotation"""
        self.cube['B'] = self.rotate_face_clockwise(self.cube['B'])

        temp = [self.cube['U'][0][0], self.cube['U'][0][1], self.cube['U'][0][2]]
        self.cube['U'][0] = [self.cube['R'][0][2], self.cube['R'][1][2], self.cube['R'][2][2]]
        self.cube['R'][0][2] = self.cube['D'][2][2]
        self.cube['R'][1][2] = self.cube['D'][2][1]
        self.cube['R'][2][2] = self.cube['D'][2][0]
        self.cube['D'][2] = [self.cube['L'][0][0], self.cube['L'][1][0], self.cube['L'][2][0]]
        self.cube['L'][0][0] = temp[2]
        self.cube['L'][1][0] = temp[1]
        self.cube['L'][2][0] = temp[0]

        self.move_history.append('B')

    def B_prime(self):
        """Back face counterclockwise rotation"""
        self.cube['B'] = self.rotate_face_counterclockwise(self.cube['B'])

        temp = [self.cube['U'][0][0], self.cube['U'][0][1], self.cube['U'][0][2]]
        self.cube['U'][0] = [self.cube['L'][2][0], self.cube['L'][1][0], self.cube['L'][0][0]]
        self.cube['L'][0][0] = self.cube['D'][2][0]
        self.cube['L'][1][0] = self.cube['D'][2][1]
        self.cube['L'][2][0] = self.cube['D'][2][2]
        self.cube['D'][2] = [self.cube['R'][2][2], self.cube['R'][1][2], self.cube['R'][0][2]]
        self.cube['R'][0][2] = temp[0]
        self.cube['R'][1][2] = temp[1]
        self.cube['R'][2][2] = temp[2]

        self.move_history.append("B'")

    def execute_moves(self, moves: str):
        """Execute a sequence of moves given as a string"""
        move_list = moves.split()
        for move in move_list:
            if move == 'F':
                self.F()
            elif move == "F'":
                self.F_prime()
            elif move == 'R':
                self.R()
            elif move == "R'":
                self.R_prime()
            elif move == 'U':
                self.U()
            elif move == "U'":
                self.U_prime()
            elif move == 'D':
                self.D()
            elif move == "D'":
                self.D_prime()
            elif move == 'L':
                self.L()
            elif move == "L'":
                self.L_prime()
            elif move == 'B':
                self.B()
            elif move == "B'":
                self.B_prime()

    def is_solved(self) -> bool:
        """Check if the cube is in solved state"""
        for face in self.cube.values():
            center_color = face[1][1]
            for row in face:
                for cell in row:
                    if cell != center_color:
                        return False
        return True

    def get_state(self) -> Dict:
        """Get the current state of the cube"""
        return copy.deepcopy(self.cube)

    def scramble(self, moves: str):
        """Scramble the cube with a sequence of moves"""
        self.move_history = []
        self.execute_moves(moves)

    def __str__(self):
        """String representation of the cube"""
        result = []
        result.append("Rubik's Cube State:")
        for face_name, face in self.cube.items():
            result.append(f"\n{face_name} face:")
            for row in face:
                result.append("  " + " ".join(row))
        return "\n".join(result)


class SimpleSolver:
    """
    Simple layer-by-layer solver for Rubik's cube
    This is a simplified solver that uses basic algorithms
    """

    def __init__(self, cube: RubiksCube):
        self.cube = cube
        self.solution = []

    def solve(self) -> List[str]:
        """
        Attempt to solve the cube using layer-by-layer method
        Returns list of moves performed
        """
        if self.cube.is_solved():
            return []

        # This is a placeholder for a full solving algorithm
        # A complete implementation would include:
        # 1. White cross
        # 2. White corners
        # 3. Middle layer edges
        # 4. Yellow cross
        # 5. Yellow edges
        # 6. Yellow corners position
        # 7. Yellow corners orientation

        # For demonstration, return empty solution
        return self.solution

    def get_solution_string(self) -> str:
        """Get the solution as a space-separated string"""
        return " ".join(self.solution)
