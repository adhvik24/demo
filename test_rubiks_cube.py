"""
Test script for Rubik's Cube Solver
Tests various functionalities without using a testing framework
"""

from rubiks_cube import RubiksCube, SimpleSolver, reverse_moves


def test_initial_state():
    """Test that a new cube is in solved state"""
    print("Test 1: Initial State")
    cube = RubiksCube()
    assert cube.is_solved(), "New cube should be solved"
    print("✓ New cube is in solved state")
    print()


def test_single_move():
    """Test single move execution"""
    print("Test 2: Single Move Execution")
    cube = RubiksCube()

    # Test R move
    cube.move_R()
    assert not cube.is_solved(), "Cube should not be solved after R move"
    print("✓ R move executed, cube is scrambled")

    # Undo with Ri
    cube.move_Ri()
    assert cube.is_solved(), "Cube should be solved after R then Ri"
    print("✓ Ri move undoes R move correctly")
    print()


def test_all_basic_moves():
    """Test all basic moves and their inverses"""
    print("Test 3: All Basic Moves")
    moves = ['R', 'L', 'U', 'D', 'F', 'B']

    for move in moves:
        cube = RubiksCube()
        # Execute move
        getattr(cube, f'move_{move}')()
        assert not cube.is_solved(), f"Cube should not be solved after {move}"

        # Execute inverse
        getattr(cube, f'move_{move}i')()
        assert cube.is_solved(), f"Cube should be solved after {move} then {move}i"
        print(f"✓ {move} and {move}i moves work correctly")

    print()


def test_move_sequence():
    """Test executing a sequence of moves"""
    print("Test 4: Move Sequence Execution")
    cube = RubiksCube()

    # Execute a sequence
    sequence = "R U R' U'"
    cube.execute_moves(sequence)
    assert not cube.is_solved(), "Cube should be scrambled after sequence"
    print(f"✓ Executed sequence: {sequence}")

    # Execute inverse sequence
    cube.execute_moves("U Ri U Ri")
    assert cube.is_solved(), "Cube should be solved after inverse sequence"
    print("✓ Inverse sequence restored cube to solved state")
    print()


def test_commutator():
    """Test that certain move sequences return to solved state"""
    print("Test 5: Commutator Property")
    cube = RubiksCube()

    # A commutator: R U Ri Ui should affect only some pieces
    # Repeating it 6 times should return to solved state
    sequence = "R U Ri Ui"
    for i in range(6):
        cube.execute_moves(sequence)

    assert cube.is_solved(), "Cube should return to solved state after 6 commutators"
    print(f"✓ Executed '{sequence}' 6 times, cube returned to solved state")
    print()


def test_face_rotations():
    """Test that rotating a face 4 times returns it to original state"""
    print("Test 6: Face Rotation Property")
    moves = ['R', 'L', 'U', 'D', 'F', 'B']

    for move in moves:
        cube = RubiksCube()
        # Rotate 4 times
        for _ in range(4):
            getattr(cube, f'move_{move}')()

        assert cube.is_solved(), f"4 {move} moves should return cube to solved state"
        print(f"✓ Four {move} moves return to solved state")

    print()


def test_scramble_and_reverse():
    """Test scrambling and reversing moves"""
    print("Test 7: Scramble and Reverse")
    cube = RubiksCube()

    # Scramble with a sequence
    scramble = "R U R' U' L' U L U F F R' L F' R L'"
    cube.scramble(scramble)
    assert not cube.is_solved(), "Cube should be scrambled"
    print(f"✓ Cube scrambled with: {scramble}")

    # Reverse the scramble
    reverse = reverse_moves(scramble)
    cube.execute_moves(reverse)
    assert cube.is_solved(), "Cube should be solved after reversing scramble"
    print(f"✓ Reversed scramble: {' '.join(reverse)}")
    print("✓ Cube returned to solved state")
    print()


def test_cube_copy():
    """Test that cube copy works correctly"""
    print("Test 8: Cube Copy")
    cube1 = RubiksCube()
    cube1.execute_moves("R U R' U'")

    cube2 = cube1.copy()

    # Modify cube2
    cube2.move_F()

    # Check that cube1 is unchanged
    cube1_state = str(cube1)
    cube2_state = str(cube2)
    assert cube1_state != cube2_state, "Copied cube should be independent"
    print("✓ Cube copy is independent of original")
    print()


def test_is_solved():
    """Test the is_solved method"""
    print("Test 9: Is Solved Detection")

    # Solved cube
    cube = RubiksCube()
    assert cube.is_solved(), "New cube should be detected as solved"
    print("✓ Solved cube detected correctly")

    # Scrambled cube
    cube.execute_moves("R U F")
    assert not cube.is_solved(), "Scrambled cube should be detected as unsolved"
    print("✓ Unsolved cube detected correctly")
    print()


def test_complex_scramble():
    """Test with a more complex scramble"""
    print("Test 10: Complex Scramble")
    cube = RubiksCube()

    # A longer scramble
    scramble = "R L U D F B R' L' U' D' F' B' R U F R' U' F'"
    cube.scramble(scramble)
    print(f"✓ Applied complex scramble: {scramble}")

    # Verify it's scrambled
    assert not cube.is_solved(), "Cube should be scrambled"
    print("✓ Cube is in scrambled state")

    # Apply reverse
    reverse = reverse_moves(scramble)
    cube.execute_moves(reverse)
    assert cube.is_solved(), "Cube should be solved after reverse"
    print("✓ Complex scramble successfully reversed")
    print()


def test_move_equivalence():
    """Test that moving 3 times counterclockwise equals 1 clockwise"""
    print("Test 11: Move Equivalence")

    for move in ['R', 'L', 'U', 'D', 'F', 'B']:
        cube1 = RubiksCube()
        cube2 = RubiksCube()

        # One clockwise
        getattr(cube1, f'move_{move}')()

        # Three counterclockwise
        for _ in range(3):
            getattr(cube2, f'move_{move}i')()

        # States should be identical
        assert str(cube1) == str(cube2), f"{move} ≠ 3×{move}i"
        print(f"✓ {move} ≡ 3×{move}i")

    print()


def test_sexy_move():
    """Test the 'sexy move' (R U R' U') pattern"""
    print("Test 12: Sexy Move Pattern")
    cube = RubiksCube()

    # The sexy move repeated 6 times should return to solved
    sexy_move = "R U Ri Ui"
    for i in range(6):
        cube.execute_moves(sexy_move)

    assert cube.is_solved(), "Sexy move ×6 should solve cube"
    print(f"✓ Sexy move '{sexy_move}' repeated 6 times returns to solved state")
    print()


def test_solver_basic():
    """Test the basic solver"""
    print("Test 13: Solver - Already Solved")
    cube = RubiksCube()
    solver = SimpleSolver(cube)

    solution = solver.solve()
    assert cube.is_solved(), "Solver should maintain solved state"
    assert len(solution) == 0, "No moves needed for solved cube"
    print("✓ Solver recognizes already-solved cube")
    print()


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("RUBIK'S CUBE SOLVER - TEST SUITE")
    print("=" * 60)
    print()

    tests = [
        test_initial_state,
        test_single_move,
        test_all_basic_moves,
        test_move_sequence,
        test_commutator,
        test_face_rotations,
        test_scramble_and_reverse,
        test_cube_copy,
        test_is_solved,
        test_complex_scramble,
        test_move_equivalence,
        test_sexy_move,
        test_solver_basic,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            failed += 1
            print(f"✗ Test failed: {test.__name__}")
            print(f"  Error: {e}")
            print()
        except Exception as e:
            failed += 1
            print(f"✗ Test error: {test.__name__}")
            print(f"  Exception: {e}")
            print()

    print("=" * 60)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)

    if failed == 0:
        print("\n🎉 All tests passed!")
    else:
        print(f"\n⚠️  {failed} test(s) failed")

    return failed == 0


def demo_cube():
    """Demonstrate cube functionality"""
    print("\n" + "=" * 60)
    print("DEMONSTRATION")
    print("=" * 60)
    print()

    print("Initial solved cube:")
    cube = RubiksCube()
    print(cube)
    print()

    print("After scramble 'R U R' U' F' L' U L U':")
    cube.scramble("R U Ri Ui Fi Li U L Ui")
    print(cube)
    print()

    print("Cube is solved:", cube.is_solved())
    print()


if __name__ == "__main__":
    # Run all tests
    success = run_all_tests()

    # Run demonstration
    demo_cube()

    # Exit with appropriate code
    exit(0 if success else 1)
