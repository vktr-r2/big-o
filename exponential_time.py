import runtime_test
measure_runtime = runtime_test.measure_runtime_single_input

# store different test list sizes in a list
input_sizes = [1, 5, 10, 15, 20, 30]

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test runtime using loop and measure_runtime function
for size in input_sizes:
  runtime = measure_runtime(fibonacci, size)
  print(f"Input size: {size}, Runtime:{runtime:.20f} seconds\n")


"""
NOTES

O(2^n)
- O(2^n) time complexity is known as exponential time and it is even more inefficient that quadratic time.
  => The number of operations needed DOUBLES for every element added to the data set.

- Seeing a function call itself twice as the fibonacci function implemented above is a great indicator that the algorithm uses exponential time

REAL WORLD EXAMPLE

Suppose you're building a small utility application that helps a user generate all possible combinations of toppings for a pizza. Since the number of possible topping combinations grows exponentially with the number of available toppings, an algorithm with O(2^n) complexity might be acceptable for small numbers of toppings.

def generate_subsets(toppings):
    if not toppings:
        return [[]]
    subsets_without_first = generate_subsets(toppings[1:])
    subsets_with_first = [[toppings[0]] + subset for subset in subsets_without_first]
    return subsets_without_first + subsets_with_first

available_toppings = ["pepperoni", "mushroom", "olive", "green pepper"]
all_subsets = generate_subsets(available_toppings)

for subset in all_subsets:
    print(subset)


In this example, the generate_subsets function uses a recursive approach to generate all possible subsets of the available pizza toppings. The time complexity of this algorithm is O(2^n), where "n" is the number of available toppings. While this approach isn't efficient for large numbers of toppings, it might still be acceptable for small pizza menus with a limited number of choices.

Remember that exponential time complexity should be used cautiously and only in situations where the input size is known to be small and the performance impact is acceptable for the application's requirements.

"""