import runtime_test
measure_runtime = runtime_test.measure_runtime

# store different test list sizes in a list
input_sizes = [10, 100, 1000, 10000]


def sum_product_pairs(list):
  length = len(list)
  result = 0

  for i in range(length):             ## \
    for j in range(length):           ## |    O(n^2)
      result += list[i] * list[j]     ## /

  return result


# Test runtime using loop and measure_runtime function
for size in input_sizes:
  runtime = measure_runtime(sum_product_pairs, size)
  print(f"Input size: {size}, Runtime:{runtime:.20f} seconds\n")