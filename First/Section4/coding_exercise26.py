# From the following text:

# string = '1 0 0 1 0 1'

# remove spaces using slicing. Then convert the result to decimal notation and print to the console as shown below.

# Expected result:

# Number found: 37

string = '1 0 0 1 0 1'
rem_space = string[0::2]
toDecimal = int(rem_space,2)
print(f"Number found: {toDecimal}")