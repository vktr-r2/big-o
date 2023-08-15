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