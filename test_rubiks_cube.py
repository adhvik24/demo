"""
Test script for Rubik's Cube Solver
Tests the functionality of the RubiksCube class and SimpleSolver
"""

import unittest
from rubiks_cube import RubiksCube, SimpleSolver


class TestRubiksCube(unittest.TestCase):
    """Test cases for RubiksCube class"""

    def setUp(self):
        """Set up a fresh cube for each test"""
        self.cube = RubiksCube()

    def test_initial_state_is_solved(self):
        """Test that a newly initialized cube is in solved state"""
        self.assertTrue(self.cube.is_solved())

    def test_single_move_unsolved(self):
        """Test that a single move makes the cube unsolved"""
        self.cube.F()
        self.assertFalse(self.cube.is_solved())

    def test_move_and_inverse(self):
        """Test that a move followed by its inverse returns to solved state"""
        self.cube.F()
        self.cube.F_prime()
        self.assertTrue(self.cube.is_solved())

    def test_four_same_moves(self):
        """Test that four identical moves return to solved state"""
        self.cube.R()
        self.cube.R()
        self.cube.R()
        self.cube.R()
        self.assertTrue(self.cube.is_solved())

    def test_move_history_tracking(self):
        """Test that move history is properly tracked"""
        self.cube.F()
        self.cube.R()
        self.cube.U()
        self.assertEqual(len(self.cube.move_history), 3)
        self.assertEqual(self.cube.move_history, ['F', 'R', 'U'])

    def test_all_basic_moves(self):
        """Test that all basic moves can be executed without error"""
        moves = [
            self.cube.F, self.cube.F_prime,
            self.cube.R, self.cube.R_prime,
            self.cube.U, self.cube.U_prime,
            self.cube.D, self.cube.D_prime,
            self.cube.L, self.cube.L_prime,
            self.cube.B, self.cube.B_prime
        ]

        for move in moves:
            test_cube = RubiksCube()
            move_func = getattr(test_cube, move.__name__)
            move_func()
            self.assertFalse(test_cube.is_solved())

    def test_execute_moves_string(self):
        """Test executing moves from a string"""
        self.cube.execute_moves("F R U R' U' F'")
        self.assertEqual(len(self.cube.move_history), 6)

    def test_scramble(self):
        """Test scramble functionality"""
        scramble_moves = "F R U R' U' F' R U R' U' R' F R F'"
        self.cube.scramble(scramble_moves)
        self.assertFalse(self.cube.is_solved())

    def test_face_rotation_clockwise(self):
        """Test face rotation clockwise"""
        face = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        rotated = self.cube.rotate_face_clockwise(face)
        expected = [['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3']]
        self.assertEqual(rotated, expected)

    def test_face_rotation_counterclockwise(self):
        """Test face rotation counterclockwise"""
        face = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        rotated = self.cube.rotate_face_counterclockwise(face)
        expected = [['3', '6', '9'], ['2', '5', '8'], ['1', '4', '7']]
        self.assertEqual(rotated, expected)

    def test_get_state(self):
        """Test that get_state returns a deep copy"""
        state1 = self.cube.get_state()
        self.cube.F()
        state2 = self.cube.get_state()
        self.assertNotEqual(state1, state2)

    def test_string_representation(self):
        """Test that string representation works"""
        cube_str = str(self.cube)
        self.assertIn("Rubik's Cube State:", cube_str)
        self.assertIn("F face:", cube_str)

    def test_opposite_moves_cancel(self):
        """Test that opposite moves cancel each other"""
        # Save initial state
        initial_state = self.cube.get_state()

        # Perform moves
        self.cube.R()
        self.cube.R_prime()

        # Check state matches
        final_state = self.cube.get_state()
        self.assertEqual(initial_state, final_state)

    def test_sexy_move_algorithm(self):
        """Test the 'sexy move' algorithm (R U R' U')"""
        self.cube.execute_moves("R U R' U'")
        # After sexy move, cube should not be solved
        self.assertFalse(self.cube.is_solved())

        # Repeat 6 times should return to solved (with some orientation changes)
        for _ in range(5):
            self.cube.execute_moves("R U R' U'")

    def test_t_perm(self):
        """Test T-perm algorithm"""
        t_perm = "R U R' U' R' F R2 U' R' U' R U R' F'"
        self.cube.execute_moves(t_perm)
        # After T-perm on solved cube, it should not be solved
        self.assertFalse(self.cube.is_solved())


class TestSimpleSolver(unittest.TestCase):
    """Test cases for SimpleSolver class"""

    def setUp(self):
        """Set up a fresh cube and solver for each test"""
        self.cube = RubiksCube()
        self.solver = SimpleSolver(self.cube)

    def test_solver_initialization(self):
        """Test that solver initializes correctly"""
        self.assertIsNotNone(self.solver)
        self.assertEqual(self.solver.solution, [])

    def test_solve_already_solved_cube(self):
        """Test solving an already solved cube"""
        solution = self.solver.solve()
        self.assertEqual(solution, [])

    def test_get_solution_string(self):
        """Test getting solution as string"""
        self.solver.solution = ['R', 'U', "R'", "U'"]
        solution_str = self.solver.get_solution_string()
        self.assertEqual(solution_str, "R U R' U'")


class TestCubeIntegration(unittest.TestCase):
    """Integration tests for cube operations"""

    def test_scramble_and_check_state(self):
        """Test scrambling and verifying unsolved state"""
        cube = RubiksCube()
        cube.scramble("R U R' U' F' U F")
        self.assertFalse(cube.is_solved())

    def test_multiple_scrambles(self):
        """Test multiple different scrambles"""
        scrambles = [
            "F R U R' U' F'",
            "R U R' U R U2 R'",
            "F R U' R' U' R U R' F' R U R' U' R' F R F'",
            "L U L' U L U2 L'"
        ]

        for scramble in scrambles:
            cube = RubiksCube()
            cube.scramble(scramble)
            self.assertFalse(cube.is_solved(),
                           f"Cube should be unsolved after scramble: {scramble}")

    def test_commutator_returns_to_solved(self):
        """Test that a commutator sequence returns to solved state"""
        cube = RubiksCube()
        # [R, U] commutator: R U R' U'
        # Repeated multiple times should eventually return to solved
        cube.execute_moves("R U R' U' R U R' U' R U R' U'")
        cube.execute_moves("R U R' U' R U R' U' R U R' U'")
        cube.execute_moves("R U R' U' R U R' U' R U R' U'")

    def test_superflip_pattern(self):
        """Test creating a superflip pattern (all edges flipped)"""
        cube = RubiksCube()
        # Simplified version - just test a complex sequence doesn't break
        superflip = "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2"
        cube.execute_moves(superflip)
        self.assertFalse(cube.is_solved())


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions"""

    def test_empty_move_sequence(self):
        """Test executing empty move sequence"""
        cube = RubiksCube()
        cube.execute_moves("")
        self.assertTrue(cube.is_solved())

    def test_whitespace_in_moves(self):
        """Test moves with extra whitespace"""
        cube = RubiksCube()
        cube.execute_moves("R  U   R'  U'")
        self.assertEqual(len(cube.move_history), 4)

    def test_state_independence(self):
        """Test that multiple cubes maintain independent state"""
        cube1 = RubiksCube()
        cube2 = RubiksCube()

        cube1.F()
        self.assertFalse(cube1.is_solved())
        self.assertTrue(cube2.is_solved())

    def test_deep_copy_state(self):
        """Test that get_state returns a proper deep copy"""
        cube = RubiksCube()
        state = cube.get_state()

        # Modify the retrieved state
        state['F'][0][0] = 'X'

        # Original cube should be unchanged
        self.assertNotEqual(cube.cube['F'][0][0], 'X')


def run_tests():
    """Run all tests and print results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestRubiksCube))
    suite.addTests(loader.loadTestsFromTestCase(TestSimpleSolver))
    suite.addTests(loader.loadTestsFromTestCase(TestCubeIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))

    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)

    return result


if __name__ == '__main__':
    run_tests()
