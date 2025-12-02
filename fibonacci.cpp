#include <iostream>
#include <vector>

using namespace std;

/**
 * Generate Fibonacci sequence up to n terms.
 *
 * @param n Number of terms to generate
 * @return Vector of Fibonacci numbers
 */
vector<long long> fibonacci(int n) {
    vector<long long> fib_sequence;

    if (n <= 0) {
        return fib_sequence;
    }

    if (n >= 1) {
        fib_sequence.push_back(0);
    }

    if (n >= 2) {
        fib_sequence.push_back(1);
    }

    for (int i = 2; i < n; i++) {
        fib_sequence.push_back(fib_sequence[i-1] + fib_sequence[i-2]);
    }

    return fib_sequence;
}

/**
 * Calculate nth Fibonacci number recursively (less efficient for large n).
 *
 * @param n Position in sequence (0-indexed)
 * @return The nth Fibonacci number
 */
long long fibonacci_recursive(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

/**
 * Calculate nth Fibonacci number iteratively (more efficient).
 *
 * @param n Position in sequence (0-indexed)
 * @return The nth Fibonacci number
 */
long long fibonacci_iterative(int n) {
    if (n <= 1) {
        return n;
    }

    long long a = 0, b = 1;
    long long result = 0;

    for (int i = 2; i <= n; i++) {
        result = a + b;
        a = b;
        b = result;
    }

    return result;
}

/**
 * Print a vector of numbers.
 *
 * @param vec Vector to print
 */
void print_vector(const vector<long long>& vec) {
    cout << "[";
    for (size_t i = 0; i < vec.size(); i++) {
        cout << vec[i];
        if (i < vec.size() - 1) {
            cout << ", ";
        }
    }
    cout << "]" << endl;
}

int main() {
    int n_terms = 10;

    cout << "First " << n_terms << " Fibonacci numbers:" << endl;
    vector<long long> fib_seq = fibonacci(n_terms);
    print_vector(fib_seq);

    cout << "\nUsing recursion for first 10 terms:" << endl;
    cout << "[";
    for (int i = 0; i < n_terms; i++) {
        cout << fibonacci_recursive(i);
        if (i < n_terms - 1) {
            cout << ", ";
        }
    }
    cout << "]" << endl;

    cout << "\nUsing iterative approach for first 10 terms:" << endl;
    cout << "[";
    for (int i = 0; i < n_terms; i++) {
        cout << fibonacci_iterative(i);
        if (i < n_terms - 1) {
            cout << ", ";
        }
    }
    cout << "]" << endl;

    // Print first 20 terms
    cout << "\nFirst 20 Fibonacci numbers:" << endl;
    vector<long long> fib_seq_20 = fibonacci(20);
    print_vector(fib_seq_20);

    return 0;
}
