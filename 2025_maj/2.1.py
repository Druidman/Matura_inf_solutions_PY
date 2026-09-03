def is_palindrome(line: str):
  i1 = 0
  i2 = len(line) - 1

  while i1 < i2:
      

    letter1 = line[i1]
    letter2 = line[i2]

    if (letter1 != letter2): 
      return False
    
    i1 += 1
    i2 -= 1
  return True
  
      
  

lines = []
with open("data/symbole_przyklad.txt", "r") as file:
  lines = file.readlines()

for line in lines:
  if is_palindrome(line.strip()):
    print(line)