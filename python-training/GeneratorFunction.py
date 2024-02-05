# Generator Function 
'''
It is a special type of function that allows you to iterate over a potentially large set of items without generating them all at once in memory.
Produces Items One at a Time.
Uses the yield Keyword.
Memory Efficiency.
'''


def square(n):
    for i in range(n):
        yield i ** 2
for num in square(5):   # Here we are using the generator function 
    print(num)
