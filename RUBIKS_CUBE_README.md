# Rubik's Cube Solver - Testing Script

A comprehensive testing suite for a 3x3x3 Rubik's Cube solver implementation in Python.

## Files

- `rubiks_cube_solver.py` - Core implementation of the Rubik's Cube and solver
- `test_rubiks_cube.py` - Complete test suite with 50+ test cases

## Features

### Rubik's Cube Implementation (`rubiks_cube_solver.py`)

The `RubiksCube` class provides:

- **Standard cube representation**: 6 faces with 3x3 grids
- **All basic moves**: U, D, R, L, F, B (and their inverses: U', D', R', L', F', B')
- **Move execution**: Execute sequences of moves from notation strings
- **Scrambling**: Generate random scrambles
- **State management**: Check if solved, get current state
- **Face rotation**: Internal mechanics for rotating faces

The `SimpleSolver` class provides:

- Placeholder methods for solving algorithms
- Framework for implementing layer-by-layer or CFOP methods

## Test Suite Coverage

The test suite (`test_rubiks_cube.py`) includes **8 test classes** with **50+ test cases**:

### 1. TestRubiksCubeInitialization (4 tests)
- Verify cube initializes in solved state
- Check all 6 faces exist
- Validate 3x3 dimensions
- Confirm correct initial colors

### 2. TestBasicMoves (18 tests)
- Test all 6 basic moves (U, D, R, L, F, B)
- Verify inverse moves (U', D', R', L', F', B')
- Confirm 4 rotations return to original state

### 3. TestMoveSequences (6 tests)
- Execute move sequences from notation
- Test the "sexy move" (R U R' U') pattern
- Verify commutators
- Test move independence

### 4. TestScramble (4 tests)
- Verify scrambling changes state
- Check scramble sequence return
- Confirm scramble creates unsolved cube
- Test custom scramble length

### 5. TestCubeState (4 tests)
- Get cube state
- Verify state is a copy (not reference)
- Test is_solved() method accuracy

### 6. TestFaceRotation (3 tests)
- Test clockwise rotation
- Test counter-clockwise rotation
- Verify 4 rotations return to original

### 7. TestSolver (6 tests)
- Verify solver class exists
- Test all solver methods (solve, solve_cross, solve_corners, etc.)

### 8. TestAdvancedPatterns (4 tests)
- Superflip pattern
- Checkerboard pattern
- Cube-in-cube pattern
- T-permutation (PLL algorithm)

### 9. TestEdgeCases (4 tests)
- Empty move sequences
- Move sequences with extra spaces
- Zero-move scrambles
- Multiple independent cube instances

## Running the Tests

### Prerequisites

```bash
# No external dependencies required - uses only Python standard library
python3 --version  # Requires Python 3.x
```

### Run All Tests

```bash
python3 test_rubiks_cube.py
```

### Run Specific Test Class

```bash
python3 -m unittest test_rubiks_cube.TestBasicMoves
```

### Run Specific Test

```bash
python3 -m unittest test_rubiks_cube.TestBasicMoves.test_move_U
```

### Run with Verbose Output

```bash
python3 test_rubiks_cube.py -v
```

## Usage Examples

### Create and Manipulate a Cube

```python
from rubiks_cube_solver import RubiksCube

# Create a solved cube
cube = RubiksCube()
print(cube.is_solved())  # True

# Perform moves
cube.move_U()
cube.move_R()
cube.move_U_prime()
cube.move_R_prime()

# Execute move sequences
cube.execute_moves("R U R' U' R' F R2 U' R' U' R U R' F'")

# Scramble the cube
scramble_sequence = cube.scramble(20)
print(f"Scramble: {scramble_sequence}")
```

### Use the Solver (Framework)

```python
from rubiks_cube_solver import RubiksCube, SimpleSolver

cube = RubiksCube()
cube.scramble(10)

solver = SimpleSolver()
solution = solver.solve(cube)
# Note: Actual solving algorithms need to be implemented
```

## Cube Notation

Standard Singmaster notation is used:

- **U** - Up face clockwise
- **D** - Down face clockwise
- **R** - Right face clockwise
- **L** - Left face clockwise
- **F** - Front face clockwise
- **B** - Back face clockwise
- **'** - Prime (counter-clockwise), e.g., U' is Up counter-clockwise

## Test Design Principles

1. **Comprehensive Coverage**: Tests cover initialization, individual moves, sequences, patterns, and edge cases
2. **Move Validation**: Each move and its inverse are verified to return to original state
3. **Pattern Testing**: Known cube patterns are tested to ensure correctness
4. **State Independence**: Tests verify cube instances are independent
5. **Edge Cases**: Empty inputs, zero-length operations, and boundary conditions

## Known Limitations

- The `SimpleSolver` class contains only placeholder methods
- Actual solving algorithms (CFOP, Kociemba, etc.) are not implemented
- No optimization for move sequences (e.g., U U = U2)
- No support for 2x2, 4x4, or other cube sizes

## Future Enhancements

- Implement actual solving algorithms
- Add support for move notation like U2, R2 (double turns)
- Optimize move sequences
- Add visualization/pretty printing
- Implement Kociemba's two-phase algorithm
- Add performance benchmarks

## License

This is a testing/educational implementation.
