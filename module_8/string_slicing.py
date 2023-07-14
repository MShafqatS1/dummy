# String Slicing
# I don't want Moh from name

name = "Mohammad Shafqat Siddiqui"

# print(len(name))
# print(name[0])

# print whol string
# print(name[:])

# print every 5 index value from a string
# print(name[::5])

# print 1 index value to 5 characters
# print(name[1:5])

# print after 2 index values
# print(name[2::])

# print reverse value with the help of negative indexing
# print(name[-1])

# print all string except last index value
# print(name[:-1])

# print all string except first and last index value
# print(name[1:-1])

# print empty string
# print(name[1 : -1 : -1])

# print empty string
# print(name[-1 : 0])

# print string in reverse order
# print(name[::-1])

# print string in reverse order second method
print(name[-1 : -len(name+1) : -1 ])