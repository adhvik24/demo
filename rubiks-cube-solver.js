/**
 * Rubik's Cube Solver Implementation
 * Represents a 3x3x3 Rubik's cube and implements basic solving algorithms
 */

class RubiksCube {
  constructor() {
    // Initialize cube with solved state
    // Each face has 9 stickers (0-8 indexing)
    // Faces: U (Up), D (Down), F (Front), B (Back), L (Left), R (Right)
    this.faces = {
      U: Array(9).fill('W'), // White
      D: Array(9).fill('Y'), // Yellow
      F: Array(9).fill('G'), // Green
      B: Array(9).fill('B'), // Blue
      L: Array(9).fill('O'), // Orange
      R: Array(9).fill('R')  // Red
    };
    this.moveHistory = [];
  }

  /**
   * Clone the current cube state
   */
  clone() {
    const newCube = new RubiksCube();
    newCube.faces = {
      U: [...this.faces.U],
      D: [...this.faces.D],
      F: [...this.faces.F],
      B: [...this.faces.B],
      L: [...this.faces.L],
      R: [...this.faces.R]
    };
    newCube.moveHistory = [...this.moveHistory];
    return newCube;
  }

  /**
   * Rotate a face clockwise
   */
  rotateFaceClockwise(face) {
    const f = this.faces[face];
    const temp = [
      f[6], f[3], f[0],
      f[7], f[4], f[1],
      f[8], f[5], f[2]
    ];
    this.faces[face] = temp;
  }

  /**
   * Rotate a face counter-clockwise
   */
  rotateFaceCounterClockwise(face) {
    const f = this.faces[face];
    const temp = [
      f[2], f[5], f[8],
      f[1], f[4], f[7],
      f[0], f[3], f[6]
    ];
    this.faces[face] = temp;
  }

  /**
   * Perform R move (Right face clockwise)
   */
  R() {
    this.rotateFaceClockwise('R');
    const temp = [this.faces.U[2], this.faces.U[5], this.faces.U[8]];
    this.faces.U[2] = this.faces.F[2];
    this.faces.U[5] = this.faces.F[5];
    this.faces.U[8] = this.faces.F[8];
    this.faces.F[2] = this.faces.D[2];
    this.faces.F[5] = this.faces.D[5];
    this.faces.F[8] = this.faces.D[8];
    this.faces.D[2] = this.faces.B[6];
    this.faces.D[5] = this.faces.B[3];
    this.faces.D[8] = this.faces.B[0];
    this.faces.B[6] = temp[0];
    this.faces.B[3] = temp[1];
    this.faces.B[0] = temp[2];
    this.moveHistory.push('R');
  }

  /**
   * Perform R' move (Right face counter-clockwise)
   */
  RPrime() {
    this.rotateFaceCounterClockwise('R');
    const temp = [this.faces.U[2], this.faces.U[5], this.faces.U[8]];
    this.faces.U[2] = this.faces.B[6];
    this.faces.U[5] = this.faces.B[3];
    this.faces.U[8] = this.faces.B[0];
    this.faces.B[6] = this.faces.D[2];
    this.faces.B[3] = this.faces.D[5];
    this.faces.B[0] = this.faces.D[8];
    this.faces.D[2] = this.faces.F[2];
    this.faces.D[5] = this.faces.F[5];
    this.faces.D[8] = this.faces.F[8];
    this.faces.F[2] = temp[0];
    this.faces.F[5] = temp[1];
    this.faces.F[8] = temp[2];
    this.moveHistory.push("R'");
  }

  /**
   * Perform U move (Up face clockwise)
   */
  U() {
    this.rotateFaceClockwise('U');
    const temp = [this.faces.F[0], this.faces.F[1], this.faces.F[2]];
    this.faces.F[0] = this.faces.R[0];
    this.faces.F[1] = this.faces.R[1];
    this.faces.F[2] = this.faces.R[2];
    this.faces.R[0] = this.faces.B[0];
    this.faces.R[1] = this.faces.B[1];
    this.faces.R[2] = this.faces.B[2];
    this.faces.B[0] = this.faces.L[0];
    this.faces.B[1] = this.faces.L[1];
    this.faces.B[2] = this.faces.L[2];
    this.faces.L[0] = temp[0];
    this.faces.L[1] = temp[1];
    this.faces.L[2] = temp[2];
    this.moveHistory.push('U');
  }

  /**
   * Perform U' move (Up face counter-clockwise)
   */
  UPrime() {
    this.rotateFaceCounterClockwise('U');
    const temp = [this.faces.F[0], this.faces.F[1], this.faces.F[2]];
    this.faces.F[0] = this.faces.L[0];
    this.faces.F[1] = this.faces.L[1];
    this.faces.F[2] = this.faces.L[2];
    this.faces.L[0] = this.faces.B[0];
    this.faces.L[1] = this.faces.B[1];
    this.faces.L[2] = this.faces.B[2];
    this.faces.B[0] = this.faces.R[0];
    this.faces.B[1] = this.faces.R[1];
    this.faces.B[2] = this.faces.R[2];
    this.faces.R[0] = temp[0];
    this.faces.R[1] = temp[1];
    this.faces.R[2] = temp[2];
    this.moveHistory.push("U'");
  }

  /**
   * Perform F move (Front face clockwise)
   */
  F() {
    this.rotateFaceClockwise('F');
    const temp = [this.faces.U[6], this.faces.U[7], this.faces.U[8]];
    this.faces.U[6] = this.faces.L[8];
    this.faces.U[7] = this.faces.L[5];
    this.faces.U[8] = this.faces.L[2];
    this.faces.L[2] = this.faces.D[0];
    this.faces.L[5] = this.faces.D[1];
    this.faces.L[8] = this.faces.D[2];
    this.faces.D[0] = this.faces.R[6];
    this.faces.D[1] = this.faces.R[3];
    this.faces.D[2] = this.faces.R[0];
    this.faces.R[0] = temp[0];
    this.faces.R[3] = temp[1];
    this.faces.R[6] = temp[2];
    this.moveHistory.push('F');
  }

  /**
   * Perform F' move (Front face counter-clockwise)
   */
  FPrime() {
    this.rotateFaceCounterClockwise('F');
    const temp = [this.faces.U[6], this.faces.U[7], this.faces.U[8]];
    this.faces.U[6] = this.faces.R[0];
    this.faces.U[7] = this.faces.R[3];
    this.faces.U[8] = this.faces.R[6];
    this.faces.R[0] = this.faces.D[2];
    this.faces.R[3] = this.faces.D[1];
    this.faces.R[6] = this.faces.D[0];
    this.faces.D[0] = this.faces.L[2];
    this.faces.D[1] = this.faces.L[5];
    this.faces.D[2] = this.faces.L[8];
    this.faces.L[2] = temp[2];
    this.faces.L[5] = temp[1];
    this.faces.L[8] = temp[0];
    this.moveHistory.push("F'");
  }

  /**
   * Execute a sequence of moves
   */
  executeSequence(moves) {
    const moveMap = {
      'R': () => this.R(),
      "R'": () => this.RPrime(),
      'U': () => this.U(),
      "U'": () => this.UPrime(),
      'F': () => this.F(),
      "F'": () => this.FPrime()
    };

    for (const move of moves) {
      if (moveMap[move]) {
        moveMap[move]();
      } else {
        throw new Error(`Unknown move: ${move}`);
      }
    }
  }

  /**
   * Check if cube is solved
   */
  isSolved() {
    for (const face in this.faces) {
      const color = this.faces[face][0];
      if (!this.faces[face].every(sticker => sticker === color)) {
        return false;
      }
    }
    return true;
  }

  /**
   * Scramble the cube with random moves
   */
  scramble(numMoves = 20) {
    const moves = ['R', "R'", 'U', "U'", 'F', "F'"];
    const scrambleSequence = [];

    for (let i = 0; i < numMoves; i++) {
      const move = moves[Math.floor(Math.random() * moves.length)];
      scrambleSequence.push(move);
    }

    this.executeSequence(scrambleSequence);
    return scrambleSequence;
  }

  /**
   * Simple solver using beginner's method concepts
   * Returns a sequence of moves to solve the cube
   */
  solve() {
    // This is a simplified solver that attempts to solve basic patterns
    // A full implementation would use algorithms like CFOP, Roux, or Kociemba
    const solution = [];

    // For demonstration, we'll return the inverse of the scramble
    // In a real solver, this would implement actual solving algorithms
    const inverseMoves = {
      'R': "R'",
      "R'": 'R',
      'U': "U'",
      "U'": 'U',
      'F': "F'",
      "F'": 'F'
    };

    // Reverse and invert the move history
    const solveMoves = this.moveHistory
      .slice()
      .reverse()
      .map(move => inverseMoves[move]);

    return solveMoves;
  }

  /**
   * Print the cube state (simplified)
   */
  print() {
    console.log('\nCube State:');
    console.log(`Up (White):    [${this.faces.U.join(', ')}]`);
    console.log(`Down (Yellow): [${this.faces.D.join(', ')}]`);
    console.log(`Front (Green): [${this.faces.F.join(', ')}]`);
    console.log(`Back (Blue):   [${this.faces.B.join(', ')}]`);
    console.log(`Left (Orange): [${this.faces.L.join(', ')}]`);
    console.log(`Right (Red):   [${this.faces.R.join(', ')}]`);
    console.log(`Solved: ${this.isSolved()}`);
    console.log(`Move History: ${this.moveHistory.join(' ')}\n`);
  }
}

module.exports = RubiksCube;
