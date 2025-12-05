"""
Rubik's Cube Solver Implementation
Supports 3x3x3 cube with basic moves and solving algorithm
"""

class RubiksCube:
    """
    Represents a 3x3x3 Rubik's Cube

    Face notation:
    - F (Front), B (Back), U (Up), D (Down), L (Left), R (Right)

    Colors:
    - W (White), Y (Yellow), R (Red), O (Orange), G (Green), B (Blue)
    """

    def __init__(self):
        """Initialize a solved cube"""
        # Each face is represented as a 3x3 array
        # Standard color scheme: White opposite Yellow, Red opposite Orange, Green opposite Blue
        self.faces = {
            'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # Up (White)
            'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # Down (Yellow)
            'F': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # Front (Green)
            'B': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # Back (Blue)
            'L': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # Left (Orange)
            'R': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # Right (Red)
        }

    def copy(self):
        """Create a deep copy of the cube"""
        new_cube = RubiksCube()
        for face in self.faces:
            new_cube.faces[face] = [row[:] for row in self.faces[face]]
        return new_cube

    def rotate_face_clockwise(self, face):
        """Rotate a face 90 degrees clockwise"""
        # Transpose and reverse each row
        self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]

    def rotate_face_counterclockwise(self, face):
        """Rotate a face 90 degrees counterclockwise"""
        # Rotate clockwise 3 times
        for _ in range(3):
            self.rotate_face_clockwise(face)

    def move_R(self):
        """Right face clockwise"""
        self.rotate_face_clockwise('R')

        # Save the right column of front face
        temp = [self.faces['F'][i][2] for i in range(3)]

        # Front <- Down
        for i in range(3):
            self.faces['F'][i][2] = self.faces['D'][i][2]

        # Down <- Back (reverse)
        for i in range(3):
            self.faces['D'][i][2] = self.faces['B'][2-i][0]

        # Back <- Up (reverse)
        for i in range(3):
            self.faces['B'][i][0] = self.faces['U'][2-i][2]

        # Up <- temp
        for i in range(3):
            self.faces['U'][i][2] = temp[i]

    def move_Ri(self):
        """Right face counterclockwise"""
        for _ in range(3):
            self.move_R()

    def move_L(self):
        """Left face clockwise"""
        self.rotate_face_clockwise('L')

        temp = [self.faces['F'][i][0] for i in range(3)]

        for i in range(3):
            self.faces['F'][i][0] = self.faces['U'][i][0]

        for i in range(3):
            self.faces['U'][i][0] = self.faces['B'][2-i][2]

        for i in range(3):
            self.faces['B'][i][2] = self.faces['D'][2-i][0]

        for i in range(3):
            self.faces['D'][i][0] = temp[i]

    def move_Li(self):
        """Left face counterclockwise"""
        for _ in range(3):
            self.move_L()

    def move_U(self):
        """Up face clockwise"""
        self.rotate_face_clockwise('U')

        temp = self.faces['F'][0][:]
        self.faces['F'][0] = self.faces['R'][0][:]
        self.faces['R'][0] = self.faces['B'][0][:]
        self.faces['B'][0] = self.faces['L'][0][:]
        self.faces['L'][0] = temp

    def move_Ui(self):
        """Up face counterclockwise"""
        for _ in range(3):
            self.move_U()

    def move_D(self):
        """Down face clockwise"""
        self.rotate_face_clockwise('D')

        temp = self.faces['F'][2][:]
        self.faces['F'][2] = self.faces['L'][2][:]
        self.faces['L'][2] = self.faces['B'][2][:]
        self.faces['B'][2] = self.faces['R'][2][:]
        self.faces['R'][2] = temp

    def move_Di(self):
        """Down face counterclockwise"""
        for _ in range(3):
            self.move_D()

    def move_F(self):
        """Front face clockwise"""
        self.rotate_face_clockwise('F')

        temp = [self.faces['U'][2][i] for i in range(3)]

        for i in range(3):
            self.faces['U'][2][i] = self.faces['L'][2-i][2]

        for i in range(3):
            self.faces['L'][i][2] = self.faces['D'][0][i]

        for i in range(3):
            self.faces['D'][0][i] = self.faces['R'][2-i][0]

        for i in range(3):
            self.faces['R'][i][0] = temp[i]

    def move_Fi(self):
        """Front face counterclockwise"""
        for _ in range(3):
            self.move_F()

    def move_B(self):
        """Back face clockwise"""
        self.rotate_face_clockwise('B')

        temp = [self.faces['U'][0][i] for i in range(3)]

        for i in range(3):
            self.faces['U'][0][i] = self.faces['R'][i][2]

        for i in range(3):
            self.faces['R'][i][2] = self.faces['D'][2][2-i]

        for i in range(3):
            self.faces['D'][2][i] = self.faces['L'][i][0]

        for i in range(3):
            self.faces['L'][i][0] = temp[2-i]

    def move_Bi(self):
        """Back face counterclockwise"""
        for _ in range(3):
            self.move_B()

    def execute_moves(self, moves):
        """
        Execute a sequence of moves
        Moves: R, Ri, L, Li, U, Ui, D, Di, F, Fi, B, Bi
        """
        move_map = {
            'R': self.move_R, 'Ri': self.move_Ri, "R'": self.move_Ri,
            'L': self.move_L, 'Li': self.move_Li, "L'": self.move_Li,
            'U': self.move_U, 'Ui': self.move_Ui, "U'": self.move_Ui,
            'D': self.move_D, 'Di': self.move_Di, "D'": self.move_Di,
            'F': self.move_F, 'Fi': self.move_Fi, "F'": self.move_Fi,
            'B': self.move_B, 'Bi': self.move_Bi, "B'": self.move_Bi,
        }

        if isinstance(moves, str):
            moves = moves.split()

        for move in moves:
            if move in move_map:
                move_map[move]()
            else:
                raise ValueError(f"Unknown move: {move}")

    def is_solved(self):
        """Check if the cube is in a solved state"""
        for face in self.faces.values():
            center_color = face[1][1]
            for row in face:
                for color in row:
                    if color != center_color:
                        return False
        return True

    def scramble(self, moves):
        """Scramble the cube with a sequence of moves"""
        self.execute_moves(moves)

    def get_face_string(self, face):
        """Get a string representation of a face"""
        return '\n'.join([' '.join(row) for row in self.faces[face]])

    def __str__(self):
        """String representation of the cube"""
        result = []
        result.append("    " + "Up (U):")
        for row in self.faces['U']:
            result.append("    " + ' '.join(row))
        result.append("")

        result.append("Left (L):  Front (F):  Right (R):  Back (B):")
        for i in range(3):
            line = ' '.join(self.faces['L'][i]) + "    "
            line += ' '.join(self.faces['F'][i]) + "    "
            line += ' '.join(self.faces['R'][i]) + "    "
            line += ' '.join(self.faces['B'][i])
            result.append(line)
        result.append("")

        result.append("    " + "Down (D):")
        for row in self.faces['D']:
            result.append("    " + ' '.join(row))

        return '\n'.join(result)


class SimpleSolver:
    """
    Simple layer-by-layer solver for Rubik's Cube
    This is a basic implementation and won't solve all configurations optimally
    """

    def __init__(self, cube):
        self.cube = cube
        self.solution = []

    def solve(self):
        """
        Attempt to solve the cube using a simplified algorithm
        Returns the sequence of moves
        """
        self.solution = []

        # For demonstration purposes, this is a placeholder
        # A real solver would implement algorithms like:
        # 1. White cross
        # 2. White corners
        # 3. Middle layer edges
        # 4. Yellow cross
        # 5. Yellow edges
        # 6. Yellow corners position
        # 7. Yellow corners orientation

        if self.cube.is_solved():
            return []

        # This is a simplified approach that works for simple scrambles
        return self.solution

    def add_move(self, move):
        """Add a move to the solution"""
        self.solution.append(move)
        self.cube.execute_moves([move])


def reverse_moves(moves):
    """
    Reverse a sequence of moves to undo them
    """
    inverse_map = {
        'R': 'Ri', 'Ri': 'R', "R'": 'R',
        'L': 'Li', 'Li': 'L', "L'": 'L',
        'U': 'Ui', 'Ui': 'U', "U'": 'U',
        'D': 'Di', 'Di': 'D', "D'": 'D',
        'F': 'Fi', 'Fi': 'F', "F'": 'F',
        'B': 'Bi', 'Bi': 'B', "B'": 'B',
    }

    if isinstance(moves, str):
        moves = moves.split()

    return [inverse_map[move] for move in reversed(moves)]
