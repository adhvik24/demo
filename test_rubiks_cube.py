"""
Test Suite for Rubik's Cube Solver
Comprehensive tests for cube operations and solving algorithms
"""

import sys
from rubiks_cube_solver import RubiksCube, SimpleSolver
from copy import deepcopy


class TestRubiksCube:
    """Test cases for RubiksCube class"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.tests = []
    
    def assert_true(self, condition, test_name):
        """Assert that condition is true"""
        if condition:
            self.passed += 1
            self.tests.append((test_name, "PASS"))
            print(f"✓ {test_name}")
        else:
            self.failed += 1
            self.tests.append((test_name, "FAIL"))
            print(f"✗ {test_name}")
    
    def assert_false(self, condition, test_name):
        """Assert that condition is false"""
        self.assert_true(not condition, test_name)
    
    def assert_equal(self, actual, expected, test_name):
        """Assert that actual equals expected"""
        if actual == expected:
            self.passed += 1
            self.tests.append((test_name, "PASS"))
            print(f"✓ {test_name}")
        else:
            self.failed += 1
            self.tests.append((test_name, "FAIL"))
            print(f"✗ {test_name} - Expected: {expected}, Got: {actual}")
    
    def test_initialization(self):
        """Test cube initialization"""
        print("\n--- Testing Initialization ---")
        cube = RubiksCube()
        
        # Test that cube starts solved
        self.assert_true(cube.is_solved(), "Cube should start in solved state")
        
        # Test that all faces have correct colors
        self.assert_equal(cube.faces['U'][0][0], 'W', "Up face should be white")
        self.assert_equal(cube.faces['D'][0][0], 'Y', "Down face should be yellow")
        self.assert_equal(cube.faces['F'][0][0], 'G', "Front face should be green")
        self.assert_equal(cube.faces['B'][0][0], 'B', "Back face should be blue")
        self.assert_equal(cube.faces['L'][0][0], 'O', "Left face should be orange")
        self.assert_equal(cube.faces['R'][0][0], 'R', "Right face should be red")
        
        # Test that move history is empty
        self.assert_equal(len(cube.move_history), 0, "Move history should be empty")
    
    def test_single_moves(self):
        """Test individual move operations"""
        print("\n--- Testing Single Moves ---")
        
        # Test U move
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_U()
        self.assert_false(cube.is_solved(), "Cube should not be solved after U move")
        self.assert_equal(len(cube.move_history), 1, "Move history should have 1 move")
        self.assert_equal(cube.move_history[0], 'U', "Last move should be U")
        
        # Test U' reverses U
        cube = RubiksCube()
        cube.move_U()
        cube.move_U_prime()
        self.assert_true(cube.is_solved(), "U followed by U' should return to solved state")
        
        # Test D move
        cube = RubiksCube()
        cube.move_D()
        self.assert_false(cube.is_solved(), "Cube should not be solved after D move")
        cube.move_D_prime()
        self.assert_true(cube.is_solved(), "D followed by D' should return to solved state")
        
        # Test F move
        cube = RubiksCube()
        cube.move_F()
        self.assert_false(cube.is_solved(), "Cube should not be solved after F move")
        cube.move_F_prime()
        self.assert_true(cube.is_solved(), "F followed by F' should return to solved state")
        
        # Test B move
        cube = RubiksCube()
        cube.move_B()
        self.assert_false(cube.is_solved(), "Cube should not be solved after B move")
        cube.move_B_prime()
        self.assert_true(cube.is_solved(), "B followed by B' should return to solved state")
        
        # Test L move
        cube = RubiksCube()
        cube.move_L()
        self.assert_false(cube.is_solved(), "Cube should not be solved after L move")
        cube.move_L_prime()
        self.assert_true(cube.is_solved(), "L followed by L' should return to solved state")
        
        # Test R move
        cube = RubiksCube()
        cube.move_R()
        self.assert_false(cube.is_solved(), "Cube should not be solved after R move")
        cube.move_R_prime()
        self.assert_true(cube.is_solved(), "R followed by R' should return to solved state")
    
    def test_move_sequences(self):
        """Test sequences of moves"""
        print("\n--- Testing Move Sequences ---")
        
        # Test that 4 U moves return to solved state
        cube = RubiksCube()
        for _ in range(4):
            cube.move_U()
        self.assert_true(cube.is_solved(), "Four U moves should return to solved state")
        
        # Test that 4 R moves return to solved state
        cube = RubiksCube()
        for _ in range(4):
            cube.move_R()
        self.assert_true(cube.is_solved(), "Four R moves should return to solved state")
        
        # Test commutator [R, U] = R U R' U'
        cube = RubiksCube()
        initial_state = cube.get_state()
        cube.move_R()
        cube.move_U()
        cube.move_R_prime()
        cube.move_U_prime()
        # After commutator, cube should be different from initial
        self.assert_false(cube.is_solved(), "Commutator should change cube state")
        
        # Test that repeating commutator 6 times returns to solved
        cube = RubiksCube()
        for _ in range(6):
            cube.move_R()
            cube.move_U()
            cube.move_R_prime()
            cube.move_U_prime()
        self.assert_true(cube.is_solved(), "Six commutators should return to solved state")
    
    def test_execute_move(self):
        """Test execute_move method"""
        print("\n--- Testing Execute Move ---")
        
        cube = RubiksCube()
        
        # Test valid moves
        cube.execute_move('U')
        self.assert_equal(len(cube.move_history), 1, "Execute move should add to history")
        
        cube.execute_move("R'")
        self.assert_equal(len(cube.move_history), 2, "Execute move should add to history")
        
        # Test invalid move
        try:
            cube.execute_move('X')
            self.assert_true(False, "Invalid move should raise ValueError")
        except ValueError:
            self.assert_true(True, "Invalid move should raise ValueError")
    
    def test_scramble(self):
        """Test scramble functionality"""
        print("\n--- Testing Scramble ---")
        
        cube = RubiksCube()
        scramble_moves = cube.scramble(20)
        
        self.assert_equal(len(scramble_moves), 20, "Scramble should generate 20 moves")
        self.assert_false(cube.is_solved(), "Cube should not be solved after scramble")
        self.assert_equal(len(cube.move_history), 20, "Move history should have 20 moves")
        
        # Test that scramble with 0 moves keeps cube solved
        cube = RubiksCube()
        cube.scramble(0)
        self.assert_true(cube.is_solved(), "Scramble with 0 moves should keep cube solved")
    
    def test_is_solved(self):
        """Test is_solved method"""
        print("\n--- Testing Is Solved ---")
        
        cube = RubiksCube()
        self.assert_true(cube.is_solved(), "New cube should be solved")
        
        cube.move_U()
        self.assert_false(cube.is_solved(), "Cube should not be solved after move")
        
        cube.move_U_prime()
        self.assert_true(cube.is_solved(), "Cube should be solved after reverse move")
    
    def test_get_state(self):
        """Test get_state method"""
        print("\n--- Testing Get State ---")
        
        cube = RubiksCube()
        state1 = cube.get_state()
        
        # Modify cube
        cube.move_R()
        state2 = cube.get_state()
        
        # States should be different
        self.assert_false(state1 == state2, "States should differ after move")
        
        # Original state should not be modified (deep copy test)
        self.assert_equal(state1['U'][0][0], 'W', "Original state should not be modified")
    
    def test_face_rotation(self):
        """Test face rotation methods"""
        print("\n--- Testing Face Rotation ---")
        
        cube = RubiksCube()
        
        # Test clockwise rotation
        original_face = deepcopy(cube.faces['U'])
        cube.rotate_face_clockwise('U')
        rotated_face = cube.faces['U']
        
        # Check that corners rotated correctly
        self.assert_equal(rotated_face[0][0], original_face[2][0], 
                         "Top-left should be bottom-left after clockwise rotation")
        self.assert_equal(rotated_face[0][2], original_face[0][0], 
                         "Top-right should be top-left after clockwise rotation")
        
        # Test counterclockwise rotation reverses clockwise
        cube.rotate_face_counterclockwise('U')
        self.assert_equal(cube.faces['U'], original_face, 
                         "Counterclockwise should reverse clockwise rotation")
    
    def test_move_history(self):
        """Test move history tracking"""
        print("\n--- Testing Move History ---")
        
        cube = RubiksCube()
        
        cube.move_R()
        cube.move_U()
        cube.move_R_prime()
        cube.move_U_prime()
        
        expected_history = ['R', 'U', "R'", "U'"]
        self.assert_equal(cube.move_history, expected_history, 
                         "Move history should track all moves correctly")
        
        # Test that scramble resets history
        cube.scramble(5)
        self.assert_equal(len(cube.move_history), 5, 
                         "Scramble should reset move history")
    
    def run_all_tests(self):
        """Run all test cases"""
        print("=" * 60)
        print("RUBIK'S CUBE SOLVER - TEST SUITE")
        print("=" * 60)
        
        self.test_initialization()
        self.test_single_moves()
        self.test_move_sequences()
        self.test_execute_move()
        self.test_scramble()
        self.test_is_solved()
        self.test_get_state()
        self.test_face_rotation()
        self.test_move_history()
        
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {self.passed + self.failed}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Success Rate: {(self.passed / (self.passed + self.failed) * 100):.1f}%")
        print("=" * 60)
        
        return self.failed == 0


class TestSimpleSolver:
    """Test cases for SimpleSolver class"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
    
    def assert_true(self, condition, test_name):
        """Assert that condition is true"""
        if condition:
            self.passed += 1
            print(f"✓ {test_name}")
        else:
            self.failed += 1
            print(f"✗ {test_name}")
    
    def test_reverse_scramble(self):
        """Test reverse scramble solving"""
        print("\n--- Testing Reverse Scramble Solver ---")
        
        # Test with simple scramble
        cube = RubiksCube()
        scramble_moves = cube.scramble(5)
        
        solver = SimpleSolver(cube)
        solution = solver.reverse_scramble(scramble_moves)
        
        self.assert_true(cube.is_solved(), "Cube should be solved after reverse scramble")
        self.assert_true(len(solution) == 5, "Solution should have same length as scramble")
        
        # Test with longer scramble
        cube = RubiksCube()
        scramble_moves = cube.scramble(20)
        
        solver = SimpleSolver(cube)
        solution = solver.reverse_scramble(scramble_moves)
        
        self.assert_true(cube.is_solved(), "Cube should be solved after reverse scramble (20 moves)")
        self.assert_true(len(solution) == 20, "Solution should have 20 moves")
    
    def test_solver_initialization(self):
        """Test solver initialization"""
        print("\n--- Testing Solver Initialization ---")
        
        cube = RubiksCube()
        solver = SimpleSolver(cube)
        
        self.assert_true(solver.cube is cube, "Solver should reference the cube")
        self.assert_true(len(solver.solution) == 0, "Solution should start empty")
    
    def run_all_tests(self):
        """Run all solver tests"""
        print("\n" + "=" * 60)
        print("SIMPLE SOLVER - TEST SUITE")
        print("=" * 60)
        
        self.test_solver_initialization()
        self.test_reverse_scramble()
        
        print("\n" + "=" * 60)
        print("SOLVER TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {self.passed + self.failed}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Success Rate: {(self.passed / (self.passed + self.failed) * 100):.1f}%")
        print("=" * 60)
        
        return self.failed == 0


def run_integration_tests():
    """Run integration tests"""
    print("\n" + "=" * 60)
    print("INTEGRATION TESTS")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    # Test 1: Full solve workflow
    print("\n--- Test: Full Solve Workflow ---")
    cube = RubiksCube()
    scramble = cube.scramble(15)
    solver = SimpleSolver(cube)
    solution = solver.reverse_scramble(scramble)
    
    if cube.is_solved():
        print("✓ Full solve workflow successful")
        passed += 1
    else:
        print("✗ Full solve workflow failed")
        failed += 1
    
    # Test 2: Multiple solve cycles
    print("\n--- Test: Multiple Solve Cycles ---")
    success = True
    for i in range(5):
        cube = RubiksCube()
        scramble = cube.scramble(10)
        solver = SimpleSolver(cube)
        solution = solver.reverse_scramble(scramble)
        if not cube.is_solved():
            success = False
            break
    
    if success:
        print("✓ Multiple solve cycles successful")
        passed += 1
    else:
        print("✗ Multiple solve cycles failed")
        failed += 1
    
    # Test 3: Edge cases
    print("\n--- Test: Edge Cases ---")
    
    # Already solved cube
    cube = RubiksCube()
    if cube.is_solved():
        print("✓ Already solved cube handled correctly")
        passed += 1
    else:
        print("✗ Already solved cube test failed")
        failed += 1
    
    print("\n" + "=" * 60)
    print("INTEGRATION TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print("=" * 60)
    
    return failed == 0


def main():
    """Main test runner"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "RUBIK'S CUBE SOLVER TEST SUITE" + " " * 17 + "║")
    print("╚" + "═" * 58 + "╝")
    
    # Run cube tests
    cube_tester = TestRubiksCube()
    cube_tests_passed = cube_tester.run_all_tests()
    
    # Run solver tests
    solver_tester = TestSimpleSolver()
    solver_tests_passed = solver_tester.run_all_tests()
    
    # Run integration tests
    integration_tests_passed = run_integration_tests()
    
    # Final summary
    print("\n" + "╔" + "═" * 58 + "╗")
    print("║" + " " * 18 + "FINAL SUMMARY" + " " * 27 + "║")
    print("╠" + "═" * 58 + "╣")
    
    total_passed = cube_tester.passed + solver_tester.passed
    total_failed = cube_tester.failed + solver_tester.failed
    
    print(f"║  Cube Tests:        {'PASSED' if cube_tests_passed else 'FAILED':<40} ║")
    print(f"║  Solver Tests:      {'PASSED' if solver_tests_passed else 'FAILED':<40} ║")
    print(f"║  Integration Tests: {'PASSED' if integration_tests_passed else 'FAILED':<40} ║")
    print("╠" + "═" * 58 + "╣")
    print(f"║  Total Passed:      {total_passed:<40} ║")
    print(f"║  Total Failed:      {total_failed:<40} ║")
    print("╚" + "═" * 58 + "╝")
    
    # Exit with appropriate code
    if cube_tests_passed and solver_tests_passed and integration_tests_passed:
        print("\n✓ All tests passed!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
