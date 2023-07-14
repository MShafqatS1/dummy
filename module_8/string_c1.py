# Print all vowels of a given string

def string_c1():
  text = "Pre-requisites for Python free certification course"

  for i in text:
    # check vowels here
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
      print(i, end=" ")

string_c1()