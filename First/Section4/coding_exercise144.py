# The following list is given:

# stocks = [
#     {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
#     {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
#     {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
# ]


# Extract companies from the 'mWIG40' index and print the result to the console.



# Formatted result:



# [{'index': 'mWIG40', 'name': 'TEN', 'price': 304},
#  {'index': 'mWIG40', 'name': 'PLW', 'price': 309}]


# Expected result:

# [{'index': 'mWIG40', 'name': 'TEN', 'price': 304}, {'index': 'mWIG40', 'name': 'PLW', 'price': 309}]

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print([mwig40_company for mwig40_company in stocks if mwig40_company['index'] == 'mWIG40'])
