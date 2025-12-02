def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.

    Args:
        n: Number of terms to generate

    Returns:
        List of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence


def fibonacci_generator(n):
    """
    Generator function for Fibonacci sequence.

    Args:
        n: Number of terms to generate

    Yields:
        Next Fibonacci number
    """
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def fibonacci_recursive(n):
    """
    Calculate nth Fibonacci number recursively (less efficient for large n).

    Args:
        n: Position in sequence (0-indexed)

    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    # Example usage
    n_terms = 10

    print(f"First {n_terms} Fibonacci numbers:")
    print(fibonacci(n_terms))

    print(f"\nUsing generator:")
    print(list(fibonacci_generator(n_terms)))

    print(f"\nUsing recursion for first 10 terms:")
    print([fibonacci_recursive(i) for i in range(n_terms)])

    # Print first 20 terms
    print(f"\nFirst 20 Fibonacci numbers:")
    print(fibonacci(20))
