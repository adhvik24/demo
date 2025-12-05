"""
Test Suite for Rubik's Cube Solver
This test script covers various aspects of the Rubik's cube implementation
"""

import unittest
from rubiks_cube_solver import RubiksCube, SimpleSolver


class TestRubiksCubeInitialization(unittest.TestCase):
    """Test cube initialization"""

    def test_cube_initialization(self):
        """Test that a new cube is in solved state"""
        cube = RubiksCube()
        self.assertTrue(cube.is_solved(), "New cube should be in solved state")

    def test_cube_faces_exist(self):
        """Test that all 6 faces are initialized"""
        cube = RubiksCube()
        expected_faces = ['U', 'D', 'F', 'B', 'L', 'R']
        self.assertEqual(set(cube.faces.keys()), set(expected_faces))

    def test_face_dimensions(self):
        """Test that each face is 3x3"""
        cube = RubiksCube()
        for face_name, face in cube.faces.items():
            self.assertEqual(len(face), 3, f"Face {face_name} should have 3 rows")
            for row in face:
                self.assertEqual(len(row), 3, f"Face {face_name} should have 3 columns")

    def test_initial_colors(self):
        """Test that initial colors are correct"""
        cube = RubiksCube()
        expected_colors = {
            'U': 'W',  # White
            'D': 'Y',  # Yellow
            'F': 'R',  # Red
            'B': 'O',  # Orange
            'L': 'B',  # Blue
            'R': 'G'   # Green
        }
        for face_name, expected_color in expected_colors.items():
            for row in cube.faces[face_name]:
                for color in row:
                    self.assertEqual(color, expected_color,
                                   f"Face {face_name} should be {expected_color}")


class TestBasicMoves(unittest.TestCase):
    """Test individual cube moves"""

    def test_move_U(self):
        """Test upper face rotation"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_U()
        self.assertNotEqual(cube.get_state(), initial_state,
                          "State should change after U move")
        self.assertFalse(cube.is_solved(), "Cube should not be solved after U move")

    def test_move_U_inverse(self):
        """Test that U followed by U' returns to original state"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_U()
        cube.move_U_prime()
        self.assertEqual(cube.get_state(), initial_state,
                        "U followed by U' should return to original state")

    def test_move_U_four_times(self):
        """Test that four U moves return to original state"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        for _ in range(4):
            cube.move_U()
        self.assertEqual(cube.get_state(), initial_state,
                        "Four U moves should return to original state")

    def test_move_D(self):
        """Test down face rotation"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_D()
        self.assertNotEqual(cube.get_state(), initial_state)

    def test_move_D_inverse(self):
        """Test that D followed by D' returns to original state"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_D()
        cube.move_D_prime()
        self.assertEqual(cube.get_state(), initial_state)

    def test_move_R(self):
        """Test right face rotation"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_R()
        self.assertNotEqual(cube.get_state(), initial_state)

    def test_move_R_inverse(self):
        """Test that R followed by R' returns to original state"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_R()
        cube.move_R_prime()
        self.assertEqual(cube.get_state(), initial_state)

    def test_move_L(self):
        """Test left face rotation"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_L()
        self.assertNotEqual(cube.get_state(), initial_state)

    def test_move_L_inverse(self):
        """Test that L followed by L' returns to original state"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_L()
        cube.move_L_prime()
        self.assertEqual(cube.get_state(), initial_state)

    def test_move_F(self):
        """Test front face rotation"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_F()
        self.assertNotEqual(cube.get_state(), initial_state)

    def test_move_F_inverse(self):
        """Test that F followed by F' returns to original state"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_F()
        cube.move_F_prime()
        self.assertEqual(cube.get_state(), initial_state)

    def test_move_B(self):
        """Test back face rotation"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_B()
        self.assertNotEqual(cube.get_state(), initial_state)

    def test_move_B_inverse(self):
        """Test that B followed by B' returns to original state"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_B()
        cube.move_B_prime()
        self.assertEqual(cube.get_state(), initial_state)


class TestMoveSequences(unittest.TestCase):
    """Test sequences of moves"""

    def test_execute_moves_single(self):
        """Test executing a single move via execute_moves"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.execute_moves("U")
        self.assertNotEqual(cube.get_state(), initial_state)

    def test_execute_moves_inverse_sequence(self):
        """Test executing moves and their inverses"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.execute_moves("U U'")
        self.assertEqual(cube.get_state(), initial_state)

    def test_execute_moves_complex_sequence(self):
        """Test executing a complex move sequence"""
        cube = RubiksCube()
        cube.execute_moves("R U R' U'")
        self.assertFalse(cube.is_solved())

    def test_sexy_move_six_times(self):
        """Test that sexy move (R U R' U') six times returns to original"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        for _ in range(6):
            cube.execute_moves("R U R' U'")
        self.assertEqual(cube.get_state(), initial_state,
                        "Sexy move repeated 6 times should return to original state")

    def test_commutator(self):
        """Test commutator [R, U] = R U R' U'"""
        cube1 = RubiksCube()
        cube2 = RubiksCube()

        cube1.execute_moves("R U R' U'")

        cube2.move_R()
        cube2.move_U()
        cube2.move_R_prime()
        cube2.move_U_prime()

        self.assertEqual(cube1.get_state(), cube2.get_state(),
                        "Both methods should produce same result")

    def test_move_independence(self):
        """Test that opposite face moves are independent"""
        cube = RubiksCube()
        initial_state = cube.get_state()

        # U and D should be independent
        cube.execute_moves("U D U' D'")
        self.assertEqual(cube.get_state(), initial_state)


class TestScramble(unittest.TestCase):
    """Test cube scrambling functionality"""

    def test_scramble_changes_state(self):
        """Test that scrambling changes the cube state"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.scramble(10)
        self.assertNotEqual(cube.get_state(), initial_state,
                          "Scramble should change cube state")

    def test_scramble_returns_sequence(self):
        """Test that scramble returns the move sequence"""
        cube = RubiksCube()
        sequence = cube.scramble(15)
        self.assertIsInstance(sequence, str, "Scramble should return a string")
        self.assertGreater(len(sequence), 0, "Scramble sequence should not be empty")

    def test_scramble_makes_unsolved(self):
        """Test that scrambling makes the cube unsolved"""
        cube = RubiksCube()
        cube.scramble(20)
        # There's a tiny chance it could randomly solve, but very unlikely
        self.assertFalse(cube.is_solved(),
                        "Scrambled cube should likely not be solved")

    def test_scramble_custom_length(self):
        """Test scrambling with custom number of moves"""
        cube = RubiksCube()
        sequence = cube.scramble(5)
        moves = sequence.split()
        # Each move is separated by space
        self.assertEqual(len(moves), 5, "Should have 5 moves in sequence")


class TestCubeState(unittest.TestCase):
    """Test cube state management"""

    def test_get_state(self):
        """Test getting cube state"""
        cube = RubiksCube()
        state = cube.get_state()
        self.assertIsInstance(state, dict)
        self.assertEqual(len(state), 6)

    def test_state_is_copy(self):
        """Test that get_state returns a copy, not reference"""
        cube = RubiksCube()
        state1 = cube.get_state()
        cube.move_U()
        state2 = cube.get_state()
        self.assertNotEqual(state1, state2,
                          "State should be a copy, not a reference")

    def test_is_solved_on_solved_cube(self):
        """Test is_solved returns True for solved cube"""
        cube = RubiksCube()
        self.assertTrue(cube.is_solved())

    def test_is_solved_on_scrambled_cube(self):
        """Test is_solved returns False for scrambled cube"""
        cube = RubiksCube()
        cube.move_U()
        self.assertFalse(cube.is_solved())


class TestFaceRotation(unittest.TestCase):
    """Test face rotation mechanics"""

    def test_rotate_face_clockwise(self):
        """Test clockwise face rotation"""
        cube = RubiksCube()
        initial_U = [row.copy() for row in cube.faces['U']]
        cube.rotate_face_clockwise('U')

        # After clockwise rotation, corners should be in new positions
        self.assertEqual(cube.faces['U'][0][2], initial_U[0][0])
        self.assertEqual(cube.faces['U'][2][2], initial_U[0][2])
        self.assertEqual(cube.faces['U'][2][0], initial_U[2][2])
        self.assertEqual(cube.faces['U'][0][0], initial_U[2][0])

    def test_rotate_face_counter_clockwise(self):
        """Test counter-clockwise face rotation"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.rotate_face_clockwise('U')
        cube.rotate_face_counter_clockwise('U')
        self.assertEqual(cube.faces['U'], initial_state['U'])

    def test_four_rotations_return_original(self):
        """Test that 4 rotations return to original"""
        cube = RubiksCube()
        initial_U = [row.copy() for row in cube.faces['U']]
        for _ in range(4):
            cube.rotate_face_clockwise('U')
        self.assertEqual(cube.faces['U'], initial_U)


class TestSolver(unittest.TestCase):
    """Test solver functionality"""

    def test_solver_exists(self):
        """Test that solver class exists"""
        solver = SimpleSolver()
        self.assertIsNotNone(solver)

    def test_solve_method_exists(self):
        """Test that solve method exists"""
        cube = RubiksCube()
        solver = SimpleSolver()
        result = solver.solve(cube)
        self.assertIsInstance(result, list)

    def test_solve_cross_method(self):
        """Test solve_cross method exists"""
        cube = RubiksCube()
        solver = SimpleSolver()
        result = solver.solve_cross(cube)
        self.assertIsInstance(result, list)

    def test_solve_corners_method(self):
        """Test solve_corners method exists"""
        cube = RubiksCube()
        solver = SimpleSolver()
        result = solver.solve_corners(cube)
        self.assertIsInstance(result, list)

    def test_solve_middle_layer_method(self):
        """Test solve_middle_layer method exists"""
        cube = RubiksCube()
        solver = SimpleSolver()
        result = solver.solve_middle_layer(cube)
        self.assertIsInstance(result, list)

    def test_solve_last_layer_method(self):
        """Test solve_last_layer method exists"""
        cube = RubiksCube()
        solver = SimpleSolver()
        result = solver.solve_last_layer(cube)
        self.assertIsInstance(result, list)


class TestAdvancedPatterns(unittest.TestCase):
    """Test known cube patterns and algorithms"""

    def test_superflip_pattern(self):
        """Test that superflip algorithm works"""
        cube = RubiksCube()
        # Superflip: all edges flipped, but cube appears solved
        superflip = "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2"
        cube.execute_moves(superflip)
        self.assertFalse(cube.is_solved(), "Superflip should not be solved state")

    def test_checkerboard_pattern(self):
        """Test checkerboard pattern"""
        cube = RubiksCube()
        checkerboard = "U2 D2 F2 B2 L2 R2"
        cube.execute_moves(checkerboard)
        self.assertFalse(cube.is_solved())

    def test_cube_in_cube_pattern(self):
        """Test cube in cube pattern"""
        cube = RubiksCube()
        cube_in_cube = "F L F U' R U F2 L2 U' L' B D' B' L2 U"
        cube.execute_moves(cube_in_cube)
        self.assertFalse(cube.is_solved())

    def test_t_perm(self):
        """Test T permutation (PLL algorithm)"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        t_perm = "R U R' U' R' F R2 U' R' U' R U R' F'"

        # Apply T-perm twice should return to original (it's a 2-cycle)
        cube.execute_moves(t_perm)
        cube.execute_moves(t_perm)
        self.assertEqual(cube.get_state(), initial_state,
                        "T-perm applied twice should return to original")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""

    def test_empty_move_sequence(self):
        """Test executing empty move sequence"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.execute_moves("")
        self.assertEqual(cube.get_state(), initial_state)

    def test_move_sequence_with_spaces(self):
        """Test move sequence with multiple spaces"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.execute_moves("U  U'")  # Double space
        self.assertEqual(cube.get_state(), initial_state)

    def test_scramble_with_zero_moves(self):
        """Test scramble with 0 moves"""
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.scramble(0)
        self.assertEqual(cube.get_state(), initial_state)

    def test_multiple_cube_instances(self):
        """Test that multiple cube instances are independent"""
        cube1 = RubiksCube()
        cube2 = RubiksCube()

        cube1.move_U()
        self.assertTrue(cube2.is_solved(),
                       "Cube2 should remain solved when cube1 is modified")
        self.assertFalse(cube1.is_solved())


if __name__ == '__main__':
    # Run the test suite
    unittest.main(verbosity=2)
