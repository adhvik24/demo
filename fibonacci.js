/**
 * Fibonacci number implementations
 */

// Recursive approach (simple but inefficient for large n)
function fibonacciRecursive(n) {
  if (n <= 1) return n;
  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Iterative approach (efficient)
function fibonacciIterative(n) {
  if (n <= 1) return n;

  let prev = 0;
  let curr = 1;

  for (let i = 2; i <= n; i++) {
    const next = prev + curr;
    prev = curr;
    curr = next;
  }

  return curr;
}

// Memoized recursive approach (efficient with caching)
function fibonacciMemoized() {
  const cache = {};

  return function fib(n) {
    if (n <= 1) return n;
    if (cache[n]) return cache[n];

    cache[n] = fib(n - 1) + fib(n - 2);
    return cache[n];
  };
}

// Generate Fibonacci sequence up to n terms
function fibonacciSequence(n) {
  if (n <= 0) return [];
  if (n === 1) return [0];

  const sequence = [0, 1];
  for (let i = 2; i < n; i++) {
    sequence.push(sequence[i - 1] + sequence[i - 2]);
  }

  return sequence;
}

// Demo usage
if (require.main === module) {
  const n = 10;

  console.log(`Fibonacci number at position ${n}:`);
  console.log(`Iterative: ${fibonacciIterative(n)}`);
  console.log(`Recursive: ${fibonacciRecursive(n)}`);

  const memoFib = fibonacciMemoized();
  console.log(`Memoized: ${memoFib(n)}`);

  console.log(`\nFirst ${n} Fibonacci numbers:`);
  console.log(fibonacciSequence(n).join(', '));

  // Performance comparison for larger number
  const largeN = 40;
  console.log(`\nPerformance test for n=${largeN}:`);

  console.time('Iterative');
  fibonacciIterative(largeN);
  console.timeEnd('Iterative');

  console.time('Memoized');
  const memoFib2 = fibonacciMemoized();
  memoFib2(largeN);
  console.timeEnd('Memoized');
}

module.exports = {
  fibonacciRecursive,
  fibonacciIterative,
  fibonacciMemoized,
  fibonacciSequence
};
