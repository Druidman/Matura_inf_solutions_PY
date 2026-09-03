
def convert_char_to_num(char: str):
  if (char == 'o'): return 0
  elif (char == '+'): return 1
  elif (char == '*'): return 2
  else: raise Exception('Unexpected char in input')
def get_number_from_str_triple(input: str):
  number = 0
  exponent = 0
  for i in range(len(input) - 1, -1, -1):
    number += convert_char_to_num(input[i]) * pow(3, exponent)
    exponent += 1

  return number
    
  

lines = []
with open("data/symbole_przyklad.txt", "r") as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]

numbers = []
for line in lines:
  number = get_number_from_str_triple(line)
  numbers.append([number, line])


# find max
max = numbers[0][0]
ind = 0
for i,num in enumerate(numbers):
  
  if num[0] > max:
    ind = i
    max = num[0]
    

print(numbers[ind][0], ' ', numbers[ind][1])