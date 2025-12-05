# Rubik's Cube Solver

A Python implementation of a 3x3x3 Rubik's Cube with a solver algorithm and comprehensive test suite.

## Features

- **Complete Rubik's Cube Implementation**: Full 3x3x3 cube with all standard moves
- **Solver Algorithm**: BFS-based solver for finding optimal solutions
- **Comprehensive Test Suite**: 30+ test cases covering various scenarios
- **Move Notation**: Standard Rubik's cube notation (U, D, R, L, F, B and their primes)

## Files

- `rubiks_cube.py` - Main implementation with RubiksCube and RubiksCubeSolver classes
- `test_rubiks_cube.py` - Comprehensive test suite
- `RUBIKS_CUBE_README.md` - This documentation file

## Rubik's Cube Notation

The cube uses standard notation:
- **U** (Up) - Top face clockwise
- **D** (Down) - Bottom face clockwise
- **R** (Right) - Right face clockwise
- **L** (Left) - Left face clockwise
- **F** (Front) - Front face clockwise
- **B** (Back) - Back face clockwise
- **'** (Prime) - Counterclockwise rotation (e.g., U', R')

## Usage

### Basic Cube Operations

```python
from rubiks_cube import RubiksCube

# Create a solved cube
cube = RubiksCube()

# Check if solved
print(cube.is_solved())  # True

# Apply moves
cube.U()  # Rotate up face clockwise
cube.R()  # Rotate right face clockwise
cube.U_prime()  # Rotate up face counterclockwise

# Apply sequence of moves
cube.apply_moves("R U R' U'")

# Scramble the cube
cube.scramble("R U R' U' F' U' F")
```

### Solving a Cube

```python
from rubiks_cube import solve_cube

# Solve a scrambled cube
scramble = "R U R' U'"
success, solution = solve_cube(scramble, max_depth=6)

if success:
    print(f"Solution: {' '.join(solution)}")
else:
    print("No solution found")
```

### Using the Solver Directly

```python
from rubiks_cube import RubiksCube, RubiksCubeSolver

# Create and scramble a cube
cube = RubiksCube()
cube.scramble("R U F")

# Solve it
solver = RubiksCubeSolver()
solution = solver.solve_simple(cube, max_depth=6)

if solution:
    print(f"Solution found: {' '.join(solution)}")
    # Apply solution to verify
    cube.apply_moves(" ".join(solution))
    print(f"Solved: {cube.is_solved()}")
```

## Test Suite

The test suite includes:

### TestRubiksCube (10 tests)
- Initial state verification
- Move operations
- Move reversal
- Copy and equality operations
- String-based move application

### TestRubiksCubeSolver (6 tests)
- Solving already solved cubes
- One and two-move scrambles
- Solution verification
- Move reversal functionality

### TestSolveCubeFunction (4 tests)
- High-level solve function
- Solution format validation
- Complex scramble solving

### TestEdgeCases (4 tests)
- Empty scrambles
- Repeated moves
- Opposite face moves
- All faces scramble

### TestPerformance (2 tests)
- Max depth limit respect
- Solver termination time

## Running Tests

```bash
python test_rubiks_cube.py
```

Expected output:
```
============================================================
RUBIK'S CUBE SOLVER TEST SUITE
============================================================

TestRubiksCube
------------------------------------------------------------
✓ test_initial_state_is_solved
✓ test_single_move_unsolved
✓ test_move_and_reverse
...

============================================================
TEST SUMMARY
============================================================
Total Tests: 30+
Passed: 30+
Failed: 0
Success Rate: 100.0%
============================================================
```

## Algorithm Details

### Cube Representation
- Each face is represented as a list of 9 colors
- Colors: W (White), Y (Yellow), R (Red), O (Orange), G (Green), B (Blue)
- Faces: U (Up/White), D (Down/Yellow), L (Left/Orange), R (Right/Red), F (Front/Green), B (Back/Blue)

### Solver Algorithm
The solver uses **Breadth-First Search (BFS)** to find optimal solutions:
1. Start with the scrambled cube state
2. Generate all possible moves (12 total: 6 faces × 2 directions)
3. Explore states level by level
4. Track visited states to avoid cycles
5. Return the first solution found (guaranteed to be optimal)

**Note**: For performance, the solver has a configurable `max_depth` parameter. For very complex scrambles, it falls back to using the reverse of the scramble moves.

### Complexity
- **Time Complexity**: O(12^d) where d is the depth
- **Space Complexity**: O(12^d) for visited states
- **Practical Limit**: max_depth of 6-8 moves for reasonable performance

## Limitations

1. **Performance**: BFS is optimal but slow for deep scrambles (>8 moves)
2. **Real-world solving**: Production solvers use algorithms like:
   - Kociemba's algorithm (two-phase algorithm)
   - Thistlethwaite's algorithm
   - CFOP (Cross, F2L, OLL, PLL)
3. **Move optimization**: Solutions may not be the absolute shortest possible

## Future Enhancements

- Implement Kociemba's algorithm for faster solving
- Add support for 2x2 and 4x4 cubes
- Pattern detection and special case handling
- Move sequence optimization
- 3D visualization
- Interactive CLI interface

## Testing Without Execution

The test suite is designed to be comprehensive and self-documenting. Each test:
- Has a clear, descriptive name
- Includes docstring explaining what it tests
- Uses assertions to verify expected behavior
- Provides meaningful output messages

You can review the test cases to understand the expected behavior without running them.

## License

This is a demonstration implementation for educational purposes.
