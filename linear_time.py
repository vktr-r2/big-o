import runtime_test
measure_runtime = runtime_test.measure_runtime

# store different test list sizes in a list
input_sizes = [10, 100, 1000, 10000, 100000, 1000000]


def sum_list(list):
    total = 0           
    for num in list:    # => O(n)
        total += num
    return total

# Test runtime using loop and measure_runtime function
for size in input_sizes:
  runtime = measure_runtime(sum_list, size)
  print(f"Input size: {size}, Runtime:{runtime:.20f} seconds\n")  

