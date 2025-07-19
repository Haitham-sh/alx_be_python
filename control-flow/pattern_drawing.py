side_length = int(input("Enter the size of the pattern: "))
col = side_length
while side_length > 0:
  for i in range(col):
    print("*", end="")
  print() 
  side_length -= 1