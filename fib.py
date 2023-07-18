"""
    CS 5008
    Spring 2023
    Midterm Fib Python Program
    Marian Padron
"""

import sys

# Increase recursion limit for testing
sys.setrecursionlimit(51000)

# Create fib table with set size
SIZE = 50000
fib_table = [-1] * SIZE
fib_table[0] = 0
fib_table[1] = 1


def print_line(i: int, val: int) -> None:
    """
    Helper function to print fibonacci value at n.
    :param i: int, fibonacci n
    :param val: int, value at fibonacci n
    :return: None
    """
    print(f"fib({i}): {val}")


def fib_iterative(n: int) -> int:
    """
    Fibonacci iterative algorithm.
    :param n: int, n element in fibonacci sequence
    :return: int, fib value at n
    """
    # Create first and second values
    first = 0
    second = 1
    val = None

    for i in range(0, n):
        # Initial fib vals
        if i <= 1:
            val = i
        else:
            val = first + second  # fib val is sum of previous two
            first, second = second, val  # swap values

    return val


def fib_recursive(n: int) -> int:
    """
    Fibonacci recursive algorithm.
    :param n: int, n element in fibonacci sequence
    :return: int, fib value at n
    """
    # Initial fib vals
    if n <= 1:
        return n

    # fib of n>1 is fib(n-1) + fib(n-2)
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dynamic(n: int) -> int:
    """
    Fibonacci dynamic algorithm.
    :param n: int, n element in fibonacci sequence
    :return: int, fib value at n
    """
    # Return n value if already stored
    if fib_table[n] != -1:
        return fib_table[n]
    
    else:
    # Store next value; fib of n>1 is fib(n-1) + fib(n-2)
        fib_table[n] = fib_dynamic(n - 1) + fib_dynamic(n - 2)
        return fib_table[n]


def argv_helper() -> None:
    """
    Helper function to prompt user for proper arguments.
    :return: None
    """
    print("At least two arguments needed.")
    print("\t- N, number of iterations of fibonacci series.")
    print("\t- Type of call: 0 for iterative, 1 for recursive, 2 for dynamic.")
    print("\t- Print: 0 for no print (default), 1 for print N val, 2 for print all calculations.")


def call_helper(n: int, call: int) -> int:
    """
    Helper function to call specific fibonacci sequence algorithm.
    :param n: int, n element of fibonacci sequence
    :param call: int, type of algorithm (0 iterative, 1 recursive, 2 dynamic)
    :return: int, value at n of fibonacci sequence
    """
    if call == 0:
        return fib_iterative(n)
    elif call == 1:
        return fib_recursive(n - 1)
    else:
        return fib_dynamic(n - 1)


def main():

    # Check valid arguments passed
    if len(sys.argv) < 2:
        argv_helper()
        return

    # Create default argument values
    n = int(sys.argv[1])
    call = 0
    print_val = 0

    # Change recursion limit
    #sys.setrecursionlimit(n) if n <= 20000 else sys.setrecursionlimit(20000)

    # Allocate argument values
    if len(sys.argv) > 2:
        call = int(sys.argv[2])  # get type of sequence call
    if len(sys.argv) > 3:
        print_val = int(sys.argv[3])  # get type of print

    # Call functions
    n_val = call_helper(n, call)

    # Print
    if print_val == 1:
        print_line(n, n_val)


if __name__ == "__main__":
    main()
