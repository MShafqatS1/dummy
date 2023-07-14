# Find if a string is Pallindrome
#   - A string is said to be pallindrome if the reverse of the string is the same as string
#   - For example, "radar" is a pallindrome, but "redix" is not a pallindrome

def string_c2():
  string = input()

  # with the help of string slicing approach we can do this
  if string == string[::-1]:
    print("Yes, it is pallindrome")
  else:
    print("No, it is not a pallindrome")

string_c2()