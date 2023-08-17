import time

# Binary search cuts the data set in half on each iteration giving it O(log(N)) complexity
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    # loop while low is less than high variable
    while low <= high:
        mid = (low + high) // 2
        
        # check to see if target is in middle of current data set
        if arr[mid] == target:
            return mid
        # if mid is less than target
        elif arr[mid] < target:
            # adjust new low to be mid + 1
            low = mid + 1
        # if mid is more than target
        else:
            # adjust new high to be mid - 1
            high = mid - 1
            
    return -1  # Target not found

def measure_runtime(function, input_data):
    start_time = time.time()
    function(input_data)
    end_time = time.time()
    return end_time - start_time


input_size = 1000000
input_data = list(range(input_size))
target_value = 500000
runtime = measure_runtime(lambda data: binary_search(data, target_value), input_data)
print(f"Binary search runtime for input size {input_size}: {runtime} seconds")






