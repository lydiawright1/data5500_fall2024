# lst = [3, 1, 4, 1, 5, 9, 2, 6]

# # for l in lst:
# #     print(l)

# #print number
def print_number(l, index, length):
    if index == length:
        return
    print(l[index])
    print_number(l, index+1, length)

print_number(lst, 0, len(lst))

# #function def
# #base case-shut it down
# #logic
# #recursive call

# #problems that can be broken into smaller parts that require the exact same logic to solve them