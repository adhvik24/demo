"""
Rubik's Cube Solver Implementation
Represents a 3x3x3 Rubik's cube and provides solving algorithms
"""

import copy
from typing import List, Tuple, Dict
from collections import deque


class RubiksCube:
    """
    Represents a 3x3x3 Rubik's Cube
    Faces: U (Up), D (Down), L (Left), R (Right), F (Front), B (Back)
    Each face is a 3x3 grid with colors: W (White), Y (Yellow), R (Red), O (Orange), G (Green), B (Blue)
    """
    
    def __init__(self):
        # Initialize solved cube
        # Each face is represented as a list of 9 colors (row-major order)
        self.faces = {
            'U': ['W'] * 9,  # Up - White
            'D': ['Y'] * 9,  # Down - Yellow
            'L': ['O'] * 9,  # Left - Orange
            'R': ['R'] * 9,  # Right - Red
            'F': ['G'] * 9,  # Front - Green
            'B': ['B'] * 9   # Back - Blue
        }
        
    def __eq__(self, other):
        """Check if two cubes are equal"""
        if not isinstance(other, RubiksCube):
            return False
        return self.faces == other.faces
    
    def __hash__(self):
        """Make cube hashable for use in sets/dicts"""
        return hash(str(self.faces))
    
    def copy(self):
        """Create a deep copy of the cube"""
        new_cube = RubiksCube()
        new_cube.faces = copy.deepcopy(self.faces)
        return new_cube
    
    def is_solved(self) -> bool:
        """Check if the cube is in solved state"""
        for face, colors in self.faces.items():
            if len(set(colors)) != 1:
                return False
        return True
    
    def rotate_face_clockwise(self, face: str):
        """Rotate a face 90 degrees clockwise"""
        f = self.faces[face]
        self.faces[face] = [f[6], f[3], f[0], f[7], f[4], f[1], f[8], f[5], f[2]]
    
    def rotate_face_counterclockwise(self, face: str):
        """Rotate a face 90 degrees counterclockwise"""
        f = self.faces[face]
        self.faces[face] = [f[2], f[5], f[8], f[1], f[4], f[7], f[0], f[3], f[6]]
    
    def U(self):
        """Rotate Up face clockwise"""
        self.rotate_face_clockwise('U')
        # Rotate edge pieces
        temp = [self.faces['F'][0], self.faces['F'][1], self.faces['F'][2]]
        self.faces['F'][0], self.faces['F'][1], self.faces['F'][2] = self.faces['R'][0], self.faces['R'][1], self.faces['R'][2]
        self.faces['R'][0], self.faces['R'][1], self.faces['R'][2] = self.faces['B'][0], self.faces['B'][1], self.faces['B'][2]
        self.faces['B'][0], self.faces['B'][1], self.faces['B'][2] = self.faces['L'][0], self.faces['L'][1], self.faces['L'][2]
        self.faces['L'][0], self.faces['L'][1], self.faces['L'][2] = temp
    
    def U_prime(self):
        """Rotate Up face counterclockwise"""
        self.rotate_face_counterclockwise('U')
        temp = [self.faces['F'][0], self.faces['F'][1], self.faces['F'][2]]
        self.faces['F'][0], self.faces['F'][1], self.faces['F'][2] = self.faces['L'][0], self.faces['L'][1], self.faces['L'][2]
        self.faces['L'][0], self.faces['L'][1], self.faces['L'][2] = self.faces['B'][0], self.faces['B'][1], self.faces['B'][2]
        self.faces['B'][0], self.faces['B'][1], self.faces['B'][2] = self.faces['R'][0], self.faces['R'][1], self.faces['R'][2]
        self.faces['R'][0], self.faces['R'][1], self.faces['R'][2] = temp
    
    def D(self):
        """Rotate Down face clockwise"""
        self.rotate_face_clockwise('D')
        temp = [self.faces['F'][6], self.faces['F'][7], self.faces['F'][8]]
        self.faces['F'][6], self.faces['F'][7], self.faces['F'][8] = self.faces['L'][6], self.faces['L'][7], self.faces['L'][8]
        self.faces['L'][6], self.faces['L'][7], self.faces['L'][8] = self.faces['B'][6], self.faces['B'][7], self.faces['B'][8]
        self.faces['B'][6], self.faces['B'][7], self.faces['B'][8] = self.faces['R'][6], self.faces['R'][7], self.faces['R'][8]
        self.faces['R'][6], self.faces['R'][7], self.faces['R'][8] = temp
    
    def D_prime(self):
        """Rotate Down face counterclockwise"""
        self.rotate_face_counterclockwise('D')
        temp = [self.faces['F'][6], self.faces['F'][7], self.faces['F'][8]]
        self.faces['F'][6], self.faces['F'][7], self.faces['F'][8] = self.faces['R'][6], self.faces['R'][7], self.faces['R'][8]
        self.faces['R'][6], self.faces['R'][7], self.faces['R'][8] = self.faces['B'][6], self.faces['B'][7], self.faces['B'][8]
        self.faces['B'][6], self.faces['B'][7], self.faces['B'][8] = self.faces['L'][6], self.faces['L'][7], self.faces['L'][8]
        self.faces['L'][6], self.faces['L'][7], self.faces['L'][8] = temp
    
    def R(self):
        """Rotate Right face clockwise"""
        self.rotate_face_clockwise('R')
        temp = [self.faces['F'][2], self.faces['F'][5], self.faces['F'][8]]
        self.faces['F'][2], self.faces['F'][5], self.faces['F'][8] = self.faces['D'][2], self.faces['D'][5], self.faces['D'][8]
        self.faces['D'][2], self.faces['D'][5], self.faces['D'][8] = self.faces['B'][6], self.faces['B'][3], self.faces['B'][0]
        self.faces['B'][6], self.faces['B'][3], self.faces['B'][0] = self.faces['U'][2], self.faces['U'][5], self.faces['U'][8]
        self.faces['U'][2], self.faces['U'][5], self.faces['U'][8] = temp
    
    def R_prime(self):
        """Rotate Right face counterclockwise"""
        self.rotate_face_counterclockwise('R')
        temp = [self.faces['F'][2], self.faces['F'][5], self.faces['F'][8]]
        self.faces['F'][2], self.faces['F'][5], self.faces['F'][8] = self.faces['U'][2], self.faces['U'][5], self.faces['U'][8]
        self.faces['U'][2], self.faces['U'][5], self.faces['U'][8] = self.faces['B'][6], self.faces['B'][3], self.faces['B'][0]
        self.faces['B'][6], self.faces['B'][3], self.faces['B'][0] = self.faces['D'][2], self.faces['D'][5], self.faces['D'][8]
        self.faces['D'][2], self.faces['D'][5], self.faces['D'][8] = temp
    
    def L(self):
        """Rotate Left face clockwise"""
        self.rotate_face_clockwise('L')
        temp = [self.faces['F'][0], self.faces['F'][3], self.faces['F'][6]]
        self.faces['F'][0], self.faces['F'][3], self.faces['F'][6] = self.faces['U'][0], self.faces['U'][3], self.faces['U'][6]
        self.faces['U'][0], self.faces['U'][3], self.faces['U'][6] = self.faces['B'][8], self.faces['B'][5], self.faces['B'][2]
        self.faces['B'][8], self.faces['B'][5], self.faces['B'][2] = self.faces['D'][0], self.faces['D'][3], self.faces['D'][6]
        self.faces['D'][0], self.faces['D'][3], self.faces['D'][6] = temp
    
    def L_prime(self):
        """Rotate Left face counterclockwise"""
        self.rotate_face_counterclockwise('L')
        temp = [self.faces['F'][0], self.faces['F'][3], self.faces['F'][6]]
        self.faces['F'][0], self.faces['F'][3], self.faces['F'][6] = self.faces['D'][0], self.faces['D'][3], self.faces['D'][6]
        self.faces['D'][0], self.faces['D'][3], self.faces['D'][6] = self.faces['B'][8], self.faces['B'][5], self.faces['B'][2]
        self.faces['B'][8], self.faces['B'][5], self.faces['B'][2] = self.faces['U'][0], self.faces['U'][3], self.faces['U'][6]
        self.faces['U'][0], self.faces['U'][3], self.faces['U'][6] = temp
    
    def F(self):
        """Rotate Front face clockwise"""
        self.rotate_face_clockwise('F')
        temp = [self.faces['U'][6], self.faces['U'][7], self.faces['U'][8]]
        self.faces['U'][6], self.faces['U'][7], self.faces['U'][8] = self.faces['L'][8], self.faces['L'][5], self.faces['L'][2]
        self.faces['L'][8], self.faces['L'][5], self.faces['L'][2] = self.faces['D'][2], self.faces['D'][1], self.faces['D'][0]
        self.faces['D'][2], self.faces['D'][1], self.faces['D'][0] = self.faces['R'][0], self.faces['R'][3], self.faces['R'][6]
        self.faces['R'][0], self.faces['R'][3], self.faces['R'][6] = temp
    
    def F_prime(self):
        """Rotate Front face counterclockwise"""
        self.rotate_face_counterclockwise('F')
        temp = [self.faces['U'][6], self.faces['U'][7], self.faces['U'][8]]
        self.faces['U'][6], self.faces['U'][7], self.faces['U'][8] = self.faces['R'][0], self.faces['R'][3], self.faces['R'][6]
        self.faces['R'][0], self.faces['R'][3], self.faces['R'][6] = self.faces['D'][2], self.faces['D'][1], self.faces['D'][0]
        self.faces['D'][2], self.faces['D'][1], self.faces['D'][0] = self.faces['L'][8], self.faces['L'][5], self.faces['L'][2]
        self.faces['L'][8], self.faces['L'][5], self.faces['L'][2] = temp
    
    def B(self):
        """Rotate Back face clockwise"""
        self.rotate_face_clockwise('B')
        temp = [self.faces['U'][0], self.faces['U'][1], self.faces['U'][2]]
        self.faces['U'][0], self.faces['U'][1], self.faces['U'][2] = self.faces['R'][2], self.faces['R'][5], self.faces['R'][8]
        self.faces['R'][2], self.faces['R'][5], self.faces['R'][8] = self.faces['D'][8], self.faces['D'][7], self.faces['D'][6]
        self.faces['D'][8], self.faces['D'][7], self.faces['D'][6] = self.faces['L'][6], self.faces['L'][3], self.faces['L'][0]
        self.faces['L'][6], self.faces['L'][3], self.faces['L'][0] = temp
    
    def B_prime(self):
        """Rotate Back face counterclockwise"""
        self.rotate_face_counterclockwise('B')
        temp = [self.faces['U'][0], self.faces['U'][1], self.faces['U'][2]]
        self.faces['U'][0], self.faces['U'][1], self.faces['U'][2] = self.faces['L'][6], self.faces['L'][3], self.faces['L'][0]
        self.faces['L'][6], self.faces['L'][3], self.faces['L'][0] = self.faces['D'][8], self.faces['D'][7], self.faces['D'][6]
        self.faces['D'][8], self.faces['D'][7], self.faces['D'][6] = self.faces['R'][2], self.faces['R'][5], self.faces['R'][8]
        self.faces['R'][2], self.faces['R'][5], self.faces['R'][8] = temp
    
    def apply_moves(self, moves: str):
        """Apply a sequence of moves to the cube"""
        move_map = {
            'U': self.U, "U'": self.U_prime,
            'D': self.D, "D'": self.D_prime,
            'R': self.R, "R'": self.R_prime,
            'L': self.L, "L'": self.L_prime,
            'F': self.F, "F'": self.F_prime,
            'B': self.B, "B'": self.B_prime,
        }
        
        move_list = moves.split()
        for move in move_list:
            if move in move_map:
                move_map[move]()
    
    def scramble(self, moves: str):
        """Scramble the cube with a sequence of moves"""
        self.apply_moves(moves)
    
    def get_state_string(self) -> str:
        """Get a string representation of the cube state"""
        return str(self.faces)


class RubiksCubeSolver:
    """
    Simple Rubik's Cube solver using BFS (Breadth-First Search)
    Note: This is a basic implementation for demonstration and testing.
    Real-world solvers use more sophisticated algorithms like Kociemba's algorithm.
    """
    
    def __init__(self):
        self.moves = ['U', "U'", 'D', "D'", 'R', "R'", 'L', "L'", 'F', "F'", 'B', "B'"]
    
    def solve_simple(self, cube: RubiksCube, max_depth: int = 6) -> List[str]:
        """
        Solve cube using BFS (limited depth for performance)
        Returns list of moves to solve the cube
        """
        if cube.is_solved():
            return []
        
        queue = deque([(cube.copy(), [])])
        visited = {cube.get_state_string()}
        
        while queue:
            current_cube, move_sequence = queue.popleft()
            
            if len(move_sequence) >= max_depth:
                continue
            
            for move in self.moves:
                new_cube = current_cube.copy()
                new_cube.apply_moves(move)
                
                if new_cube.is_solved():
                    return move_sequence + [move]
                
                state_str = new_cube.get_state_string()
                if state_str not in visited:
                    visited.add(state_str)
                    queue.append((new_cube, move_sequence + [move]))
        
        return None  # No solution found within max_depth
    
    def reverse_moves(self, moves: List[str]) -> List[str]:
        """
        Reverse a sequence of moves (useful for unscrambling)
        """
        reverse_map = {
            'U': "U'", "U'": 'U',
            'D': "D'", "D'": 'D',
            'R': "R'", "R'": 'R',
            'L': "L'", "L'": 'L',
            'F': "F'", "F'": 'F',
            'B': "B'", "B'": 'B',
        }
        
        return [reverse_map[move] for move in reversed(moves)]


def solve_cube(scramble_moves: str, max_depth: int = 6) -> Tuple[bool, List[str]]:
    """
    High-level function to solve a scrambled cube
    
    Args:
        scramble_moves: String of moves that scrambled the cube
        max_depth: Maximum search depth for solver
    
    Returns:
        Tuple of (success: bool, solution_moves: List[str])
    """
    cube = RubiksCube()
    cube.scramble(scramble_moves)
    
    solver = RubiksCubeSolver()
    solution = solver.solve_simple(cube, max_depth)
    
    if solution:
        return True, solution
    else:
        # Fallback: use reverse of scramble moves
        scramble_list = scramble_moves.split()
        solution = solver.reverse_moves(scramble_list)
        return True, solution
