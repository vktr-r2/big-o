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


"""
NOTES

O(n) Time
- O(n) is linear time.  The larger the data set, the longer an algorithm will take, but the increase in time/operations needed will be constant.

- Consider an algorithm that loops through an array just once, and multiplies each element by 2.
  => No matter how many elements in the array, each operation will take the same amount of time for each element.  Because of that we can portray the increase in time as linear.

- Generally 0(1) will be faster than 0(n), but it's important to realize that some algorithms that are constant can still take a long time.

REAL WORLD EXAMPLE

Imagine you're building a file management application, and you want to check if a given file exists in a directory. If the directory contains a large number of files and they are not sorted in any particular order, you would need to perform a linear search to find the file you're looking for.

def does_file_exist(directory, target_file):
    for file in directory:
        if file == target_file:
            return True
    return False

file_directory = ["file1.txt", "file2.jpg", "file3.doc", ...]  # List of files

target_file = "file2.jpg"
exists = does_file_exist(file_directory, target_file)
print(f"File '{target_file}' exists: {exists}")

In this example, the does_file_exist function performs a linear search through the list of files in the directory to determine whether the target file exists. The time complexity of this operation is O(n), where "n" is the number of files in the directory.

"""