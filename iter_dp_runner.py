"""
    CS 5008
    Spring 2023
    Midterm Python and C test runner
    Marian Padron

    This python "script" was taken from the sample test runner from the sample
    midterm provided. I have adjusted the script to run and time the execution
    of the iterative, recursive, and dynamic algorithms for calculating the fibonacci 
    sequence. Additionally, the program can take as an input whether it should run the 
    generated C code or Python code.

    Sample execution:
        python3 test_runner.py 30 (will NOT write to file)
        python3 test_runner.py 30 csv > fib_c_csv.csv (writes to csv file)
        python3 test_runner.py 30 > fib_c_table.md (writes to md file)

"""

import subprocess
import time
import sys
import math

COMMON_ARG_FORMAT = "./fib.out {n} {algo}"
FORMAT = "markdown"
TIMEOUT = 60
COMMON_ARG_PYTHON = "python3 fib.py {n} {algo}" 

LAST_RUN_TRACKER = {"0": 0.0, "1": 0.0, "2": 0.0, "iterative": 0.0, "recursive": 0.0, "dp": 0.0}


def run_single(n: int, typ: int, command=COMMON_ARG_FORMAT) -> float:
    """Run a single instance collecting the total execution time
    Args:
        command:
        n (int): the row to generate
        typ (int): the type of algorithm to use
    Returns:
        float: the time it took, or nan if TIMEOUT is reached first
    """
    command = command.format(n=n, algo=typ)
    if math.isnan(LAST_RUN_TRACKER[str(typ)]):
        return math.nan  # skip running if we are already timing out
    try:
        start = time.time()
        subprocess.run(command.split(), timeout=TIMEOUT)
        end = time.time()
        result = end - start

    except subprocess.TimeoutExpired:
        result = math.nan
    LAST_RUN_TRACKER[str(typ)] = result
    return result


def build_row(n: int) -> str:
    """Builds a row to print to the screen either in csv format or markdown
    Args:
        n (int): the row to build in the triangle
    Returns:
        str: a markdown formatted or csv string of the result
    """
    results_lst = []
    for t in [0, 2]:
        result = run_single(n, t)
        results_lst.append("-" if math.isnan(result) else f"{result:.5f}")
    iterative, dynamic_programming = results_lst

    results_lst = []
    for t in [0, 2]:
        result = run_single(n, t, COMMON_ARG_PYTHON)
        results_lst.append("-" if math.isnan(result) else f"{result:.5f}")
    iterative_p, dynamic_programming_p = results_lst

    if FORMAT == "markdown":
        return f"| {n:<7} | {iterative.center(11, ' ')} | {dynamic_programming.center(22, ' ')} |" \
            + f"{iterative_p.center(12, ' ')} | {dynamic_programming_p.center(22, ' ')} |"
    return f"{n},{iterative},{dynamic_programming},{iterative_p},{dynamic_programming_p}"


def table_header() -> str:
    """Returns a markdown table header for this data set"""
    if FORMAT == "markdown":
        return "|    n    | Iterative C | Dynamic Programming  C | Iterative P | Dynamic Programming  P |\n" + \
               "|---------|-------------|------------------------|-------------|------------------------|"
    return "n,Iterative C,Dynamic Programming C,Iterative P,Dynamic Programming P"


def main(n):
    print(table_header())
    for i in range(100, n + 1, 100):
        print(build_row(i))


if __name__ == "__main__":
    n = 20000 if len(sys.argv) < 2 else int(sys.argv[1])
    if len(sys.argv) == 3:
        FORMAT = "csv"
    main(n)