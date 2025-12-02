/**
 * Calculate the nth Fibonacci number
 * @param {number} n - The position in the Fibonacci sequence
 * @returns {number} The nth Fibonacci number
 */
function fibonacci(n) {
  if (n <= 0) return 0;
  if (n === 1) return 1;

  let a = 0, b = 1;
  for (let i = 2; i <= n; i++) {
    let temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}

/**
 * Generate Fibonacci sequence up to n terms
 * @param {number} n - Number of terms to generate
 * @returns {number[]} Array of Fibonacci numbers
 */
function fibonacciSequence(n) {
  if (n <= 0) return [];
  if (n === 1) return [0];

  const sequence = [0, 1];
  for (let i = 2; i < n; i++) {
    sequence.push(sequence[i - 1] + sequence[i - 2]);
  }
  return sequence;
}

// Example usage
console.log('Fibonacci of 10:', fibonacci(10));
console.log('First 10 Fibonacci numbers:', fibonacciSequence(10));

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { fibonacci, fibonacciSequence };
}
