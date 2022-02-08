def arithmetic_arranger(problems, solve = False):
  first = []
  max_length = []
  requiredLength = []

  for i in range(len(problems)):
    first.append(problems[i].split(" "))

  if len(first) > 5:
    return_error= "Error: Too many problems."
    return return_error

  for i in range(len(first)):
    
    if(len(first[i]) != 3):
      return_error = "Error: Use one operator and two numbers"
      return return_error

    if first[i][1] != '+' and first[i][1] != '-':
      return_error = "Error: Operator must be '+' or '-'."
      return return_error
    
    try:
      first[i][0] = int(first[i][0])
      first[i][2] = int(first[i][2])
    except:
      return_error = "Error: Numbers must only contain digits."
      return return_error
    
    max_length.append(max(len(str(first[i][0])), len(str(first[i][2]))))
    requiredLength.append(int(max_length[i]) + 2)

    if first[i][0] > 9999 or first[i][2] > 9999:
      return_error = "Error: Numbers cannot be more than four digits."
      return return_error

  arranged_problems = ""

  for i in range(len(first)):
    spaceBetween = requiredLength[i] - len(str(first[i][0]))
    for j in range(spaceBetween):
      arranged_problems += " "
    arranged_problems += str(first[i][0]) + "    "

  arranged_problems = arranged_problems.rstrip()
  arranged_problems += "\n"

  for i in range(len(first)):
    arranged_problems += first[i][1]
    spaceBetween = requiredLength[i] - len(str(first[i][2])) - 1
    for j in range(spaceBetween):
      arranged_problems += " "
    arranged_problems += str(first[i][2]) + "    "

  arranged_problems = arranged_problems.rstrip()
  arranged_problems += "\n"

  for i in range(len(first)):
    for j in range(requiredLength[i]):
      arranged_problems += "-" 
    arranged_problems += "    "
  
  arranged_problems = arranged_problems.rstrip()

  if(not solve):
    return arranged_problems

  arranged_problems += "\n"
  for i in range(len(first)):
    if first[i][1] == "+":
      sum = first[i][0] + first[i][2]
    else:
      sum = first[i][0] - first[i][2]
    spaceBetween = requiredLength[i] - len(str(sum))
    for j in range(spaceBetween):
      arranged_problems += " "  
    arranged_problems += str(sum) + "    "
  
  arranged_problems = arranged_problems.rstrip()
  return arranged_problems
  