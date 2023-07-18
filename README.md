# Report on Analysis of Fibonacci  Series
* **Author**: Marian Padron
* **Semester** Spring 2023
* **Languages Used**: C, Python

## Overview
This report is a speed and code analysis of different algorithmic implementations used to compute the values in the Fibonacci sequence. The Fibonacci sequence is a set of positive integers in which a value at Nth position in the sequence is calculated by summing the preceding two numbers. The sequence can have its first element as either 0 or 1, but for the purposes of this report, 0 was used as the starting first number of the sequence. 

Elements in the Fibonacci sequence can be calculated by using the following mathematical equation: 

$$
fib(n) = fib(n – 1) + fib(n – 2)
$$

So, with 0 being the first element, and 1 being the second element, the first few values of the sequence would be as follows:

$$0, 1, 1,  2,  3,  5,  8,  13,  21,  34,  55,  89,  144 $$

The three algorithms being studied in this report are an iterative algorithm, recursive algorithm, and dynamic programming algorithm. I used both C and Python to implement such algorithms, and their speed when computing different values in the Fibonacci sequence was compared and analyzed.

## Big O Analysis
The time and space complexities for all three algorithms as well as the logic behind them is represented below.
|  Version  | Big O  | Space Used |
|-----------|--------|------------|
| Iterative |  O(n)  |    O(1)    |
| Recursive | O(2^n) |    O(n)    |
| Dynamic P |  O(n)  |    O(n)    |

For the iterative implementation of the code, I choose to use variable assignments to store the values of the two preceding Fibonacci numbers. This variable assignment has a space and time complexity of O(1); however, in order to iterate up to the Nth number in the Fibonacci sequence, a “for loop” is used where the sum of the two previous numbers is summed, stored, and the values for the next preceding two numbers are updated. While the space complexity stays at O(1), the use of the “for loop” up to the Nth Fibonacci number gives the algorithm a runtime complexity of O(n). Making it one of the most efficient time complexities after O(1) and O(log n).

The Fibonacci sequence is intrinsically a recursive mathematical equation, as you must have computed the Fibonacci values of the preceding numbers in order to calculate the Nth one. For evaluating the runtime complexity the recursive algorithm, I first read an [article](https://www.baeldung.com/cs/fibonacci-computational-complexity#:~:text=Therefore%2C%20our%20iterative%20algorithm%20has,) that uses backwards substitution to solve the Big O time complexity of using recursion for solving Fibonacci numbers.  Additionally, I watched the Module 07 videos to help me better understand the space and time implications of the recursive tree. Each time that we call the recursive function fib(n), if the Nth value we are looking for is anything other than 0 or 1, then the function will have to make two calls to fib(n – 1) and fib(n - 2). In turn each of these two calls will have to make another two calls, thus doubling the fib() call and resulting in an exponential runtime complexity of O(2^n). This results in an extremely slow algorithm, and makes the space complexity equal to O(n) since the depth of the tree is proportional to the size of N.

The dynamic programming algorithm for calculating the Fibonacci numbers optimizes the recursive method by taking advantage of memoization to increase speed. Although memoization implies sacrificing some space complexity for speed, not having to recompute all previous numbers up to the Nth value eliminates the exponential speed implications of the recursive algorithm. Because we are now storing all values up to N, space complexity is O(n). However, using index values to access an array is a runtime of O(1), which coupled with the individual new calculation per N value results in a polynomial time complexity of O(n).

## Empirical Data & Discussion 
To run both the C and Python programs, I took the test scripts provided in the sample midterm and adjusted them to call the iterative, recursive and dynamic programming algorithms for solving the Fibonacci sequence at a given Nth value. The max time interval for each method call was kept at 60 seconds; additionally, I created another running script that only calls the iterative and dynamic programming methods of both programs for a larger N. This was done to avoid the possible speed limitations caused by running the recursive method.

A brief overview of the results can be seen in the following graph, where overall, the C program ran faster than the Python program, and the recursive methods for both programs increased in runtime exponentially faster than the others.

<br></br>
<img src="/charts/all_algos.png" alt="p_iter_dp" style="width:75%; height:75%"/>
<br></br>

### Recursive Versions
Given the Big O time complexity of the recursive algorithm, it is not a surprise to see that for both languages it was the slowest algorithm. For both programs, one can see that the results draw out to be lines with exponential growth in time.

<br></br>
<img src="/charts/recursive.png" alt="p_iter_dp" style="width:60%; height:60%"/>
<br></br>

For the C program, the recursive call timed out once the Fibonacci sequence passed N = 45. The Python program times out a bit before the C program, once the sequence passed N = 40.

### Iterative & Dynamic Versions
The following graphs shows the comparison between the iterative and dynamic methods for each program when ran alongside the recursive method for an N = 60. 

<br></br>
<img src="/charts/c_all_algos.png" alt="p_iter_dp" style="width:70%; height:70%"/>
<br></br>

<img src="/charts/p_all_algos.png" alt="p_iter_dp" style="width:70%; height:70%"/>
<br></br>

One can see that the throughs and peaks for iterative and dynamic lines seem to stay within the same range of each other, which makes sense given that they both have a runtime complexity of O(n). Once I ran the test scripts that excluded the recursive method, I was able to iterate up to a Fibonacci number of N = 50000 within a couple of seconds. Upon doing this, we can see the slight differences between both algorithms as the N value increases.

<br></br>
<img src="/charts/c_iter_dp.png?raw=true" alt="p_iter_dp" style="width:75%; height:75%"/>
<br></br>

Although the peaks and throughs remain within the same range, the iterative implementation of the C program shows up to be on average faster than the dynamic programming version.

<img src="/charts/p_iter_dp.png" alt="p_iter_dp" style="width:75%; height:75%"/>
<br></br>

Although both algorithms have the same time complexity, we can see that in the Python program the opposite is true. The lines peaks and throughs are again within the same range, but once the Nth value is significantly higher, the dynamic programming algorithm runs on average faster than the iterative algorithm.

## Language Analysis
The code and running scripts can be found at the following files:

* [fib.c](fib.c) -- implementations of functions in C
* [fib.py](fib.py) -- implementations of functions in Python
* [test_runner](test_runner.py) -- script to help with test and data collection
* [iter_dp_runner.py](iter_dp_runner.py) -- script that excludes recursive call for testing and data collection

I’ve also included the two main csv files used to visualize the data:
* [fib_test_all.csv](fib_test_all.csv) -- csv file with all calls, N = 60
* [fib_iter_dp_test_1.csv](fib_iter_dp_test_1.csv) -- csv file with iterative and dynamic programming calls, N = 50000

### Language 1: C
For my C code I followed a similar structure to that taught to us in the Pascal triangle lab, as well as the methods provided in the Analysis of Fibonacci Numbers video in Module 07 of this class. The first intuitive way of implementing the iterative algorithm was to use a small array that would hold the values of the two numbers preceding N. I then realized that I could just use in place variables, and swap their values within each “for loop”, as shown below:

    int fib_iterative(int n) {
        int first = 0;
        int second = 1;
        int val;

        for (int i = 0; i < n; i++) {
            if (i <= 1) {
                val = i;
            } else {
                val = first + second;
                first = second;
                second = val;
            }
        }
        return val;
    }


For the recursive method I implemented code more closely related to that taught in Module 07 by using a recursive fib() function.

    int fib_recursive(int n) {
        if(n <= 1) {
            return n;
        }
        return fib_recursive(n-1) + fib_recursive(n-2);
    }

For my dynamic programming method I also took instruction form the module videos by using memoization to first initialize a global array (fib_table) that would hold the calculated values of the Fibonacci numbers as the function used recursion to return a value from the table or calculate and store a new one.

    #define SIZE 50000
    static long fib_table[SIZE];

    unsigned long fib_d(int n) {
        if(n <= 1) {
            return n;
        } else if (fib_table[n] != -1){
            return fib_table[n];
        }

        fib_table[n] = fib_d(n-1) + fib_d(n-2);
        return fib_table[n];
    }
    
    int fib_dynamic(int n) {

        for(int i = 0; i < SIZE; i++) {
            fib_table[i] = -1;
        }

        fib_table[0] = 0;
        fib_table[1] = 1;

        int val;
        for (int i = 0; i < n; i++) {
            val = fib_d(i);
        }

        return val;
    }

The fib_dynamic() method gets called once when the main program is run, which initializes the fib_table with placeholder values of -1 and then calls the fib_d() helper method that uses recursion to fill the array.

### Language 2: Python
I deliberated on whether I wanted to use Python or Java for my second language but chose Python for two main reasons. Firstly, I wanted to be able to visualize and compare the potential speed differences between a strictly interpreted language like Python, and a compiled language like C. Secondly, when thinking about how I would approach the dynamic programming in respect to memoization, Python’s ability to easily use Lists and append to them made me believe it would be more efficient in terms of memory instead of having to initialize a large table with a fixed size. 

In terms of my iterative and recursive methods, my C and Python code is nearly identical. However, when approaching the dynamic programming I first went in by initializing a global table (fib_table) that held two values, 0 and 1. As I went recursively through the dynamic programming method the function would either find a Fibonacci value at a given index or append to the fib_table list.

    fib_table = [0, 1]

    def fib_dynamic(n: int) -> int:
        try:
            return fib_table[n]
        except IndexError:
            fib_table.insert(n, fib_dynamic(n - 1) + fib_dynamic(n - 2))
            return fib_table[n]

However, after looking into how Python implements Lists I found Python uses dynamic arrays (instead of linked lists as I previously thought). This meant that within each recursion call in which the fib_table was full, Python would then double the array.

After thinking on it for a bit, I concluded that the purpose of memiozation is to sacrifice some memory allocation for speed. So in trying to save up on memory, I was potentially slowing down my program and defeating the purpose of dynamic programming. Finally, I ended up implementing the code very similarly to my C code, where I initialize a table with a fixed size at the beginning of the code to be used for storing the Fibonacci values.

    SIZE = 50000
    fib_table = [-1] * SIZE
    fib_table[0] = 0
    fib_table[1] = 1

    def fib_dynamic(n: int) -> int:
        if fib_table[n] != -1:
            return fib_table[n]
        else:
            fib_table[n] = fib_dynamic(n - 1) + fib_dynamic(n - 2)
            return fib_table[n]

### Comparison and Discussion Between Experiences
As a general rule, for all three algorithms C was able to run through the Fibonacci sequence faster than Python. That becomes intuitive when you consider that Python needs to be interpreted, which adds to the number of CPU instructions before the code fully executes. In terms of the algorithms themselves, for both languages the graphs help visualize the iterative and dynamic programming time complexities of O(n), and the recursive algorithm time complexity of O(2^n). Although the linear growth for the iterative and dynamic programming algorithms is not very well defined, I do believe it has to do with the slow time complexity of O(n) relative to O(2^n). Where if I had iterated through a much larger set of Fibonacci numbers the graphs would’ve displayed more linear behavior over the sequence.

When running the test scripts that included the recursive method, I was only able to get up to around 40 to 45 numbers before my recursive timed out above 60 seconds. There was a vast difference between that and the ability to run the iterative and dynamic methods for up to N = 50000 just within a couple of seconds.

Looking at both languages’ data for the iterative and dynamic programming algorithms, I spent a while pondering on the reason why they show opposite behaviors in terms of speed. For C, the empirical data displays the iterative algorithm runtime line below the dynamic programming line on average. This makes sense when you consider the implications of using a bottom-up approach versus a top-down approach. Where the latter can become slower due to the overhead caused many recursive calls. When it came to the behavior of the Python program, however, this became a bit confusing. At lower N values, the Python iterative and dynamic programming versions run at around the same speed, but once N reaches around 20000, the dynamic programming algorithm runs faster than the iterative version. I first hypothesized that it might have something to do with Python being interpreted and ran line by line, therefore making the “for loop” of the iterative version slower than the recursion of the dynamic programming version. Although I was not able to find anything to prove this hypothesis, the fact that Python is dynamically typed, means that there are more steps involved with any operation that assigns values. This could be a factor playing into the speed differences because, unlike C where variables already know their type, I am re-defining three variables during each “for loop”.  On top of this, Python’s for loops are not very efficient when scaling up to massive datasets or values, which might also play into the reduced speed in the iterative implementation versus the dynamic programming implementation. Perhaps using a package such as NumPy would’ve countered some of the speed implications of my iterative “for loop”, and is something to consider for the future.

When it came to the code itself there wasn’t much difference between my C approach and Python, aside from my initial implementation of Python Lists. I did encounter an error when trying to run my Python code for higher N values. Where the C code didn’t seem to have a max recursion error, I did have to specify to Python to allow for greater recursion to be able to calculate a larger Fibonacci number.

## Conclusions / Reflection
Running these tests and visualizing them has allowed me to better see the difference between the iterative, recursive, and dynamic programming algorithms in terms of implementation, time and space complexity. I can more fully understand the power of Big O, and see more of its relevance even when thinking about previous assignments such as the different sorting algorithms.

When it came to the programming languages, I personally enjoyed coding in Python more as I find it more intuitive. However, I fully appreciate the importance of understanding and writing C code. This was particularly relevant when thinking about how I would implement the memoization in Python. Given that Python is written in C programming language, not fully thinking about how Python objects may be implemented using C code is naïve and could’ve resulted in slower running code. Additionally, the speed differences between Python’s iterative code versus the dynamic programming code made me reflect a bit more about the compile and runtime between both languages. I would like to more fully explore why my dynamic programming version (which uses recursion) ran faster than the iterative version, as well as how using a package such as NumPy might’ve changed the overall runtime for the algorithms.

## References
1. “Difference between Recursion and Iteration.” GeeksforGeeks, GeeksforGeeks, 11 Feb. 2023, https://www.geeksforgeeks.org/difference-between-recursion-and-iteration/. 
2. Gautam, Shubham. “Top-down vs Bottom-up Approach in Dynamic Programming.” Enjoyalgorithms, https://www.enjoyalgorithms.com/blog/top-down-memoization-vs-bottom-up-tabulation. 
3. “Is Your Python for-Loop Slow? Use Numpy Instead.” The Analytics Club, https://www.the-analytics.club/speed-up-slow-for-loops-in-python. 
4. Marshall, Written by: Emily. “Computational Complexity of Fibonacci Sequence.” Baeldung on Computer Science, 25 Nov. 2022, https://www.baeldung.com/cs/fibonacci-computational-complexity#:~:text=Therefore%2C%20our%20iterative%20algorithm%20has,)%20%3D%20O(n). 
5. “Python: Handling Recursion Limit.” GeeksforGeeks, GeeksforGeeks, 26 May 2021, https://www.geeksforgeeks.org/python-handling-recursion-limit/. 
6. “Subprocess - Subprocess Management.” Python Documentation, https://docs.python.org/3/library/subprocess.html. 
7. VanderPlas, Jake. “Why Python Is Slow: Looking under the Hood.” Why Python Is Slow: Looking Under the Hood | Pythonic Perambulations, http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/. 
8. Writer, PFB Staff. “Command Line Arguments (Sys.argv).” PythonForBeginners.com, 27 Aug. 2020, https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv. 
9. Zhiyanov, Anton. “How Python List Works.” Anton Zhiyanov, 12 Nov. 1970, https://antonz.org/list-internals/. 
