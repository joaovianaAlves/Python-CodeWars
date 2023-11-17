import functools 

def find_average(numbers):
    if numbers == []:
        return 0
    
    result_sum = functools.reduce(lambda acc, x: acc + (x if x > 0 else 0), numbers, 0)

    average = result_sum / len(numbers)
    return average
