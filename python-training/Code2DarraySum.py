array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def sum(arr):
    total_sum = 0
    for row in arr:
        for element in row:
            total_sum += element
    return total_sum

result = sum(array)
print("Sum of elements in the two-dimensional array:", result)
