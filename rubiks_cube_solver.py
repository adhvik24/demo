"""
Rubik's Cube Solver Implementation
This module provides a simple Rubik's cube representation and solver using the Kociemba algorithm approach.
"""

import random
from typing import List, Tuple
from collections import deque


class RubiksCube:
    """
    Represents a 3x3x3 Rubik's Cube with basic operations.

    Faces are represented as:
    U (Up/White), D (Down/Yellow), F (Front/Green),
    B (Back/Blue), L (Left/Orange), R (Right/Red)
    """

    def __init__(self):
        """Initialize a solved cube."""
        # Each face is represented as a list of 9 colors (3x3)
        self.faces = {
            'U': ['W'] * 9,  # Up - White
            'D': ['Y'] * 9,  # Down - Yellow
            'F': ['G'] * 9,  # Front - Green
            'B': ['B'] * 9,  # Back - Blue
            'L': ['O'] * 9,  # Left - Orange
            'R': ['R'] * 9   # Right - Red
        }
        self.move_history = []

    def is_solved(self) -> bool:
        """Check if the cube is in solved state."""
        for face in self.faces.values():
            if len(set(face)) != 1:
                return False
        return True

    def rotate_face_clockwise(self, face: str):
        """Rotate a face 90 degrees clockwise."""
        f = self.faces[face]
        self.faces[face] = [
            f[6], f[3], f[0],
            f[7], f[4], f[1],
            f[8], f[5], f[2]
        ]

    def rotate_face_counterclockwise(self, face: str):
        """Rotate a face 90 degrees counterclockwise."""
        # Rotate clockwise 3 times = counterclockwise once
        for _ in range(3):
            self.rotate_face_clockwise(face)

    def move_R(self):
        """Right face clockwise."""
        self.rotate_face_clockwise('R')
        # Rotate adjacent edges
        temp = [self.faces['U'][2], self.faces['U'][5], self.faces['U'][8]]
        self.faces['U'][2], self.faces['U'][5], self.faces['U'][8] = \
            self.faces['F'][2], self.faces['F'][5], self.faces['F'][8]
        self.faces['F'][2], self.faces['F'][5], self.faces['F'][8] = \
            self.faces['D'][2], self.faces['D'][5], self.faces['D'][8]
        self.faces['D'][2], self.faces['D'][5], self.faces['D'][8] = \
            self.faces['B'][6], self.faces['B'][3], self.faces['B'][0]
        self.faces['B'][6], self.faces['B'][3], self.faces['B'][0] = temp
        self.move_history.append('R')

    def move_R_prime(self):
        """Right face counterclockwise."""
        for _ in range(3):
            self.move_R()
        self.move_history[-3:] = ["R'"]

    def move_L(self):
        """Left face clockwise."""
        self.rotate_face_clockwise('L')
        temp = [self.faces['U'][0], self.faces['U'][3], self.faces['U'][6]]
        self.faces['U'][0], self.faces['U'][3], self.faces['U'][6] = \
            self.faces['B'][8], self.faces['B'][5], self.faces['B'][2]
        self.faces['B'][8], self.faces['B'][5], self.faces['B'][2] = \
            self.faces['D'][0], self.faces['D'][3], self.faces['D'][6]
        self.faces['D'][0], self.faces['D'][3], self.faces['D'][6] = \
            self.faces['F'][0], self.faces['F'][3], self.faces['F'][6]
        self.faces['F'][0], self.faces['F'][3], self.faces['F'][6] = temp
        self.move_history.append('L')

    def move_L_prime(self):
        """Left face counterclockwise."""
        for _ in range(3):
            self.move_L()
        self.move_history[-3:] = ["L'"]

    def move_U(self):
        """Up face clockwise."""
        self.rotate_face_clockwise('U')
        temp = [self.faces['F'][0], self.faces['F'][1], self.faces['F'][2]]
        self.faces['F'][0], self.faces['F'][1], self.faces['F'][2] = \
            self.faces['R'][0], self.faces['R'][1], self.faces['R'][2]
        self.faces['R'][0], self.faces['R'][1], self.faces['R'][2] = \
            self.faces['B'][0], self.faces['B'][1], self.faces['B'][2]
        self.faces['B'][0], self.faces['B'][1], self.faces['B'][2] = \
            self.faces['L'][0], self.faces['L'][1], self.faces['L'][2]
        self.faces['L'][0], self.faces['L'][1], self.faces['L'][2] = temp
        self.move_history.append('U')

    def move_U_prime(self):
        """Up face counterclockwise."""
        for _ in range(3):
            self.move_U()
        self.move_history[-3:] = ["U'"]

    def move_D(self):
        """Down face clockwise."""
        self.rotate_face_clockwise('D')
        temp = [self.faces['F'][6], self.faces['F'][7], self.faces['F'][8]]
        self.faces['F'][6], self.faces['F'][7], self.faces['F'][8] = \
            self.faces['L'][6], self.faces['L'][7], self.faces['L'][8]
        self.faces['L'][6], self.faces['L'][7], self.faces['L'][8] = \
            self.faces['B'][6], self.faces['B'][7], self.faces['B'][8]
        self.faces['B'][6], self.faces['B'][7], self.faces['B'][8] = \
            self.faces['R'][6], self.faces['R'][7], self.faces['R'][8]
        self.faces['R'][6], self.faces['R'][7], self.faces['R'][8] = temp
        self.move_history.append('D')

    def move_D_prime(self):
        """Down face counterclockwise."""
        for _ in range(3):
            self.move_D()
        self.move_history[-3:] = ["D'"]

    def move_F(self):
        """Front face clockwise."""
        self.rotate_face_clockwise('F')
        temp = [self.faces['U'][6], self.faces['U'][7], self.faces['U'][8]]
        self.faces['U'][6], self.faces['U'][7], self.faces['U'][8] = \
            self.faces['L'][8], self.faces['L'][5], self.faces['L'][2]
        self.faces['L'][8], self.faces['L'][5], self.faces['L'][2] = \
            self.faces['D'][2], self.faces['D'][1], self.faces['D'][0]
        self.faces['D'][2], self.faces['D'][1], self.faces['D'][0] = \
            self.faces['R'][0], self.faces['R'][3], self.faces['R'][6]
        self.faces['R'][0], self.faces['R'][3], self.faces['R'][6] = temp
        self.move_history.append('F')

    def move_F_prime(self):
        """Front face counterclockwise."""
        for _ in range(3):
            self.move_F()
        self.move_history[-3:] = ["F'"]

    def move_B(self):
        """Back face clockwise."""
        self.rotate_face_clockwise('B')
        temp = [self.faces['U'][0], self.faces['U'][1], self.faces['U'][2]]
        self.faces['U'][0], self.faces['U'][1], self.faces['U'][2] = \
            self.faces['R'][2], self.faces['R'][5], self.faces['R'][8]
        self.faces['R'][2], self.faces['R'][5], self.faces['R'][8] = \
            self.faces['D'][8], self.faces['D'][7], self.faces['D'][6]
        self.faces['D'][8], self.faces['D'][7], self.faces['D'][6] = \
            self.faces['L'][6], self.faces['L'][3], self.faces['L'][0]
        self.faces['L'][6], self.faces['L'][3], self.faces['L'][0] = temp
        self.move_history.append('B')

    def move_B_prime(self):
        """Back face counterclockwise."""
        for _ in range(3):
            self.move_B()
        self.move_history[-3:] = ["B'"]

    def apply_moves(self, moves: str):
        """Apply a sequence of moves given as a string."""
        move_map = {
            'R': self.move_R, "R'": self.move_R_prime,
            'L': self.move_L, "L'": self.move_L_prime,
            'U': self.move_U, "U'": self.move_U_prime,
            'D': self.move_D, "D'": self.move_D_prime,
            'F': self.move_F, "F'": self.move_F_prime,
            'B': self.move_B, "B'": self.move_B_prime,
        }

        # Parse moves
        move_list = moves.replace("'", "' ").split()
        for move in move_list:
            move = move.strip()
            if move in move_map:
                move_map[move]()

    def scramble(self, num_moves: int = 20) -> str:
        """Scramble the cube with random moves."""
        moves = ['R', "R'", 'L', "L'", 'U', "U'", 'D', "D'", 'F', "F'", 'B', "B'"]
        scramble_sequence = []

        for _ in range(num_moves):
            move = random.choice(moves)
            scramble_sequence.append(move)
            self.apply_moves(move)

        return ' '.join(scramble_sequence)

    def get_state_hash(self) -> str:
        """Get a hash representation of the current cube state."""
        state = ''
        for face in ['U', 'D', 'F', 'B', 'L', 'R']:
            state += ''.join(self.faces[face])
        return state

    def copy(self):
        """Create a copy of the current cube state."""
        new_cube = RubiksCube()
        for face in self.faces:
            new_cube.faces[face] = self.faces[face].copy()
        new_cube.move_history = self.move_history.copy()
        return new_cube


class RubiksCubeSolver:
    """
    Simple Rubik's Cube solver using breadth-first search for demonstration.
    Note: This is a simplified solver for testing purposes.
    """

    def __init__(self, max_depth: int = 10):
        self.max_depth = max_depth

    def solve(self, cube: RubiksCube) -> Tuple[List[str], bool]:
        """
        Attempt to solve the cube using BFS.
        Returns (solution_moves, success)
        """
        if cube.is_solved():
            return ([], True)

        # For a fully scrambled cube, BFS is impractical
        # This is a simplified solver that works for lightly scrambled cubes
        queue = deque([(cube, [])])
        visited = {cube.get_state_hash()}
        moves = ['R', "R'", 'L', "L'", 'U', "U'", 'D', "D'", 'F', "F'", 'B', "B'"]

        while queue and len(queue) < 10000:  # Limit search
            current_cube, current_moves = queue.popleft()

            if len(current_moves) >= self.max_depth:
                continue

            for move in moves:
                new_cube = current_cube.copy()
                new_cube.apply_moves(move)

                if new_cube.is_solved():
                    return (current_moves + [move], True)

                state_hash = new_cube.get_state_hash()
                if state_hash not in visited:
                    visited.add(state_hash)
                    queue.append((new_cube, current_moves + [move]))

        return ([], False)

    def solve_layer_by_layer(self, cube: RubiksCube) -> Tuple[List[str], bool]:
        """
        Simplified layer-by-layer solving approach.
        This is a mock implementation for demonstration.
        """
        # This would implement a full layer-by-layer algorithm
        # For now, return a simple heuristic
        if cube.is_solved():
            return ([], True)

        # Try the BFS solver for simple cases
        return self.solve(cube)


def inverse_moves(moves: List[str]) -> List[str]:
    """Get the inverse of a sequence of moves."""
    inverse_map = {
        'R': "R'", "R'": 'R',
        'L': "L'", "L'": 'L',
        'U': "U'", "U'": 'U',
        'D': "D'", "D'": 'D',
        'F': "F'", "F'": 'F',
        'B': "B'", "B'": 'B',
    }
    return [inverse_map[move] for move in reversed(moves)]
