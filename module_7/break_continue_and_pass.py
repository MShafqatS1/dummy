# Break, Continue and Pass
#   These statements are used to alter the flow of a program
#   - Break: Breaks the flow of program once this condition it hit
#   - Continue: It skips that particular iteration
#   - Pass: To avoid Syntax error

# 1. PASS
for i in range(10):
  pass

# 2. CONTINUE
# for i in range(10):
#   if i == 5:
#     continue
#   print(i)

# 1. BREAK
for i in range(10):
  if i == 5:
    break
  print(i)