"""
Test script for Rubik's Cube Solver
Tests various scenarios without actually running the tests
"""

import sys
from rubiks_cube import RubiksCube, RubiksCubeSolver, solve_cube


class TestRubiksCube:
    """Test cases for RubiksCube class"""
    
    def test_initial_state_is_solved(self):
        """Test that a new cube is in solved state"""
        cube = RubiksCube()
        assert cube.is_solved(), "New cube should be solved"
        print("✓ test_initial_state_is_solved")
    
    def test_single_move_unsolved(self):
        """Test that a single move makes cube unsolved"""
        cube = RubiksCube()
        cube.U()
        assert not cube.is_solved(), "Cube should be unsolved after one move"
        print("✓ test_single_move_unsolved")
    
    def test_move_and_reverse(self):
        """Test that a move followed by its reverse returns to solved state"""
        cube = RubiksCube()
        cube.U()
        cube.U_prime()
        assert cube.is_solved(), "U followed by U' should return to solved state"
        print("✓ test_move_and_reverse")
    
    def test_four_same_moves_returns_to_start(self):
        """Test that four identical moves return to original state"""
        cube = RubiksCube()
        original_state = cube.copy()
        cube.R()
        cube.R()
        cube.R()
        cube.R()
        assert cube == original_state, "Four R moves should return to original state"
        print("✓ test_four_same_moves_returns_to_start")
    
    def test_all_basic_moves(self):
        """Test that all basic moves execute without error"""
        cube = RubiksCube()
        moves = [cube.U, cube.D, cube.R, cube.L, cube.F, cube.B]
        for move in moves:
            move()
        assert not cube.is_solved(), "Multiple moves should unsolved the cube"
        print("✓ test_all_basic_moves")
    
    def test_all_prime_moves(self):
        """Test that all prime (reverse) moves execute without error"""
        cube = RubiksCube()
        moves = [cube.U_prime, cube.D_prime, cube.R_prime, cube.L_prime, cube.F_prime, cube.B_prime]
        for move in moves:
            move()
        assert not cube.is_solved(), "Multiple prime moves should unsolved the cube"
        print("✓ test_all_prime_moves")
    
    def test_apply_moves_string(self):
        """Test applying moves from a string"""
        cube = RubiksCube()
        cube.apply_moves("R U R' U'")
        assert not cube.is_solved(), "Sexy move should unsolved the cube"
        print("✓ test_apply_moves_string")
    
    def test_scramble_method(self):
        """Test scramble method"""
        cube = RubiksCube()
        cube.scramble("R U R' U' F' U' F")
        assert not cube.is_solved(), "Scrambled cube should be unsolved"
        print("✓ test_scramble_method")
    
    def test_cube_copy(self):
        """Test that cube copy creates independent instance"""
        cube1 = RubiksCube()
        cube1.R()
        cube2 = cube1.copy()
        cube2.U()
        assert cube1 != cube2, "Copied cubes should be independent"
        print("✓ test_cube_copy")
    
    def test_cube_equality(self):
        """Test cube equality comparison"""
        cube1 = RubiksCube()
        cube2 = RubiksCube()
        assert cube1 == cube2, "Two new cubes should be equal"
        cube1.R()
        assert cube1 != cube2, "Cubes with different states should not be equal"
        print("✓ test_cube_equality")


class TestRubiksCubeSolver:
    """Test cases for RubiksCubeSolver class"""
    
    def test_solve_already_solved_cube(self):
        """Test solving an already solved cube"""
        cube = RubiksCube()
        solver = RubiksCubeSolver()
        solution = solver.solve_simple(cube, max_depth=3)
        assert solution == [], "Solved cube should return empty solution"
        print("✓ test_solve_already_solved_cube")
    
    def test_solve_one_move_scramble(self):
        """Test solving a cube scrambled with one move"""
        cube = RubiksCube()
        cube.U()
        solver = RubiksCubeSolver()
        solution = solver.solve_simple(cube, max_depth=3)
        assert solution is not None, "Should find solution for one-move scramble"
        assert len(solution) <= 1, "Solution should be at most 1 move"
        print("✓ test_solve_one_move_scramble")
    
    def test_solve_two_move_scramble(self):
        """Test solving a cube scrambled with two moves"""
        cube = RubiksCube()
        cube.apply_moves("R U")
        solver = RubiksCubeSolver()
        solution = solver.solve_simple(cube, max_depth=4)
        assert solution is not None, "Should find solution for two-move scramble"
        assert len(solution) <= 2, "Solution should be at most 2 moves"
        print("✓ test_solve_two_move_scramble")
    
    def test_solution_actually_solves(self):
        """Test that applying solution actually solves the cube"""
        cube = RubiksCube()
        cube.apply_moves("R U")
        solver = RubiksCubeSolver()
        solution = solver.solve_simple(cube, max_depth=4)
        
        # Apply solution to scrambled cube
        test_cube = RubiksCube()
        test_cube.apply_moves("R U")
        test_cube.apply_moves(" ".join(solution))
        
        assert test_cube.is_solved(), "Applying solution should solve the cube"
        print("✓ test_solution_actually_solves")
    
    def test_reverse_moves(self):
        """Test reverse moves function"""
        solver = RubiksCubeSolver()
        moves = ["R", "U", "F'"]
        reversed_moves = solver.reverse_moves(moves)
        expected = ["F", "U'", "R'"]
        assert reversed_moves == expected, f"Expected {expected}, got {reversed_moves}"
        print("✓ test_reverse_moves")
    
    def test_reverse_moves_solves_scramble(self):
        """Test that reversed moves solve the scramble"""
        cube = RubiksCube()
        scramble = "R U F"
        cube.apply_moves(scramble)
        
        solver = RubiksCubeSolver()
        reversed_moves = solver.reverse_moves(scramble.split())
        
        cube.apply_moves(" ".join(reversed_moves))
        assert cube.is_solved(), "Reversed moves should solve the scramble"
        print("✓ test_reverse_moves_solves_scramble")


class TestSolveCubeFunction:
    """Test cases for high-level solve_cube function"""
    
    def test_solve_simple_scramble(self):
        """Test solving a simple scramble"""
        success, solution = solve_cube("R U", max_depth=4)
        assert success, "Should successfully solve simple scramble"
        assert solution is not None, "Should return a solution"
        assert len(solution) > 0, "Solution should not be empty"
        print("✓ test_solve_simple_scramble")
    
    def test_solution_format(self):
        """Test that solution is in correct format"""
        success, solution = solve_cube("R", max_depth=3)
        assert isinstance(solution, list), "Solution should be a list"
        assert all(isinstance(move, str) for move in solution), "All moves should be strings"
        print("✓ test_solution_format")
    
    def test_verify_solution_works(self):
        """Test that returned solution actually solves the cube"""
        scramble = "R U R'"
        success, solution = solve_cube(scramble, max_depth=5)
        
        # Verify solution
        cube = RubiksCube()
        cube.scramble(scramble)
        cube.apply_moves(" ".join(solution))
        
        assert cube.is_solved(), "Solution should solve the scrambled cube"
        print("✓ test_verify_solution_works")
    
    def test_complex_scramble(self):
        """Test solving a more complex scramble"""
        scramble = "R U R' U' F' U' F"
        success, solution = solve_cube(scramble, max_depth=8)
        assert success, "Should find solution for complex scramble"
        
        # Verify it works
        cube = RubiksCube()
        cube.scramble(scramble)
        cube.apply_moves(" ".join(solution))
        assert cube.is_solved(), "Complex scramble solution should work"
        print("✓ test_complex_scramble")


class TestEdgeCases:
    """Test edge cases and special scenarios"""
    
    def test_empty_scramble(self):
        """Test solving with empty scramble"""
        success, solution = solve_cube("", max_depth=3)
        assert success, "Empty scramble should succeed"
        print("✓ test_empty_scramble")
    
    def test_repeated_moves(self):
        """Test scramble with repeated moves"""
        cube = RubiksCube()
        cube.apply_moves("R R R")
        solver = RubiksCubeSolver()
        solution = solver.solve_simple(cube, max_depth=3)
        assert solution is not None, "Should solve repeated moves"
        print("✓ test_repeated_moves")
    
    def test_opposite_faces(self):
        """Test moves on opposite faces"""
        cube = RubiksCube()
        cube.apply_moves("U D")
        solver = RubiksCubeSolver()
        solution = solver.solve_simple(cube, max_depth=4)
        assert solution is not None, "Should solve opposite face moves"
        print("✓ test_opposite_faces")
    
    def test_all_faces_once(self):
        """Test scramble using all faces once"""
        scramble = "U D R L F B"
        success, solution = solve_cube(scramble, max_depth=8)
        assert success, "Should handle all faces scramble"
        print("✓ test_all_faces_once")


class TestPerformance:
    """Test performance characteristics"""
    
    def test_max_depth_limit(self):
        """Test that solver respects max_depth limit"""
        cube = RubiksCube()
        cube.scramble("R U R' U' R U R' U'")  # Complex scramble
        solver = RubiksCubeSolver()
        solution = solver.solve_simple(cube, max_depth=2)
        # Should either find solution within depth or return None
        if solution:
            assert len(solution) <= 2, "Solution should respect max_depth"
        print("✓ test_max_depth_limit")
    
    def test_solver_terminates(self):
        """Test that solver terminates in reasonable time"""
        import time
        cube = RubiksCube()
        cube.scramble("R U F")
        solver = RubiksCubeSolver()
        
        start_time = time.time()
        solution = solver.solve_simple(cube, max_depth=5)
        elapsed_time = time.time() - start_time
        
        assert elapsed_time < 10, "Solver should complete within 10 seconds"
        print(f"✓ test_solver_terminates (completed in {elapsed_time:.2f}s)")


def run_all_tests():
    """Run all test suites"""
    print("=" * 60)
    print("RUBIK'S CUBE SOLVER TEST SUITE")
    print("=" * 60)
    
    test_classes = [
        TestRubiksCube,
        TestRubiksCubeSolver,
        TestSolveCubeFunction,
        TestEdgeCases,
        TestPerformance
    ]
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    for test_class in test_classes:
        print(f"\n{test_class.__name__}")
        print("-" * 60)
        
        test_instance = test_class()
        test_methods = [method for method in dir(test_instance) if method.startswith('test_')]
        
        for test_method_name in test_methods:
            total_tests += 1
            try:
                test_method = getattr(test_instance, test_method_name)
                test_method()
                passed_tests += 1
            except AssertionError as e:
                failed_tests += 1
                print(f"✗ {test_method_name} - FAILED: {e}")
            except Exception as e:
                failed_tests += 1
                print(f"✗ {test_method_name} - ERROR: {e}")
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    print("=" * 60)
    
    return failed_tests == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
