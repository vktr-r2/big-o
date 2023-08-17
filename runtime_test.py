# time module is built into Python 3
import time

def measure_runtime(function, input_size):
    
  # create list that will range from 0 - input_size
  input_data = list(range(input_size))

  # capture start time in variable
  start_time = time.time()

  # run argument function on input_data
  function(input_data)

  # capture end time in variable
  end_time = time.time()

  # return the total run time
  return end_time - start_time



def measure_runtime_single_input(function, input):
  
  # capture start time in variable
  start_time = time.time()

  # run argument function on input_data
  function(input)

  # capture end time in variable
  end_time = time.time()

  # return the total run time
  return end_time - start_time




"""
NOTES

- Big O describes overall performance of algorithms
  => short for "Order of"

- Algorithm's rate of growth can grow in both time and space
  => time = total runtime
  => space = space in memory

* Generally with Big O notation we focus on the runtime rate of growth.

- Big O is user to determine the worst-case or expected/most common case scenarios (if worst case is very rate)
  => Big 0 is never used to determin best case
  => worst case scenario = upper bound

- UPPER BOUND is the absolute most number of operations that an algorithm will need to take when it executes.

** So Big O is less about how long, and more about how many (operations)
  => Different computers have different computing speeds, so time may vary, but the number of operations to reach upper bound stays constant
  => We don’t measure the speed of an algorithm in seconds (or minutes!). We measure the rate of growth of an algorithm in the number of operations it takes to complete.

- Ultimately Big 0 answers whether an algorithm can scale efficiently


Efficient
O(1): Constant time
O(log(n)): Logarithmic time
O(n): Linear time

Less Efficient
O(Nlog(N)): Linear logarithmic time

Inefficient
O(n^2): Quadratic time
O(n^3):	Cubic time
O(2^n): Exponential time
O(!n): Factorial time

"""