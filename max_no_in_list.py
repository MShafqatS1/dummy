#Find Maximum Number from the given List

number_list = [10, 30, 90, 100, 50, 20, 40, 70, 80, 60, 101]

user_value = number_list[0]
for i in number_list:
  # check the condition and then update user_value's value
  if i > user_value:
    user_value = i

print(user_value)