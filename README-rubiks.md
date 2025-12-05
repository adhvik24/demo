# Rubik's Cube Solver

A simplified 2x2x2 Rubik's Cube solver implementation with a comprehensive testing suite.

## Features

- **2x2x2 Rubik's Cube simulation** with 6 faces (Up, Down, Front, Back, Left, Right)
- **Basic move operations**: R (Right), U (Up), F (Front) and their inverses (R', U', F')
- **Scramble function** to generate random cube configurations
- **BFS-based solver** to find optimal solutions for simple scrambles
- **Comprehensive test suite** with 12 test cases

## Files

- `rubiks-cube-solver.js` - Main implementation of the Rubik's Cube and solver
- `test-rubiks-cube.js` - Test suite with 12 test cases
- `package.json` - Node.js package configuration

## Usage

### Run Tests

```bash
npm test
# or
node test-rubiks-cube.js
```

### Use the Solver Programmatically

```javascript
const { RubiksCube, RubiksCubeSolver } = require('./rubiks-cube-solver');

// Create a new cube
const cube = new RubiksCube();

// Scramble it
const scramble = cube.scramble(5);
console.log('Scramble:', scramble.join(' '));

// Solve it
const solver = new RubiksCubeSolver(7);
const solution = solver.solve(cube);
console.log('Solution:', solution.join(' '));
```

## Test Cases

The test suite includes:

1. Initialize solved cube
2. Clone cube functionality
3. Apply single move
4. Move reversibility (R × 4)
5. Inverse moves (R and R')
6. Apply move sequence
7. Scramble cube
8. Solve 1-move scramble
9. Solve 2-move scramble
10. Solve 3-move scramble
11. Test all basic moves (U, F, R)
12. Verify U × 4 = identity

## Implementation Notes

- This is a **2x2x2 cube** (simplified version) for demonstration purposes
- The solver uses **Breadth-First Search (BFS)** to find optimal solutions
- Maximum search depth is configurable (default: 7 moves)
- For larger scrambles, the solver may not find a solution within the depth limit

## Cube Notation

- **R**: Rotate right face clockwise
- **R'**: Rotate right face counter-clockwise
- **U**: Rotate up face clockwise
- **U'**: Rotate up face counter-clockwise
- **F**: Rotate front face clockwise
- **F'**: Rotate front face counter-clockwise

## Color Scheme

- **W** - White (Up)
- **Y** - Yellow (Down)
- **G** - Green (Front)
- **B** - Blue (Back)
- **O** - Orange (Left)
- **R** - Red (Right)
