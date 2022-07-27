def Error_Handle(n1, n2, operation):
  try:
    int(n1)
    int(n2)
  except:
    return "Error: Numbers must only contain digits."
  try:
    if operation !='-' and operation != '+':
      raise BaseException
  except:
    return "Error: Operator must be '+' or '-'."
  try:
    if len(n1)>4 or len(n2)>4:
      raise BaseException
  except:
    return "Error: Numbers cannot be more than four digits."

  return "pass"

def arithmetic_arranger(problems, Calculate=False):

  arranged_problems = ['','','','']

  if len(problems)>5:
    return "Error: Too many problems."

  index=0
  for problem in problems:
    Nproblem=problem.split()
    n1 = Nproblem[0]
    op=Nproblem[1]
    n2 = Nproblem[2]
    check = Error_Handle(n1, n2, op)
    if check!="pass":
      return check
    num1=int(Nproblem[0])
    num2=int(Nproblem[2])
    space=max(len(n1), len(n2))
    if Nproblem[1]=='+':
      num3=num1+num2
    elif Nproblem[1]=='-':
      num3=num1-num2
    
    if index==0:
      arranged_problems[0]+=str(num1).rjust(space+2)
      arranged_problems[1]+=op + ' ' + str(num2).rjust(space)
      arranged_problems[2]+= '-' * (space+2)
      arranged_problems[3]+=str(num3).rjust(space+2)
      index=1
    else:
      arranged_problems[0]+= '    ' + str(num1).rjust(space+2)
      arranged_problems[1]+= '    ' + op + ' ' + str(num2).rjust(space)
      arranged_problems[2]+= '    ' + '-' * (space+2)
      arranged_problems[3]+= '    ' + str(num3).rjust(space+2)
    
    
  if Calculate ==  True:
    return arranged_problems[0]+ '\n' + arranged_problems[1]+ '\n' + arranged_problems[2] + '\n' + arranged_problems[3]
  else:
    return arranged_problems[0]+ '\n' + arranged_problems[1]+ '\n' + arranged_problems[2]