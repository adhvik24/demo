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
- **Double move notation**: Support for U2, D2, R2, L2, F2, B2 moves
- **Move execution**: Execute sequences of moves from notation strings
- **Scrambling**: Generate random scrambles (including double moves)
- **State management**: Check if solved, get current state
- **Face rotation**: Internal mechanics for rotating faces
- **Visualization**: Display cube in 2D unfolded format
- **Serialization**: Save and load cube states to/from dictionaries
- **Move optimization**: Optimize move sequences by canceling redundant moves
- **Performance tracking**: Optional metrics tracking with timing
- **Move history**: Track all moves executed on the cube
- **Deep copy**: Create independent copies of cube instances

The `SimpleSolver` class provides:

- Placeholder methods for solving algorithms
- Framework for implementing layer-by-layer or CFOP methods

The `CubeMetrics` class provides:

- Move counting
- Execution time tracking
- Average time per operation
- Performance statistics

## Test Suite Coverage

The test suite (`test_rubiks_cube.py`) includes **15+ test classes** with **90+ test cases**:

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

### 10. TestDoubleMovesAndNotation (4 tests)
- Test U2, D2, R2, L2, F2, B2 moves
- Verify double moves equal two single moves
- Test all double moves together
- Test mixed notation sequences

### 11. TestCubeVisualization (4 tests)
- Display cube in 2D format
- Test string representation
- Verify colors in display
- Display after moves

### 12. TestCubeSerialization (4 tests)
- Serialize cube state to dictionary
- Deserialize cube from dictionary
- Round-trip serialization
- Deep copy functionality

### 13. TestMoveOptimization (6 tests)
- Cancel opposite moves (U U')
- Combine consecutive moves (U U = U2)
- Optimize three moves (U U U = U')
- Remove full rotations (U U U U)
- Mixed move optimization
- Preserve different face moves

### 14. TestPerformanceMetrics (6 tests)
- Initialize with metrics tracking
- Record move execution times
- Track move history
- Track double moves in history
- Calculate average execution time
- Reset metrics

### 15. TestEnhancedScrambling (2 tests)
- Scramble with double moves
- Verify scramble execution

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

# Execute move sequences (including double moves)
cube.execute_moves("R U2 R' U' R U R2 U' R U'")

# Scramble the cube
scramble_sequence = cube.scramble(20)
print(f"Scramble: {scramble_sequence}")

# Display the cube
print(cube)
```

### Visualization

```python
from rubiks_cube_solver import RubiksCube

cube = RubiksCube()
cube.execute_moves("R U R' U'")

# Display cube in unfolded 2D format
print(cube.display())
# Or simply:
print(cube)
```

### State Management

```python
from rubiks_cube_solver import RubiksCube

# Save and restore cube state
cube1 = RubiksCube()
cube1.execute_moves("R U R' U'")
state = cube1.to_dict()

cube2 = RubiksCube()
cube2.from_dict(state)
print(cube1.get_state() == cube2.get_state())  # True

# Create independent copy
cube3 = cube1.copy()
cube3.execute_moves("R U")
print(cube1.get_state() == cube3.get_state())  # False
```

### Move Optimization

```python
from rubiks_cube_solver import RubiksCube

cube = RubiksCube()

# Optimize redundant moves
moves = "R U U U R' R R"
optimized = cube.optimize_moves(moves)
print(optimized)  # "R U' R2"

# Optimization rules:
# U U = U2
# U U U = U'
# U U U U = (nothing, full rotation)
# U U' = (nothing, cancels out)
```

### Performance Tracking

```python
from rubiks_cube_solver import RubiksCube

# Create cube with metrics tracking
cube = RubiksCube(track_metrics=True)

# Execute moves with timing
elapsed = cube.execute_moves("R U R' U'", track_time=True)

# View metrics
print(cube.metrics)  # Shows move count, total time, average

# Check move history
print(cube.move_history)  # ['R', 'U', "R'", "U'"]

# Reset metrics
cube.metrics.reset()
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
- **2** - Double turn (180 degrees), e.g., U2 is Up twice

## Test Design Principles

1. **Comprehensive Coverage**: Tests cover initialization, individual moves, sequences, patterns, and edge cases
2. **Move Validation**: Each move and its inverse are verified to return to original state
3. **Pattern Testing**: Known cube patterns are tested to ensure correctness
4. **State Independence**: Tests verify cube instances are independent
5. **Edge Cases**: Empty inputs, zero-length operations, and boundary conditions

## Known Limitations

- The `SimpleSolver` class contains only placeholder methods
- Actual solving algorithms (CFOP, Kociemba, etc.) are not implemented
- No support for 2x2, 4x4, or other cube sizes
- Move optimization only handles consecutive same-face moves
- No 3D visualization (only 2D unfolded display)

## Recent Enhancements (v2.0)

✅ **Double move notation** - Support for U2, R2, etc. (180-degree turns)
✅ **Cube visualization** - Display cube in 2D unfolded format
✅ **Move optimization** - Automatically cancel and combine redundant moves
✅ **State serialization** - Save and load cube states
✅ **Performance metrics** - Track move counts and execution times
✅ **Move history** - Full history of all executed moves
✅ **Deep copy** - Create independent cube instances
✅ **Enhanced scrambling** - Scrambles now include double moves

## Future Enhancements

- Implement actual solving algorithms (layer-by-layer, CFOP, Kociemba)
- Add 3D visualization with WebGL or similar
- Implement more advanced move optimization (cross-face cancellation)
- Add support for 2x2, 4x4, and other cube sizes
- Implement pattern detection and analysis
- Add benchmark suite for performance testing

## License

This is a testing/educational implementation.
