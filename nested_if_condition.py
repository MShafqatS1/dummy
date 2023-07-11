#check if age is greater than and equals to 18 then we can vote
#check person gender

age = int(input())
if age >=18:
  gender = str(input())
  if gender == "M":
    print("He is Elegible to vote")
  else:
    print("She is Elegible to vote")
else:
  print("Sorry but you are not Eligible to vote")