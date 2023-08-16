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


"""
NOTES

0(1) TIME
- 0(1) is constant time.  No matter the size of the data set, the algorithm will always take same amount of operations to reach upper bound.

- Imagine a function which returns first element of an array.  No matter the length of the array, finding first element will always take same amount of steps.

- IMPORTANT: 0(1) doesn't mean fast!  It means constant!
  => It just so happens that 0(1) algorithms are very efficient in most cases


REAL WORLD EXAMPLE

Suppose you're building a social media application, and you want to quickly retrieve user profile information given a user's username. You could use a hash map to store user profiles, where the usernames are keys and the corresponding profiles are values. This way, when a user's profile needs to be displayed, you can fetch it in constant time using their username as the key.

user_profiles = {
    "alice": {"name": "Alice Johnson", "age": 28, "followers": 500},
    "bob": {"name": "Bob Smith", "age": 35, "followers": 1000},
    # ... other user profiles ...
}

def get_user_profile(username):
    return user_profiles.get(username, None)  # O(1) retrieval

"""