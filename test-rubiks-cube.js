/**
 * Test Script for Rubik's Cube Solver
 * Run with: node test-rubiks-cube.js
 */

const { RubiksCube, RubiksCubeSolver } = require('./rubiks-cube-solver');

// Helper function to print test results
function printTestResult(testName, passed, message = '') {
  const status = passed ? '✓ PASS' : '✗ FAIL';
  const color = passed ? '\x1b[32m' : '\x1b[31m';
  console.log(`${color}${status}\x1b[0m ${testName}`);
  if (message) {
    console.log(`  ${message}`);
  }
}

// Helper function to print section header
function printSection(title) {
  console.log('\n' + '='.repeat(50));
  console.log(title);
  console.log('='.repeat(50));
}

// Test Suite
function runTests() {
  let passedTests = 0;
  let totalTests = 0;

  printSection('Rubik\'s Cube Solver Test Suite');

  // Test 1: Initialize a solved cube
  totalTests++;
  try {
    const cube = new RubiksCube();
    const isSolved = cube.isSolved();
    if (isSolved) {
      printTestResult('Test 1: Initialize solved cube', true);
      passedTests++;
    } else {
      printTestResult('Test 1: Initialize solved cube', false, 'Cube should be solved on initialization');
    }
  } catch (error) {
    printTestResult('Test 1: Initialize solved cube', false, error.message);
  }

  // Test 2: Clone cube
  totalTests++;
  try {
    const cube1 = new RubiksCube();
    const cube2 = cube1.clone();
    const statesMatch = cube1.getState() === cube2.getState();
    const areDistinct = cube1 !== cube2;

    if (statesMatch && areDistinct) {
      printTestResult('Test 2: Clone cube', true);
      passedTests++;
    } else {
      printTestResult('Test 2: Clone cube', false, 'Cloned cube should have same state but be a different object');
    }
  } catch (error) {
    printTestResult('Test 2: Clone cube', false, error.message);
  }

  // Test 3: Apply single move and verify cube is scrambled
  totalTests++;
  try {
    const cube = new RubiksCube();
    cube.rotateR();
    const isScrambled = !cube.isSolved();

    if (isScrambled) {
      printTestResult('Test 3: Apply single move', true);
      passedTests++;
    } else {
      printTestResult('Test 3: Apply single move', false, 'Cube should be scrambled after a move');
    }
  } catch (error) {
    printTestResult('Test 3: Apply single move', false, error.message);
  }

  // Test 4: Verify move reversibility (R move 4 times = identity)
  totalTests++;
  try {
    const cube = new RubiksCube();
    const originalState = cube.getState();
    cube.rotateR();
    cube.rotateR();
    cube.rotateR();
    cube.rotateR();
    const finalState = cube.getState();

    if (originalState === finalState) {
      printTestResult('Test 4: Move reversibility (R × 4)', true);
      passedTests++;
    } else {
      printTestResult('Test 4: Move reversibility (R × 4)', false, 'Four R moves should return to original state');
    }
  } catch (error) {
    printTestResult('Test 4: Move reversibility (R × 4)', false, error.message);
  }

  // Test 5: Verify R and R' are inverses
  totalTests++;
  try {
    const cube = new RubiksCube();
    const originalState = cube.getState();
    cube.rotateR();
    cube.rotateRPrime();
    const finalState = cube.getState();

    if (originalState === finalState) {
      printTestResult('Test 5: R and R\' are inverses', true);
      passedTests++;
    } else {
      printTestResult('Test 5: R and R\' are inverses', false, 'R followed by R\' should return to original state');
    }
  } catch (error) {
    printTestResult('Test 5: R and R\' are inverses', false, error.message);
  }

  // Test 6: Apply move sequence
  totalTests++;
  try {
    const cube = new RubiksCube();
    cube.applyMoves(['R', 'U', 'R\'', 'U\'']);
    const stateChanged = cube.getState() !== new RubiksCube().getState();

    if (stateChanged) {
      printTestResult('Test 6: Apply move sequence', true);
      passedTests++;
    } else {
      printTestResult('Test 6: Apply move sequence', false, 'Move sequence should change cube state');
    }
  } catch (error) {
    printTestResult('Test 6: Apply move sequence', false, error.message);
  }

  // Test 7: Scramble cube
  totalTests++;
  try {
    const cube = new RubiksCube();
    const scramble = cube.scramble(10);
    const isScrambled = !cube.isSolved();
    const hasScrambleMoves = scramble.length === 10;

    if (isScrambled && hasScrambleMoves) {
      printTestResult('Test 7: Scramble cube', true, `Scramble: ${scramble.join(' ')}`);
      passedTests++;
    } else {
      printTestResult('Test 7: Scramble cube', false, 'Scramble should generate 10 moves and scramble the cube');
    }
  } catch (error) {
    printTestResult('Test 7: Scramble cube', false, error.message);
  }

  // Test 8: Solve a simple scramble (1 move)
  totalTests++;
  try {
    const cube = new RubiksCube();
    cube.applyMoves(['R']);

    const solver = new RubiksCubeSolver(5);
    const solution = solver.solve(cube);

    if (solution && solution.length > 0) {
      const testCube = new RubiksCube();
      testCube.applyMoves(['R']);
      testCube.applyMoves(solution);

      if (testCube.isSolved()) {
        printTestResult('Test 8: Solve simple scramble (1 move)', true, `Solution: ${solution.join(' ')}`);
        passedTests++;
      } else {
        printTestResult('Test 8: Solve simple scramble (1 move)', false, 'Solution does not solve the cube');
      }
    } else {
      printTestResult('Test 8: Solve simple scramble (1 move)', false, 'Solver did not find a solution');
    }
  } catch (error) {
    printTestResult('Test 8: Solve simple scramble (1 move)', false, error.message);
  }

  // Test 9: Solve a 2-move scramble
  totalTests++;
  try {
    const cube = new RubiksCube();
    cube.applyMoves(['R', 'U']);

    const solver = new RubiksCubeSolver(5);
    const solution = solver.solve(cube);

    if (solution && solution.length > 0) {
      const testCube = new RubiksCube();
      testCube.applyMoves(['R', 'U']);
      testCube.applyMoves(solution);

      if (testCube.isSolved()) {
        printTestResult('Test 9: Solve 2-move scramble', true, `Solution: ${solution.join(' ')}`);
        passedTests++;
      } else {
        printTestResult('Test 9: Solve 2-move scramble', false, 'Solution does not solve the cube');
      }
    } else {
      printTestResult('Test 9: Solve 2-move scramble', false, 'Solver did not find a solution');
    }
  } catch (error) {
    printTestResult('Test 9: Solve 2-move scramble', false, error.message);
  }

  // Test 10: Solve a 3-move scramble
  totalTests++;
  try {
    const cube = new RubiksCube();
    cube.applyMoves(['R', 'U', 'F']);

    const solver = new RubiksCubeSolver(6);
    const solution = solver.solve(cube);

    if (solution && solution.length > 0) {
      const testCube = new RubiksCube();
      testCube.applyMoves(['R', 'U', 'F']);
      testCube.applyMoves(solution);

      if (testCube.isSolved()) {
        printTestResult('Test 10: Solve 3-move scramble', true, `Solution: ${solution.join(' ')}`);
        passedTests++;
      } else {
        printTestResult('Test 10: Solve 3-move scramble', false, 'Solution does not solve the cube');
      }
    } else {
      printTestResult('Test 10: Solve 3-move scramble', false, 'Solver did not find a solution within depth limit');
    }
  } catch (error) {
    printTestResult('Test 10: Solve 3-move scramble', false, error.message);
  }

  // Test 11: Test all basic moves (U, F, R)
  totalTests++;
  try {
    const cube = new RubiksCube();
    cube.rotateU();
    cube.rotateF();
    cube.rotateR();
    const stateChanged = cube.getState() !== new RubiksCube().getState();

    if (stateChanged) {
      printTestResult('Test 11: All basic moves (U, F, R)', true);
      passedTests++;
    } else {
      printTestResult('Test 11: All basic moves (U, F, R)', false, 'Applying U, F, R should change state');
    }
  } catch (error) {
    printTestResult('Test 11: All basic moves (U, F, R)', false, error.message);
  }

  // Test 12: Verify U × 4 = identity
  totalTests++;
  try {
    const cube = new RubiksCube();
    const originalState = cube.getState();
    cube.rotateU();
    cube.rotateU();
    cube.rotateU();
    cube.rotateU();
    const finalState = cube.getState();

    if (originalState === finalState) {
      printTestResult('Test 12: U × 4 = identity', true);
      passedTests++;
    } else {
      printTestResult('Test 12: U × 4 = identity', false, 'Four U moves should return to original state');
    }
  } catch (error) {
    printTestResult('Test 12: U × 4 = identity', false, error.message);
  }

  // Print summary
  printSection('Test Summary');
  const percentage = ((passedTests / totalTests) * 100).toFixed(1);
  console.log(`Tests passed: ${passedTests}/${totalTests} (${percentage}%)`);

  if (passedTests === totalTests) {
    console.log('\x1b[32m✓ All tests passed!\x1b[0m');
  } else {
    console.log(`\x1b[31m✗ ${totalTests - passedTests} test(s) failed\x1b[0m`);
  }
  console.log();

  return passedTests === totalTests;
}

// Run the test suite
if (require.main === module) {
  const allPassed = runTests();
  process.exit(allPassed ? 0 : 1);
}

module.exports = { runTests };
