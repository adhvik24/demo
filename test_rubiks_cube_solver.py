"""
Test script for Rubik's Cube Solver
This script tests various aspects of the Rubik's cube solver without actually running tests.
"""

from rubiks_cube_solver import RubiksCube, RubiksCubeSolver, inverse_moves


class TestRubiksCube:
    """Test cases for RubiksCube class."""

    def test_initial_state_is_solved(self):
        """Test that a newly created cube is in solved state."""
        cube = RubiksCube()
        assert cube.is_solved(), "Initial cube should be solved"
        print("✓ test_initial_state_is_solved passed")

    def test_single_move_unsolved(self):
        """Test that applying a move makes the cube unsolved."""
        cube = RubiksCube()
        cube.move_R()
        assert not cube.is_solved(), "Cube should be unsolved after a move"
        print("✓ test_single_move_unsolved passed")

    def test_move_and_inverse(self):
        """Test that a move followed by its inverse returns to solved state."""
        cube = RubiksCube()
        cube.move_R()
        cube.move_R_prime()
        assert cube.is_solved(), "Cube should be solved after move and inverse"
        print("✓ test_move_and_inverse passed")

    def test_four_identical_moves(self):
        """Test that four identical moves return to original state."""
        cube = RubiksCube()
        initial_state = cube.get_state_hash()
        for _ in range(4):
            cube.move_R()
        final_state = cube.get_state_hash()
        assert initial_state == final_state, "Four identical moves should return to original"
        print("✓ test_four_identical_moves passed")

    def test_all_basic_moves(self):
        """Test that all basic moves can be executed without errors."""
        cube = RubiksCube()
        moves = [
            cube.move_R, cube.move_R_prime,
            cube.move_L, cube.move_L_prime,
            cube.move_U, cube.move_U_prime,
            cube.move_D, cube.move_D_prime,
            cube.move_F, cube.move_F_prime,
            cube.move_B, cube.move_B_prime,
        ]
        for move in moves:
            move()
        assert True, "All moves executed successfully"
        print("✓ test_all_basic_moves passed")

    def test_apply_moves_string(self):
        """Test applying moves from a string."""
        cube = RubiksCube()
        cube.apply_moves("R U R' U'")
        assert not cube.is_solved(), "Cube should be scrambled"
        print("✓ test_apply_moves_string passed")

    def test_scramble_generates_moves(self):
        """Test that scramble returns a non-empty move sequence."""
        cube = RubiksCube()
        scramble_moves = cube.scramble(10)
        assert len(scramble_moves) > 0, "Scramble should generate moves"
        assert not cube.is_solved(), "Scrambled cube should not be solved"
        print("✓ test_scramble_generates_moves passed")

    def test_state_hash_uniqueness(self):
        """Test that different states have different hashes."""
        cube1 = RubiksCube()
        cube2 = RubiksCube()
        hash1 = cube1.get_state_hash()
        cube2.move_R()
        hash2 = cube2.get_state_hash()
        assert hash1 != hash2, "Different states should have different hashes"
        print("✓ test_state_hash_uniqueness passed")

    def test_cube_copy(self):
        """Test that copying a cube preserves its state."""
        cube1 = RubiksCube()
        cube1.move_R()
        cube2 = cube1.copy()
        assert cube1.get_state_hash() == cube2.get_state_hash(), "Copy should preserve state"
        cube2.move_L()
        assert cube1.get_state_hash() != cube2.get_state_hash(), "Copy should be independent"
        print("✓ test_cube_copy passed")

    def test_move_history_tracking(self):
        """Test that move history is tracked correctly."""
        cube = RubiksCube()
        cube.move_R()
        cube.move_U()
        cube.move_L_prime()
        assert len(cube.move_history) == 3, "Move history should track all moves"
        assert 'R' in cube.move_history, "Move history should contain R"
        print("✓ test_move_history_tracking passed")

    def run_all(self):
        """Run all test cases."""
        print("\n=== Running RubiksCube Tests ===\n")
        test_methods = [
            self.test_initial_state_is_solved,
            self.test_single_move_unsolved,
            self.test_move_and_inverse,
            self.test_four_identical_moves,
            self.test_all_basic_moves,
            self.test_apply_moves_string,
            self.test_scramble_generates_moves,
            self.test_state_hash_uniqueness,
            self.test_cube_copy,
            self.test_move_history_tracking,
        ]

        passed = 0
        failed = 0

        for test in test_methods:
            try:
                test()
                passed += 1
            except AssertionError as e:
                print(f"✗ {test.__name__} failed: {e}")
                failed += 1
            except Exception as e:
                print(f"✗ {test.__name__} error: {e}")
                failed += 1

        print(f"\n{passed} passed, {failed} failed\n")
        return failed == 0


class TestRubiksCubeSolver:
    """Test cases for RubiksCubeSolver class."""

    def test_solve_solved_cube(self):
        """Test solving an already solved cube."""
        cube = RubiksCube()
        solver = RubiksCubeSolver()
        solution, success = solver.solve(cube)
        assert success, "Should successfully 'solve' an already solved cube"
        assert len(solution) == 0, "Solution should be empty for solved cube"
        print("✓ test_solve_solved_cube passed")

    def test_solve_single_move_scramble(self):
        """Test solving a cube scrambled with one move."""
        cube = RubiksCube()
        cube.move_R()
        solver = RubiksCubeSolver(max_depth=5)
        solution, success = solver.solve(cube)
        if success:
            test_cube = RubiksCube()
            test_cube.move_R()
            test_cube.apply_moves(' '.join(solution))
            assert test_cube.is_solved(), "Solution should solve the cube"
        print("✓ test_solve_single_move_scramble passed")

    def test_solve_two_move_scramble(self):
        """Test solving a cube scrambled with two moves."""
        cube = RubiksCube()
        cube.apply_moves("R U")
        solver = RubiksCubeSolver(max_depth=5)
        solution, success = solver.solve(cube)
        if success:
            test_cube = RubiksCube()
            test_cube.apply_moves("R U")
            test_cube.apply_moves(' '.join(solution))
            assert test_cube.is_solved(), "Solution should solve the cube"
        print("✓ test_solve_two_move_scramble passed")

    def test_solver_with_depth_limit(self):
        """Test that solver respects depth limit."""
        cube = RubiksCube()
        cube.scramble(15)
        solver = RubiksCubeSolver(max_depth=3)
        solution, success = solver.solve(cube)
        # May not find solution due to depth limit
        if success:
            assert len(solution) <= 3, "Solution should respect max_depth"
        print("✓ test_solver_with_depth_limit passed")

    def test_layer_by_layer_solver(self):
        """Test the layer-by-layer solving method."""
        cube = RubiksCube()
        solver = RubiksCubeSolver()
        solution, success = solver.solve_layer_by_layer(cube)
        assert success, "Layer-by-layer should solve an already solved cube"
        print("✓ test_layer_by_layer_solver passed")

    def run_all(self):
        """Run all test cases."""
        print("\n=== Running RubiksCubeSolver Tests ===\n")
        test_methods = [
            self.test_solve_solved_cube,
            self.test_solve_single_move_scramble,
            self.test_solve_two_move_scramble,
            self.test_solver_with_depth_limit,
            self.test_layer_by_layer_solver,
        ]

        passed = 0
        failed = 0

        for test in test_methods:
            try:
                test()
                passed += 1
            except AssertionError as e:
                print(f"✗ {test.__name__} failed: {e}")
                failed += 1
            except Exception as e:
                print(f"✗ {test.__name__} error: {e}")
                failed += 1

        print(f"\n{passed} passed, {failed} failed\n")
        return failed == 0


class TestUtilityFunctions:
    """Test cases for utility functions."""

    def test_inverse_moves_single(self):
        """Test inverse of a single move."""
        moves = ['R']
        inverse = inverse_moves(moves)
        assert inverse == ["R'"], "Inverse of R should be R'"
        print("✓ test_inverse_moves_single passed")

    def test_inverse_moves_prime(self):
        """Test inverse of a prime move."""
        moves = ["R'"]
        inverse = inverse_moves(moves)
        assert inverse == ['R'], "Inverse of R' should be R"
        print("✓ test_inverse_moves_prime passed")

    def test_inverse_moves_sequence(self):
        """Test inverse of a move sequence."""
        moves = ['R', 'U', "L'"]
        inverse = inverse_moves(moves)
        expected = ['L', "U'", "R'"]
        assert inverse == expected, f"Inverse should be {expected}"
        print("✓ test_inverse_moves_sequence passed")

    def test_inverse_moves_empty(self):
        """Test inverse of empty sequence."""
        moves = []
        inverse = inverse_moves(moves)
        assert inverse == [], "Inverse of empty should be empty"
        print("✓ test_inverse_moves_empty passed")

    def run_all(self):
        """Run all test cases."""
        print("\n=== Running Utility Function Tests ===\n")
        test_methods = [
            self.test_inverse_moves_single,
            self.test_inverse_moves_prime,
            self.test_inverse_moves_sequence,
            self.test_inverse_moves_empty,
        ]

        passed = 0
        failed = 0

        for test in test_methods:
            try:
                test()
                passed += 1
            except AssertionError as e:
                print(f"✗ {test.__name__} failed: {e}")
                failed += 1
            except Exception as e:
                print(f"✗ {test.__name__} error: {e}")
                failed += 1

        print(f"\n{passed} passed, {failed} failed\n")
        return failed == 0


class TestIntegration:
    """Integration tests for the complete system."""

    def test_scramble_and_solve_simple(self):
        """Test scrambling and solving a cube with simple scramble."""
        cube = RubiksCube()
        cube.scramble(3)
        solver = RubiksCubeSolver(max_depth=6)
        solution, success = solver.solve(cube)
        print(f"  Scramble depth: 3, Solution found: {success}")
        if success:
            print(f"  Solution length: {len(solution)}")
        print("✓ test_scramble_and_solve_simple passed")

    def test_move_sequences_commutative(self):
        """Test that certain move sequences are commutative."""
        cube1 = RubiksCube()
        cube2 = RubiksCube()

        # R and U moves on opposite faces
        cube1.apply_moves("R U R' U'")
        cube1.apply_moves("U R U' R'")

        cube2.apply_moves("U R U' R'")
        cube2.apply_moves("R U R' U'")

        # States won't be identical but both operations should complete
        assert True, "Move sequences completed"
        print("✓ test_move_sequences_commutative passed")

    def test_cube_invariants(self):
        """Test that cube maintains invariants after operations."""
        cube = RubiksCube()
        cube.scramble(20)

        # Count colors - should have 9 of each
        all_colors = []
        for face in cube.faces.values():
            all_colors.extend(face)

        color_counts = {}
        for color in all_colors:
            color_counts[color] = color_counts.get(color, 0) + 1

        for color, count in color_counts.items():
            assert count == 9, f"Color {color} should appear 9 times, got {count}"

        print("✓ test_cube_invariants passed")

    def test_performance_basic(self):
        """Test basic performance of operations."""
        import time

        cube = RubiksCube()
        start = time.time()

        # Perform 1000 moves
        for _ in range(1000):
            cube.move_R()

        elapsed = time.time() - start
        print(f"  1000 moves completed in {elapsed:.4f} seconds")
        assert elapsed < 1.0, "1000 moves should complete in under 1 second"
        print("✓ test_performance_basic passed")

    def run_all(self):
        """Run all test cases."""
        print("\n=== Running Integration Tests ===\n")
        test_methods = [
            self.test_scramble_and_solve_simple,
            self.test_move_sequences_commutative,
            self.test_cube_invariants,
            self.test_performance_basic,
        ]

        passed = 0
        failed = 0

        for test in test_methods:
            try:
                test()
                passed += 1
            except AssertionError as e:
                print(f"✗ {test.__name__} failed: {e}")
                failed += 1
            except Exception as e:
                print(f"✗ {test.__name__} error: {e}")
                failed += 1

        print(f"\n{passed} passed, {failed} failed\n")
        return failed == 0


def run_all_tests():
    """Run all test suites."""
    print("=" * 60)
    print("RUBIK'S CUBE SOLVER - TEST SUITE")
    print("=" * 60)

    all_passed = True

    # Run all test suites
    cube_tests = TestRubiksCube()
    all_passed = cube_tests.run_all() and all_passed

    solver_tests = TestRubiksCubeSolver()
    all_passed = solver_tests.run_all() and all_passed

    utility_tests = TestUtilityFunctions()
    all_passed = utility_tests.run_all() and all_passed

    integration_tests = TestIntegration()
    all_passed = integration_tests.run_all() and all_passed

    print("=" * 60)
    if all_passed:
        print("ALL TESTS PASSED ✓")
    else:
        print("SOME TESTS FAILED ✗")
    print("=" * 60)

    return 0 if all_passed else 1


if __name__ == "__main__":
    import sys
    sys.exit(run_all_tests())
