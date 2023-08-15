import runtime_test
measure_runtime = runtime_test.measure_runtime

# store different test list sizes in a list
input_sizes = [10, 100, 1000, 10000, 100000, 1000000]


def return_first_element(list):
    return list[0] # => O(1)

# Test runtime using loop and measure_runtime function
for size in input_sizes:
  runtime = measure_runtime(return_first_element, size)
  print(f"Input size: {size}, Runtime:{runtime:.20f} seconds\n")