#Lambda_function
'''
A lambda function is a concise way to create anonymous functions.
Anonymous functions are functions that are defined without a name.
 Lambda functions are often used for short, simple operations that can be expressed in a single line of code.
'''


def square(x):  # Normal function to square a number
    return x ** 2

lambda_square = lambda x: x ** 2  # lambda function

print(square(5))
print(lambda_square(5))  


'''
Both generate same output 
Use Regular Functions when
  Complex Logic
  Reusability

Use Lambda Functions when
  Short, Simple Operation
  When a function is needed for a short duration and won't be reused


'''
   
