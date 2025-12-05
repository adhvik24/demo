/**
 * Testing Script for Rubik's Cube Solver
 * This script tests various functionalities without using a testing framework
 */

const RubiksCube = require('./rubiks-cube-solver');

// Test utilities
let testsPassed = 0;
let testsFailed = 0;
const failedTests = [];

function assert(condition, testName) {
  if (condition) {
    testsPassed++;
    console.log(`✓ ${testName}`);
  } else {
    testsFailed++;
    failedTests.push(testName);
    console.log(`✗ ${testName}`);
  }
}

function assertEqual(actual, expected, testName) {
  const condition = JSON.stringify(actual) === JSON.stringify(expected);
  assert(condition, testName);
  if (!condition) {
    console.log(`  Expected: ${JSON.stringify(expected)}`);
    console.log(`  Actual: ${JSON.stringify(actual)}`);
  }
}

function printTestSummary() {
  console.log('\n' + '='.repeat(50));
  console.log('TEST SUMMARY');
  console.log('='.repeat(50));
  console.log(`Total Tests: ${testsPassed + testsFailed}`);
  console.log(`Passed: ${testsPassed}`);
  console.log(`Failed: ${testsFailed}`);

  if (failedTests.length > 0) {
    console.log('\nFailed Tests:');
    failedTests.forEach(test => console.log(`  - ${test}`));
  }
  console.log('='.repeat(50) + '\n');
}

// Test 1: Cube Initialization
console.log('\n--- Test Suite: Cube Initialization ---\n');

function testCubeInitialization() {
  const cube = new RubiksCube();

  assert(cube.faces.U.every(sticker => sticker === 'W'),
    'Up face initialized with white');
  assert(cube.faces.D.every(sticker => sticker === 'Y'),
    'Down face initialized with yellow');
  assert(cube.faces.F.every(sticker => sticker === 'G'),
    'Front face initialized with green');
  assert(cube.faces.B.every(sticker => sticker === 'B'),
    'Back face initialized with blue');
  assert(cube.faces.L.every(sticker => sticker === 'O'),
    'Left face initialized with orange');
  assert(cube.faces.R.every(sticker => sticker === 'R'),
    'Right face initialized with red');
  assert(cube.isSolved(), 'Newly initialized cube is solved');
  assertEqual(cube.moveHistory.length, 0, 'Move history is empty on initialization');
}

testCubeInitialization();

// Test 2: Basic Moves
console.log('\n--- Test Suite: Basic Moves ---\n');

function testBasicMoves() {
  const cube = new RubiksCube();

  // Test R move
  cube.R();
  assert(!cube.isSolved(), 'Cube is not solved after R move');
  assertEqual(cube.moveHistory.length, 1, 'Move history contains 1 move after R');
  assertEqual(cube.moveHistory[0], 'R', 'Move history records R move correctly');

  // Test R' move (should undo R)
  cube.RPrime();
  assert(cube.isSolved(), "Cube is solved after R followed by R'");
  assertEqual(cube.moveHistory.length, 2, 'Move history contains 2 moves');

  // Test U move
  const cube2 = new RubiksCube();
  cube2.U();
  assert(!cube2.isSolved(), 'Cube is not solved after U move');

  // Test F move
  const cube3 = new RubiksCube();
  cube3.F();
  assert(!cube3.isSolved(), 'Cube is not solved after F move');
}

testBasicMoves();

// Test 3: Move Sequences
console.log('\n--- Test Suite: Move Sequences ---\n');

function testMoveSequences() {
  const cube = new RubiksCube();

  // Test simple sequence
  cube.executeSequence(['R', 'U', "R'", "U'"]);
  assert(cube.isSolved(), "Cube is solved after [R, U, R', U']");
  assertEqual(cube.moveHistory.length, 4, 'Move history contains 4 moves');

  // Test longer sequence
  const cube2 = new RubiksCube();
  cube2.executeSequence(['R', 'R', 'R', 'R']);
  assert(cube2.isSolved(), 'Four R moves return cube to solved state');

  // Test mixed sequence
  const cube3 = new RubiksCube();
  cube3.executeSequence(['U', 'U', 'U', 'U']);
  assert(cube3.isSolved(), 'Four U moves return cube to solved state');
}

testMoveSequences();

// Test 4: Cube Cloning
console.log('\n--- Test Suite: Cube Cloning ---\n');

function testCubeCloning() {
  const cube = new RubiksCube();
  cube.executeSequence(['R', 'U', 'F']);

  const clonedCube = cube.clone();

  assertEqual(clonedCube.faces.U, cube.faces.U, 'Cloned cube has same U face');
  assertEqual(clonedCube.faces.R, cube.faces.R, 'Cloned cube has same R face');
  assertEqual(clonedCube.moveHistory, cube.moveHistory, 'Cloned cube has same move history');

  // Modify original and ensure clone is unchanged
  cube.R();
  assert(cube.moveHistory.length !== clonedCube.moveHistory.length,
    'Cloned cube move history is independent');
}

testCubeCloning();

// Test 5: Scrambling
console.log('\n--- Test Suite: Scrambling ---\n');

function testScrambling() {
  const cube = new RubiksCube();
  const scrambleSequence = cube.scramble(10);

  assertEqual(scrambleSequence.length, 10, 'Scramble generates 10 moves');
  assertEqual(cube.moveHistory.length, 10, 'Move history contains scramble moves');

  // Most likely not solved after 10 random moves
  // (There's a tiny chance it could be, but extremely unlikely)
  const cube2 = new RubiksCube();
  cube2.scramble(20);
  // We can't assert it's not solved with 100% certainty, but check move history
  assertEqual(cube2.moveHistory.length, 20, 'Scramble with 20 moves records correctly');
}

testScrambling();

// Test 6: Solving
console.log('\n--- Test Suite: Solving ---\n');

function testSolving() {
  const cube = new RubiksCube();
  const scrambleSequence = cube.scramble(15);

  console.log(`  Scramble: ${scrambleSequence.join(' ')}`);

  const solution = cube.solve();
  console.log(`  Solution: ${solution.join(' ')}`);

  assert(solution.length > 0, 'Solver returns non-empty solution');
  assertEqual(solution.length, 15, 'Solution has same length as scramble');

  // Apply solution
  cube.executeSequence(solution);
  assert(cube.isSolved(), 'Cube is solved after applying solution');
}

testSolving();

// Test 7: Face Rotation
console.log('\n--- Test Suite: Face Rotation ---\n');

function testFaceRotation() {
  const cube = new RubiksCube();
  const originalFace = [...cube.faces.R];

  cube.rotateFaceClockwise('R');
  assert(JSON.stringify(cube.faces.R) !== JSON.stringify(originalFace),
    'Face changes after clockwise rotation');

  // Rotate 4 times should return to original
  cube.rotateFaceClockwise('R');
  cube.rotateFaceClockwise('R');
  cube.rotateFaceClockwise('R');
  assertEqual(cube.faces.R, originalFace,
    'Four clockwise rotations return face to original state');
}

testFaceRotation();

// Test 8: Move Inverses
console.log('\n--- Test Suite: Move Inverses ---\n');

function testMoveInverses() {
  // Test R and R'
  const cube1 = new RubiksCube();
  cube1.R();
  cube1.RPrime();
  assert(cube1.isSolved(), "R followed by R' solves cube");

  // Test U and U'
  const cube2 = new RubiksCube();
  cube2.U();
  cube2.UPrime();
  assert(cube2.isSolved(), "U followed by U' solves cube");

  // Test F and F'
  const cube3 = new RubiksCube();
  cube3.F();
  cube3.FPrime();
  assert(cube3.isSolved(), "F followed by F' solves cube");

  // Test reverse order
  const cube4 = new RubiksCube();
  cube4.RPrime();
  cube4.R();
  assert(cube4.isSolved(), "R' followed by R solves cube");
}

testMoveInverses();

// Test 9: Complex Patterns
console.log('\n--- Test Suite: Complex Patterns ---\n');

function testComplexPatterns() {
  // Test sexy move (R U R' U') repeated 6 times returns to solved
  const cube = new RubiksCube();
  for (let i = 0; i < 6; i++) {
    cube.executeSequence(['R', 'U', "R'", "U'"]);
  }
  assert(cube.isSolved(), "Sexy move repeated 6 times solves cube");

  // Test checkerboard pattern and back
  const cube2 = new RubiksCube();
  const pattern = ['R', 'R', 'U', 'U', 'F', 'F'];
  cube2.executeSequence(pattern);
  assert(!cube2.isSolved(), 'Checkerboard pattern is not solved state');
  cube2.executeSequence(pattern);
  assert(cube2.isSolved(), 'Checkerboard pattern repeated twice solves cube');
}

testComplexPatterns();

// Test 10: Edge Cases
console.log('\n--- Test Suite: Edge Cases ---\n');

function testEdgeCases() {
  // Empty sequence
  const cube1 = new RubiksCube();
  cube1.executeSequence([]);
  assert(cube1.isSolved(), 'Empty sequence keeps cube solved');

  // Single move repeated many times
  const cube2 = new RubiksCube();
  for (let i = 0; i < 100; i++) {
    cube2.R();
  }
  assert(cube2.isSolved(), '100 R moves (4 cycles of 25) returns to solved');

  // Test invalid move handling
  const cube3 = new RubiksCube();
  try {
    cube3.executeSequence(['X']);
    assert(false, 'Invalid move should throw error');
  } catch (error) {
    assert(true, 'Invalid move throws error correctly');
  }
}

testEdgeCases();

// Print final summary
printTestSummary();

// Exit with appropriate code
process.exit(testsFailed > 0 ? 1 : 0);
