# Implement a generator called enum() that works just like the enumerate() built-in function.

# For simplicity, the function gets an iterable object and returns a tuple (index, element).

# Example:

# [IN]: list(enum(['TEN', 'CDR', 'BBT']))
# [OUT]: [(0, 'TEN'), (1, 'CDR'), (2, 'BBT')]

# Note! All you have to do is define a generator.

def enum(lst):
    index = 0
    for i in lst:
        yield (index,i)
        index+=1

lst = list(enum(['TEN', 'CDR', 'BBT']))

print(lst)