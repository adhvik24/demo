"""
Rubik's Cube Solver Implementation
A basic implementation of a 3x3x3 Rubik's cube with solving capabilities
"""

import time
from functools import wraps


def timed_operation(func):
    """Decorator to time operations"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        return result, elapsed
    return wrapper


class CubeMetrics:
    """Track performance metrics for cube operations"""

    def __init__(self):
        self.move_count = 0
        self.total_time = 0
        self.operation_times = []

    def record_moves(self, num_moves, elapsed_time):
        """Record move execution metrics"""
        self.move_count += num_moves
        self.total_time += elapsed_time
        self.operation_times.append(elapsed_time)

    def get_average_time(self):
        """Get average time per operation"""
        if not self.operation_times:
            return 0
        return sum(self.operation_times) / len(self.operation_times)

    def reset(self):
        """Reset metrics"""
        self.move_count = 0
        self.total_time = 0
        self.operation_times = []

    def __str__(self):
        return f"Moves: {self.move_count}, Total Time: {self.total_time:.4f}s, Avg: {self.get_average_time():.4f}s"

class RubiksCube:
    """Represents a 3x3x3 Rubik's Cube"""

    def __init__(self, track_metrics=False):
        """Initialize a solved cube with standard color scheme"""
        # Each face is represented as a 3x3 array
        # Colors: W=White, Y=Yellow, R=Red, O=Orange, B=Blue, G=Green
        self.faces = {
            'U': [['W'] * 3 for _ in range(3)],  # Up (White)
            'D': [['Y'] * 3 for _ in range(3)],  # Down (Yellow)
            'F': [['R'] * 3 for _ in range(3)],  # Front (Red)
            'B': [['O'] * 3 for _ in range(3)],  # Back (Orange)
            'L': [['B'] * 3 for _ in range(3)],  # Left (Blue)
            'R': [['G'] * 3 for _ in range(3)]   # Right (Green)
        }
        self.metrics = CubeMetrics() if track_metrics else None
        self.move_history = []

    def rotate_face_clockwise(self, face):
        """Rotate a face 90 degrees clockwise"""
        # Transpose and reverse each row
        self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]

    def rotate_face_counter_clockwise(self, face):
        """Rotate a face 90 degrees counter-clockwise"""
        # Rotate clockwise 3 times
        for _ in range(3):
            self.rotate_face_clockwise(face)

    def move_U(self):
        """Rotate upper face clockwise"""
        self.rotate_face_clockwise('U')
        # Rotate edge pieces
        temp = self.faces['F'][0].copy()
        self.faces['F'][0] = self.faces['R'][0]
        self.faces['R'][0] = self.faces['B'][0]
        self.faces['B'][0] = self.faces['L'][0]
        self.faces['L'][0] = temp

    def move_U_prime(self):
        """Rotate upper face counter-clockwise"""
        for _ in range(3):
            self.move_U()

    def move_D(self):
        """Rotate down face clockwise"""
        self.rotate_face_clockwise('D')
        temp = self.faces['F'][2].copy()
        self.faces['F'][2] = self.faces['L'][2]
        self.faces['L'][2] = self.faces['B'][2]
        self.faces['B'][2] = self.faces['R'][2]
        self.faces['R'][2] = temp

    def move_D_prime(self):
        """Rotate down face counter-clockwise"""
        for _ in range(3):
            self.move_D()

    def move_R(self):
        """Rotate right face clockwise"""
        self.rotate_face_clockwise('R')
        temp = [self.faces['F'][i][2] for i in range(3)]
        for i in range(3):
            self.faces['F'][i][2] = self.faces['D'][i][2]
            self.faces['D'][i][2] = self.faces['B'][2-i][0]
            self.faces['B'][2-i][0] = self.faces['U'][i][2]
            self.faces['U'][i][2] = temp[i]

    def move_R_prime(self):
        """Rotate right face counter-clockwise"""
        for _ in range(3):
            self.move_R()

    def move_L(self):
        """Rotate left face clockwise"""
        self.rotate_face_clockwise('L')
        temp = [self.faces['F'][i][0] for i in range(3)]
        for i in range(3):
            self.faces['F'][i][0] = self.faces['U'][i][0]
            self.faces['U'][i][0] = self.faces['B'][2-i][2]
            self.faces['B'][2-i][2] = self.faces['D'][i][0]
            self.faces['D'][i][0] = temp[i]

    def move_L_prime(self):
        """Rotate left face counter-clockwise"""
        for _ in range(3):
            self.move_L()

    def move_F(self):
        """Rotate front face clockwise"""
        self.rotate_face_clockwise('F')
        temp = self.faces['U'][2].copy()
        self.faces['U'][2] = [self.faces['L'][2-i][2] for i in range(3)]
        for i in range(3):
            self.faces['L'][i][2] = self.faces['D'][0][i]
        self.faces['D'][0] = [self.faces['R'][2-i][0] for i in range(3)]
        for i in range(3):
            self.faces['R'][i][0] = temp[i]

    def move_F_prime(self):
        """Rotate front face counter-clockwise"""
        for _ in range(3):
            self.move_F()

    def move_B(self):
        """Rotate back face clockwise"""
        self.rotate_face_clockwise('B')
        temp = self.faces['U'][0].copy()
        self.faces['U'][0] = [self.faces['R'][i][2] for i in range(3)]
        for i in range(3):
            self.faces['R'][i][2] = self.faces['D'][2][2-i]
        self.faces['D'][2] = [self.faces['L'][i][0] for i in range(3)]
        for i in range(3):
            self.faces['L'][i][0] = temp[2-i]

    def move_B_prime(self):
        """Rotate back face counter-clockwise"""
        for _ in range(3):
            self.move_B()

    def execute_moves(self, moves, track_time=False):
        """Execute a sequence of moves given as a string"""
        start_time = time.time() if track_time else None

        move_map = {
            'U': self.move_U, "U'": self.move_U_prime, 'U2': lambda: (self.move_U(), self.move_U()),
            'D': self.move_D, "D'": self.move_D_prime, 'D2': lambda: (self.move_D(), self.move_D()),
            'R': self.move_R, "R'": self.move_R_prime, 'R2': lambda: (self.move_R(), self.move_R()),
            'L': self.move_L, "L'": self.move_L_prime, 'L2': lambda: (self.move_L(), self.move_L()),
            'F': self.move_F, "F'": self.move_F_prime, 'F2': lambda: (self.move_F(), self.move_F()),
            'B': self.move_B, "B'": self.move_B_prime, 'B2': lambda: (self.move_B(), self.move_B())
        }

        moves_list = moves.split()
        for move in moves_list:
            if move in move_map:
                move_map[move]()
                self.move_history.append(move)

        if track_time:
            elapsed = time.time() - start_time
            if self.metrics:
                self.metrics.record_moves(len(moves_list), elapsed)
            return elapsed

    def is_solved(self):
        """Check if the cube is in solved state"""
        for face in self.faces.values():
            first_color = face[0][0]
            for row in face:
                for color in row:
                    if color != first_color:
                        return False
        return True

    def get_state(self):
        """Return current state of the cube"""
        return {face: [row.copy() for row in grid] for face, grid in self.faces.items()}

    def scramble(self, num_moves=20):
        """Scramble the cube with random moves"""
        import random
        moves = ['U', "U'", 'U2', 'D', "D'", 'D2', 'R', "R'", 'R2',
                 'L', "L'", 'L2', 'F', "F'", 'F2', 'B', "B'", 'B2']
        scramble_sequence = ' '.join(random.choices(moves, k=num_moves))
        self.execute_moves(scramble_sequence)
        return scramble_sequence

    def display(self):
        """Display the cube in a 2D unfolded format"""
        output = []

        # Display upper face
        for row in self.faces['U']:
            output.append('      ' + ' '.join(row))

        output.append('')

        # Display left, front, right, back faces side by side
        for i in range(3):
            line = ' '.join(self.faces['L'][i]) + ' '
            line += ' '.join(self.faces['F'][i]) + ' '
            line += ' '.join(self.faces['R'][i]) + ' '
            line += ' '.join(self.faces['B'][i])
            output.append(line)

        output.append('')

        # Display down face
        for row in self.faces['D']:
            output.append('      ' + ' '.join(row))

        return '\n'.join(output)

    def __str__(self):
        """String representation of the cube"""
        return self.display()

    def to_dict(self):
        """Serialize cube state to dictionary"""
        return {
            'faces': {face: [row.copy() for row in grid] for face, grid in self.faces.items()},
            'is_solved': self.is_solved()
        }

    def from_dict(self, state_dict):
        """Deserialize cube state from dictionary"""
        if 'faces' in state_dict:
            self.faces = {face: [row.copy() for row in grid]
                         for face, grid in state_dict['faces'].items()}

    def copy(self):
        """Create a deep copy of the cube"""
        new_cube = RubiksCube()
        new_cube.faces = {face: [row.copy() for row in grid]
                         for face, grid in self.faces.items()}
        return new_cube

    def optimize_moves(self, move_sequence):
        """Optimize a move sequence by canceling redundant moves"""
        if not move_sequence:
            return ""

        moves_list = move_sequence.split()
        optimized = []

        i = 0
        while i < len(moves_list):
            current = moves_list[i]
            face = current[0]

            # Count consecutive moves of same face
            count = 0
            j = i
            while j < len(moves_list) and moves_list[j][0] == face:
                move = moves_list[j]
                if move == face:
                    count += 1
                elif move == face + "'":
                    count -= 1
                elif move == face + "2":
                    count += 2
                j += 1

            # Normalize count to 0-3 range
            count = count % 4

            # Add optimized move
            if count == 1:
                optimized.append(face)
            elif count == 2:
                optimized.append(face + '2')
            elif count == 3:
                optimized.append(face + "'")
            # count == 0 means moves cancel out, add nothing

            i = j

        return ' '.join(optimized)


class SimpleSolver:
    """A simple solver using basic algorithms"""

    @staticmethod
    def solve(cube):
        """
        Attempt to solve the cube using a simplified approach
        This is a placeholder for a more sophisticated solving algorithm
        """
        # In a real implementation, this would use algorithms like:
        # - Layer-by-layer method
        # - CFOP (Cross, F2L, OLL, PLL)
        # - Kociemba's algorithm
        # - IDA* search

        # For now, return an empty solution
        return []

    @staticmethod
    def solve_cross(cube):
        """Solve the white cross (first step of beginner's method)"""
        # Placeholder for cross solving logic
        return []

    @staticmethod
    def solve_corners(cube):
        """Solve the first layer corners"""
        # Placeholder for corner solving logic
        return []

    @staticmethod
    def solve_middle_layer(cube):
        """Solve the middle layer edges"""
        # Placeholder for middle layer logic
        return []

    @staticmethod
    def solve_last_layer(cube):
        """Solve the last layer (OLL + PLL)"""
        # Placeholder for last layer logic
        return []
