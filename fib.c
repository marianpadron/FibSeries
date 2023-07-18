/*
    CS 5008
    Spring 2023
    Midterm Fib C Program
    Marian Padron
*/


#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// Create fib table with given size
#define SIZE 50000
static long fib_table[SIZE];

/*
* Helper function to print fibonacci value at n.
* Params:
*   - i: int, fibonacci n
*   - val: int, val at fibonacci n
* Returns: None
*/
void print_line(int i, int val) {
    printf("fib(%d): %d\n", i, val);
}

/*
* Fibonacci iterative algorithm.
* Params:
*   - n: int, n element in fibonacci sequence
* Returns: int, fib value at n
*/
int fib_iterative(int n) {
    // Create first and second values
    int first = 0;
    int second = 1;
    int val;

    for (int i = 0; i < n; i++) {

        // Inital fib vals
        if (i <= 1) {
            val = i;

        } else {
            val = first + second; // fib value is sum of previous two
            first = second; // make first value equal to second
            second = val; // second value is now the jsut calculated fib_r val
        }

    }

    return val;
}

/*
* Fibonacci recursive algorithm.
* Params:
*   - n: int, n element in fibonacci sequence
* Returns: int, fib value at n
*/
int fib_recursive(int n) {
    // Inital fib vals
    if(n <= 1) {
        return n;
    }

    // fib of n>1 is fib(n-1) + fib(n-2)
    return fib_recursive(n-1) + fib_recursive(n-2);
}

/**
* Helper function to call within fibonacci dynamic programing algorithm.
* Params:
*   - n: n element in fibonacci sequence
* Retuns: int, value at n in fibonacci sequence
*/
unsigned long fib_d(int n) {

    // Inital fib vals
    if(n <= 1) {
        return n;

    // Return val from table if already stored
    } else if (fib_table[n] != -1){
        return fib_table[n];
    }

    // Store next val; fib of n>1 is fib(n-1) + fib(n-2)
    fib_table[n] = fib_d(n-1) + fib_d(n-2);
    return fib_table[n];
}

/*
* Fibonacci dynamic programing algorithm.
* Params:
*   - n: int, n element in fibonacci sequence
* Returns: int, fib value at n
*/
int fib_dynamic(int n) {

    // Initialize table
    for(int i = 0; i < SIZE; i++) {
        fib_table[i] = -1;
    }

    // Base case
    fib_table[0] = 0;
    fib_table[1] = 1;

    // Use dynamic fib function
    int val;
    for (int i = 0; i < n; i++) {
        val = fib_d(i);
    }

    return val;
}

/*
* Helper function to prompt user for proper arguments.
* Params: None
* Returns: None 
*/
void argv_helper() {
    printf("At least two arguments needed.\n");
    printf("\t- N, number of iterations of fibonacci series.\n");
    printf("\t- Type of call: 0 for iterative, 1 for recursive, 2 for dynamic.\n");
    printf("\t- Print: 0 for no print (default), 1 for print N val, 2 for print all calculations.\n");

}

/*
* Helper function to call specific fibonacci sequence algorithm.
* Params:
*   - n: int, n element of fibonacci sequence
*   - call: int, type of algorithm (0 iterative, 1 recursive, 2 dynamic)
* Returns: int, value at n of fibonacci sequence
*/
int call_helper(int n, int call) {

    // Call iterative function
    if(call == 0) {
        return fib_iterative(n);
    
    // Call recursive function
    } else if(call == 1) {
        return fib_recursive(n - 1);
    
    // Call dynamic function
    } else {
        return fib_dynamic(n);
    }

}

int main(int argc, char* argv[]) {

    // Check valid arguments passed
    if (argc < 2) {
        argv_helper();
        return 1;
    }

    // Create default argument values
    int n = atoi(argv[1]);
    int call = 0;
    int print = 0;

    // Allocate argument values
    if (argc > 2) {
        call = atoi(argv[2]); // get type of sequence call
    }
    if (argc > 3) {
        print = atoi(argv[3]); // get type of print
    }

    // Call functions
    int n_val = call_helper(n, call);

    // Print
    if(print == 1) {
        print_line(n, n_val);
    }

    return 0;

}
