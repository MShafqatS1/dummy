#check if age is greater than and equals to 18 then we can vote
#check person gender
#check if he/she is not older than 70 years

age = int(input())
if age >= 18 and age <= 70:
  if age >= 18:
    gender = input()
    if gender == "M":
      print("He is Eligible to vote")
    else:
      print("She is Eligible to vote")
elif age >= 70:
  print("Sorry, but you are overaged")
else:
  print("Sorry, but you are not eligible to vote")
