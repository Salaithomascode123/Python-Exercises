# The following variable is given:

# number = 1.0

# Test whether the variable is an instance of the built-in class int. Print 'YES' if true, 'NO' if false.

# Expected result:

# NO

number = 1.0

print('YES' if type(number) == type(int()) else 'NO' )
