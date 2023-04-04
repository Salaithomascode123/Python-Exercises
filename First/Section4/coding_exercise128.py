# Implement a function called multi(), which accepts an iterable object (list, tuple) as an argument and returns the product of all elements of this iterable object.

# Example:

# [IN]: multi((-4, 6, 2))
# [OUT]: -48

# [IN]: multi([4, 2, -5])
# [OUT]: -40

# Note! You only need to define the function

def multi(datas):
    result = 1
    for element in datas:
        result *= element
    print(result)

multi((-4, 6, 2))
multi([4, 2, -5])
