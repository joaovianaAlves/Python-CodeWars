def positive_sum(arr):
    sum = 0
    for number in arr:
        sum += number if number >= 0 else 0
    return sum
