/**
 * Demo Script for Rubik's Cube Solver
 * Demonstrates the functionality of the solver
 */

const RubiksCube = require('./rubiks-cube-solver');

console.log('='.repeat(60));
console.log('RUBIK\'S CUBE SOLVER DEMO');
console.log('='.repeat(60));

// Demo 1: Basic initialization
console.log('\n--- Demo 1: Cube Initialization ---');
const cube1 = new RubiksCube();
console.log('Creating a new solved cube...');
cube1.print();

// Demo 2: Basic moves
console.log('\n--- Demo 2: Performing Basic Moves ---');
const cube2 = new RubiksCube();
console.log('Executing move sequence: R U R\' U\'');
cube2.executeSequence(['R', 'U', "R'", "U'"]);
cube2.print();

// Demo 3: Scrambling
console.log('\n--- Demo 3: Scrambling the Cube ---');
const cube3 = new RubiksCube();
console.log('Scrambling cube with 15 random moves...');
const scramble = cube3.scramble(15);
console.log(`Scramble sequence: ${scramble.join(' ')}`);
cube3.print();

// Demo 4: Solving
console.log('\n--- Demo 4: Solving the Cube ---');
const cube4 = new RubiksCube();
console.log('Initial state (solved):');
console.log(`Solved: ${cube4.isSolved()}`);

console.log('\nScrambling...');
const scrambleSequence = cube4.scramble(12);
console.log(`Scramble: ${scrambleSequence.join(' ')}`);
console.log(`Solved: ${cube4.isSolved()}`);

console.log('\nSolving...');
const solution = cube4.solve();
console.log(`Solution: ${solution.join(' ')}`);
console.log(`Solution length: ${solution.length} moves`);

cube4.executeSequence(solution);
console.log(`\nAfter applying solution:`);
console.log(`Solved: ${cube4.isSolved()}`);

// Demo 5: Famous patterns
console.log('\n--- Demo 5: Famous Cube Patterns ---');

// Checkerboard pattern
const checkerboard = new RubiksCube();
console.log('\nCheckerboard Pattern:');
console.log('Move sequence: R R U U F F');
checkerboard.executeSequence(['R', 'R', 'U', 'U', 'F', 'F']);
console.log(`Is solved: ${checkerboard.isSolved()}`);
console.log('(Applying same sequence again solves it)');
checkerboard.executeSequence(['R', 'R', 'U', 'U', 'F', 'F']);
console.log(`Is solved: ${checkerboard.isSolved()}`);

// Sexy move cycle
const sexyMove = new RubiksCube();
console.log('\n"Sexy Move" Pattern:');
console.log('Move sequence: (R U R\' U\') repeated 6 times');
for (let i = 0; i < 6; i++) {
  sexyMove.executeSequence(['R', 'U', "R'", "U'"]);
}
console.log(`Is solved: ${sexyMove.isSolved()}`);

// Demo 6: Move inverses
console.log('\n--- Demo 6: Move Inverses ---');
const inverseDemo = new RubiksCube();
console.log('Demonstrating that R followed by R\' returns to solved state:');
inverseDemo.R();
console.log(`After R: Solved = ${inverseDemo.isSolved()}`);
inverseDemo.RPrime();
console.log(`After R': Solved = ${inverseDemo.isSolved()}`);

// Demo 7: Performance test
console.log('\n--- Demo 7: Performance Test ---');
console.log('Executing 10,000 random moves...');
const perfCube = new RubiksCube();
const startTime = Date.now();
for (let i = 0; i < 10000; i++) {
  const moves = ['R', "R'", 'U', "U'", 'F', "F'"];
  const move = moves[Math.floor(Math.random() * moves.length)];
  perfCube.executeSequence([move]);
}
const endTime = Date.now();
console.log(`Time taken: ${endTime - startTime}ms`);
console.log(`Average time per move: ${((endTime - startTime) / 10000).toFixed(3)}ms`);

console.log('\n' + '='.repeat(60));
console.log('DEMO COMPLETE');
console.log('='.repeat(60));
console.log('\nTo run tests, use: npm test');
console.log('To run this demo again, use: npm run demo\n');
