#We task input from user and according to that input value we assign grade

marks = int(input())

if marks >=90 and marks <= 100:
  print("A Grade")
elif marks >=80 and marks < 90:
  print("B Grade")
elif marks >=70 and marks < 80:
  print("C Grade")
elif marks >=60 and marks < 70:
  print("D Grade")
elif marks < 60:
  print("E Grade")
else:
  print("Invalid")