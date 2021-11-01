def pyramid():
  stacks = int(input("How tall would you like your pyramid?: "))
  ###let's go steal code from the class repository
  if stacks > 8:
      print("Please enter a nunmber one through eight.")
  else:
      count = 0
      while (count =< stacks):

##      for i in range(stacks):
##          print("#")


for i in range(stacks):
  for j in range(stacks):
    if j <= i:
      print(j, end='')
  print()
