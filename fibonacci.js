/**
 * Fibonacci sequence generator and calculator
 */

// Iterative approach - most efficient
function fibonacciIterative(n) {
  if (n <= 0) return 0;
  if (n === 1) return 1;

  let prev = 0, curr = 1;

  for (let i = 2; i <= n; i++) {
    const next = prev + curr;
    prev = curr;
    curr = next;
  }

  return curr;
}

// Recursive approach with memoization
function fibonacciMemo() {
  const memo = {};

  return function fib(n) {
    if (n <= 0) return 0;
    if (n === 1) return 1;
    if (memo[n]) return memo[n];

    memo[n] = fib(n - 1) + fib(n - 2);
    return memo[n];
  };
}

// Generate sequence up to n terms
function fibonacciSequence(n) {
  const sequence = [];
  for (let i = 0; i < n; i++) {
    sequence.push(fibonacciIterative(i));
  }
  return sequence;
}

// Demo
if (require.main === module) {
  console.log('Fibonacci Numbers:\n');

  // Show first 15 numbers
  console.log('First 15 Fibonacci numbers:');
  console.log(fibonacciSequence(15).join(', '));

  console.log('\nIndividual calculations:');
  console.log(`fib(10) = ${fibonacciIterative(10)}`);
  console.log(`fib(20) = ${fibonacciIterative(20)}`);
  console.log(`fib(30) = ${fibonacciIterative(30)}`);

  // Using memoized version
  const fibMemo = fibonacciMemo();
  console.log('\nUsing memoized version:');
  console.log(`fib(40) = ${fibMemo(40)}`);
  console.log(`fib(45) = ${fibMemo(45)}`);
}

module.exports = {
  fibonacciIterative,
  fibonacciMemo,
  fibonacciSequence
};
