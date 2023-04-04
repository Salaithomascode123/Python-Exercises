# The following text is given:

# text = """Python is powerful... and fast
# plays well with others
# runs everywhere
# is friendly & easy to learn
# is Open
# These are some of the reasons people who use Python would rather not use anything else"""

# Create a list of words from the given text. Then standardize this text (change uppercase letters to lowercase, remove punctuation marks). Extract words longer than six characters and print the result to the console.

# Expected result:

# ['powerful', 'everywhere', 'friendly', 'reasons', 'anything']

text = """Python is powerful... and fast
 plays well with others
 runs everywhere
 is friendly & easy to learn
 is Open
 These are some of the reasons people who use Python would rather not use anything else"""

textL = text.lower()
rm_pun = textL.replace('.','')
txt_lst = rm_pun.split()
result = []

for x in txt_lst:
    if len(x) > 6:
        result.append(x)

print(result)



