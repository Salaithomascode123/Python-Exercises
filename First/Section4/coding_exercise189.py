# The following list is given:

# items = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Implement a function called flatten(), which takes the nested list and returns the following:

# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Note: You only need to implement this function.

items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
lst = []
def flatten(nested_lst):
    for i in nested_lst:
        global lst
        lst += i


flatten(items)
print(lst)

    

