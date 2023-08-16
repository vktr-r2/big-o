import runtime_test
measure_runtime = runtime_test.measure_runtime_single_input

# store different test list sizes in a list
input_sizes = [1, 5, 25, 50, 100]

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test runtime using loop and measure_runtime function
for size in input_sizes:
  runtime = measure_runtime(fibonacci, size)
  print(f"Input size: {size}, Runtime:{runtime:.20f} seconds\n")