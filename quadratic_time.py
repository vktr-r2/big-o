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


"""
NOTES

O(n^2)
- O(n^2) is also known as quadratic time complexity.

- Quadratic time sees an increase in time that is proportional to the square of the data set.

- Quadratic time takes a lot longer as data sets get bigger.  This kind of runtime is actually common.  An example is a nested loop.
  => The inner loop looks at each element for every element in the outer loop.  Such an algorithm has quadratic time complexity whiche makes it quite slow

REAL WORLD EXAMPLE

Suppose you're building a graphics application that needs to transform 2D points using a transformation matrix. For a 2x2 matrix, which is relatively small, a nested loop to perform the matrix-vector multiplication might be acceptable.

def matrix_vector_multiply(matrix, vector):
    result = [0, 0]
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result

transformation_matrix = [[2, 0], [0, 2]]  # 2x2 transformation matrix
point = [3, 4]  # 2D point

transformed_point = matrix_vector_multiply(transformation_matrix, point)
print("Transformed Point:", transformed_point)


"""