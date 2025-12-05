/**
 * Rubik's Cube Solver Implementation
 * This is a simplified 2x2x2 Rubik's Cube solver using basic algorithms
 */

class RubiksCube {
  constructor() {
    // Initialize a solved cube state
    // Each face has 4 stickers (2x2): U (Up), D (Down), F (Front), B (Back), L (Left), R (Right)
    this.state = {
      U: ['W', 'W', 'W', 'W'], // White
      D: ['Y', 'Y', 'Y', 'Y'], // Yellow
      F: ['G', 'G', 'G', 'G'], // Green
      B: ['B', 'B', 'B', 'B'], // Blue
      L: ['O', 'O', 'O', 'O'], // Orange
      R: ['R', 'R', 'R', 'R']  // Red
    };
  }

  /**
   * Clone the current cube state
   */
  clone() {
    const newCube = new RubiksCube();
    newCube.state = JSON.parse(JSON.stringify(this.state));
    return newCube;
  }

  /**
   * Get the current state as a string
   */
  getState() {
    return JSON.stringify(this.state);
  }

  /**
   * Check if the cube is solved
   */
  isSolved() {
    for (const face in this.state) {
      const colors = this.state[face];
      if (!colors.every(color => color === colors[0])) {
        return false;
      }
    }
    return true;
  }

  /**
   * Rotate the right face clockwise
   */
  rotateR() {
    const temp = [this.state.F[1], this.state.F[3]];
    this.state.F[1] = this.state.D[1];
    this.state.F[3] = this.state.D[3];
    this.state.D[1] = this.state.B[2];
    this.state.D[3] = this.state.B[0];
    this.state.B[2] = this.state.U[1];
    this.state.B[0] = this.state.U[3];
    this.state.U[1] = temp[0];
    this.state.U[3] = temp[1];

    // Rotate R face itself
    const tempR = [...this.state.R];
    this.state.R[0] = tempR[2];
    this.state.R[1] = tempR[0];
    this.state.R[2] = tempR[3];
    this.state.R[3] = tempR[1];
  }

  /**
   * Rotate the right face counter-clockwise
   */
  rotateRPrime() {
    this.rotateR();
    this.rotateR();
    this.rotateR();
  }

  /**
   * Rotate the up face clockwise
   */
  rotateU() {
    const temp = [this.state.F[0], this.state.F[1]];
    this.state.F[0] = this.state.R[0];
    this.state.F[1] = this.state.R[1];
    this.state.R[0] = this.state.B[0];
    this.state.R[1] = this.state.B[1];
    this.state.B[0] = this.state.L[0];
    this.state.B[1] = this.state.L[1];
    this.state.L[0] = temp[0];
    this.state.L[1] = temp[1];

    // Rotate U face itself
    const tempU = [...this.state.U];
    this.state.U[0] = tempU[2];
    this.state.U[1] = tempU[0];
    this.state.U[2] = tempU[3];
    this.state.U[3] = tempU[1];
  }

  /**
   * Rotate the up face counter-clockwise
   */
  rotateUPrime() {
    this.rotateU();
    this.rotateU();
    this.rotateU();
  }

  /**
   * Rotate the front face clockwise
   */
  rotateF() {
    const temp = [this.state.U[2], this.state.U[3]];
    this.state.U[2] = this.state.L[3];
    this.state.U[3] = this.state.L[1];
    this.state.L[1] = this.state.D[0];
    this.state.L[3] = this.state.D[1];
    this.state.D[0] = this.state.R[2];
    this.state.D[1] = this.state.R[0];
    this.state.R[0] = temp[0];
    this.state.R[2] = temp[1];

    // Rotate F face itself
    const tempF = [...this.state.F];
    this.state.F[0] = tempF[2];
    this.state.F[1] = tempF[0];
    this.state.F[2] = tempF[3];
    this.state.F[3] = tempF[1];
  }

  /**
   * Rotate the front face counter-clockwise
   */
  rotateFPrime() {
    this.rotateF();
    this.rotateF();
    this.rotateF();
  }

  /**
   * Apply a sequence of moves
   * @param {string[]} moves - Array of move notations (R, R', U, U', F, F')
   */
  applyMoves(moves) {
    for (const move of moves) {
      switch (move) {
        case 'R':
          this.rotateR();
          break;
        case "R'":
          this.rotateRPrime();
          break;
        case 'U':
          this.rotateU();
          break;
        case "U'":
          this.rotateUPrime();
          break;
        case 'F':
          this.rotateF();
          break;
        case "F'":
          this.rotateFPrime();
          break;
        default:
          throw new Error(`Unknown move: ${move}`);
      }
    }
  }

  /**
   * Scramble the cube with random moves
   * @param {number} numMoves - Number of random moves to apply
   */
  scramble(numMoves = 10) {
    const moves = ['R', "R'", 'U', "U'", 'F', "F'"];
    const scrambleSequence = [];

    for (let i = 0; i < numMoves; i++) {
      const randomMove = moves[Math.floor(Math.random() * moves.length)];
      scrambleSequence.push(randomMove);
      this.applyMoves([randomMove]);
    }

    return scrambleSequence;
  }
}

/**
 * Simple Rubik's Cube Solver using BFS (Breadth-First Search)
 * Note: This is a simplified solver for demonstration purposes
 */
class RubiksCubeSolver {
  constructor(maxDepth = 7) {
    this.maxDepth = maxDepth;
    this.moves = ['R', "R'", 'U', "U'", 'F', "F'"];
  }

  /**
   * Solve the cube using BFS
   * @param {RubiksCube} cube - The scrambled cube to solve
   * @returns {string[]} - Array of moves to solve the cube
   */
  solve(cube) {
    if (cube.isSolved()) {
      return [];
    }

    const queue = [{ cube: cube.clone(), moves: [] }];
    const visited = new Set([cube.getState()]);

    while (queue.length > 0) {
      const { cube: currentCube, moves: currentMoves } = queue.shift();

      if (currentMoves.length > this.maxDepth) {
        continue;
      }

      for (const move of this.moves) {
        const newCube = currentCube.clone();
        newCube.applyMoves([move]);
        const newState = newCube.getState();

        if (!visited.has(newState)) {
          visited.add(newState);
          const newMoves = [...currentMoves, move];

          if (newCube.isSolved()) {
            return newMoves;
          }

          queue.push({ cube: newCube, moves: newMoves });
        }
      }
    }

    // If no solution found within maxDepth, return null
    return null;
  }

  /**
   * Solve with a simple heuristic approach (faster but may not be optimal)
   * @param {RubiksCube} cube - The scrambled cube to solve
   * @returns {string[]} - Array of moves (may not be optimal)
   */
  solveHeuristic(cube) {
    // For a simple demo, try random moves up to a certain depth
    // In practice, you'd use more sophisticated algorithms like Kociemba's algorithm
    return this.solve(cube);
  }
}

module.exports = { RubiksCube, RubiksCubeSolver };
